from cProfile import label
import asyncio
import discord
from discord import ButtonStyle
from discord.ext import commands
from discord.ui import Button, View

import time


from vinted import *

intents = discord.Intents.default()
intents.message_content = True
bot =commands.Bot(command_prefix='!',description="bot teste",intents=intents)
"""@bot.event
async def on_ready():
    print("ready")"""


posting = []
@bot.command()



async def bouton(ctx):
    while True:
        try:
            z = search("https://www.vinted.fr/vetements?catalog%5B%5D=76&order=newest_first&price_to=15&currency=EUR&brand_id%5B%5D=304")
            x = z["items"]["catalogItems"]["byId"]
            dictlist = list(x)
            for i in range(9, -1, -1):
                    time.sleep(0)
                    post = dictlist[i - 1]
                    if str(post) in posting:
                        print(f"{Spy.blanc}[{Spy.rouge}{post}{Spy.blanc}] - Item déjà envoyé !")
                        time.sleep(0)
                        continue
                    else:
                        print(f"{Spy.blanc}[{Spy.vert}{post}{Spy.blanc}] - Nouvel item trouvé !")
                        info = get_info_post(x[str(post)]["url"])
                        posting.append(str(post))


                        embed=discord.Embed(title=f"{x[post]['title']}",url=f"{x[post]['url']}",color=0xef9aff)
                        embed.set_author(name="RESELL EXPO",icon_url="https://cdn.discordapp.com/avatars/1010967491733901482/b068cfb2fa571f847b0b959060702dc6.png")
                        embed.set_image(url=f"{x[post]['photo']['thumbnails'][4]['url']}")
                        embed.add_field(name="Auteur",value=f"{info['username']}",inline=False)
                        embed.add_field(name="Prix",value=f"{x[post]['price']} €")
                        embed.add_field(name="Taille",value=f"{x[post]['size_title']}")
                        embed.add_field(name="Marque",value=f"{x[post]['brand_title']}")
                        buttonacheter = Button(label="Acheter",style=discord.ButtonStyle.green, emoji="💵",url=f"https://www.vinted.fr/transaction/buy/new?source_screen=item&transaction%5Bitem_id%5D={str(post)}")
                        buttonfavorie = Button(label="Négociation",style=discord.ButtonStyle.danger, emoji="🤝",url=f"https://www.vinted.fr/items/{str(post)}/want_it/new?button_name=receiver_id={str(post)}")
                        buttondetails = Button(label="Détails",style=discord.ButtonStyle.grey, emoji="🔎",url=f"{x[post]['url']}")
                        
                        
                        view=View()
                        view.add_item(buttondetails)
                        view.add_item(buttonacheter)
                        view.add_item(buttonfavorie)
                                        

                       
                        print(f"{Spy.blanc}[{Spy.bleu}ENVOYER{Spy.blanc}] - L'article a été envoyer ! {Spy.vert}{post}")
                        await ctx.send(embed=embed,view=view)
                        time.sleep(0)
        except:
            print(f"{Spy.blanc}[{Spy.rouge}ERREUR{Spy.blanc}] - L'envoi na pas été réusi!")
            time.sleep(0)






token=input("entrer vitre token: ")

bot.run(token)

