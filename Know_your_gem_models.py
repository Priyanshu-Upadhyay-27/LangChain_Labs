# to run this code, first load your api key then run this...

from google import genai
from dotenv import load_dotenv
load_dotenv()


client = genai.Client()

print("List of models that support generateContent:\n")
for m in client.models.list():
    for action in m.supported_actions:
        if action == "generateContent":
            print(m.name)

print("List of models that support embedContent:\n")
for m in client.models.list():
    for action in m.supported_actions:
        if action == "embedContent":
            print(m.name)
"""from google import genai
from dotenv import load_dotenv
load_dotenv()
client = genai.Client()

try:
    r = client.models.generate_content(model="gemini-2.0-flash", contents="hello")
    print("WORKED:", r.text)
except Exception as e:
    print("FAILED:", e)"""
