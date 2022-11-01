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

    def is_same_setting(self, num):
        if self.__top == num[0] and self.__fro == num[1] and self.__rig == num[2] and \
            self.__lef == num[3] and self.__bac == num[4] and self.__bot == num[5] :
            return True

    def is_same_dice(self, num):
        is_same = False
        for _ in range(2):
            for _ in range(3):
                for  _ in range(4):
                    if self.is_same_setting(num):
                        is_same = True
                    self.roll__e()
                self.roll__n()
            self.roll__w()
            self.roll__s()
        return is_same

dice1 = list(map(int,input().split()))
dice2 = list(map(int,input().split()))

dice = Dice(dice1)
if dice.is_same_dice(dice2):
    print("Yes")
else:
    print("No")
    
