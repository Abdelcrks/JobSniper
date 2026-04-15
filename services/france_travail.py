import requests
import os
from dotenv import load_dotenv

load_dotenv()

def get_token():
    url= "https://entreprise.francetravail.fr/connexion/oauth2/access_token?realm=%2Fpartenaire"
    response = requests.post(url, data={
        "grant_type": "client_credentials",
        "client_id": os.getenv("FRANCE_TRAVAIL_CLIENT_ID"),
        "client_secret": os.getenv("FRANCE_TRAVAIL_CLIENT_SECRET"),
        "scope": "api_offresdemploiv2 o2dsoffre"
        }
    )
    return response.json()["access_token"]


def get_offers():
    url = "https://api.francetravail.io/partenaire/offresdemploi/v2/offres/search"
    response = requests.get(url, headers={
        "Authorization": f"Bearer {get_token()}",   
    },
    params={
            "motsCles":"développeur"
        }
    )

    data = response.json()
    resultats = data.get("resultats", [])
    return [offre for offre in resultats if offre.get("alternance") == True]