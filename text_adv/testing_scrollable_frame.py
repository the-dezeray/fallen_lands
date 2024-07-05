import tkinter as tk
import customtkinter as ctk

ctk.set_appearance_mode("System")  # Modes: system (default), light, dark
ctk.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

app = ctk.CTk()  # create CTk window like you do with the Tk window
app.geometry("1280x720")

def button_function():
    print("button pressed")

class App(ctk.CTK):
    def __init__(self):
        super().__init__()
        self.title = "title"
        self.geometry("1280x720")
        from left_frame import LeftFrame
        from right_frame import RightFrame
        from center_frame import CenterFrame

        self.left_frame = LeftFrame(parent = self)
        self.center_frame = CenterFrame(parent = self)
        self.right_frame= RightFrame(parent=self)
        
m_frame= ctk.CTkScrollableFrame(app,width=800,height=720,border_width=1,border_color="black")

m_frame.pack()

label = ctk.CTkLabel(m_frame,width=40,height=40,text="desd",font=ctk.CTkFont(size=30))
label.pack(expand = True,fill ="both")


af =ctk.CTkFrame(m_frame,width =100,height =150,border_width=1,border_color="black")
af.pack(anchor ="w")
button = ctk.CTkButton(af,width=40,height=40,text="how are you my brother are you doing well",bg_color="transparent",fg_color="transparent",font=ctk.CTkFont(size=15))
button.pack_propagate(False)
button.pack(side = "left")
a = ctk.CTkFrame(m_frame,width =150,height =50)
a.pack_propagate(False)
a.pack(anchor ="w",pady = 5)
b1 = ctk.CTkButton(a,width=40,height=40,text="not fine",bg_color="transparent",text_color="grey",fg_color="transparent",border_color="grey",border_width=1,font=ctk.CTkFont(size=15))
b1.pack(side ="left",padx = 5)
b2= ctk.CTkButton(a,width=40,height=40,text="am fine",bg_color="transparent",text_color="grey",fg_color="transparent",border_color="grey",border_width=1,font=ctk.CTkFont(size=15))
b2.pack(side="right",padx = 5)
# Use CTkButton instead of tkinter Button


af1 =ctk.CTkFrame(m_frame,width =100,height =150,border_width=1,border_color="black")
af1.pack(anchor ="w")
button2 = ctk.CTkButton(af1,width=40,height=40,text="how are you my brother are you doing well",bg_color="transparent",fg_color="transparent",font=ctk.CTkFont(size=15))
button2.pack_propagate(False)
button2.pack(side = "left")
a1 = ctk.CTkFrame(m_frame,width =150,height =50)
a1.pack_propagate(False)
a1.pack(anchor ="w",pady = 5)
b11 = ctk.CTkButton(a1,width=40,height=40,text="not fine",bg_color="transparent",text_color="grey",fg_color="transparent",border_color="grey",border_width=1,font=ctk.CTkFont(size=15))
b11.pack(side ="left",padx = 5)
b21= ctk.CTkButton(a1,width=40,height=40,text="am fine",bg_color="transparent",text_color="grey",fg_color="transparent",border_color="grey",border_width=1,font=ctk.CTkFont(size=15))
b21.pack(side="right",padx = 5)
# Use CTkButton instead of tkinter Button



app.mainloop()  