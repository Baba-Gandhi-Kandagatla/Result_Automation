import urllib3
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from bs4 import BeautifulSoup
import requests
from threading import Thread

urllib3.disable_warnings()
l_nh = []


class Ui_MainWindow(object):

    def prnt(self):
        print("clicked")
        print(self.csv())
        print(self.excel())
        print(self.url())

    def Both(self):
        choice = self.r_u_sure()
        if choice != 16384:
            return

        # self.prnt()
        self.functionality()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        # MainWindow.resize(1045, 620)
        MainWindow.setFixedSize(1045, 620)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Background = QtWidgets.QWidget(self.centralwidget)
        self.Background.setGeometry(QtCore.QRect(-10, -30, 1181, 761))
        self.Background.setStyleSheet(
            "background-color:qlineargradient(spread:pad, x1:0.02, y1:0.460455, x2:1, y2:0.477, stop:0 rgba(20, 30, 48, 255), stop:1 rgba(36, 79, 120, 255))")
        self.Background.setObjectName("Background")
        self.label = QtWidgets.QLabel(self.Background)
        self.label.setGeometry(QtCore.QRect(330, 40, 401, 91))
        self.label.setStyleSheet("background:transparent;\n"
                                 "margin-left:auto;\n"
                                 "color:white;\n"
                                 "font: 24pt \"Microsoft Sans Serif\";\n"
                                 "margin-right:auto;")
        self.label.setObjectName("label")
        self.label_csv = QtWidgets.QLabel(self.Background)
        self.label_csv.setGeometry(QtCore.QRect(50, 170, 221, 41))
        self.label_csv.setStyleSheet("background:transparent;\n"
                                     "color:white;\n"
                                     "font: 14pt \"Segoe MDL2 Assets\";")
        self.label_csv.setObjectName("label_csv")
        self.label_url = QtWidgets.QLabel(self.Background)
        self.label_url.setGeometry(QtCore.QRect(50, 260, 221, 41))
        self.label_url.setStyleSheet("background:transparent;\n"
                                     "font: 75 15pt \"Segoe UI Variable Display\";\n"
                                     "color:white;\n"
                                     "")
        self.label_url.setObjectName("label_url")
        self.label_excel = QtWidgets.QLabel(self.Background)
        self.label_excel.setGeometry(QtCore.QRect(50, 350, 221, 41))
        self.label_excel.setStyleSheet("background:transparent;\n"
                                       "color:white;\n"
                                       "font: 13pt \"Segoe MDL2 Assets\";")
        self.label_excel.setObjectName("label_excel")
        self.lineEdit_url = QtWidgets.QLineEdit(self.Background)
        self.lineEdit_url.setGeometry(QtCore.QRect(300, 260, 641, 51))
        self.lineEdit_url.setStyleSheet("background:rgb(170, 255, 255);\n"
                                        "border-radius: 23px;\n"
                                        "font-size:20px;\n"
                                        "padding-left:10px;")
        self.lineEdit_url.setObjectName("lineEdit_url")
        self.lineEdit_csv = QtWidgets.QLineEdit(self.Background)
        self.lineEdit_csv.setGeometry(QtCore.QRect(300, 170, 641, 51))
        self.lineEdit_csv.setStyleSheet("QLineEdit{\n"
                                        "    background:rgb(170, 255, 255);\n"
                                        "    border-radius: 23px;\n"
                                        "    color:black;\n"
                                        "    padding-left:10px;\n"
                                        "    font-size: 20px;\n"
                                        "}\n"
                                        "\n"
                                        "\n"
                                        "")
        self.lineEdit_csv.setObjectName("lineEdit_csv")
        self.excel_path = QtWidgets.QLineEdit(self.Background)
        self.excel_path.setGeometry(QtCore.QRect(300, 350, 641, 51))
        self.excel_path.setStyleSheet("background:rgb(170, 255, 255);\n"
                                      "border-radius: 23px;\n"
                                      "font-size:20px;\n"
                                      "padding-left:10px;\n"
                                      "\n"
                                      "")
        self.excel_path.setObjectName("excel_path")
        self.StartButton = QtWidgets.QPushButton(self.Background)
        self.StartButton.setGeometry(QtCore.QRect(790, 470, 181, 121))
        self.StartButton.clicked.connect(self.Both)
        self.StartButton.setStyleSheet("QPushButton{\n"
                                       "    color:white;\n"
                                       "    border-radius:25px ;\n"
                                       "    border :2px solid white;\n"
                                       "    font-size:22px;\n"
                                       "    background:qlineargradient(spread:pad, x1:0.02, y1:0.460455, x2:1, y2:0.477, stop:0 rgba(20, 30, 48, 255), stop:1 rgba(36, 59, 85, 255))\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:hover{\n"
                                       "  border: 5px solid white;\n"
                                       "   font-size:34px;\n"
                                       "}")
        self.StartButton.setObjectName("StartButton")
        self.label_2 = QtWidgets.QLabel(self.Background)
        self.label_2.setGeometry(QtCore.QRect(50, 380, 171, 31))
        self.label_2.setStyleSheet("color:white;\n"
                                   "background:transparent;\n"
                                   "font-size:16px;")
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1045, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def r_u_sure(self):
        msg_err = QMessageBox()
        msg_err.setWindowTitle("About")
        msg_err.setText("Are you sure with the details you entered ?")
        msg_err.setIcon(QMessageBox.Question)
        msg_err.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        result = msg_err.exec_()
        return result

        #
        # def msg_Text(self,msg):
        #     print(msg.text())

    def connectionError(self):
        msg_err = QMessageBox()
        msg_err.setWindowTitle("Error")
        msg_err.setText("Check your Internet Connectivity")
        msg_err.setIcon(QMessageBox.Critical)
        msg_err.exec_()

    def csv_error(self):
        msg_err = QMessageBox()
        msg_err.setWindowTitle("Warning")
        msg_err.setText("PATH doesn't refer to a CSV file")
        msg_err.setIcon(QMessageBox.Warning)
        msg_err.exec_()

    def url_error(self):
        msg_err = QMessageBox()
        msg_err.setWindowTitle("Error")
        msg_err.setText("Please check the entered URL")
        msg_err.setIcon(QMessageBox.Critical)
        msg_err.exec_()

    def no_roll_no(self):
        msg_err = QMessageBox()
        msg_err.setWindowTitle("Error")
        msg_err.setText("The given file doesn't contain any roll numbers")
        msg_err.setIcon(QMessageBox.Warning)
        msg_err.exec_()

    def html_page_error(self, i):
        msg_err = QMessageBox()
        msg_err.setWindowTitle("Page Error")
        msg_err.setText(f"{i} SERVER Error")
        msg_err.setIcon(QMessageBox.Critical)
        msg_err.exec_()

    def no_directory(self):
        msg_err = QMessageBox()
        msg_err.setWindowTitle("Error")
        msg_err.setText("Path doesn't refer to a CSV file")
        msg_err.setIcon(QMessageBox.Warning)
        msg_err.exec_()

    def marks_imported(self):
        msg_err = QMessageBox()
        msg_err.setWindowTitle("Info")
        msg_err.setText("MARKS ARE IMPORTED")
        msg_err.setIcon(QMessageBox.Information)
        res = msg_err.exec_()
        return res

    def htno_not_found(self, l):
        msg_err = QMessageBox()
        msg_err.setWindowTitle("Info")
        msg_err.setText(f"Some of the hall-Ticket numbers are missing \n They are {l}")
        msg_err.setIcon(QMessageBox.Information)
        msg_err.exec_()

    def csv(self):
        return self.lineEdit_csv.text()

    def excel(self):
        return self.excel_path.text()

    def url(self):
        return self.lineEdit_url.text()

    def functionality(self):

        def lcr(path5):
            f = open(path5, 'r')
            l = f.readlines()
            for i in range(len(l)):
                l[i] = int(l[i][:-1])
            return l
        def star(z1, url2, path2):
            for i in z1:
                f = open(path2, 'a+')

                def writef(w):
                    f.write(w + ",")

                hall_ticket_no = i
                payload = {'mbstatus': 'SEARCH', 'htno': hall_ticket_no}
                try:
                    res = requests.post(url2, verify=False, data=payload, allow_redirects=True)
                    soup = BeautifulSoup(res.text, 'html.parser')
                    data = []
                    for row in soup.find_all("tr"):
                        row_data = []
                        for cell in row.find_all(["th", "td"]):
                            row_data.append(cell.text.replace("\n", ' ').strip())
                        data.append(row_data)
                    if len(data) != 6:
                        mins = len(data) - 30
                        info = [data[5:7], data[-19 - mins:-10], data[-14:-6]]
                        for j in info[1]:
                            if len(j) == 5:
                                writef(str(i))
                                for k in j:
                                    if k != j[2]:
                                        writef(k)
                                f.write('\n')
                    else:
                        l_nh.append(int(i))
                except requests.exceptions.ConnectionError:
                    self.connectionError()
                f.close()

        def ending(list_roll1, url1, path2):
            threads = []
            # for i in list_roll1:
            #     t = Thread(target=star, args=(i, url1, path2))
            #     threads.append(t)
            #     t.start()
            while len(list_roll1) >= 5:
                t = Thread(target=star, args=(
                    [list_roll1[0], list_roll1[1], list_roll1[2], list_roll1[3], list_roll1[4]], url1, path2))
                threads.append(t)
                t.start()
                for i in range(5):
                    list_roll1.pop(0)
            t = Thread(target=star, args=(list_roll1, url1, path2))
            threads.append(t)
            t.start()
            for t in threads:
                t.join()

        def starting():
            path3 = self.csv()
            url3 = self.url()
            path4 = self.excel()
            # path4 = r"C:\Users\bhara\Downloads\roll.csv"

            # path4 = r'C:\Users\babag\python_folders\webscrapping\roll.csv'

            if not path3.endswith('.csv'):
                self.csv_error()
                return False

            if not url3.endswith(".jsp") or "https://www.osmania.ac.in/res07/" not in url3:
                self.url_error()
                return False

            if not path4.endswith(".csv"):
                self.no_roll_no()
                return False

            list_roll2 = lcr(path4)
            # print(list_roll2)
            payload = {'mbstatus': 'SEARCH', 'htno': 245522748065}
            try:
                res = requests.post(url3, verify=False, data=payload)
                if res.status_code != 200:
                    self.html_page_error(res.status_code)
                    return False
            except requests.exceptions.ConnectionError:
                self.connectionError()
                return False
            try:
                f = open(path3, 'w')
            except FileNotFoundError:
                self.csv_error()
                return False
            f.write(
                'ROLL NUMBER,Sub code,Subject Name,Grade Points,Grade Secured,\n')
            f.close()

            return [list_roll2, url3, path3]

        fl = starting()
        if fl!= False:
            ending(fl[0],fl[1],fl[2])
            if len(l_nh) != 0:
                self.htno_not_found(l_nh)
            if self.marks_imported() == 1024:
                self.lineEdit_csv.clear()
                self.excel_path.clear()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "EXAM RESULTS"))
        self.label_csv.setText(_translate("MainWindow", "Path for your CSV file"))
        self.label_url.setText(_translate("MainWindow", "Results website URL"))
        self.label_excel.setText(_translate("MainWindow", "Path for your Excel file "))
        self.StartButton.setText(_translate("MainWindow", "Start"))
        self.label_2.setText(_translate("MainWindow", "file containing Roll-no"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
