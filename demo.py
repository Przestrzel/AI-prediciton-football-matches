import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtWidgets import QApplication, QWidget, QListWidget, QHBoxLayout,QListWidgetItem, QGridLayout


class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Demo'
        self.left = 500
        self.top = 200
        self.width = 720
        self.height = 400

        #self.setStyleSheet("background-image: url(background.jpg)")

        self.myLayout = QGridLayout()    
        self.myListWidget1 = QListWidget()
        self.myListWidget1.setMaximumHeight(200)
        
        self.myListWidget_home_team = QListWidget()
        self.myListWidget_away_team = QListWidget()
        self.myListWidget_home_team.setMaximumSize(120,130)
        self.myListWidget_away_team.setMaximumSize(120,130)
        self.myListWidget_home_team.setViewMode(QListWidget.IconMode)
        self.myListWidget_away_team.setViewMode(QListWidget.IconMode)
        self.myListWidget1.setViewMode(QListWidget.IconMode)
        self.myListWidget1.setAcceptDrops(True)
        self.myListWidget1.setDragEnabled(True)
        self.myListWidget1.setDefaultDropAction(Qt.MoveAction)
        self.myListWidget_home_team.setAcceptDrops(True)
        self.myListWidget_home_team.setDragEnabled(True)
        self.myListWidget_home_team.setDefaultDropAction(Qt.MoveAction)
        self.myListWidget_away_team.setAcceptDrops(True)
        self.myListWidget_away_team.setDragEnabled(True)   
        self.myListWidget_away_team.setDefaultDropAction(Qt.MoveAction)
        
        self.myLayout.addWidget(self.myListWidget1, 0,0,1,3)
        self.myLayout.addWidget(self.myListWidget_home_team, 2,0)
        self.myLayout.addWidget(self.myListWidget_away_team, 2,2)
        
        l = []

        l.append(QListWidgetItem(QIcon('logos\\arsenal.svg'), 'Arsenal'))
        l.append(QListWidgetItem(QIcon('logos\\aston_villa.svg'), 'Aston Villa'))
        l.append(QListWidgetItem(QIcon('logos\\burnley.svg'), 'Burnley'))
        l.append(QListWidgetItem(QIcon('logos\\chelsea.svg'), 'Chelsea'))
        l.append(QListWidgetItem(QIcon('logos\\brighton.svg'), 'Brighton'))
        l.append(QListWidgetItem(QIcon('logos\\crystal_palace.svg'), 'Crystal Palace'))
        l.append(QListWidgetItem(QIcon('logos\\everton.svg'), 'Everton'))
        l.append(QListWidgetItem(QIcon('logos\\fulham.svg'), 'Fulham'))
        l.append(QListWidgetItem(QIcon('logos\\leeds.svg'), 'Leeds'))
        l.append(QListWidgetItem(QIcon('logos\\leicester.svg'), 'Leicester'))
        l.append(QListWidgetItem(QIcon('logos\\liverpool.svg'), 'Liverpool'))
        l.append(QListWidgetItem(QIcon('logos\\man_city.svg'), 'Man City'))
        l.append(QListWidgetItem(QIcon('logos\\man_utd.svg'), 'Man Utd'))
        l.append(QListWidgetItem(QIcon('logos\\newcastle.svg'), 'Newcastle'))
        l.append(QListWidgetItem(QIcon('logos\\sheffield.svg'), 'Sheffield'))
        l.append(QListWidgetItem(QIcon('logos\\southampton.svg'), 'Southampton'))
        l.append(QListWidgetItem(QIcon('logos\\tottenham.svg'), 'Tottenham'))
        l.append(QListWidgetItem(QIcon('logos\\wba.svg'), 'West Brom'))
        l.append(QListWidgetItem(QIcon('logos\\west_ham.svg'), 'West Ham'))
        l.append(QListWidgetItem(QIcon('logos\\wolves.svg'), 'Wolves'))
        
        self.myListWidget1.setIconSize(QtCore.QSize(50,50))
        self.myListWidget_away_team.setIconSize(QtCore.QSize(100,100))
        self.myListWidget_home_team.setIconSize(QtCore.QSize(100,100))        

        self.home_team = QLabel('Home Team', self)
        self.home_team.move(40, 220)
        self.away_team = QLabel('Away Team', self)
        self.away_team.move(620, 220)

        self.setLayout(self.myLayout)
        for i in range(20):
            self.myListWidget1.insertItem((i+1), l[i])    

        print(self.myListWidget1.count())

        self.initUI()
    
    def iterAllItems(self, l):
        for i in range(l.count()):
            yield l.item(i)

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        button = QPushButton('Predict the winner!', self)
        
        button.move(260,300)
        button.setMinimumSize(200,30)
        button.clicked.connect(self.predictButton)
                                                                            
        self.show()

    @pyqtSlot()
    def predictButton(self):
        items = []
        for x in range(self.myListWidget_home_team.count()):
            items.append(self.myListWidget_home_team.item(x))
        
        for item in items:
            print(item.text())



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
