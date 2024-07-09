from threading import Thread
from enum import Enum, auto
from queue import Queue

import customtkinter as ctk

from gui.left_frame import LeftFrame
from gui.right_frame import RightFrame
from gui.center_frame import CenterFrame
from core.main import load_game,start_core


#defaults
ctk.set_appearance_mode("System")  # Modes: system (default), light, dark
ctk.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green
class TicketPurpose(Enum):
    UPDATE_PROGRESS = auto()
    
class Ticket():
    def __init__(self,ticket_type:TicketPurpose,ticket_value:str):
        self.ticket_type = ticket_type

class GUI(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title = "title"
        self.geometry("1280x720")
        self.gui_updates_queue = Queue()
        self.bind("<<Check-Gui-Updates-Queue>>",self.update_gui)

        self.left_frame = LeftFrame(master = self)
        self.center_frame = CenterFrame(master = self)
        self.right_frame= RightFrame(master=self)
    def update_gui(self)->None:
        ticket : Ticket
        ticket =self.gui_updates_queue.get()

        match(ticket.ticket_type):
            case TicketPurpose.UPDATE_PROGRESS:
                pass
            case _:
                pass
    def display_simple_message(self):
        ticket = Ticket(ticket_type=TicketPurpose.UPDATE_PROGRESS, ticket_value="1")
        self.gui_updates_queue.put("dfasd") 

def main():
    gui = GUI()

    gui.mainloop()
def render_game():
    interface = GUI()
    start_core(gui = interface)
    interface.mainloop()
if __name__ == "main":    
    main()