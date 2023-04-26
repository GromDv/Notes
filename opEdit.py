import view as vw
import clsnote as note
from datetime import datetime

class opEdit:

    def execute(self, view, dbNotes):
        mystr = "Редактируем: "
        num = view.getUserNum()
        nt = dbNotes.getNoteByNum(num)
        if nt == -1:
            return "Нет такой заметки!"
        vw.view.showStr(mystr)
        vw.view.showStr(repr(nt))
        tit = view.getUserTitle()
        txt = view.getUserText()
        dt = datetime.now()
        date = dt.strftime("%Y-%m-%d %H:%M:%S")
        nt = note.note(num, tit, txt, date)
        dbNotes.replaceNote(num, nt)
        return "\n"
    