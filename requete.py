from ampalibe import Model

class Requete(Model):
    
    def __init__(self,conf):
        
        Model.__init__(self, conf)
        
    
    @Model.verif_db
    def get_membres(self):
        req = """
                SELECT nom, prenom, prenom_usuel, user_github_pic, fonction, facebook, linkedin
                FROM membre
        """
        self.cursor.execute(req)
        data = self.cursor.fetchall()
        self.db.commit()
        return data 
    
    @Model.verif_db
    def get_url_fb(self, id):
        req = "SELECT facebook FROM membre WHERE id=%s"  
        self.cursor.execute(req,(id,))    
        data = self.cursor.fetchone()[0] 
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