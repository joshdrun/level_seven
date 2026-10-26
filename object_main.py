from objects import Bot

bot1 = Bot("chat")
bot2 = Bot("steve")
bot1.take_damage(30)
bot2.take_damage(50)
print(bot1.health)
print(bot1.bot_name)
print(bot2.health)
print(bot2.bot_name)