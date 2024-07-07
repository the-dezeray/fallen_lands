
class Entity():
    def __init__(self,**kwargs) -> None:
        self.name = kwargs.get('name')
        self.lvl = kwargs.get('lvl')
        self.hp =100
        self.dmg = 6