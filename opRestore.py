class opRestore:

    def execute(self, view):
        view.restoreDB()
        return "\n"