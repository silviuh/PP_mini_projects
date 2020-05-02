from Observable import Observable
from take_money_package.DisplayObserver import DisplayObserver
from take_money_package.InsertMoney import InsertMoney
from take_money_package.WaitingForClient import WaitingForClient


class TakeMoneyFSM(Observable):
    states: dict
    states_activity: dict
    money: float

    def __init__(self):
        super().__init__()

        self.states = dict()
        self.states_activity = dict()
        self.money = 0
        self.attach(DisplayObserver())

        self.states["wait_state"] = WaitingForClient(self)
        self.states["insert_money_state"] = InsertMoney(self)
        self.states_activity["wait_state"] = "idle"
        self.states_activity["insert_money_state"] = "idle"

    def add_money(self):
        self.update_amount_of_money(self.states["insert_money_state"].choose_amount())

    def update_amount_of_money(self, money_to_add: float):
        self.notify_all(money_to_add)

    def notify_all(self, money_to_add):
        for observer in self.observers:
            observer.update(money_to_add)
