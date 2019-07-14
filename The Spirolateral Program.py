from tkinter import *

class Spirolateral:
    #class to assign inputs to Digital root list
    def __init__(self,name,dr_list):
        self.name = name
        self.dr_list = dr_list

class Gui:
    #Class to setup GUI
    def __init__(self, master):
        #digital root list setup
        self.drs = []
        #general code to setup pads and background colour for GUI and widgets
        self.COLOUR_BG = "yellow"
        PAD_LX = 30
        PAD_LY = 20
        PAD_BX = 6
        PAD_BY = 6
        WIDTH = 40

        #setsup main frame which will contain main buttons
        self.frame_menu = Frame(master, background = self.COLOUR_BG)
        self.frame_menu.grid(row = 0, column = 0, columnspan = 2,sticky = 'nesw')

        #setsup secondary frame which will contain sections for users to put inputs
        self.frame_secondary = Frame(master, background = self.COLOUR_BG)
        self.frame_secondary.grid(row = 1, column = 1, sticky = 'nesw')

        #setsup bottom frame which will contain section to display roots with previous and next buttons
        self.root_frame = Frame(master, background = self.COLOUR_BG)
        self.root_frame.grid(row = 2, column = 1, sticky = 'nesw')

        #setsup buttons in main frame
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

        #setsup frame_secondary sections for displaying text and inputs
        self.output_section_1 = Label(self.frame_secondary, pady = PAD_LY, background = self.COLOUR_BG)
        self.output_section_2 = Label(self.frame_secondary, pady = PAD_LY, background = self.COLOUR_BG)
        self.output_section_3 = Label(self.frame_secondary, pady = PAD_LY, background = self.COLOUR_BG)

        self.invalid_section_1 = Label(self.frame_secondary, padx = PAD_LX, background = self.COLOUR_BG)
        self.invalid_section_2 = Label(self.frame_secondary, padx = PAD_LX, background = self.COLOUR_BG)
        self.invalid_section_3 = Label(self.frame_secondary, padx = PAD_LX, background = self.COLOUR_BG)

        self.input_section_1 = Entry(self.frame_secondary)
        self.input_section_2 = Entry(self.frame_secondary)
        self.input_section_3 = Entry(self.frame_secondary)

        #setsup root_frame which contains text to display digital roots and previous and next buttons
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
        #sets index at start of program
        self.index = 0

    def info(self):
        #function used to display information about program
        self.output_section_1.configure(text = "")
        self.output_section_2.configure(text = "")
        self.output_section_3.configure(text = "")

        self.output_section_1.configure(text = "Welcome to the Spirolateral Program. \nThis program finds the digital root of a times table. \nThank you and enjoy your stay.:")
        self.output_section_1.grid(row = 0, column = 0, sticky = W)

    def add_root(self):
        #function used to configure frame_secondary for adding Spirolateral
        self.output_section_1.configure(text = "")
        self.output_section_2.configure(text = "")
        self.output_section_3.configure(text = "")

        self.output_section_1.configure(text = "Name:")
        self.output_section_2.configure(text = "Times Table:")

        self.output_section_1.grid(row = 0, column = 0, sticky = W)
        self.output_section_2.grid(row = 1, column = 0, sticky = W)

        self.input_section_1.grid(row = 0, column = 1)
        self.input_section_2.grid(row = 1, column = 1)

        self.button_enter.grid(row = 3, column = 0)

        self.button_enter.configure(command = self.process_add)

        self.input_section_1.delete(0, END)
        self.input_section_2.delete(0, END)

    def process_add(self):
        #function used to get user input and run them through class and 'digital_root' function
        find_root = int(self.input_section_2.get())
        find_name = str(self.input_section_1.get())

        self.drs.append(Spirolateral(find_name,
                                      (self.digital_root(find_root))))
        if len(self.drs)==1:
            #makes next button unclickable if there is only 1 root
            self.next_btn.configure(state = DISABLED)
            self.show_data()
        if len(self.drs)>1:
            #makes next button clickable if there is more than 1 root
            self.next_btn.configure(state = NORMAL)
            self.show_data()

        self.clear()

    def clear(self):
        #function used to clear text from input sections of GUI
        self.input_section_1.delete(0, END)
        self.input_section_2.delete(0, END)
        self.input_section_3.delete(0, END)

    def next_btn(self):
        #function used to configure next button
        self.index+=1
        if self.index == len(self.drs)-1:
            #makes next button disabled if index is at its max
            self.next_btn.configure(state = DISABLED)

        self.prev_btn.configure(state = NORMAL)
        self.show_data()

    def previous(self):
        #function used to configure previous button
        self.index -= 1
        if self.index == 0:
            #makes previous button disabled if program is displaying first root
            self.prev_btn.configure(state = DISABLED)

        self.next_btn.configure(state = NORMAL)
        self.show_data()

    def show_data(self):
        #function used to display root and name in bottom of GUI
        self.name.configure(text = self.drs[self.index].name)
        self.pin.configure(text = self.drs[self.index].dr_list)

    def digital_root(self, n):
        #function used to calculate digital root
        x = -1
        m = n
        self.dr = []
        self.dr.append((m - 1) % 9 + 1)
        while x == -1:
            m += n
            if (m - 1) % 9 + 1 == self.dr[0]:
                x = 1
                return self.dr
            else:
                self.dr.append((m - 1) % 9 + 1)



#main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Drs")
    buttons = Gui(root)
    root.mainloop()
