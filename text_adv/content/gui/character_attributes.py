   
import customtkinter as ctk
class CharacterAtrributesFrame(ctk.CTkFrame):
    def __init__(self,parent):
        super().__init__(
            master = parent,

            )
        strength_attribute = character_attribute(self,label = "strength",count =0)
        dexitiy_attribtute = character_attribute(self,label ="dexity",count = 0)
        vitatlity = character_attribute(self,"vitality",count =0 )
        luck = character_attribute(self,"luck",count =0)

def character_attribute(parent,label,count):
    frame = ctk.CTkFrame(master=parent,width=200,height=30)
    frame.pack_propagate(False)
    frame.pack(anchor ="w",pady=3)

    attribute_label = ctk.CTkLabel(master = frame,text=label,font=ctk.CTkFont(size=13)).pack(side= "left",padx =4)

    attribute_level_frame =ctk.CTkFrame(frame,width=50,height=20)
    attribute_level_frame.pack(side="right")
    attribute_level_frame.pack_propagate(False)

    attribute_level_count = ctk.CTkButton(attribute_level_frame,width=10,height=10,text="",fg_color = "green",corner_radius= 10).pack(padx=1,side="left")
