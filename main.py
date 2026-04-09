import discord
from discord.ext import commands

# Настройка доступов
intents = discord.Intents.default()
intents.message_content = True # Чтобы бот видел текст сообщений

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Бот {bot.user} запущен!')

# Команда !сказать [текст]
@bot.command()
async def сказать(ctx, *, message):
    await ctx.message.delete() # Бот удалит твою команду, чтобы никто не видел
    await ctx.send(message)    # И напишет твой текст от своего имени

# Вставь сюда свой токен из Discord Developer Portal
bot.run('MTQ5MTQ1MzcxMTM4NDU4MDE1Ng.GBWPJW.P6dWjShXoGsGVQgsvvOLd1wA9YWSsHCBugbkuM')
