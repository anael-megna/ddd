from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import date, datetime, timedelta, timezone

from abonnement.hexagon.domain.formule import Formule
from abonnement.hexagon.domain.prospect import Prospect


@dataclass
class IdAbonnement:
    valeur: str


@dataclass
class Abonnement:
    id: IdAbonnement
    formule: Formule
    prospect: Prospect
    date_souscription: date
    events: list[Event]  # peut contenir des events utiles pour le logging

    @classmethod
    def souscrire(cls, id_abonnement, formule, prospect, date_souscription) -> 'Abonnement':
        demain = datetime.now(tz=timezone.utc) + timedelta(days=1)
        if date_souscription < demain:
            raise ValueError('date pas avant demain')

        return cls(
            id=id_abonnement,
            formule=formule,
            prospect=prospect,
            date_souscription=date_souscription,
            events=[AbonnementSouscrit(
                id_abonnement=id_abonnement,
            )],
        )


class AbonnementRepo(ABC):

    @abstractmethod
    def enregistrer(self, abonnement: Abonnement):
        ...


@dataclass
class AbonnementSouscrit:
    id_abonnement: IdAbonnement
