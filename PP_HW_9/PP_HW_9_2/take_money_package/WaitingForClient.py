from State import State
from take_money_package import TakeMoneyFSM


class WaitingForClient(State):
    state_machine: TakeMoneyFSM

    def __init__(self, state_machine):
        self.state_machine = state_machine

    def client_arrived(self):
        self.state_machine.states_activity["wait_state"] = "active"
