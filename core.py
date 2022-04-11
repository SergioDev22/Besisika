import ampalibe
from conf import Configuration
from requete import Requete
from Traitements import Traitement
import const

bot = ampalibe.init(Configuration())
req = Requete(Configuration())
opt = Traitement()
query = bot.query
chat = bot.chat

"""
    get_started method, Utile pour permettre certainnes
    fonctionnalités pour le bot afin que les utilisateurs
    les benéficient

"""
# chat.get_started(payload="/get_started")


@ampalibe.command("/get_started")
def get_started(sender_id, **extends):
    chat.send_message(sender_id, const.salutation)
    chat.send_message(sender_id, const.description)
    chat.send_media(sender_id, const.url_logo, "image")
    chat.send_media(sender_id, const.url_video_presentation, "video")
    chat.send_quick_reply(
        sender_id, const.quick_rep_principal, const.quick_title_principal
    )
    chat.persistent_menu(sender_id, const.persistent_menu, action="PUT")


@ampalibe.command("/")
def main(sender_id, **extends):
    chat.send_quick_reply(
        sender_id, const.quick_rep_principal, const.quick_title_principal
    )


# --------------COMMANDES QUICK_PRINCIPAL ET MENU PRINCIPAL-----------------#
@ampalibe.command("/nos_domaines")
def domaines(sender_id, **extends):
    chat.send_message(sender_id, const.domaine_title_template)
    chat.send_template(
        sender_id,
        opt.trt_template_domaine(),
        quick_rep=const.quick_retour_principal,
    )


@ampalibe.command("/nos_projets")
def projets(sender_id, **extends):
    chat.send_message(sender_id, const.projets_title_template)
    chat.send_template(
        sender_id,
        opt.trt_liste_projets(req.get_projet()),
        quick_rep=const.quick_retour_principal,
        next=True,
    )


@ampalibe.command("/nos_competences")
def competence(sender_id, **extends):
    chat.send_template(sender_id, opt.trt_competence())


@ampalibe.command("/nos_actualites")
def actualite(sender_id, **extends):
    chat.send_message(sender_id, const.actualites_title_template)
    chat.send_template(
        sender_id,
        opt.trt_liste_actualite(req.get_actualites()),
        next=True,
    )


@ampalibe.command("/nos_membres")
def membres(sender_id, **extends):
    chat.send_message(sender_id, const.nos_projets_title_template)
    chat.send_template(sender_id, opt.trt_liste_membre(req.get_membres()), next=True)


@ampalibe.command("/contact")
def contact(sender_id, **extends):
    chat.send_message(
        sender_id,
        f"\t\tNOS CONTACTS:\n🏢Adresse : {const.adresse}\n☎Téléphone : {const.phone}\n✉Email : {const.email}",
    )
    chat.send_quick_reply(
        sender_id, const.quick_retour_principal, const.quick_retour_principal_title
    )


# ----------------------------------------------------------------------------#

# explication domaine
@ampalibe.command("/explication")
def explication(sender_id, explication, **extends):
    chat.send_message(sender_id, explication)
    chat.send_quick_reply(
        sender_id, const.quick_retour_principal, const.quick_retour_principal_title
    )


@ampalibe.command("/explicaion_competence")
def exlpicaion_competence(sender_id, explication, **extends):
    chat.send_message(sender_id, explication)
    chat.send_quick_reply(
        sender_id, const.quick_retour_principal, const.quick_retour_principal_title
    )


# voir details actualités
@ampalibe.command("/voir_details")
def details(sender_id, details, **extends):
    chat.send_message(sender_id, details)
    chat.send_quick_reply(
        sender_id, const.quick_retour_principal, const.quick_retour_principal_title
    )


# retoure au menu precédents
@ampalibe.command("/retour")
def retour(sender_id, **extends):
    chat.send_quick_reply(
        sender_id, const.quick_rep_principal, const.quick_title_principal
    )


# interessé(e)
@ampalibe.command("/interesse")
def interesse(sender_id, id_membre, **extends):
    data_membre = req.get_descriptions_membres(id_membre)
    chat.send_button(
        sender_id,
        opt.trt_interesse(data_membre),
        opt.trt_titre_button_interesse(data_membre),
    )
