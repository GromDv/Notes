import clsnote as note

class expImp:

    def saveDB(dbNotes):
        print(dbNotes.toString())
        with open("data.csv","w") as fp:
            fp.write(dbNotes.toString())
    
    def restoreDB(dbNotes):
        dbNotes.clearDB()
        fp = open("data.csv","r")
        for line in fp:
            line = str(line).replace("\n","")
            strl = str(line).split(";")
            tit = strl[2]
            txt = strl[3]
            dt = strl[1]
            nm = strl[0]
            nt = note.note(nm, tit, txt, dt)
            dbNotes.appendNote(nt)
        fp.close()
        