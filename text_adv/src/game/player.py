class Player():
    def __init__(self) -> None:
        self.hp :float = 10.0
        self.dmg = 1
        self.entity = None
        from inventory import Inventory
        self.inv = Inventory()
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