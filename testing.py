import yaml


class Dialogue():
    def __init__(self) -> None:
        self.cur= None
        self.dialogues = None

with open("log.yml","r") as f :
    data = yaml.safe_load(f)
current_chapter = "chapter1"

chapter = data[current_chapter]

main_dialogue = chapter["dialogue"]
dialogue = main_dialogue["start"]
print(dialogue["text"])
for i in dialogue["choices"]:
    print(i["text"])
us = 1
next_node = 1
b = dialogue["choices"][1]
next_node = b["next_node"]
a=main_dialogue
dialogue = main_dialogue[next_node]
print(next_node)

current_chapter = "chapter2"
chapter = data[current_chapter]
main_dialogue = chapter["dialogue"]
dialogue = main_dialogue["start"]
print(dialogue["text"])
for i in dialogue["choices"]:
    print(i["text"])
us = 1
def fight(name,lvl):
    pass
if i["function"] != None:
    exec(i["function"])