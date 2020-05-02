from select_package.SelectProductFSM import SelectProductFSM
from take_money_package.TakeMoneyFSM import TakeMoneyFSM
from vending_package.ChoiceObserver import ChoiceObserver


class VendingMachineFSM(ChoiceObserver):
    take_money_fsm: TakeMoneyFSM
    select_product_fsm: SelectProductFSM
    loopIsOn = True

    def __init__(self):
        self.take_money_fsm = TakeMoneyFSM()
        self.select_product_fsm = SelectProductFSM()
        self.take_money_fsm.states_activity["insert_money_state"] = "active"

    def proceed_to_checkout(self):
        if self.take_money_fsm.states_activity["insert_money_state"] == "active":
            choice = input("Do you need something to buy? [y/n] ")
            if choice == "y":
                self.take_money_fsm.add_money()
                self.take_money_fsm.states_activity["insert_money_state"] == "idle"
                self.take_money_fsm.states_activity["wait_state"] == "active"

                while self.take_money_fsm.states_activity["wait_state"] == "active":
                    self.update()
            else:
                print("You have exited de program")
                exit(0)

    def update(self):
        if self.take_money_fsm.states_activity["wait_state"] == "active":
            product = self.select_product_fsm.states_activity["select_product"]
            if product != "idle":
                if self.select_product_fsm.states[product].price <= self.take_money_fsm.money:
                    self.select_product_fsm.states_activity[product] = "active"
                    print("{} was purchased...".format(product))
                    self.take_money_fsm.states_activity["wait_state"] == "idle"

                    choice = input("Do you want another product [y] or the change [n] ? ")
                    if choice == "y":
                        self.take_money_fsm.states_activity["wait_state"] == "active"
                    else:
                        print("Change: {}".format(self.take_money_fsm.money))
                        self.take_money_fsm.money = 0
                        self.take_money_fsm.states_activity["insert_money_state"] = "active"
                        self.take_money_fsm.states_activity["wait_state"] = "idle"
                        self.proceed_to_checkout()
                else:
                    self.take_money_fsm.states_activity["insert_money_state"] = "active"
                    self.take_money_fsm.states_activity["wait_state"] = "idle"
                    print("not enough money to buy {}".format(product))
                    self.proceed_to_checkout()
