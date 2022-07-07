import os
import discord
from dotenv import load_dotenv
import mysql.connector



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
        host="remotemysql.com",
        user="xkY2VihBPB",
        password="eed9xj8iHb",
        database="xkY2VihBPB",
        auth_plugin='mysql_native_password'
        )
        mycursor = Database.cursor()
        query = "SELECT * FROM property_cords"
        mycursor.execute(query)
        rows = mycursor.fetchall()
        flag = True
        for i in rows:
            if i[5] == message.author:
                flag = True
                pass
            else:
                flag = False
        if not flag:
            query = ""
        else:
            pass
        response = test_message
        await message.channel.send(response)
client.run(TOKEN)