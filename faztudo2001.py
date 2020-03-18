import discord
import os
from random import randint
from ast import literal_eval

client = discord.Client()


async def RegistraMagia(message):
    #le o arquivo(txt) e 'converte' em dicionario
    with open ('testetxt') as le:
        variavel=literal_eval(le.read())
    msgr=message.content.lower().replace("!r","").split()
    #adiciona valor na variavel correspondente ao txt
    #msg[0]= nome da magia;
    #msg[-2]= dado da magia;
    #msg[-1]= quantidade de dados
    variavel[" ".join(msgr[0:-2])]=f'{msgr[-2]} {msgr[-1]}'
    #escreve o valor da variavel no txt
    with open ('testetxt', 'w') as escreve:
        escreve.write(str(variavel))
    await message.channel.send("Sua magia foi registrada no grimório com sucesso")

async def CastMagia(message):
     #le o arquivo(txt) e 'converte' em dicionario
    with open ('testetxt') as le:
        variavel=literal_eval(le.read())

    #recebe os valores da chave em '[]'
    variavel=variavel[message.content.lower().replace("!cast","").strip()]

    variavel=variavel.split()
    await RollDice(message,variavel,True)
    
async def CharlieBrown(message):
    await message.channel.send('brown'+message.content.lower().replace("charlie","").replace("!",""))

async def RollDice(message="", variavel=0, flag=False):
    #lista[0]=tipo de dado
    #lista[1]=vezes a rolar
    resul=[]
    if flag:
        lista=variavel
    else:
        lista=message.content.lower().replace("!d","").split()
    for x in range(int(lista[1])):
        resul.append(randint(1,int(lista[0].replace("d",""))))
    await message.channel.send(str(resul)[1:-1])
        
    
@client.event
async def on_ready():
     print(f'Logante como {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user: return None
        
    if message.content.lower().startswith('!'):
        if message.content.lower().replace("!","").startswith('charlie'):
            await CharlieBrown(message)
        if message.content.lower().replace("!","").startswith('d'):
            await RollDice(message)
        if message.content.lower().replace("!","").startswith('r'):
            await RegistraMagia(message)
        if message.content.lower().replace("!","").startswith('cast'):
            await CastMagia(message)
        

client.run(os.environ['mudaessafitan'])
