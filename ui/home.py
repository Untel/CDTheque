from Tkinter import *
 
class ApplicationBasic():
	'''Application principale'''
	def __init__(self, collection):
		'''constructeur'''
		self.fen = Tk()
		self.fen.title('Tkinter')
		self.bou_action = Button(self.fen)
		self.bou_action.config(text='Action', command=self.action)
		self.bou_action.pack()
 
		self.bou_quitter = Button(self.fen)
		self.bou_quitter.config(text='Quitter', command=self.fen.destroy)
		self.bou_quitter.pack()
        self.albums = collection.get()
        for album in self.albums:
            name = Label(self.fen)
            name.config(text=album.name)
            name.pack()

 
	def run(self):
                self.fen.mainloop()
    
	def action(self):
		'''Action sur un bouton'''
		self.lab = Label(self.fen)
		self.lab.config(text='Bravo!!!')
		self.lab.pack()
