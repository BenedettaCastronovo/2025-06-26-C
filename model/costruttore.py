from dataclasses import dataclass, field

@dataclass
class Costruttore:
    constructorId: int
    constructorRef: str
    name: str
    nationality: str
    url: str
    piaz: dict = field(default_factory=dict)


    def __eq__(self, other):
        return self.constructorId == other.constructorId

    def __hash__(self):
        return hash(self.constructorId)

    def __str__(self):
        return f"costruttore: {self.constructorId}"



