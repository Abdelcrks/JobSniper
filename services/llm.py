import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)

def generate_cover_letter(profile,offer):
    prompt= f"""
    Écris une lettre de motivation en fonction du poste : {offer["intitule"]},
        le nom de l'entreprise :{offer["entreprise"]},
            la description de l'offre :{offer["description"]},
                ainsi que le nom du profil qui postulera :{profile.name}, 
                    et son expérience :{profile.experience}
    """

    response = client.chat.completions.create(
        model="google/gemma-3-4b-it:free",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content
