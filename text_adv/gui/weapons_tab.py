   
import customtkinter as ctk
class WeaponsFrame(ctk.CTkFrame):
    def __init__(self,parent):
        super().__init__(
            master = parent,
            
            )

  
        
        strength_attribute = character_attribute(self,label = "strength",count =0)
        dexitiy_attribtute = character_attribute(self,label ="dexity",count = 0)
        vitatlity = character_attribute(self,"vitality",count =0 )
        luck = character_attribute(self,"luck",count =0)

def character_attribute(parent,label,count):
    frame = ctk.CTkFrame(master=parent,width=80,height=30,corner_radius= 3)
    frame.pack_propagate(False)
    frame.pack(anchor = "w",pady=10,padx=10)

    attribute_label = ctk.CTkLabel(master = frame,text=label,font=ctk.CTkFont(size=13)).pack(side= "left",padx =4)
