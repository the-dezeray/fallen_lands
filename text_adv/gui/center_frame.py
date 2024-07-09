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
        ctk.CTkLabel(self,text="Location >> Fallen-Lands",font = ctk.CTkFont(size =20)).pack(padx = 10,pady =5,anchor ='w')
        ctk.CTkLabel(self,text ="stanger",font = ctk.CTkFont(size =15)).pack(padx =20, anchor = "w")
        self.sad = ctk.CTkFrame(self,fg_color="transparent")
        self.sad.pack(anchor ="w",padx = 30)
        self.text = ctk.CTkLabel(master=self.sad,text="You seem lost where do you think are going to ",anchor="w")
        self.text.pack(padx=5,pady=5,anchor="w")
        self.dc = ctk.CTkFrame(self.sad)
        self.dc.pack()
        self.choice1 = ctk.CTkButton(master=self.dc,text = "am well")
        self.choice1.pack(padx =7,pady = 7,side ="left")
        
        self.choice2 = ctk.CTkButton(master=self.dc,text = "am well")
        self.choice2.pack(padx =7,pady = 7,side ="left")
        

        ctk.CTkLabel(self,text ="stanger",font = ctk.CTkFont(size =15)).pack(padx =20, anchor = "w")
        self.sad1 = ctk.CTkFrame(self,fg_color="transparent")
        self.sad1.pack(anchor ="w",padx = 30)
        self.text1 = ctk.CTkLabel(master=self.sad,text="You seem lost where do you think are going to ",anchor="w")
        self.text1.pack(padx=5,pady=5,anchor="w")
        self.choice11 = ctk.CTkButton(master=self.sad,text = "am well")
        self.choice11.pack(padx =7,pady = 7,side ="left")
        
        self.choice21 = ctk.CTkButton(master=self.sad,text = "am well")
        self.choice21.pack(padx =7,pady = 7,side ="left")

