import view as w
import mMenu
import opEmpty
import opPass
import opCreate
import opEdit
import opDelete
import opShow
import opSave
import opRestore
import menuPoint as mp
import clsListNotes as db


class controller:

    def start(self):
        myMenu = mMenu.mMenu()
        myNotes = db.listNotes()

        myMenu.addMenuPoint(mp.menuPoint("Создать заметку", 1, opCreate.opCreateNote()))
        myMenu.addMenuPoint(mp.menuPoint("Редактировать заметку", 2, opEdit.opEdit()))
        myMenu.addMenuPoint(mp.menuPoint("Удалить заметку", 3, opDelete.opDelete()))
        myMenu.addMenuPoint(mp.menuPoint("Сохранить список заметок", 4, opSave.opSave()))
        myMenu.addMenuPoint(mp.menuPoint("Загрузить список заметок", 5, opRestore.opRestore()))
        myMenu.addMenuPoint(mp.menuPoint("Посмотреть список заметок", 6, opShow.opShow()))
        myMenu.addMenuPoint(mp.menuPoint("Закончить работу", 9, opEmpty.opEmpty()))

        vw = w.view(myMenu, myNotes)

        n = 0
        while not (n == 9):
            n = vw.Prompt()
            vw.show(myMenu.getMenuPointByNum(n).oper.execute(vw))
