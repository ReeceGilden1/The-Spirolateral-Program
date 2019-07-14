from tkinter import *

class Spirolateral:
    def __init__(self,name,dr_list):
        self.name = name
        self.dr_list = dr_list

class Gui:
    def __init__(self, master):
        self.drs = []
        self.COLOUR_BG = "yellow"
        PAD_LX = 30
        PAD_LY = 20
        PAD_BX = 6
        PAD_BY = 6
        WIDTH = 40

        self.frame_menu = Frame(master, background = self.COLOUR_BG)
        self.frame_menu.grid(row = 0, column = 0, columnspan = 2,sticky = 'nesw')

        self.frame_secondary = Frame(master, background = self.COLOUR_BG)
        self.frame_secondary.grid(row = 1, column = 1, sticky = 'nesw')

        self.root_frame = Frame(master, background = self.COLOUR_BG)
        self.root_frame.grid(row = 2, column = 1, sticky = 'nesw')

        self.label_menu = Label(self.frame_menu, text = "Menu", background = self.COLOUR_BG)
        self.label_menu.grid(row = 0, column = 0, rowspan = 2, padx = PAD_LX)

        self.button_info = Button(self.frame_menu, text="Information", command = self.info)
        self.button_info.grid(row = 1, column = 1, padx = PAD_BX, pady = PAD_BY,sticky = EW)

        self.button_add = Button(self.frame_menu, text="Add List", command = self.add_root)
        self.button_add.grid(row = 1, column = 2, padx = PAD_BX, pady = PAD_BY,sticky = EW)

        self.button_quit = Button(self.frame_menu, text="Quit Program", command = root.destroy)
        self.button_quit.grid(row = 2, column = 2, padx = PAD_BX, pady = PAD_BY,sticky = EW)

        self.button_enter = Button(self.frame_secondary, text = "Enter",
                                   width = WIDTH)

        self.output_section_1 = Label(self.frame_secondary, pady = PAD_LY, background = self.COLOUR_BG)
        self.output_section_2 = Label(self.frame_secondary, pady = PAD_LY, background = self.COLOUR_BG)
        self.output_section_3 = Label(self.frame_secondary, pady = PAD_LY, background = self.COLOUR_BG)

        self.invalid_section_1 = Label(self.frame_secondary, padx = PAD_LX, background = self.COLOUR_BG)
        self.invalid_section_2 = Label(self.frame_secondary, padx = PAD_LX, background = self.COLOUR_BG)
        self.invalid_section_3 = Label(self.frame_secondary, padx = PAD_LX, background = self.COLOUR_BG)

        self.input_section_1 = Entry(self.frame_secondary)
        self.input_section_2 = Entry(self.frame_secondary)
        self.input_section_3 = Entry(self.frame_secondary)

        self.roots_header = Frame(self.root_frame,  bg = self.COLOUR_BG,
                                       width = 320, height = 60)
        self.roots_header.grid_propagate(0)
        self.roots_header.grid(row = 0, columnspan = 2)

        roots_label = Label(self.roots_header, bg = self.COLOUR_BG, anchor= NW, text = "Roots Displayed Below: ")
        roots_label.grid(row = 0, column = 0, sticky = NW,  padx = 20, pady = 10)

        name_label_d = Label(self.root_frame, anchor= NW,
                              text = "Name :")
        name_label_d.grid(row = 1, column = 0, sticky = NW, padx = 20,
                           pady = 10)

        self.name = Label(self.root_frame, anchor= NW)
        self.name.grid(row = 1, column = 1, sticky = NW, pady = 10)

        pin_label_d = Label(self.root_frame, anchor= NW, text = "Digital Root:")
        pin_label_d.grid(row = 2, column = 0, sticky = NW, padx = 20, pady = 10)

        self.pin = Label(self.root_frame, anchor= NW)
        self.pin.grid(row = 2, column = 1, sticky = NW, pady = 5)

        self.prev_btn = Button(self.root_frame, text = "Previous",
                               state = DISABLED, command = self.previous)
        self.prev_btn.grid(row = 4, column = 0, sticky = W, padx = 20, pady = 10)

        self.next_btn = Button(self.root_frame, text = "Next",
                               state = DISABLED, command = self.next_btn)
        self.next_btn.grid(row = 4, column = 1, sticky = E, padx = 20,
                           pady = 10)
        self.index = 0

    def info(self):
        print(1)

    def add_root(self):
        print(2)

    def process_add(self):
        print(3)

    def clear(self):
        print(4)

    def next_btn(self):
        print(5)

    def previous(self):
        print(6)

    def show_data(self):
        print(7)

    def digital_root(self, n):
        print(8)



if __name__ == "__main__":
    root = Tk()
    root.title("Drs")
    buttons = Gui(root)
    root.mainloop()