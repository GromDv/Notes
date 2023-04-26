from exportImport import expImp  as exp

class listNotes:

    def __init__(self) -> None:
        self.dbListNotes = []

    def __repr__(self) -> str:
        strdb = ""
        for line in self.dbListNotes:
            strdb += repr(line) + "\n"
        return strdb
    
    def sortTime(self):
        self.dbListNotes.sort(key=lambda note: note.getDate(), reverse=True)

    def sortId(self):
        self.dbListNotes.sort(key=lambda note: note.getNum() )

    def toString(self):
        str = ""
        for i in range(0,len(self.dbListNotes)):
            str += self.dbListNotes[i].toString() + "\n"
        return str
    
    def getDbLen(self):
        return len(self.dbListNotes)
    
    def getNumNoteById(self, id):
        return self.dbListNotes[id].getNum()
    
    def appendNote(self, note):
        self.dbListNotes.append(note)

    def clearDB(self):
        self.dbListNotes.clear()

    def getNoteByNum(self, num):
        for note in self.dbListNotes:
            if note.getNum() == num:
                return note
        else:
            return -1
        
    def replaceNote(self, num, nt):
        for note in self.dbListNotes:
            if note.getNum() == num:
                self.dbListNotes.remove(note)
                self.dbListNotes.append(nt)

    def removeNote(self, num):
        for note in self.dbListNotes:
            if note.getNum() == num:
                self.dbListNotes.remove(note)

    def importFromCsv(self):
        exp.restoreDB(self, self.dbListNotes)
        