import clsnote as note
# import clsListNotes as db
# import view as vw

class opCreateNote:

    def execute(self, view):
        tit = view.getUserTitle()
        txt = view.getUserText()
        nm = 0
        for i in range(0,view.db.getDbLen()):
            #print(view.db.getNumNoteById(i))
             if view.db.getNumNoteById(i) > nm:
                 nm = view.db.getNumNoteById(i)
        nm += 1
        nt = note.note(nm, tit, txt)
        view.db.appendNote(nt)
        return "\n"
