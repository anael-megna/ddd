from abc import ABC, abstractmethod
from dataclasses import dataclass

from abonnement.hexagon.domain.formule import Formule


@dataclass
class Formule:
    pass


@dataclass
class IdFormule:
    valeur: str


class FormuleService(ABC):

    @abstractmethod
    def recuperer(self, id_formule: IdFormule) -> Formule:
        ...
