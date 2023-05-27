#######################模組#######################
import discord as dc
import os
from dotenv import load_dotenv as ld

#######################初始化#######################
ld()  #載入環境變數
bot = dc.bot()  #建立機器人


#######################事件#######################
@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")


#######################指令#######################
@bot.slash_command(name="hello", description="Say hello to the bot")
async def hello(ctx):
    """輸入hello, 會回傳Hey!"""
    await ctx.respond("Hey!")


#######################啟動#######################
def main():
    bot.run(os.getenv('TOKEN'))


if __name__ == '__main__':
    main()