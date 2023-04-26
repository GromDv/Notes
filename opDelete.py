class opDelete:

    def execute(self, view, dbNotes):
        num = view.getUserNum()
        nt = dbNotes.getNoteByNum(num)
        if nt == -1:
            return "Нет такой заметки!"
        dbNotes.removeNote(num)
        return "\n"
    