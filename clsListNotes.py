class listNotes:

    def __init__(self) -> None:
        self.dbListNotes = []

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
        if num >= 0 and num < len(self.dbListNotes):
            return self.dbListNotes[num]
        else:
            return -1
        
    def replaceNote(self, num, nt):
        self.dbListNotes.pop(num)
        self.dbListNotes.insert(num, nt)

    def removeNote(self, num):
        self.dbListNotes.pop(num)