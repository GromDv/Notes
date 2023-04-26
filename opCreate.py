import clsnote as note

class opCreateNote:

    def execute(self, view, dbNotes):
        tit = view.getUserTitle()
        txt = view.getUserText()
        nm = 0
        for i in range(0,dbNotes.getDbLen()):
             if dbNotes.getNumNoteById(i) > nm:
                 nm = dbNotes.getNumNoteById(i)
        nm += 1
        nt = note.note(nm, tit, txt)
        dbNotes.appendNote(nt)
        return "\n"
