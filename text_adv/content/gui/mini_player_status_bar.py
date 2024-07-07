   
import customtkinter as ctk
class MiniPlayerStatusBar(ctk.CTkFrame):
    def __init__(self,master):
        super().__init__(
        
        master = master,
        width=250,
        
        height=80,)

        
        self.pack_propagate(False)
        self.pack(anchor = "w",pady =5,padx=4)
        self.player_name_label = ctk.CTkLabel(self,text="The Hero",font=ctk.CTkFont(size=15)).pack(anchor = "w",padx =4,pady = 3)
        self.player_level_bar = ctk.CTkProgressBar(self,height = 5,progress_color="#32CD32",width=250).pack(padx=5,anchor="w")
        self.player_current_level_label = ctk.CTkLabel(self,text="hp 04",text_color="#32CD32",font=ctk.CTkFont(size=12)).pack(side ="right",padx =40,pady =4)
        self.player_poison = ctk.CTkButton(self,text="P",width=7,height=7).pack(side ="left",pady=3,padx=4)