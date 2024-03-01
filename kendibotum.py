import discord
import random
import time
from discord.ext import commands


intents = discord.Intents.default()
intents.message_content = True


bot = commands.Bot(command_prefix='$', intents=intents)


@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')


@bot.command()
async def merhaba(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}. Bana oynamak istediğin oyunu söyle! Birlikte yazı tura, taş kağıt makas, zar atma oynayabiliriz. Kitap tavsiyesi de verebilirim :)')
    

@bot.command()
async def yazitura(ctx,tahmin):
    a=["yazı","tura"]
    b=random.choice(a)
    if tahmin==b:
        await ctx.send("doğru tahmin ettin")
    else:
        await ctx.send(f"yanlış tahmin ettin, cevap {b}")

@bot.command()
async def tas_kagıt_makas(ctx, tahmin):
    x=["taş","kağıt","makas"]
    y=random.choice(x)
    
    if y== "taş" and tahmin=="makas":
        await ctx.send("Yanlış tahmin ettin ve seni yendim! Ben taş tutmuştum.")
    elif y== "taş" and tahmin=="kağıt":
        await ctx.send("Beni yendin! Tebrikler. Ben taş tutmuştum")    
    elif y=="taş" and tahmin=="taş":
        await ctx.send("Berabere kaldık! Aynı şeyi tutmuşuz :)")

    if y== "makas" and tahmin=="kağıt":
        await ctx.send("Yanlış tahmin ettin ve seni yendim! Ben taş tutmuştum.")
    elif y== "makas" and tahmin=="taş":
        await ctx.send("Beni yendin! Tebrikler. Ben makas tutmuştum.")    
    elif y=="makas" and tahmin=="makas" :
        await ctx.send("Berabere kaldık! Aynı şeyi tutmuşuz :)")

    if y== "kağıt" and tahmin=="taş":
        await ctx.send("Yanlış tahmin ettin ve seni yendim! Ben taş tutmuştum.")
    elif y== "kağıt" and tahmin=="makas":
        await ctx.send("Beni yendin! Tebrikler. Ben kağıt tutmuştum")    
    elif y=="kağıt" and tahmin=="kağıt":
        await ctx.send("Berabere kaldık! Aynı şeyi tutmuşuz :)")




@bot.command()
async def zar_atma(ctx, tahmin:int):
    z=[1,2,3,4,5,6]
    t=random.choice(z)
    if tahmin==t:
        await ctx.send(f"Aynı sayıyı attık! Bu sayıların toplamı: {t+tahmin} " )
    else:
        await ctx.send(f"Sen {tahmin} attın! Sayılarımızın toplamı: {t+tahmin} Benim attığım sayıyı bulabilir misin?")
        time.sleep(5)
        await ctx.send(f"Benim sayım {t}'idi!")
















bot.run("MTIwNTU4MTY1OTcyMjg3OTAxOA.G832xt.FsKXDNalremyjiIKITCaIHBdGJXHSE9RG0ixug")