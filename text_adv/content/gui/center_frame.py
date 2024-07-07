import customtkinter as ctk
class CenterFrame(ctk.CTkFrame):
    def __init__(self,master):
        super().__init__(
        
        master = master,
        width=800,
        height=720,
        border_width=1,
        border_color="black")
        
        self.pack_propagate(False)
        self.pack(side ="left",padx = 20)