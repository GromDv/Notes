import view as vw
import clsnote as note
from datetime import datetime

class opEdit:

    def execute(self, view):
        mystr = "Редактируем: "
        num = view.getUserNum()
        nt = view.db.getNoteByNum(num-1)
        if nt == -1:
            return "Нет такой заметки!"
        vw.view.showStr(mystr)
        vw.view.showStr(nt.toString())
        strnt = str(nt.toString()).split(";")
        tit = view.getUserTitle()
        txt = view.getUserText()
        dt = datetime.now()
        date = dt.strftime("%Y-%m-%d %H:%M:%S")
        nt = note.note(num, tit, txt, date)
        view.db.replaceNote(num-1, nt)
        return "\n"