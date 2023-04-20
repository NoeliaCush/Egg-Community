from dataclasses import dataclass
from pprint import pprint
from typing import ClassVar, Optional

@dataclass
class País:
    lista_países: ClassVar[list["País"]] = []
    pais: str
    descripción: Optional[str] = None

    def __post_init__(self):
        País.lista_países.append(self)

@dataclass(kw_only=True)
class Capital(País):
    poblacion: int
    capital: Optional[str] = None

    def __post_init__(self):
        super().__post_init__()

    def ver_población(self):
        print(f"{self.pais}: {self.poblacion}")

dato_1 = Capital("Argentina", descripción="país del sur de América",
                 capital= "Buenos Aires", poblacion = 1_000_000)

dato_2 = Capital("España", poblacion=500_00)
dato_1.ver_población
pprint(País.lista_países)