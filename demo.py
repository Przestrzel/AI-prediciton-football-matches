import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QRadioButton
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import pyqtSlot, Qt, QDate
from PyQt5.QtWidgets import QApplication, QWidget, QListWidget, QHBoxLayout, QListWidgetItem, QGridLayout, QMessageBox
from datetime import datetime
import pandas as pd
from pandas import DataFrame as df

# IMPORTANT : To run demo you need to run main first in order to prepare data correctly, once it its prepared you can play with your demo version!

class EventPicker(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Event picker'
                                        
    def pickEvent(self, matches_to_show):
        df_matches = pd.read_csv('ConcatenatedFiles.csv')
        items = []
        self.buttons = []
        self.matches_to_show = matches_to_show
        self.info = QLabel('We found '+str(len(matches_to_show))+' events between choosen teams.\nPick the exact date that you are interested in.', self)
        self.info.move(125, 50)
        for i in range(len(matches_to_show)):
            items.append(df_matches.loc[[matches_to_show[i]]])
            self.buttons.append(QRadioButton(str(df_matches['Date'][matches_to_show[i]]), self))
            self.buttons[i].setGeometry(200, 100+i*50, 100, 40)
        self.confirmButton = QPushButton('See who will win!', self)
        last_b_y = 100+(len(matches_to_show)-1)*50
        self.confirmButton.setGeometry(200, 100+last_b_y+20, 130, 80)
        self.confirmButton.clicked.connect(self.readToggledButton)
        self.show()
        
    @pyqtSlot()
    def readToggledButton(self):
        for i in range(len(self.buttons)):
            if self.buttons[i].isChecked():
                self.makePrediction(i)

    def makePrediction(self, index):

        dataset = pd.read_csv("ConcatenatedFiles.csv")
        attributes = dataset.drop('FTR', axis = 1)
        attributes = attributes.drop('HomeTeam', axis = 1)
        attributes = attributes.drop('AwayTeam', axis = 1)
        attributes = attributes.drop('HT Form', axis = 1)
        attributes = attributes.drop('AT Form', axis = 1)
        attributes = attributes.drop('Season', axis = 1)
        attributes = attributes.drop('Date', axis = 1)
        labels = dataset["FTR"]
        
        from sklearn.model_selection import train_test_split as split
        attributes_test = attributes.loc[[self.matches_to_show[index]]]
        labels_test = labels.loc[[self.matches_to_show[index]]]

        from sklearn.tree import DecisionTreeClassifier
        classifier = DecisionTreeClassifier(criterion="entropy", ccp_alpha=0.025)
        attributes_train, garbage_1, labels_train, garbage_2 = split(attributes, labels, test_size = 0.2)
        classifier = classifier.fit(attributes_train, labels_train)

        labels_prediction = classifier.predict(attributes_test)
        labels_test.to_csv('picked matches.csv')
        res = pd.read_csv('picked matches.csv')
        res['prediction'] = ''
        res['prediction'] = labels_prediction
        if res['prediction'][0] == 'H':
            self.prediction_result = QMessageBox.information(self, 'Our prediction',str(dataset['HomeTeam'][self.matches_to_show[index]]) + ' to win')
        else:
            self.prediction_result = QMessageBox.information(self, 'Our prediction',str(dataset['AwayTeam'][self.matches_to_show[index]]) + ' to win or draw')
             

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Demo'
        self.left = 500
        self.top = 200
        self.width = 750
        self.height = 450

        self.myLayout = QGridLayout()
        self.myListWidget1 = QListWidget()
        self.myListWidget1.setMaximumHeight(200)

        self.myListWidget_home_team = QListWidget()
        self.myListWidget_away_team = QListWidget()
        self.myListWidget_home_team.setMaximumSize(110, 130)
        self.myListWidget_away_team.setMaximumSize(110, 130)
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

        self.myLayout.addWidget(self.myListWidget1, 0, 0, 1, 5)
        self.myLayout.addWidget(self.myListWidget_home_team, 2, 0)
        self.myLayout.addWidget(self.myListWidget_away_team, 2, 4)

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
        l.append(QListWidgetItem(QIcon('logos\\man_utd.svg'), 'Man United'))
        l.append(QListWidgetItem(QIcon('logos\\newcastle.svg'), 'Newcastle'))
        l.append(QListWidgetItem(QIcon('logos\\sheffield.svg'), 'Sheffield United'))
        l.append(QListWidgetItem(QIcon('logos\\southampton.svg'), 'Southampton'))
        l.append(QListWidgetItem(QIcon('logos\\tottenham.svg'), 'Tottenham'))
        l.append(QListWidgetItem(QIcon('logos\\wba.svg'), 'West Brom'))
        l.append(QListWidgetItem(QIcon('logos\\west_ham.svg'), 'West Ham'))
        l.append(QListWidgetItem(QIcon('logos\\wolves.svg'), 'Wolves'))

        self.myListWidget1.setIconSize(QtCore.QSize(50, 50))
        self.myListWidget_away_team.setIconSize(QtCore.QSize(100, 100))
        self.myListWidget_home_team.setIconSize(QtCore.QSize(100, 100))

        self.home_team = QLabel('Home Team', self)
        self.home_team.move(40, 220)
        self.away_team = QLabel('Away Team', self)
        self.away_team.move(650, 220)

        self.setLayout(self.myLayout)
        for i in range(20):
            self.myListWidget1.insertItem((i+1), l[i])

        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        button = QPushButton('Predict the winner!', self)
        button.move(285, 300)
        button.setMinimumSize(160, 60)
        button.clicked.connect(self.predictButton)
        

        self.dateedit = QtWidgets.QDateEdit(calendarPopup=True)
        self.dateedit.setDateTime(QtCore.QDateTime.currentDateTime())
        self.myLayout.addWidget(self.dateedit, 3, 2, 1, 2)
        self.dateedit.setMaximumWidth(130)
        self.show()

    @pyqtSlot()
    def predictButton(self):
        self.recognizeTeams()
        self.setDate()
        self.findSuitableMatches()
        self.dialog = EventPicker()
        self.dialog.pickEvent(self.matches_to_show)
        #self.makePrediction(self.matches_to_show[0])

    def recognizeTeams(self):
        items = []
        self.teams = []
        items.append(self.myListWidget_home_team.item(0))
        items.append(self.myListWidget_away_team.item(0))
        for item in items:
            self.teams.append(item.text())

    def setDate(self):
        self.picked_date = self.dateedit.date().toPyDate()
        self.picked_date = self.picked_date.strftime('%d/%m/%Y')

    def findSuitableMatches(self):
        df_matches = pd.read_csv('ConcatenatedFiles.csv')
        self.matches_to_show = []

        # picked_date            format -> dd/mm/yyyy -> longer
        # picked_date_variant_2  format -> dd/mm/yy   -> normal

        # change date format in second variant:
        picked_date_variant_2 = self.adjustDateFormat()

        for ind in df_matches.index:
            # 2 options because in csv sometimes there is dd/mm/yy and sometimes dd/mm/yyyy
            if len(df_matches['Date'][ind]) > 8:
                if self.longerDateSuits(df_matches['Date'][ind]) == True:
                    if (df_matches['HomeTeam'][ind] == self.teams[0] or df_matches['HomeTeam'][ind] == self.teams[1]) and (df_matches['AwayTeam'][ind] == self.teams[0] or df_matches['AwayTeam'][ind] == self.teams[1]):
                        self.matches_to_show.append(ind)

            else:
                if self.dateSuits(picked_date_variant_2, df_matches['Date'][ind]) == True:
                    if (df_matches['HomeTeam'][ind] == self.teams[0] or df_matches['HomeTeam'][ind] == self.teams[1]) and (df_matches['AwayTeam'][ind] == self.teams[0] or df_matches['AwayTeam'][ind] == self.teams[1]):
                        self.matches_to_show.append(ind)

    def adjustDateFormat(self):
        tmp = list(self.picked_date)
        length = len(self.picked_date)
        tmp[length-3] = tmp[length-1]
        tmp[length-4] = tmp[length-2]
        tmp.pop()
        tmp.pop()
        return (''.join(tmp))

    def dateSuits(self, date_given, csv_date):

        date = list(date_given)
        d_day = 10 * int(date[0])+int(date[1])
        d_month = 10 * int(date[3])+int(date[4])
        d_year = 10 * int(date[6])+int(date[7])

        csv_date = list(csv_date)
        c_day = 10 * int(csv_date[0])+int(csv_date[1])
        c_month = 10 * int(csv_date[3])+int(csv_date[4])
        c_year = 10 * int(csv_date[6])+int(csv_date[7])

        if c_year > d_year:
            return True
        elif c_year == d_year:
            if c_month > d_month:
                return True
            elif c_month == d_month:
                if c_day >= d_day:
                    return True

        return False

    def longerDateSuits(self, csv_date):

        date = list(self.picked_date)
        d_day = 10 * int(date[0])+int(date[1])
        d_month = 10 * int(date[3])+int(date[4])
        d_year = 10 * int(date[8])+int(date[9])

        csv_date = list(csv_date)
        c_day = 10 * int(csv_date[0])+int(csv_date[1])
        c_month = 10 * int(csv_date[3])+int(csv_date[4])
        c_year = 10 * int(csv_date[8])+int(csv_date[9])

        if c_year > d_year:
            return True
        elif c_year == d_year:
            if c_month > d_month:
                return True
            elif c_month == d_month:
                if c_day >= d_day:
                    return True

        return False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
