import discord
from discord import ButtonStyle
from discord.ext import commands
from discord.ui import Button, View
import cfscrape
from bs4 import BeautifulSoup as bs


import os
import json
import shutil
import threading
import time
import sys
try:
    import requests
    from urllib3.exceptions import InsecureRequestWarning
    from bs4 import BeautifulSoup
except:
    os.system("pip install requests")
    os.system("pip install bs4")


from cProfile import label
import asyncio
import discord
from discord import ButtonStyle
from discord.ext import commands
from discord.ui import Button, View



class Spy:
    gris = "\033[1;30;1m"
    rouge = "\033[1;31;1m"
    vert = "\033[1;32;1m"
    rose=""
    jaune = "\033[1;33;1m"
    bleu = "\033[1;34;1m"
    violet = "\033[1;35;1m"
    cyan = "\033[1;36;1m"
    blanc = "\033[1;0;1m"



def get_info_post(url):
    try:

        time.sleep(1)
        print(f"{Spy.blanc}[{Spy.jaune}RECHERCHE{Spy.blanc}] - Le bot recupere les informations de l'item...")
        headers = requests.utils.default_headers()
        headers.update({'User-agent': 'Mozilla/5.0'})
        scraper=cfscrape.create_scraper()
        reponse = scraper.get(str(url))
        if 429 == reponse.status_code:
            print(f"{Spy.blanc}[{Spy.rouge}ERREUR{Spy.blanc}] - Rate Limit !")
            time.sleep(1)
        soup = BeautifulSoup(reponse.text, "html.parser")

        res = soup.findAll('script', {"class": "js-react-on-rails-component"})

        descindice = 0
        userinfoindice = 0
        for i in range(len(res)):
            if 'data-component-name="ItemDescription"' in str(res[i]).split():
                descindice = i
            if 'data-component-name="ItemUserInfo"' in str(res[i]).split():
                userinfoindice = i

        description = json.loads(res[descindice].text.replace(
            '<script class="js-react-on-rails-component" data-component-name="ItemDescription" data-dom-id="ItemDescription-react-component-3d79657d-a1b5-4f1d-b501-2f470f328c66" type="application/json">',
            "").replace("</script>", ''))

        userinfo = json.loads(res[userinfoindice].text.replace(
            '<script class="js-react-on-rails-component" data-component-name="ItemUserInfo" data-dom-id="ItemUserInfo-react-component-2105d904-b161-47d1-bfce-9b897a8c1cc6" type="application/json">',
            '').replace("</script>", ''))

        titre = description["content"]["title"]
        description = description["content"]["description"]
        positive = userinfo["user"]["positive_feedback_count"]
        negative = userinfo["user"]["negative_feedback_count"]
        username = userinfo["user"]["login"]
        pays = userinfo["user"]["country_title"]
        ville = userinfo["user"]["city"]

        lesinfo = {}

        if titre == "":
            titre = "Pas de donnée"
        if description == "":
            description = "Pas de donnée"
        if positive == "":
            positive = "Pas de donnée"
        if negative == "":
            negative = "Pas de donnée"
        if username == "":
            username = "Pas de donnée"
        if pays == "":
            pays = "Pas de donnée"
        if ville == "":
            ville = "Pas de donnée"

        try:
            lesinfo["titre"] = titre
            lesinfo["description"] = description
            lesinfo["positive"] = positive
            lesinfo["negative"] = negative
            lesinfo["username"] = username
            lesinfo["pays"] = pays
            lesinfo["ville"] = ville
        except Exception as err:
            print(err)
        return lesinfo
    except:
        pass


def search(url):

    try:
        time.sleep(1)
        print(f"{Spy.blanc}[{Spy.gris}RECHERCHE{Spy.blanc}] - Le bot cherche des nouveaux items...")
        headers = requests.utils.default_headers()
        headers.update({'User-agent': 'Mozilla/5.0'})
        scraper=cfscrape.create_scraper()
        reponse = scraper.get(str(url))
        print(reponse)
        if 429 == reponse.status_code:
            print(f"{Spy.blanc}[{Spy.rouge}ERREUR{Spy.blanc}] - Rate Limit !")
            time.sleep(1)
        soup = BeautifulSoup(reponse.text, "html.parser")

        res = soup.findAll('script')
        indices = 0
        for i in range(len(res) + 1):
            if 'data-js-react-on-rails-store="MainStore"' in str(res[i]).split():
                indices += i
                break
        value = res[indices].text.replace('<script z-js-react-on-rails-store="MainStore" type="application/json">', "")
        z = json.loads(value)

        return z
    except:
        print(f"{Spy.blanc}[{Spy.rouge}ERREUR{Spy.blanc}] - La fonction search na pas fonctionner!")
        pass



"""  
posting = []
def teste():
    while True:
        z = search("https://www.vinted.fr/vetements?catalog%5B%5D=76&brand_id%5B%5D=53&order=newest_first&price_to=12&currency=EUR")
        x = z["items"]["catalogItems"]["byId"]
        dictlist = list(x)
        for i in range(9, -1, -1):
                time.sleep(1)
                post = dictlist[i - 1]
                if str(post) in posting:
                    print(f"{Spy.blanc}[{Spy.rouge}{post}{Spy.blanc}] - Item déjà envoyé !")
                    time.sleep(1)
                    continue
                else:
                    print(f"{Spy.blanc}[{Spy.vert}{post}{Spy.blanc}] - Nouvel item trouvé !")
                    info = get_info_post(x[str(post)]["url"])
                    posting.append(str(post))
                    print(posting)
                    intents = discord.Intents.default()
                    intents.message_content = True
                    bot =commands.Bot(command_prefix='!',description="bot teste",intents=intents)
                    print("le bot est en ligne ")
                    bot.run('MTAzMjM1NzIwNDM5NDc3MDQ3NA.GoNQMF.1hGvCooNn0aF-TyJJhzADNgrTlbkVTGJSPiq5U')
    icon_url=ctx.author.avatar.url 
teste()
"""
