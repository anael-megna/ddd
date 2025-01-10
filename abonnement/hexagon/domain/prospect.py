from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class IdProspect:
    valeur: str


@dataclass
class Prospect:
    id: IdProspect
    est_etudiant: bool
    email: str


class ProspectIntrouvable(object):
    pass


class ProspectService(ABC):

    @abstractmethod
    def recuperer(self, id_prospect: IdProspect) -> Prospect | ProspectIntrouvable:
        ...
