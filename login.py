from tkinter import *
# Nathan working on login system :)

class login():
    def __init__(self):
        self.window = Tk()
        self.window.geometry("800x600")
        self.window.title("login")

        filename = PhotoImage(file="C:\\Users\\natha\\Pictures\\stuff\\ow_glow2.png")
        background_label = Label(self.window, image=filename)
        background_label.image = filename
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

    def window_build(self):
        self.lbl1 = Label(self.window, text= "Please enter your battletag", font= ("comic sans","15"))
        self.inp1 = Entry(self.window, width= 20)
        self.inp1.bind("<Return>", self.runCmd)
        self.lbl1.pack()
        self.inp1.pack()

        self.lbl1.focus_set()
        self.inp1.focus_set()

        self.start()

    def runCmd(self, event):
        self.btag = self.inp1.get()
        goodTag = False
        if not goodTag:
            temp = self.btag.split("#")
            try:
                self.linkTag = (str(temp[0]) + "-" + str(temp[1]))
                goodTag = True
                
            except:
                self.lbl1.config(text= "Try another Battletag")
        if goodTag:
            return self.load()
        
    def start(self):
        self.window.mainloop()

    def load(self):
        self.lbl1.destroy()
        self.inp1.destroy()
        self.window.destroy()
        print(self.linkTag)
        return self.linkTag
        
def run():
    log = login()
    log.window_build()
    return log.linkTag
    

