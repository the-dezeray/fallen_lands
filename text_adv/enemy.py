class Enemy():

    def __init__(self) -> None:
        self.hp = 10
        self.dmg = 1
        self.name =''
        self.entity = None
    def do(self):
        self.entity.hp -= self.dmg
        print(f"the enemy has done {self.dmg}")   