class opDelete:

    def execute(self, view):
        num = view.getUserNum()
        nt = view.db.getNoteByNum(num-1)
        if nt == -1:
            return "Нет такой заметки!"
        view.db.removeNote(num-1)
        return "\n"