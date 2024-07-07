import customtkinter as ctk
from .mini_player_status_bar import MiniPlayerStatusBar
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
        from .character_attributes import CharacterAtrributesFrame
        self.character_attributes  = CharacterAtrributesFrame(parent= self).pack(anchor = "w",pady =5)

        from .weapons_tab import WeaponsFrame
        self.weapnons = WeaponsFrame(parent = self).pack()


        self.w1= ctk.CTkLabel(self,text="WEAPON 1",font=ctk.CTkFont(size=15)).pack(anchor = "w",padx =4)
        self.w2 =  ctk.CTkLabel(self,text="WEAPON 2",font=ctk.CTkFont(size=15)).pack(anchor = "w",padx =4)
        self.w3 =  ctk.CTkLabel(self,text="WEAPON 3",font=ctk.CTkFont(size=15)).pack(anchor = "w",padx =4)
        self.w4 =  ctk.CTkLabel(self,text="WEAPON 4",font=ctk.CTkFont(size=15)).pack(anchor = "w",padx =4)
        
if __name__ == "__main__":
    from main_loop import main    
    main()