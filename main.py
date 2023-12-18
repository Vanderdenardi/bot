import discord
from discord.ext import tasks, commands
import asyncio
from datetime import datetime, timedelta

# Configurações
token = 'MTE4NjEyMDQxNzE0OTIwMjUyMg.Gs-Lit.n0j3D4EzaNdsyVBz0yeTAkkbcPCxvhPyy2uiJM'
channel_id = '1186126176956203060'

# Lista de mensagens
mensagens = [
    {
        'titulo': 'Reset do Servidor',
        'texto': 'Reset do servidor em 15 minutos, coloquem seus sets de poder máximo, ajude a manter o clã sempre no Top ranking!!!\n\nSe não doou, realize a doação antes da vida do servidor e realize as cooperações!!',
        'horario': '03:45',
    },
    {
        'titulo': 'Evento Krukan',
        'texto': 'Hoje tem Krukan fiquem ligados caso houver mudanças informaremos!',
        'horario': '19:00',
        'dia_semana': 'MON',
    },
    {
        'titulo': 'Evento Nerkan',
        'texto': 'Hoje tem Krukan fiquem ligados caso houver mudanças informaremos!',
        'horario': '19:00',
        'dia_semana': 'THU',
    },
    {
        'titulo': 'World Boss Labirinto',
        'texto': 'World Boss em 30 minutos, entre no discord para ouvir a call. World Boss 10:00 (horário do servidor)',
        'horario': '09:30',
    },
    {
        'titulo': 'World Boss Vale',
        'texto': 'World Boss em 30 minutos, entre no discord para ouvir a call. World Boss 12:00 (horário do servidor)',
        'horario': '11:30',
    },
    {
        'titulo': 'World Boss Labirinto',
        'texto': 'World Boss em 30 minutos, entre no discord para ouvir a call. World Boss 20:00 (horário do servidor)',
        'horario': '19:30',
    },
    {
        'titulo': 'World Boss Vale',
        'texto': 'World Boss em 30 minutos, entre no discord para ouvir a call. World Boss 22:00 (horário do servidor)',
        'horario': '21:30',
    },
    {
        'titulo': 'Guerra de Vale',
        'texto': 'Guerra de Vale em 30 minutos, entre no discord para ouvir a call. Início 22:00',
        'horario': '21:29',
        'dia_semana': 'WED',
    },
    {
        'titulo': 'Saque do Castelo',
        'texto': 'Guerra de Vale em 30 minutos, entre no discord para ouvir a call. Início 22:00',
        'horario': '21:29',
        'dia_semana': 'FRI',
    },
    {
        'titulo': 'Expedição do Clãn',
        'texto': 'Expedição do clã em 30 minutos, entre no discord para ouvir a call. Expedição do clãn sábado às 19:00 (horário do servidor)',
        'horario': '18:29',
        'dia_semana': 'SAT',
    },
    {
        'titulo': 'Desafio do Clãn',
        'texto': 'Expedição do clã em 30 minutos, entre no discord para ouvir a call. Expedição do clãn domingo às 19:00 (horário do servidor)',
        'horario': '18:29',
        'dia_semana': 'SUN',
    },
]

# Inicializa o bot
intents = discord.Intents.default()
intents.messages = True  # Permite a leitura de mensagens

bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print('Bot online!')
    # Inicia as tarefas agendadas
    for mensagem in mensagens:
        agendar_mensagem(mensagem)

# Função para agendar mensagens
def agendar_mensagem(mensagem):
    canal = bot.get_channel(int(channel_id))
    horario = obter_horario_mensagem(mensagem)

    @tasks.loop(seconds=60)
    async def enviar_mensagem():
        agora = datetime.now().strftime('%H:%M')
        if agora == horario:
            await canal.send(f'**{mensagem["titulo"]}**\n{mensagem["texto"]}')
            enviar_mensagem.stop()

    enviar_mensagem.start()

# Função para obter o horário da mensagem
def obter_horario_mensagem(mensagem):
    if 'dia_semana' in mensagem:
        horario = f'{mensagem["dia_semana"]} {mensagem["horario"]}'
    else:
        horario = mensagem['horario']
    return horario

bot.run(token)
