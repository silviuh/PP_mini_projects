from State import State
from select_package import SelectProductFSM


class Sprite(State):
    state_machine: SelectProductFSM
    price: float

    def __init__(self, state_machine):
        self.state_machine = state_machine

    def set_state_machine(self, state_machine):
        self.state_machine = state_machine

    def set_price(self, price):
        self.price = price
