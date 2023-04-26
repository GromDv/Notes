import exportImport

class opRestore:

    def execute(self, view, dbNotes):
        exportImport.expImp.restoreDB(dbNotes)
        return "\n"
    