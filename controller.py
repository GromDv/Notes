import view as w
import mMenu
import opEmpty
import opPass
import menuPoint as mp


class controller:

    def start(self):
        myMenu = mMenu.mMenu()

        myMenu.addMenuPoint(mp.menuPoint("Make some work..", 1, opPass.opPass()))
        myMenu.addMenuPoint(mp.menuPoint("Make some work..", 5, opPass.opPass()))
        myMenu.addMenuPoint(mp.menuPoint("Закончить работу", 9, opEmpty.opEmpty()))

        vw = w.view(myMenu)

        n = 0
        while not (n == 9):
            n = vw.Prompt()
            vw.show(myMenu.getMenuPointByNum(n).oper.execute(vw))
