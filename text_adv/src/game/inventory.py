class Inventory():
    def __init__(self) -> None:
        self.array = []
    def get(self,string):
        for i in self.array:
            print(i.name)
            if i.name == string: return i
    def add(self,instance):
        for i in self.array:
            if i.name == instance.name:
                i.count += 1
                return 0
            
        self.array.append(instance)
    def list(self,argument):
        array = []
        for i in self.array:
            if i.type == argument:
                array.append(i)
        return array