import ampalibe
from conf import Configuration
from requete import Requete
from controllers import Controller
import const

bot = ampalibe.init(Configuration())
req = Requete(Configuration())
opt = Controller()
query = bot.query
chat = bot.chat

@ampalibe.command('/')
def main(sender_id,**extends):
    chat.send_message(sender_id, const.salutation)
    chat.send_message(sender_id,const.description)
    chat.send_media(sender_id, const.url_logo, "image")
    chat.send_media(sender_id, const.url_video_presentation,"video")
    chat.send_quick_reply(
        sender_id, 
        const.quick_rep_principal,
        const.quick_title_principal
        
    )
    chat.persistent_menu(sender_id, const.persistent_menu,action="PUT") 
    


#----------COMMANDES QUICK_PRINCIPAL------------------------------#

@ampalibe.command('/nos_domaines') 
def domaines(sender_id, **extends):
    chat.send_message(sender_id,const.domaine_title_template)
    chat.send_template(
        sender_id,
        opt.trt_template_domaine()
    )

@ampalibe.command('/nos_projets')
def projets(sender_id,**extends):
    chat.send_message(sender_id,const.projets_title_template)
    chat.send_template(
        sender_id,
        opt.trt_liste_projets(
            req.get_projet()
        )
    )
    
@ampalibe.command('/nos_actualites')
def actualite(sender_id,**extends):
    chat.send_message(sender_id,const.actualites_title_template)
    chat.send_template(
        sender_id,
        opt.trt_liste_actualite(
            req.get_actualites()
        ),
        next=True
    )

@ampalibe.command('/nos_membres')
def membres(sender_id,**extends):
    # print(req.get_membres())
    
    chat.send_message(sender_id,"Voici nos membres")
    chat.send_template(
        sender_id,
        opt.trt_liste_membre(
            req.get_membres()
        ),
        next=True
    )
    
@ampalibe.command('/contact')
def contact(sender_id,**extends):
    chat.send_message(sender_id,"Voici nos contacts")

#explication domaine
@ampalibe.command('/explication')
def explication(sender_id, explication, **extends):
    chat.send_message(sender_id,explication)

#chek reseaux sociaux
@ampalibe.command('/voir_facebook')
def facebook(sender_id, id, fullname, **extends):
    url_facebook = "https://www.facebook.com" + req.get_url_fb(id)
    chat.send_message(
        sender_id,
        "le lien de facebook de " + fullname + " est " + url_facebook)

#voir details actualités
@ampalibe.command('/voir_details')
def details(sender_id, details, **extends):
    chat.send_message(sender_id, details)