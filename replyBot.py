import discord 
import random

word_list = [word.strip() for word in open('INSERT_WORD_LIST','r').readlines()]
name_list = [word.strip() for word in open('INSERT_NAME_LIST','r').readlines()]


intents = discord.Intents.default()
intents.message_content = True



client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return 
    if message.content.startswith('$hello'):
        await message.channel.send(f'Chup kar { random.choice(name_list)} ke { random.choice(word_list) } ',mention_author=True)
    
    

client.run('INSERT_API_TOKEN_KEY')