class Bot:

    max_health = 100

    def __init__(self, bot_name):    #constructor runs once when an instance of the class is created
        self.health = 100 #attribute of the Bot instance
        self.bot_name = bot_name #attribute of the Bot instance 



    def take_damage(self, amount): #method
        self.health -= amount
        return self.health

    
    health = 100 #class attribute shared by all instances of the Bot class