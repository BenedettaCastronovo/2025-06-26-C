from dataclasses import dataclass

from model.costruttore import Costruttore


@dataclass
class Arco:
    c1: Costruttore
    c2: Costruttore
    peso: int