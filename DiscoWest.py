import discord
from urllib.request import Request, urlopen
import random

TOKEN = "PUT TOKEN HERE"
keyword = "kanye"

client = discord.Client()
embed = discord.Embed()


@client.event
async def on_ready():
  print("Bot is ready to party, logged in as {0.user}.".format(client))

@client.event
async def on_message(message):
  global keyword
  if message.author == client.user:
    return
  elif keyword.lower() in message.content.lower():
    image_num = random.randint(1,5)
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3"}
    # reg_url = "https:XXXXOOOO"
    req = Request(url="https://api.kanye.rest", headers=headers) 
    html = urlopen(req).read().strip().decode()
    k_quote = html[9:]
    k_quote = k_quote[:-1]
    if image_num == 1 and image_num:
          embed.set_image(url="https://www.nicepng.com/png/full/227-2279480_kanye-west-full-body-png.png")
    elif image_num == 2 and image_num:
          embed.set_image(url="https://www.pngitem.com/pimgs/b/243-2434615_kanye-west-face-png.png")
    elif image_num == 3 and image_num:
          embed.set_image(url="http://clipart-library.com/image_gallery2/Kanye-West-PNG-HD.png")
    elif image_num == 4 and image_num:
          embed.set_image(url="http://clipart-library.com/images_k/kanye-transparent/kanye-transparent-2.png")
    elif image_num == 5 and image_num:
          embed.set_image(url="https://www.pngfind.com/pngs/b/1-16258_kanye-png.png")
    await message.channel.send(embed=embed) 
    await message.channel.send(f"{k_quote} - Kanye West")
  elif message.content.startswith("!set keyword"):
    keyword = message.content.strip()[13:]
    await message.channel.send(f"You can now call kanye with '{keyword}'.")
  else:
    return

client.run(TOKEN)