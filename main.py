import discord
import random
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}, который поможет тебе сделать природу чище!')

@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)

@bot.command()
async def repeat(ctx, times: int, content: str):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)

@bot.command()
async def glob(ctx):
    await ctx.send('Глобальное потепление — долгосрочное повышение средней температуры Земли, происходящее уже более века, основной причиной чего является человеческая деятельность')

@bot.command()
async def prot(ctx):
    list_gl = ['Чаще пользуйся общественным транспортом, чтобы выброс опасных веществ в атмосферу был меньше.', 'Экономь энергию, например: суши постиранное белье на веревке, а не в электросушилке.', 'Сажай деревья - они очищают воздух, фильтруют воду и являются домом для 80% наземных животных.', 'Попроси помощи у друзей с каким-либо важным для природы делом, например: Займитесь сортировкой мусора вместе.', 'Ходи в магазин со своей сумкой, так ты уменьшиш выброс опасных газов при производстве пластиковых пакетов.', 
               'Экономь воду, например: При чистке зубов выключай ее.', 'Не оставляй много пищевых отходов, их можно использовать повторно, например: Сделать из них компост или удобрение для растений.', 'Выключай свет там, где он не нужен, так ты будешь беречь электроэнергию.']
    await ctx.send(f'Вот один из способов внести свой вклад в борьбу с глобальным потеплением - {random.choice(list_gl)}')

@bot.command()
async def plastic(ctx):
    list_pl = ['Из пластиковой бутылки можно сделать пенал, отрезав верхнюю часть, дополнительно украсив его.', "Из пластиковой бутылки можно сделать кормушку, она очень пригодится птицам.", 'Из пластиковой бутылки можно сделать горшок для небольшого растения.', "Из пластиковой бутылки можно сделать елочные игрушки."]
    await ctx.send(f'•{random.choice(list_pl)}')

@bot.command()
async def metal(ctx):
    list_mt = ['Создавай металлические скульптуры, светильники или настенные украшения, используя металлические пластины или проволоку.', "Из металлических уголков и листов можно собрать прочные полки для хранения вещей в гараже или мастерской.", 'Используй металлические пластины или трубки для создания держателей для инструментов.', "Из листового металла можно сделать простой ящик с замком для хранения ценностей."]
    await ctx.send(f'•{random.choice()}')


def calculate_carbon_footprint(driving_km: float, electricity_kwh: float, meat_days: int) -> float:
    car_emission_per_km = 0.12  
    electricity_emission_per_kwh = 0.475  
    meat_emission_per_day = 5.0  
    total_emission = (driving_km * car_emission_per_km) + (electricity_kwh * electricity_emission_per_kwh) + (meat_days * meat_emission_per_day)
    return total_emission

@bot.command(name='carbon', help="Рассчитайте свой углеродный след. Введите расстояние (км), электричество (кВт⋅ч) и дни с мясом.")
async def carbon_footprint(ctx, driving_km: float, electricity_kwh: float, meat_days: int):
    try:
        total_emission = calculate_carbon_footprint(driving_km, electricity_kwh, meat_days)
        if total_emission > 200:
            status = "Опасно! Ваш углеродный след высок и может сильно повлиять на окружающую среду."
        else:
            status = "Не опасно. Ваш углеродный след в пределах нормы."
        await ctx.send(f"Ваш углеродный след составляет примерно {total_emission:.2f} кг CO2. {status}")
    except Exception as e:
        await ctx.send(f"Произошла ошибка: {str(e)}")

bot.run("")