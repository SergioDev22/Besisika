import const
from ampalibe import Payload
from datetime import datetime, date

class Controller():
    
    def trt_liste_membre(self, data):
        
        liste_membre = []
        for i in range(len(data)):
            liste_membre.append(
                {
                    "title":data[i][0]+" "+ data[i][1],
                    "subtitle" : data[i][4] if data[i][4] else "No Fonction" ,
                    "image_url": data[i][3],
                    "buttons": [
                        {
                            "type": "web_url",
                            "title": "FACEBOOK",
                            "url": "https://www.facebook.com/"+data[i][-2] if data[i][-2] else "https://www.facebook.com"
                            
                        },
                        {
                            "type": "web_url",
                            "title": "LINKEDIN",
                            "url": "https://www.linkedin.com/in/"+data[i][-1] if data[i][-1] else "https://www.linkedin.com"
                            
                        },
                        {
                            "type": "web_url",
                            "title": "PORTFOLIO",
                            "url":"https://portfolio.iteam-s.mg/?u="+data[i][2] if data[i][2] else "https://portfolio.iteam-s.mg/?u=sergio"
                        }
                    ]
                }
            )
        
        return liste_membre
    
    def trt_template_domaine(self):

        domaine_data = const.domaine_liste
        liste_domaine = []
        for i in range(len(domaine_data)):
            liste_domaine.append(
                {
                    "title":domaine_data[i][0].upper(),
                    "image_url": domaine_data[i][1],
                    "buttons": [
                        {
                            "type": "postback",
                            "title": "EXPLICATION",
                            "payload":Payload("/explication", explication=domaine_data[i][-1])
                        }
                    ]
                }
            )
        return liste_domaine

    def trt_liste_projets(self, data):

        liste_projets = []
        for i in range(len(data)):
            liste_projets.append(
                {
                    "title":data[i][0].upper(),
                    "subtitle" : data[i][1],
                    "image_url": data[i][2],
                    "buttons": [
                        {
                            "type": "web_url",
                            "title": "VOIR SUR GITHUB",
                            "url": data[i][-1]
                        }
                    ]
                }
            )
        return liste_projets
    
    def trt_liste_actualite(self, data):

        liste_actualite = []
        for i in range(len(data)):
            liste_actualite.append(
                {
                    "title":data[i][0].upper(),
                    "subtitle" : "Date : " + data[i][-1].strftime("%d - %m - %Y"),
                    "image_url": data[i][2],
                    "buttons": [
                        {
                            "type": "postback",
                            "title": "DETAILS",
                            "payload":Payload("/voir_details", details=data[i][1]),
                        },
                        {
                            "type": "web_url",
                            "title": "VOIR SUR SITEWEB",
                            "url" : "https://iteam-s.mg/view/actualite.html"
                        }
                    ]
                }
            )
        
        return liste_actualite
