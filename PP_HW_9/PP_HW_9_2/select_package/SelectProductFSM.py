from Observable import Observable
from select_package.CocaCola import CocaCola
from select_package.Pepsi import Pepsi
from select_package.SelectProduct import SelectProduct
from select_package.Sprite import Sprite
from vending_package.ChoiceObserver import ChoiceObserver


class SelectProductFSM(Observable):
    states: dict
    states_activity: dict

    def __init__(self):
        super().__init__()

        self.states = dict()
        self.states_activity = dict()
        self.attach(ChoiceObserver())

        self.states["cola"] = CocaCola(self)
        self.states["pepsi"] = Pepsi(self)
        self.states["sprite"] = Sprite(self)
        self.states["select_product"] = SelectProduct(self)

        self.states_activity["cola"] = "idle"
        self.states_activity["pepsi"] = "idle"
        self.states_activity["sprite"] = "idle"
        self.states_activity["select_product"] = "idle"

    def choose_another_product(self):
        self.states["select_product"].choose()
        self.notify_all()

    def notify_all(self):
        for observer in self.observers:
            observer.update()
