import customtkinter as ctk
from mini_player_status_bar import MiniPlayerStatusBar
class LeftFrame(ctk.CTkFrame):
    def __init__(self,master):
        super().__init__(
        
        master = master,
        width=300,
        height=720,
        border_width=1)
        
        
        self.pack_propagate(False)
        self.pack(side ="left",padx = 20)
        self.mini_player_status= MiniPlayerStatusBar(self)



        self.effects_name_label = ctk.CTkLabel(self,text="state",font=ctk.CTkFont(size=13)).pack(anchor = "w",padx =4)
        self.strength_label =  ctk.CTkLabel(self,text="Attributes",font=ctk.CTkFont(size=13)).pack(anchor = "w",padx =4)
        self.speed_label =  ctk.CTkLabel(self,text="Attribute",font=ctk.CTkFont(size=13)).pack(anchor = "w",padx =4)
        self.dexirity_label =  ctk.CTkLabel(self,text="Attributes",font=ctk.CTkFont(size=13)).pack(anchor = "w",padx =4)
        self.w1= ctk.CTkLabel(self,text="WEAPON 1",font=ctk.CTkFont(size=15)).pack(anchor = "w",padx =4)
        self.w2 =  ctk.CTkLabel(self,text="WEAPON 2",font=ctk.CTkFont(size=15)).pack(anchor = "w",padx =4)
        self.w3 =  ctk.CTkLabel(self,text="WEAPON 3",font=ctk.CTkFont(size=15)).pack(anchor = "w",padx =4)
        self.w4 =  ctk.CTkLabel(self,text="WEAPON 4",font=ctk.CTkFont(size=15)).pack(anchor = "w",padx =4)
        
if __name__ == "__main__":
    from gui import main    
    main()