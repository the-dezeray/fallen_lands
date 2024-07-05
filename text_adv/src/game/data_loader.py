import yaml

from entity import Entity
from item import Item

from typing import Type
def load_instances_from_yaml(file_path,instance_class):
    with open(file_path, 'r') as file:
        data = yaml.safe_load(file)
        items  = []
        for item_data in data:
            item = instance_class(**item_data)
            items.append(item)
        return items
    
def load_story_from_yaml(file_path):
    with open(file_path,"r") as f :
        data = yaml.safe_load(f)
        return data
    
class Collection():
    def __init__(self,file_path :str ,instance_class:Type):
        self.array =[]
        self.array = load_instances_from_yaml(file_path,instance_class)
    def get(self,string):
        for i in self.array:
            print(i.name)
            if i.name == string: return i
class EntityCollection(Collection):
    def __init__(self, file_path: str, instance_class:Type):
        super().__init__(file_path, instance_class)
    def get(self,name :str= "",**kwargs):
        a = super().get(name)
        a.__dict__.update(kwargs)
        return a



from pathlib import Path

# Define the relative path to the file
story_file_path = Path(__file__).parent / "story_content" / "dialogues.yml"
item_file_path = Path(__file__).parent / "story_content" / "items.yml"
entity_file_path = Path(__file__).parent / "story_content" / "entities.yml"

STORY_DICT = load_story_from_yaml(story_file_path)
ITEM_COLLECTION = Collection(item_file_path,Item)
ENTITY_COLLECTION = EntityCollection(entity_file_path,Entity)

