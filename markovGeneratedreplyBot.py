import discord 
from markov import Markov

trainingData = "INSERT_DATA_LOCATION"
order = 3 
generate_size = 1000 

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
    if message.content.startswith('INSERT_TRIGGER'):
        await message.channel.send(Markov.generate_text(trainingData,order,generate_size),mention_author=True)
    
    

client.run('INSERT_API_TOKEN')