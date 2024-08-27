import json
import string
import random
from playwright.sync_api import sync_playwright

from dotenv import load_dotenv
import os
from faker import Faker

fake = Faker()
load_dotenv()
context = None
global_id = None
id_user = None
bearer = os.getenv('BEARER_KEY')
bearerDemoQA = os.getenv('BEARER_DEMOQA_KEY')
SUT = os.getenv('BASE_URL')
urlUsers = os.getenv('URL_USERS')

def get_bearer_header():
    """Devuelve el encabezado de autorización Bearer."""
    return {"Authorization": f"Bearer {bearer}"}

def get_bearer_header_demoqa():
    return {"Authorization:" f"Bearer {bearerDemoQA}"}

def get_random_user_id(response):
    users = response.json()
    ids = [user["id"] for user in users]
    return random.choice(ids)

def patchUser():
    with open('tests/jsonFiles/PatchNewUser.json', "r") as read_file:
        data = json.load(read_file)  # Lee el archivo JSON dentro del bloque with
    
    randomNameMale = fake.name_male()
    randomNameFemale = fake.name_female()
    genre = random.choice(["male", "female"])
    
    # Dependiendo del género, selecciona el nombre correspondiente
    if genre == "male":
        random_user_name = randomNameMale
    else:
        random_user_name = randomNameFemale
    
    data["name"] = random_user_name
    data["gender"] = genre
    
    return data
def createNewUser():
    #randomUser = "".join(random.choices(string.ascii_uppercase + string.digits, k=5))
    random_user = fake.user_name().replace(" ", "")
    randomNameMale = fake.name_male()
    randomNameFemale = fake.name_female()
    genre = random.choice(["male", "female"])
    
    
    # Dependiendo del género, selecciona el nombre correspondiente
    if genre == "male":
        random_user_name = randomNameMale
    else:
        random_user_name = randomNameFemale
    
 
    
    with open('tests/jsonFiles/CreateNewUser.json', "r") as read_file:
       
        data = json.load(read_file)
        data["name"] = random_user_name
        data["email"] = random_user + "@gmail.com"
        data["gender"] = genre 
    
    return data

def verify_name_in_response(resJson, name):
    """
    Verifica si el nombre proporcionado está en la respuesta JSON.
    """
    size = len(resJson)
    for i in range(size):
        if name:
            assert name == resJson[i].get("name")
            break
def urlPatch(urlUsers, global_id):
         url = f"{urlUsers}{str(global_id)}"
         return url     
     
def createNewUserDemoqa():
    random_user = fake.user_name()
    random_password = fake.password()
    with open('tests/jsonFiles/NewUserDemoqa.json', "r") as read_file:
        data = json.load(read_file)
        data["userName"] = random_user
        data["password"] = random_password
    return data