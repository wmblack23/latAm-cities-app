from openai import OpenAI
from dotenv import load_dotenv
from pymongo import MongoClient
import json

load_dotenv()

# Initialize client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Chat-GPT function to call
def correct_spanish_entry(text):
    response = client.chat.completions.create(
        model="gpt-4",
        temperature=0.2,
        timeout=15,
        messages=[
            {
                "role": "system",
                "content": (
                    """You are going to receive a city name and a country code. Do the following:

                    1. Return a city safety score out of 10. 
                    2. For each city, you will give the local way they say the following words in Spanish
                    'Friend', 'Party', 'Bus', 'Beer', 'Cool', 'Money', 'Drunk', 'Guy', 'Girl', 'Hang out'
                    3. Return each as a json object
                    EXAMPLE:
                    {'city': 'City Name', 'country_code': 'Country Code', 'safety': 7.2/10, words={'Friend': , 'Party': ,}} etc
                    """
                )
            },
            {
                "role": "user",
                "content": f"Please use this city name and country code and provide the appropriate feedback in the appropriate format:\n{text}"
            }
        ]
    )
    data = response.choices[0].message.content
    return data