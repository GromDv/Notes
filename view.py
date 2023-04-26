class view:

    def __init__(self, menu):
        self.menu = menu

    def Prompt(self):
        inpt = int(input(f"{self.menu.ToString()}"))
        return inpt

    def show(self, mystr):
        print(mystr)

    def showDB(self, dbNotes):
        print()
        print("Список заметок по порядку:")
        dbNotes.sortId()
        print(repr(dbNotes))
        #print(dbNotes.toString())

    def showDBDate(self, dbNotes):
        print()
        print("Список заметок по времени:")
        dbNotes.sortTime()
        print(repr(dbNotes))

    @staticmethod
    def showStr(mystr):
        print(mystr)

    def getUserText(self):
        return input("Введите текст: ")
    
    def getUserTitle(self):
        return input("Введите название: ")
    
    def getUserNum(self):
        return int(input("Введите номер заметки: "))
