from conf import Configuration

# VARIABLES
salutation = "Miarahaba tompoka, Tongasoa eto amin'ny BOT MESSENGER iTeam-$"

description = "Communauté IT de jeunes motivés."

url_logo = (
    "https://www.facebook.com/iTeam.Community/photos/a.102143328508332/102143775174954/"
)
url_video_presentation = (
    "https://www.facebook.com/iTeam.Community/videos/476926027465187"
)

domaine_title_template = "Voici donc nos domaines de competetence"
domaine_explications_1 = """En tant que communauté composée essentiellement de programmeur, \
réussir la mise en place d'outil informatique est l'une des compétences à maîtriser pour \
chacun de nos membres. 
"""
domaine_explications_2 = """On dit toujours que le cordonnier est le plus mal chaussé... \
chez iTeam-$ nous essayons d'être différent ! Nos membres développent des outils en interne \
pour que la communauté vive pleinement digital. Une occasion d'acquérir de l'expérience pour \
nos nouveaux membres et en même temps concevoir quelque chose d'utile pour la communauté. \
"""
domaine_explications_3 = """Les compétences acquises par nos membres sont mises à disposition \
pour aider les particuliers ou les entreprises de toutes tailles dans la réalisation de leurs \
projets de développement.
"""
domaine_explications_4 = """La transformation digital n'est pas seulement de "mettre en place \
un outil digital", il faut un accompagnement jusqu’au déploiement et s'assurer du bon fonctionnement \
en production
"""

domaine_liste = [
    (
        "Transformation Digital",
        "https://media.istockphoto.com/photos/digital-transformation-technology-strategy-digitization-and-of-and-picture-id1072111648?k=20&m=1072111648&s=612x612&w=0&h=m1UVi3Kh86AQmsxZQnyPwZ9gWOONrk-umW7SPLU1J40=",
        domaine_explications_1,
    ),
    (
        "Développement de projet en Interne ",
        "https://iteam-s.mg/assets/img/open.jpg",
        domaine_explications_2,
    ),
    (
        "Développement de projet en Externe",
        "https://img.freepik.com/vecteurs-libre/modeles-logo-electronique-design-plat_23-2148985012.jpg?w=2000",
        domaine_explications_3,
    ),
    (
        "Accompagnement et déploiement",
        "https://www.partner-informatique.fr/wp-content/uploads/2017/12/securite-parc-informatique.jpg",
        domaine_explications_4,
    ),
]

competence_explications_1 = "Nous sommes dotés de riche expérience dans le domaine d'extraction de données \
sur des sites Web."
competence_explications_2 = "C'est aussi une des spécialités de la communauté. La communauté a même sortie \
une librairie open-source en python pour le développement de Chatbot"
competence_explications_3 = "C'est une des principaux intérêts d'utiliser la technologie, nous réalisons \
divers scripts pour des tâches répétitives qui peuvent être automatisés."
competence_explications_4 = "Nous réalisons des applications pour toutes les plateformes : \
Web, Mobile(Android,ios), Windows, Linux."

competence_liste = [
    (
        "Web Scrapping",
        "https://i2.wp.com/challengingcoder.com/wp-content/uploads/2022/02/Web-Scraping.png?w=1400&ssl=1",
        competence_explications_1,
    ),
    (
        "ChatBot Messenger",
        "https://cdn2.iconfinder.com/data/icons/chatbot-line/100/bot_and_messenger-10-512.png",
        competence_explications_2,
    ),
    (
        "Automatisation & Scripting",
        "https://www.qualitylogic.com/wp-content/uploads/2014/11/Test-automation-Process-640x640.png",
        competence_explications_3,
    ),
    (
        "Développement d'application",
        "https://e7.pngegg.com/pngimages/565/313/png-clipart-web-development-mobile-app-development-app-inventor-for-android-web-design-mobile-app-template-web-design-service.png",
        competence_explications_4,
    ),
]

projets_title_template = "Voici donc tout nos projets"
actualites_title_template = "Voici nos actualités"
nos_projets_title_template = "Voici nos membres"
nos_contacts_title_template = "Voici nos contacts"

# contact
adresse = "Ambatoroka IV17JZ Antananarivo Madagascar"
phone = "+261 34 61 780 78"
email = "contact@iteams.mg"


quick_title_principal = "Que-ce que vous voulez faire maintenant?"
quick_rep_principal = [
    {
        "content_type": "text",
        "title": "NOS DOMAINES",
        "image_url": "https://iteam-s.mg/assets/img/open.jpg",
        "payload": "/nos_domaines",
    },
    {
        "content_type": "text",
        "title": "NOS PROJETS",
        "image_url": "https://iteam-s.mg/assets/img/bjj.png",
        "payload": "/nos_projets",
    },
    {
        "content_type": "text",
        "title": "NOS ACTUALITÉS",
        "image_url": "https://clarolineconnect.univ-lyon1.fr/file/resource/media/1351783",
        "payload": "/nos_actualites",
    },
    {
        "content_type": "text",
        "title": "NOS COMPETENCES",
        "image_url": f"{Configuration.APP_URL}/asset/img/competence.png",
        "payload": "/nos_competences",
    },
    {
        "content_type": "text",
        "title": "NOS MEMBRES",
        "image_url": "https://communaute.ebay.fr/t5/image/serverpage/image-id/53895iF052C8AAF31A3905/image-size/original?v=mpbl-1&px=-1",
        "payload": "/nos_membres",
    },
    {
        "content_type": "text",
        "title": "CONTACT",
        "image_url": "https://www.maroc.campusfrance.org/sites/pays/files/maroc/styles/desktop_visuel_principal_page/public/medias/images/2021-05/Contact%202.png?itok=gVswANwh",
        "payload": "/contact",
    },
]

persistent_menu = [
    {"type": "postback", "title": "🔷MENU PRINCIPAL", "payload": "/"},
    {"type": "postback", "title": "☎CONTACT", "payload": "/contact"},
]


quick_retour_principal_title = "Revenir au précedent"
quick_retour_principal = [
    {"content_type": "text", "title": "⏪RETOUR", "payload": "/retour"}
]
