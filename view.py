import clsnote as note

class view:

    def __init__(self, menu, db):
        self.menu = menu
        self.db = db

    def Prompt(self):
        inpt = int(input(f"{self.menu.ToString()}"))
        return inpt

    def show(self, mystr):
        print(mystr)

    def showDB(self):
        print()
        print("Список заметок:")
        print(self.db.toString())

    def saveDB(self):
        with open("data.csv","w") as fp:
            fp.write(self.db.toString())
    
    def restoreDB(self):
        self.db.clearDB()
        fp = open("data.csv","r")
        for line in fp:
            line = str(line).replace("\n","")
            strl = str(line).split(";")
 #           print(strl)
            tit = strl[2]
            txt = strl[3]
            dt = strl[1]
            nm = strl[0]
 #           print(strl)
            nt = note.note(nm, tit, txt, dt)
            self.db.appendNote(nt)
        fp.close()

    @staticmethod
    def showStr(mystr):
        print(mystr)

    def getUserText(self):
        return input("Введите текст: ")
    
    def getUserTitle(self):
        return input("Введите название: ")
    
    def getUserNum(self):
        return int(input("Введите номер заметки: "))
