print ("choose a character ")
characters =["thief","sword"]
for cha in characters:
    print(cha)
# a = input("\n enter char :n") 
class Item():
    def __init__(self) -> None:
        self.name = ""
        self.type = ""

class Weapon(Item):
    def __init__(self) -> None:
        super().__init__()
        self.type ="weapon"
        self.effect =""
        self.dmg =0
        self.condition =10
class Knife(Weapon):
    def __init__(self) -> None:
        super().__init__()
        self.name ="knife"
        self.dmg =10
class Player():
    def __init__(self) -> None:
        self.hp = 10
        self.dmg = 1
        self.entity = None
        self.inv = []
        self.inv.append(Knife())
        self.weapon = None
    def deal_dmg(self,weapon):
        self.entity.hp -= weapon.dmg
        print(f"you dealt {weapon.dmg}")

    def show_user_options(self):
        for count,i in enumerate (self.inv):
            if i.type == "weapon":
                print(f"{count}. choose  - {i.name} dmg = {i.dmg} condition ={i.condition} \n effect = {i.effect}")
        a = input("\ nenter input : ")
        self.deal_dmg(self.inv[int(a)])

class Enemy():

    def __init__(self) -> None:
        self.hp = 10
        self.dmg = 1
        self.name =''
        self.entity = None
    def do(self):
        self.entity.hp -= self.dmg
        print(f"the enemy has done {self.dmg}")        
class LVL():
    def __init__(self) -> None:
        self.entity = Enemy()
        self.entity.name ="desiree"

def fight(player,entity):
    player.entity = entity
    entity.entity = player
    while True:
        player.show_user_options()
        entity.do()

def main():
    player =  Player()
    level = []
    a = LVL()
    level.append(a)
    current_chapter = 0
    chapter = chapter.load()
    while True:
        event = story['current_chapter']["event"]
main()
