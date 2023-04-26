import exportImport

class opSave:

    def execute(self, view, dbNotes):
        exportImport.expImp.saveDB(dbNotes)
        return "\n"
    