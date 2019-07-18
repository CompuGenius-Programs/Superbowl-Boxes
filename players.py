import tkinter as tk
import players_support
import manager

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root, top
    root = tk.Tk()
    players_support.set_Tk_var()
    top = Toplevel1 (root)
    players_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    players_support.set_Tk_var()
    top = Toplevel1 (w)
    players_support.init(w, top, *args, **kwargs)
    return (w, top)

def new_player_btn():
    global top

    new_player_btn.name = top.PlayerNameEntry.get()
    new_player_btn.email = top.PlayerEmailEntry.get()
    new_player_btn.boxCount = top.BoxCountSpinbox.get()
    
    manager.boxes_taken += int(top.BoxCountSpinbox.get())
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
        font11 = "-family {Times New Roman} -size 20 -weight normal "  \
            "-slant roman -underline 0 -overstrike 0"
        font9 = "-family {Times New Roman} -size 20 -weight bold "  \
            "-slant roman -underline 1 -overstrike 0"

        top.geometry("600x370+550+350")
        top.title("Player Configurations")
        top.configure(background="#d9d9d9")

        self.TitleText = tk.Label(top)
        self.TitleText.place(relx=0.0, rely=0.081, height=41, width=604)
        self.TitleText.configure(background="#d9d9d9")
        self.TitleText.configure(disabledforeground="#a3a3a3")
        self.TitleText.configure(font=font9)
        self.TitleText.configure(foreground="#000000")
        self.TitleText.configure(text='''Player Configurations''')
        self.TitleText.configure(width=604)

        self.PlayerNameText = tk.Label(top)
        self.PlayerNameText.place(relx=0.2, rely=0.243, height=41, width=134)
        self.PlayerNameText.configure(background="#d9d9d9")
        self.PlayerNameText.configure(disabledforeground="#a3a3a3")
        self.PlayerNameText.configure(font=font10)
        self.PlayerNameText.configure(foreground="#000000")
        self.PlayerNameText.configure(text='''Player Name''')
        self.PlayerNameText.configure(width=134)

        self.PlayerNameEntry = tk.Entry(top)
        self.PlayerNameEntry.place(relx=0.467, rely=0.27, height=25
                , relwidth=0.307)
        self.PlayerNameEntry.configure(background="white")
        self.PlayerNameEntry.configure(disabledforeground="#a3a3a3")
        self.PlayerNameEntry.configure(font=font10)
        self.PlayerNameEntry.configure(foreground="#000000")
        self.PlayerNameEntry.configure(insertbackground="black")
        self.PlayerNameEntry.configure(justify='center')

        self.PlayerEmailText = tk.Label(top)
        self.PlayerEmailText.place(relx=0.2, rely=0.405, height=37, width=137)
        self.PlayerEmailText.configure(background="#d9d9d9")
        self.PlayerEmailText.configure(disabledforeground="#a3a3a3")
        self.PlayerEmailText.configure(font=font10)
        self.PlayerEmailText.configure(foreground="#000000")
        self.PlayerEmailText.configure(text='''Player Email''')
        self.PlayerEmailText.configure(width=137)

        self.PlayerEmailEntry = tk.Entry(top)
        self.PlayerEmailEntry.place(relx=0.467, rely=0.432, height=25
                , relwidth=0.307)
        self.PlayerEmailEntry.configure(background="white")
        self.PlayerEmailEntry.configure(disabledforeground="#a3a3a3")
        self.PlayerEmailEntry.configure(font=font10)
        self.PlayerEmailEntry.configure(foreground="#000000")
        self.PlayerEmailEntry.configure(insertbackground="black")
        self.PlayerEmailEntry.configure(justify='center')

        self.BoxCountText = tk.Label(top)
        self.BoxCountText.place(relx=0.2, rely=0.568, height=37, width=137)
        self.BoxCountText.configure(background="#d9d9d9")
        self.BoxCountText.configure(disabledforeground="#a3a3a3")
        self.BoxCountText.configure(font=font10)
        self.BoxCountText.configure(foreground="#000000")
        self.BoxCountText.configure(text='''Box Count''')
        self.BoxCountText.configure(width=137)

        self.BoxCountSpinbox = tk.Spinbox(top, from_=1.0, to=100.0 - manager.boxes_taken)
        self.BoxCountSpinbox.place(relx=0.467, rely=0.595, relheight=0.068
                , relwidth=0.312)
        self.BoxCountSpinbox.configure(activebackground="#f9f9f9")
        self.BoxCountSpinbox.configure(background="white")
        self.BoxCountSpinbox.configure(buttonbackground="#d9d9d9")
        self.BoxCountSpinbox.configure(disabledforeground="#a3a3a3")
        self.BoxCountSpinbox.configure(font=font10)
        self.BoxCountSpinbox.configure(foreground="black")
        self.BoxCountSpinbox.configure(highlightbackground="black")
        self.BoxCountSpinbox.configure(highlightcolor="black")
        self.BoxCountSpinbox.configure(insertbackground="black")
        self.BoxCountSpinbox.configure(justify='center')
        self.BoxCountSpinbox.configure(selectbackground="#c4c4c4")
        self.BoxCountSpinbox.configure(selectforeground="black")
        defaultCount = tk.IntVar(root)
        defaultCount.set(1)
        self.BoxCountSpinbox.configure(textvariable=defaultCount)
        self.BoxCountSpinbox.configure(width=187)

        self.NewPlayerButton = tk.Button(top, command=new_player_btn)
        self.NewPlayerButton.place(relx=0.15, rely=0.757, height=54, width=427)
        self.NewPlayerButton.configure(activebackground="#ececec")
        self.NewPlayerButton.configure(activeforeground="#000000")
        self.NewPlayerButton.configure(background="#d9d9d9")
        self.NewPlayerButton.configure(disabledforeground="#a3a3a3")
        self.NewPlayerButton.configure(font=font11)
        self.NewPlayerButton.configure(foreground="#000000")
        self.NewPlayerButton.configure(highlightbackground="#d9d9d9")
        self.NewPlayerButton.configure(highlightcolor="black")
        self.NewPlayerButton.configure(pady="0")
        self.NewPlayerButton.configure(text='''Continue''')
        self.NewPlayerButton.configure(width=427)

if __name__ == '__main__':
    vp_start_gui()





