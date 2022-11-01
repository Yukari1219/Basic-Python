class Dice:
    def __init__(self, num):
        self.__top = num[0]
        self.__fro = num[1]
        self.__rig = num[2]
        self.__lef = num[3]
        self.__bac = num[4]
        self.__bot = num[5]

    def roll__n(self):
        self.__top, self.__fro, self.__bot, self.__bac = self.__fro, self.__bot, self.__bac, self.__top

    def roll__s(self):
        self.__top, self.__fro, self.__bot, self.__bac = self.__bac, self.__top, self.__fro, self.__bot
   
    def roll__e(self):
        self.__top, self.__lef, self.__bot, self.__rig = self.__lef, self.__bot, self.__rig, self.__top

    def roll__w(self):
        self.__top, self.__lef, self.__bot, self.__rig = self.__rig, self.__top, self.__lef, self.__bot

    def show_top(self):
        return self.__top

sides = list(map(int,input().split()))
directions = list(input())

dice = Dice(sides)

for d in directions:
    if d == "N":
        dice.roll__n()
    if d == "S":
        dice.roll__s()
    if d == "E":
        dice.roll__e()
    if d == "W":
        dice.roll__w()

print(dice.show_top())
