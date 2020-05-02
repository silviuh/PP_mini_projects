from State import State
from select_package import SelectProductFSM


class SelectProduct(State):
    state_machine: SelectProductFSM
    price: float

    def __init__(self, state_machine):
        self.state_machine = state_machine

    def set_state_machine(self, state_machine):
        self.state_machine = state_machine

    def set_price(self, price):
        self.price = price

    def choose(self):
        product = input("Choose a product [cola] [pepsi] [sprite] : ")
        self.state_machine.states_activity["select_product"] = product
