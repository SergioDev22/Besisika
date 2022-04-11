from ampalibe import Model


class Requete(Model):
    def __init__(self, conf):

        Model.__init__(self, conf)

    @Model.verif_db
    def get_membres(self):
        req = """
                SELECT id, nom, prenom, user_github_pic, fonction
                FROM membre
        """
        self.cursor.execute(req)
        data = self.cursor.fetchall()
        self.db.commit()
        return data

    @Model.verif_db
    def get_descriptions_membres(self, id_membre):
        req = """
                SELECT description, prenom_usuel, facebook, linkedin, mail, tel1
                FROM membre
                WHERE id = %s
        """
        self.cursor.execute(req, (id_membre,))
        data = self.cursor.fetchone()
        self.db.commit()
        return data

    @Model.verif_db
    def get_projet(self):
        req = """
            SELECT nom, descriptions, couverture, lien
            FROM projetsIteams
        """
        self.cursor.execute(req)
        data = self.cursor.fetchall()
        self.db.commit()
        return data

    @Model.verif_db
    def get_actualites(self):
        req = """
            SELECT titre, description, image, date
            FROM actualites
        """
        self.cursor.execute(req)
        data = self.cursor.fetchall()
        self.db.commit()
        return data
