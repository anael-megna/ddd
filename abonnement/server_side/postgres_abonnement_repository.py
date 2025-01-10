from db import postgres
from abonnement.hexagon.domain.abonnement import Abonnement, AbonnementRepo


class PostgresAbonnementRepo(AbonnementRepo):

    def __init__(self):
        self.db = postgres.get_pool

    def enregistrer(self, abonnement: Abonnement):
        self.db.....
