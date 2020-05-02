from State import State
from take_money_package import TakeMoneyFSM


class InsertMoney(State):
    state_machine: TakeMoneyFSM

    def __init__(self, state_machine):
        self.state_machine = state_machine

    def choose_amount(self):
        amount = int(input("How much money do you want to spend? [10 bani] [50 bani] [1 leu] [5 lei] [10 "
                           "lei]"))

        money_added = 0.0

        if amount == 10:
            choice = str(input("lei or bani? "))
            if choice == "bani":
                money_added = self.insert_10bani()
            elif choice == "lei":
                money_added = self.insert_10lei()
        elif amount == 50:
            money_added = self.insert_50bani()
        elif amount == 1:
            money_added = self.insert_1leu()
        elif amount == 5:
            money_added = self.insert_5lei()

        return money_added

    def insert_10bani(self):
        self.state_machine.money += 0.10
        return 0.10

    def insert_50bani(self):
        self.state_machine.money += 0.50
        return 0.50

    def insert_1leu(self):
        self.state_machine.money += 1
        return 1

    def insert_5lei(self):
        self.state_machine.money += 5
        return 5

    def insert_10lei(self):
        self.state_machine.money += 10
        return 10
