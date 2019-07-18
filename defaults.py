import tkinter as tk
import defaults_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root, top
    root = tk.Tk()
    defaults_support.set_Tk_var()
    top = Toplevel1 (root)
    defaults_support.init(root, top)
    root.mainloop()

def return_info():
    global top
    return_info.organizer = top.GameOrganizerEntry.get()
    return_info.playerCount = top.Scale1.get()
    return_info.boxPrice = top.BoxPriceSpinbox.get()
    root.destroy()

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        font10 = "-family {Times New Roman} -size 14 -weight normal "  \
            "-slant roman -underline 0 -overstrike 0"
        font11 = "-family {Times New Roman} -size 20 -weight bold "  \
            "-slant roman -underline 0 -overstrike 0"
        font9 = "-family {Times New Roman} -size 20 -weight bold "  \
            "-slant roman -underline 1 -overstrike 0"

        top.geometry("595x315+550+350")
        top.title("Superbowl Boxes Generator")
        top.configure(background="#d9d9d9")

        self.TitleText = tk.Label(top)
        self.TitleText.place(relx=0.0, rely=0.063, height=41, width=594)
        self.TitleText.configure(background="#d9d9d9")
        self.TitleText.configure(disabledforeground="#a3a3a3")
        self.TitleText.configure(font=font9)
        self.TitleText.configure(foreground="#000000")
        self.TitleText.configure(text='''Superbowl Boxes Generator''')
        self.TitleText.configure(width=594)

        self.GameOrganierText = tk.Label(top)
        self.GameOrganierText.place(relx=0.202, rely=0.286, height=27, width=127)

        self.GameOrganierText.configure(background="#d9d9d9")
        self.GameOrganierText.configure(disabledforeground="#a3a3a3")
        self.GameOrganierText.configure(font=font10)
        self.GameOrganierText.configure(foreground="#000000")
        self.GameOrganierText.configure(text='''Game Organizer''')

        self.GameOrganizerEntry = tk.Entry(top)
        self.GameOrganizerEntry.place(relx=0.471, rely=0.286, height=25
                , relwidth=0.309)
        self.GameOrganizerEntry.configure(background="white")
        self.GameOrganizerEntry.configure(disabledforeground="#a3a3a3")
        self.GameOrganizerEntry.configure(font=font10)
        self.GameOrganizerEntry.configure(foreground="#000000")
        self.GameOrganizerEntry.configure(insertbackground="black")
        self.GameOrganizerEntry.configure(justify='center')

        self.BoxPriceText = tk.Label(top)
        self.BoxPriceText.place(relx=0.202, rely=0.54, height=27, width=130)
        self.BoxPriceText.configure(background="#d9d9d9")
        self.BoxPriceText.configure(disabledforeground="#a3a3a3")
        self.BoxPriceText.configure(font=font10)
        self.BoxPriceText.configure(foreground="#000000")
        self.BoxPriceText.configure(text='''Box Price''')
        self.BoxPriceText.configure(width=130)

        self.BoxPriceSpinbox = tk.Spinbox(top, from_=0.0, to=100.0)
        self.BoxPriceSpinbox.place(relx=0.471, rely=0.54, relheight=0.079
                 , relwidth=0.314)
        self.BoxPriceSpinbox.configure(activebackground="#f9f9f9")
        self.BoxPriceSpinbox.configure(background="white")
        self.BoxPriceSpinbox.configure(buttonbackground="#d9d9d9")
        self.BoxPriceSpinbox.configure(disabledforeground="#a3a3a3")
        self.BoxPriceSpinbox.configure(font=font10)
        self.BoxPriceSpinbox.configure(foreground="black")
        self.BoxPriceSpinbox.configure(format="%.2f")
        self.BoxPriceSpinbox.configure(highlightbackground="black")
        self.BoxPriceSpinbox.configure(highlightcolor="black")
        self.BoxPriceSpinbox.configure(increment="0.25")
        self.BoxPriceSpinbox.configure(insertbackground="black")
        self.BoxPriceSpinbox.configure(justify='center')
        self.BoxPriceSpinbox.configure(selectbackground="#c4c4c4")
        self.BoxPriceSpinbox.configure(selectforeground="black")
        defaultPrice = tk.StringVar(root)
        defaultPrice.set("0.50")
        self.BoxPriceSpinbox.configure(textvariable=defaultPrice)
        self.BoxPriceSpinbox.configure(width=187)
        self.BoxPriceSpinbox.configure

        self.Label3 = tk.Label(top)
        self.Label3.place(relx=0.202, rely=0.413, height=31, width=124)
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(font=font10)
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(text='''Player Count''')
        self.Label3.configure(width=124)
        
        self.Scale1 = tk.Scale(top, from_=1.0, to=100.0)
        self.Scale1.place(relx=0.471, rely=0.349, relwidth=0.319, relheight=0.0
                    , height=48, bordermode='ignore')
        self.Scale1.configure(activebackground="#ececec")
        self.Scale1.configure(background="#d9d9d9")
        self.Scale1.configure(font=font10)
        self.Scale1.configure(foreground="#000000")
        self.Scale1.configure(highlightbackground="#d9d9d9")
        self.Scale1.configure(highlightcolor="black")
        self.Scale1.configure(length="184")
        self.Scale1.configure(orient="horizontal")
        self.Scale1.configure(troughcolor="white")

        self.ContinueButton = tk.Button(top, command=return_info)
        self.ContinueButton.place(relx=0.118, rely=0.73, height=52, width=464)
        self.ContinueButton.configure(activebackground="#ececec")
        self.ContinueButton.configure(activeforeground="#000000")
        self.ContinueButton.configure(background="#d9d9d9")
        self.ContinueButton.configure(disabledforeground="#a3a3a3")
        self.ContinueButton.configure(font=font11)
        self.ContinueButton.configure(foreground="#000000")
        self.ContinueButton.configure(highlightbackground="#d9d9d9")
        self.ContinueButton.configure(highlightcolor="black")
        self.ContinueButton.configure(pady="0")
        self.ContinueButton.configure(text='''Continue''')
        self.ContinueButton.configure(width=464)
