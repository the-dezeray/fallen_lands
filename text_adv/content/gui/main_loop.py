import customtkinter as ctk

#defaults
ctk.set_appearance_mode("System")  # Modes: system (default), light, dark
ctk.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title = "title"
        self.geometry("1280x720")
        from .left_frame import LeftFrame
        from .right_frame import RightFrame
        from .center_frame import CenterFrame

        self.left_frame = LeftFrame(master = self)
        self.center_frame = CenterFrame(master = self)
        self.right_frame= RightFrame(master=self)
def something():
    print("i work")

def main():
    app = App()
    app.mainloop()
def render_game():
    main()  
if __name__ == "main":    
    main()