from tkinter import *


class App(Tk):
    def __init__(self):
        super().__init__()
        self.title('My app')
        self.geometry('400x400')
        self.put_frames()

    def put_frames(self):
        self.frame_main = MainWindow(self).place(relwidth=1, relheight=1)


class FinishWindow(Tk):
    def __init__(self):
        super().__init__()
        self.title(' ')
        self.geometry('100x100')
        self.put_widgets()
        self.config(bg='green')
        
    def put_widgets(self):
    	text = Label(self, text='Привет, мир!', bg='green').pack()
       

class MainWindow(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.config(bg='blue')
        self.put_widgets()

    def press(self):
        self.config(bg='red')
        FinishWindow().mainloop()
        
    def put_widgets(self):
        button = Button(self, text='Press', command=self.press).place(relx=0.5, rely=0.5)


if __name__== '__main__':
    app = App()
    app.mainloop()