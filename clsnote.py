from datetime import datetime

class note:

    def __init__(self, num, title, text, dt = '-1') -> None:
        self.id = num
        self.title = title
        self.text = text
        if dt == '-1':
            dt = datetime.now()
            self.date = dt.strftime("%Y-%m-%d %H:%M:%S")
        else:
            self.date = dt 

    def __repr__(self) -> str:
        return str(self.id) + ". " + self.date + "   " + self.title + "   " + str(self.text) + ";"
    
    def toString(self):
        return str(self.id) + ";" + self.date + ";" + self.title + ";" + str(self.text) 
    
    def getNum(self):
        return int(self.id)
    
    def getDate(self):
        return str(self.date)
