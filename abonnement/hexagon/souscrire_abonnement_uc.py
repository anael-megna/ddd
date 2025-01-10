from datetime import date

from abonnement.hexagon.domain.abonnement import Abonnement, AbonnementRepo, IdAbonnement
from abonnement.hexagon.domain.prospect import IdProspect
from abonnement.hexagon.domain.formule import FormuleService, IdFormule
from abonnement.hexagon.domain.prospect import ProspectService


class SouscrireAbonnementUc:

    def __init__(
        self,
        prospect_service: ProspectService,
        formule_service: FormuleService,
        abonnement_repo: AbonnementRepo,
    ):
        self.prospect_service = prospect_service
        self.formule_service = formule_service
        self.abonnement_repo = abonnement_repo

    def souscrire_abonnement(
        self,
        *,
        id_abonnement: IdAbonnement,
        id_formule: IdFormule,
        id_prospect: IdProspect,
        date_souscription: date,
    ) -> Events:
        prospect = self.prospect_service.recuperer(id_prospect)
        formule = self.formule_service.recuperer(id_formule)

        abonnement = Abonnement.souscrire(
            id_abonnement=id_abonnement,
            formule=formule,
            prospect=prospect,
            date_souscription=date_souscription,
        )
        self.abonnement_repo.enregistrer(abonnement)

        return abonnement.events
