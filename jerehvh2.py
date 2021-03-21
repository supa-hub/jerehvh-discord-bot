import discord
import requests
from bs4 import BeautifulSoup
import asyncio
import time
from discord.ext import commands
activate = 0
sivu = requests.get("https://www.gametracker.com/server_info/95.217.39.250:27061/")
sivu2= requests.get("https://www.gametracker.com/server_info/95.216.234.245:27052/")
soppa = BeautifulSoup(sivu.content, "html.parser")
soppa2 = BeautifulSoup(sivu2.content, "html.parser")

class info():
    def __init__(self):
        self.status_info = []
        self.status_info2 = []
        self.soppa = BeautifulSoup(sivu.content, "html.parser")
        self.servu_nimi = soppa.find(xpath="/html/body/div[3]/div[4]/div[1]/span[2]/a/span")
        self.ip = soppa.find("div", class_="block630_content_left")
        self.ip2 = soppa2.find("div", class_="block630_content_left")
        self.online = soppa.find("span", class_="item_color_success")
        self.online2 = self.online.string
        self.status_info.append(self.online2)
    def tell_info(self):
        self.sivu = requests.get("https://www.gametracker.com/server_info/95.217.39.250:27061/")
        self.soppa = BeautifulSoup(self.sivu.content, "html.parser")
        self.pelaajalista = self.soppa.find(id="HTML_num_players")
        return self.pelaajalista.text
    def tell_ip(self):
        a = []
        for ip_nimi in self.ip.find_all("a", href=True):
            a.append(ip_nimi.attrs)
        ip_juu = str(a[0])
        ip_juu2 = ip_juu.split("/")
        return ip_juu2[2]
    def tell_online(self):
        self.online = soppa.find("span", class_="item_color_success")
        print(self.online2)
        if self.online.string in self.status_info:
            self.online = "Online :white_check_mark:"
        else:
            self.online = "Offline :x:"
        return self.online
    def tell_info2(self):
        self.sivu = requests.get("https://www.gametracker.com/server_info/95.216.234.245:27052/")
        self.soppa = BeautifulSoup(self.sivu.content, "html.parser")
        self.pelaajalista2 = self.soppa.find(id="HTML_num_players")
        return self.pelaajalista2.text

    def tell_ip2(self):
        a2 = []
        for ip_nimi in self.ip2.find_all("a", href=True):
            a2.append(ip_nimi.attrs)
        ip_juu3 = str(a2[0])
        ip_juu4 = ip_juu3.split("/")
        return ip_juu4[2]
    def tell_online2(self):
        self.online = soppa.find("span", class_="item_color_success")
        print(self.online2)
        if self.online.string in self.status_info:
            self.online = "Online :white_check_mark:"
        else:
            self.online = "Offline :x:"
        return self.online

def read_token():
    with open("token2.txt", "r") as f:
              lines = f.readlines()
              return lines[0].strip()

#waiha token 
token = "ODA5Njc4OTA5MzczMDIyMjEw.YCYmPw.rzdaR-wLdjG6-7KOjDfVj5yZH2k"


client = commands.Bot(command_prefix="!")

pelaajainfo = info()
@client.event
async def on_ready():
    #await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Discord.io/JereHvH"))
    await client.change_presence(status=discord.Status.do_not_disturb, activity=discord.Activity(type=discord.ActivityType.watching, name="Discord.io/JereHvH"))

@client.command()
async def info(ctx):
    activate = 1
    await info2(ctx)
    while activate == 1:
        time.sleep(20)
        await info3(ctx)

activate2 = 0
async def info2(ctx):
    global activate2
    global viesti
    global viesti2
    if activate2 == 0:
        pelaajamäärä = pelaajainfo.tell_info()
        ip_nimi = pelaajainfo.tell_ip()
        tell_online = pelaajainfo.tell_online()
        pelaajamäärä2 = pelaajainfo.tell_info2()
        ip_nimi2 = pelaajainfo.tell_ip2()
        tell_online2 = pelaajainfo.tell_online2()
        embed = discord.Embed(title="Server:", description="[JereHvH | EU | 16K | Mirage Only]", colour=discord.Colour.blue())
        embed2 = discord.Embed(title="Server:", description="[JereHvH | EU | 16K | Office Only]", colour=discord.Colour.blue())
        embed.set_thumbnail(url=r"https://cdn.discordapp.com/attachments/546146847396462603/809858166472310784/jerehvh.png")
        embed.add_field(name="Player count:", value=pelaajamäärä + "/24")
        embed.add_field(name="|",value="|")
        embed.add_field(name="IP:", value=ip_nimi + "    steam://connect/"+ip_nimi)
        embed.add_field(name="Status:",value=tell_online)
        embed.add_field(name="|",value="|")
        embed.add_field(name="Map:",value="de_mirage")
        embed2.set_thumbnail(url=r"https://cdn.discordapp.com/attachments/546146847396462603/809858166472310784/jerehvh.png")
        embed2.add_field(name="Player count:", value=pelaajamäärä2 + "/14")
        embed2.add_field(name="|",value="|")
        embed2.add_field(name="IP:", value=ip_nimi2 + "    steam://connect/"+ip_nimi2)
        embed2.add_field(name="Status:",value=tell_online2)
        embed2.add_field(name="|",value="|")
        embed2.add_field(name="Map:",value="de_office")
        viesti = await ctx.send(embed=embed)
        viesti2 = await ctx.send(embed=embed2)
        activate2 = 1


async def info3(ctx):
    pelaajamäärä = pelaajainfo.tell_info()
    ip_nimi = pelaajainfo.tell_ip()
    tell_online = pelaajainfo.tell_online()
    embed = discord.Embed(title="Server name", description="[JereHvH | EU | 16K | Mirage Only]", colour=discord.Colour.blue())
    embed.set_thumbnail(url=r"https://cdn.discordapp.com/attachments/546146847396462603/809858166472310784/jerehvh.png")
    embed.add_field(name="Player count:", value=pelaajamäärä +"/24")
    embed.add_field(name="|",value="|")
    embed.add_field(name="IP:", value=ip_nimi + "    steam://connect/"+ip_nimi)
    embed.add_field(name="Status:",value=tell_online)
    embed.add_field(name="|",value="|")
    embed.add_field(name="Map:",value="de_mirage")
    pelaajamäärä2 = pelaajainfo.tell_info2()
    ip_nimi2 = pelaajainfo.tell_ip2()
    tell_online2 = pelaajainfo.tell_online2()
    embed2 = discord.Embed(title="Server:", description="[JereHvH | EU | 16K | Office Only]", colour=discord.Colour.blue())
    embed2.set_thumbnail(url=r"https://cdn.discordapp.com/attachments/546146847396462603/809858166472310784/jerehvh.png")
    embed2.add_field(name="Player count:", value=pelaajamäärä2 + "/14")
    embed2.add_field(name="|",value="|")
    embed2.add_field(name="IP:", value=ip_nimi2 + "    steam://connect/"+ip_nimi2)
    embed2.add_field(name="Status:",value=tell_online2)
    embed2.add_field(name="|",value="|")
    embed2.add_field(name="Map:",value="de_office")
    await viesti.edit(embed=embed)
    await viesti2.edit(embed=embed2)


client.run(token)
