import os
import discord
from dotenv import load_dotenv
import mysql.connector
class Coord:
    def __init__(self, x1, z1, x2, z2):
        self.x1 = x1
        self.x2 = x2
        self.z1 = z1
        self.z2 = z2
    def GetArea(self):
        deb = 0
        if self.x1 > 0 and self.x2 > 0 or self.x1 < 0 and self.x2 <0:
            if self.x1 > self.x2:
                deb = (abs(self.x1) - abs(self.x2)) + 1
            else:
                deb = (abs(self.x2) - abs(self.x1)) + 1
        elif self.x1 >= 0 and self.x2 <=0 or self.x1 <= 0 and self.x2 >= 0:
            deb = (abs(self.x1) + abs(self.x2)) + 1
        if self.z1 > 0 and self.z2 > 0 or self.z1 < 0 and self.z2 < 0:
            if self.z1 > self.z2:
                ate = (abs(self.z1) - abs(self.z2) ) + 1
            else:
                ate = (abs(self.z2) - abs(self.z1)) + 1
        elif self.z1 >= 0 and self.z2 <= 0 or self.z1 <=0 and self.z2 >=0:
            ate = (abs(self.z1) + abs(self.z2)) + 1
        return (deb * ate)


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break
    print(f'{client.user} has connected to discord' f'{guild.name}(id: {guild.id})')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(f'Hi {member.name}, welcome to a Brave New Realm!')

@client.event
async def on_message(message):
    if '!coords' in message.content:
        Database = mysql.connector.connect(
        host="localhost",
        user="BotDis",
        password="Jacob123",
        database="snowdenmc",
        auth_plugin='mysql_native_password'
        )
        mycursor = Database.cursor()
        query = "SELECT * FROM coords"
        mycursor.execute(query)
        rows = mycursor.fetchall()
        flag = False
        try:
            for i in rows:
                if i[5] == message.author:
                    flag = True
                else:
                    flag = False
            if not flag:
                print ("if")
                fcord = False
                count = 0
                x1 = 0
                x2 = 0
                z1 = 0
                z2 = 0
                for i in message.content:
                    if i == '(' and fcord == False:
                        fcord = True
                        print ("loop1")
                        end = message.content.index(')')
                        start = count
                        mid = message.content.index(',')
                        x1 = float(message.content[start+1:mid])
                        z1 = float(message.content[mid+1:end])
                    elif i == '(' and fcord == True:
                        end = message.content.rfind(')')
                        start = count
                        mid = message.content.rfind(',')
                        x2 = float(message.content[start+1:mid])
                        z2 = float(message.content[mid+1:end])
                    count += 1
                panda = Coord(x1, z1, x2, z2)
                query = ""
            else:
                query = ""
        except:
            pass
        response = panda.GetArea()
        await message.channel.send(response)
client.run(TOKEN)