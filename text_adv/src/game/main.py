from player import Player
from _functions import Fight,get_user_input
from data_loader import ENTITY_COLLECTION,ITEM_COLLECTION,STORY_DICT

import yaml

class Dialogue():
    def __init__(self) -> None:
        self.cur= None
        self.dialogues = None

main_story_dict = STORY_DICT
chapter_name= "chapter1"      

player = Player()

player.inv.add(ITEM_COLLECTION.get("knife"))
player.inv.add(ITEM_COLLECTION.get("sword"))

while True:
    current_chapter = main_story_dict[chapter_name]
    print("\n ------------------------------------")
    print(f"LOCATION - {current_chapter["location"]} \n")
    print(f"{current_chapter["text"]}")
    available_choices = 0
    choices = current_chapter["choices"]
    for index,choice in enumerate(choices):
        available_choices +=1
        print(f"    {index} - {choice["text"]}")

    inputs = get_user_input(available_choices)
     
    function_string =choices[inputs]["function"]
    if function_string != None:
        exec(function_string)
    chapter_name = choices[inputs]["next_node"]
if __name__ == "main":
    main()
    