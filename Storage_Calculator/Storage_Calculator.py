import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QPushButton
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import random

class storekalkulator(QWidget):
    def __init__(self, parent=None):
        super(storekalkulator, self).__init__(parent)
        hbox = QHBoxLayout(self)                          # Boxlayout
        topleft = QFrame()                                # topleft Framdefinition
        topleft.setFrameShape(QFrame.StyledPanel)         # Rahmen
        self.figure = plt.figure(facecolor='#F0F0F0')     # Hintergrundfarbe grau
        self.canvas = FigureCanvas(self.figure)
        #self.toolbar = NavigationToolbar(self.canvas, self)  keine Toolbar
        #---------------- Eingabefelder Definitionen --------------------
        label_ueberschrift_topleft = QLabel("Eingabefelder")
        label_ueberschrift_topleft.setFont(QFont("Arial", 8, QFont.Bold))

        self.eingabe_kapazitaet_v = QLineEdit(topleft)  # SET
        self.eingabe_kapazitaet_v.setValidator(QIntValidator())  # Konfig des eingabefeldes
        self.eingabe_kapazitaet_v.setMaxLength((4))  # Konfig des eingabefeldes
        self.eingabe_kapazitaet_v.setFont(QFont("Arial", 8))  # Konfig des eingabefeldes
        self.label_eingabe_kapazitaet = QLabel("Aktuelle Kapazität:")  # Definition Label

        self.eingabe_freier_speicher_v = QLineEdit(topleft)  # SET
        self.eingabe_freier_speicher_v.setValidator(QIntValidator())  # Konfig des eingabefeldes
        self.eingabe_freier_speicher_v.setMaxLength((4))  # Konfig des eingabefeldes
        self.eingabe_freier_speicher_v.setFont(QFont("Arial", 8))  # Konfig des eingabefeldes
        self.label_eingabe_freier_speicher = QLabel("Freier Speicher in GB:")  # Definition Label

        self.eingabe_neue_vm_v = QLineEdit(topleft)  # SET
        self.eingabe_neue_vm_v.setValidator(QIntValidator())  # Konfig des eingabefeldes
        self.eingabe_neue_vm_v.setMaxLength((4))  # Konfig des eingabefeldes
        self.eingabe_neue_vm_v.setFont(QFont("Arial", 8))  # Konfig des eingabefeldes
        self.label_eingabe_neue_vm = QLabel("Zusätzliche VM:")  # Definition Label

        self.label_topright_ueberschrift = QLabel("Ausgabefelder")
        self.label_topright_ueberschrift.setFont(QFont("Arial", 8, QFont.Bold))

        self.label_topright_ueberschrift2 = QLabel("")    #Label für das füllen der Variable

        self.label_neu_belegter_speicher = QLabel("Zukünftige Kapazität:")  # Definition Label
        self.label_topright_belegter_speicher = self.label_neu_belegter_speicher    # Kopie des Labels

        self.label_topright_frei_prozent_vor_hinzufuegen = QLabel("% frei vor Erw.:")
        self.label_topright_frei_prozent_vor_hinzufuegen2 = QLabel("")   #Label für das füllen der Variable
        #self.label_topright_frei_prozent_vor_hinzufuegen2.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)

        self.label_topright_frei_prozent_nach_hinzufuegen = QLabel("% frei nach Erw.:")
        self.label_topright_frei_prozent_nach_hinzufuegen2 = QLabel("")   #Label für das füllen der Variable

        self.label_topright_neu_belegter_speicher = QLabel("Belegter Storage nach Erw.:")
        self.label_topright_neu_belegter_speicher2 = QLabel("")  #Label für das füllen der Variable

        self.label_topright_neu_kapazitaet = QLabel("Neue Kapazität.:")
        self.label_topright_neu_kapazitaet2 = QLabel("")  #Label für das füllen der Variable

        self.label_topright_freier_Speicher_nach_hinzufuegen = QLabel("Freier Storage nach Erw.:")
        self.label_topright_freier_Speicher_nach_hinzufuegen2 = QLabel("")  #Label für das füllen der Variable

        self.label_topright_ausgabe_ergebniss = QLabel("Hallo")
        # ---------------------------Topleft --------------------------------------
        fbox = QFormLayout(topleft)  # zeigt felder an in der Reihenfolge die hier steht für topleft
        fbox.addRow(label_ueberschrift_topleft)
        fbox.addRow(self.label_eingabe_kapazitaet, self.eingabe_kapazitaet_v)  # fügt Label und eigabe hinzu
        fbox.addRow(self.label_eingabe_freier_speicher, self.eingabe_freier_speicher_v)
        fbox.addRow(self.label_eingabe_neue_vm, self.eingabe_neue_vm_v)
        self.button_berechnen = QPushButton(topleft)
        self.button_berechnen.setText("Berechne Storage")
        fbox.addRow(self.button_berechnen)
        self.button_berechnen.clicked.connect(self.button_berechnen_clicked)  # Gedrück dann def button_berechenne_clicked
        # ------------------------ Bottom ---------------------------------------
        bottom = QFrame()
        bottom.setFrameShape(QFrame.StyledPanel)
        vbox = QVBoxLayout(bottom)
        vbox.addWidget(self.canvas)
        self.setLayout(vbox)
        # ------------------------Topright ---------------------------------------
        topright = QFrame()                                   # Subfenster topright
        topright.setFrameShape(QFrame.StyledPanel)            # Rahmen für topright
        rbox = QFormLayout(topright)
        rbox.addRow(self.label_topright_ueberschrift, self.label_topright_ueberschrift2)
        #gridlayout.addWidget(self.label_topright_ueberschrift2, 1, 0)
        self.label_topright_ausgabe_testfeld = QLineEdit(topright)  # SET
        self.label_topright_ausgabe_testfeld.setEnabled(False)
        rbox.addRow(self.label_topright_belegter_speicher, self.label_topright_ausgabe_testfeld)
        rbox.addRow(self.label_topright_frei_prozent_vor_hinzufuegen, self.label_topright_frei_prozent_vor_hinzufuegen2)
        rbox.addRow(self.label_topright_frei_prozent_nach_hinzufuegen, self.label_topright_frei_prozent_nach_hinzufuegen2)
        rbox.addRow(self.label_topright_neu_belegter_speicher, self.label_topright_neu_belegter_speicher2)
        rbox.addRow(self.label_topright_neu_kapazitaet, self.label_topright_neu_kapazitaet2)
        rbox.addRow(self.label_topright_freier_Speicher_nach_hinzufuegen, self.label_topright_freier_Speicher_nach_hinzufuegen2)
        #self.setLayout(rbox) ????????????????????????????????????????????????

        # ------------------------Splitter ---------------------------------------
        splitter1 = QSplitter(Qt.Horizontal)
        splitter1.addWidget(topleft)  # Teilung der beiden Fenster horiz.
        splitter1.addWidget(topright)  # Teilung der beiden Fenster
        splitter1.setSizes([250, 250])  #
        splitter2 = QSplitter(Qt.Vertical)  # Teilung der beiden Fenster verti.
        splitter2.addWidget(splitter1)  #
        splitter2.addWidget(bottom)  #
        hbox.addWidget(splitter2)  #
        self.setLayout(hbox)  # Layout Box

        # ------------------------zentale Fenster definition ---------------------------------------
        QApplication.setStyle(QStyleFactory.create('Cleanlooks'))
        self.setGeometry(500, 500, 400, 400)  # Fenstergröße
        self.setWindowTitle('Storage Calkulator')  # Titel
        image = mpimg.imread("netapp.png")
        plt.axis('off')
        plt.set_cmap('hot')
        plt.imshow(image)

    def button_berechnen_clicked(self):
        # Prüfen ob alle Felder gefüllt

        def testverarbeitung(self):
            print("testverarbeitung")
            belegter_speicher_ohne_vm = int(self.eingabe_kapazitaet_v.text()) - int(self.eingabe_freier_speicher_v.text())  # Berechne Diff = freierStorag
            belegter_speicher_mit_vm_v = int(self.eingabe_kapazitaet_v.text()) - int(self.eingabe_freier_speicher_v.text()) + int(self.eingabe_neue_vm_v.text())
            neu_belegter_speicher_v = int(belegter_speicher_mit_vm_v)   # Berechnung belegter Speicher = VM + Belegter Speicher
            prozent_frei_von_kapazitaet_mit_neuer_vm = 100 - (int((belegter_speicher_mit_vm_v / int(self.eingabe_kapazitaet_v.text())) * 100))
            if ((prozent_frei_von_kapazitaet_mit_neuer_vm >= 20) and (prozent_frei_von_kapazitaet_mit_neuer_vm < 100)):
                # Anweisungsblock für Sonderfall, wenn Storage nicht erhöht werden muss bedeutet prozent_frei differenz_v  / (self.eingabe_kapazitaet_v.text -neu_belegter_speicher_v
                frei_prozent_vor_hinzufuegen_v = 100 - (((belegter_speicher_ohne_vm / int(self.eingabe_kapazitaet_v.text())) * 100))  # Berechne in % wieviel freier Storage vor VM hinzufügen
                neu_kapazitaet_v = int(self.eingabe_kapazitaet_v.text())
                differenz_nach_neuer_vm_v = neu_kapazitaet_v - neu_belegter_speicher_v  # Berechne neue Diff
                frei_prozent_nach_hinzufuegen_v = ((differenz_nach_neuer_vm_v / neu_kapazitaet_v) * 100)  # Berechnung % frei
                freier_Speicher_nach_hinzufuegen_v = neu_kapazitaet_v - neu_belegter_speicher_v
                # -----------------------------------------------------------------------
                print("Balken gleich")
                print("prozent_frei_von_kapazitaet_mit_neuer_vm", prozent_frei_von_kapazitaet_mit_neuer_vm)
            else:
                # -----------Berechnungen--------------------------------------------------
                #differenz_v = int(self.eingabe_kapazitaet_v.text()) - int(self.eingabe_belegter_speicher_v.text())  # Berechne Diff = freier Storage vor VM hinzufügen
                frei_prozent_vor_hinzufuegen_v = 100 - (((belegter_speicher_ohne_vm / int(self.eingabe_kapazitaet_v.text())) * 100))  # Berechne in % wieviel freier Storage vor VM hinzufügen
                neu_belegter_speicher_v = int(belegter_speicher_ohne_vm) + int(self.eingabe_neue_vm_v.text()) # Berechnung belegter Speicher = VM + Belegter Speicher
                neu_kapazitaet_v = int(neu_belegter_speicher_v * 1.25)
                differenz_nach_neuer_vm_v = neu_kapazitaet_v - neu_belegter_speicher_v  # Berechne neue Diff.
                frei_prozent_nach_hinzufuegen_v = ((differenz_nach_neuer_vm_v / neu_kapazitaet_v) * 100)  # Berechnung % frei
                freier_Speicher_nach_hinzufuegen_v = neu_kapazitaet_v - neu_belegter_speicher_v  # -----------------------------------------------------------------------
            self.label_topright_ausgabe_ergebniss2 = QLabel(str(neu_kapazitaet_v))  # bestehendes Label ändern in anderer Dim
            self.label_topright_ausgabe_testfeld.setEnabled(True)  # Ausgabefeld aktivieren um Wert kopieren zu können
            self.label_topright_ausgabe_testfeld.setReadOnly(True)  # readonly
            self.label_topright_ausgabe_testfeld.setText(str(neu_kapazitaet_v))  # Textfeld füllen
            self.label_topright_frei_prozent_vor_hinzufuegen2.setText(str(frei_prozent_vor_hinzufuegen_v.__round__(0)))
            self.label_topright_frei_prozent_nach_hinzufuegen2.setText(str(frei_prozent_nach_hinzufuegen_v.__round__(0)))
            self.label_topright_neu_belegter_speicher2.setText(str(neu_belegter_speicher_v))
            self.label_topright_neu_kapazitaet2.setText(str(neu_kapazitaet_v))
            self.label_topright_freier_Speicher_nach_hinzufuegen2.setText(str(freier_Speicher_nach_hinzufuegen_v))
            self.figure.clear()  # init Graph
            vm_bar = [0, int(self.eingabe_neue_vm_v.text())]
            belegter_speicher_bar = [int(belegter_speicher_ohne_vm), belegter_speicher_mit_vm_v]
            kapazit_bar = [int(self.eingabe_kapazitaet_v.text()), neu_kapazitaet_v]
            r = range(2)
            countries = ['vor Erweit.', 'nach Erweit.']
            ind = [r for r, _ in enumerate(countries)]
            # plt.figure(figsize=(4, 4)) FEHLER FEHLER
            plt.ylabel("GB")
            plt.xlabel("Zustände")
            plt.bar(ind, kapazit_bar, width=0.5, color='#000066', edgecolor='black', hatch="/")
            plt.bar(ind, belegter_speicher_bar, width=0.5, color='b', edgecolor='black', hatch="/")
            plt.bar(ind, vm_bar, width=0.5, color='#616ccf', edgecolor='black', label='test', hatch="/")
            plt.xticks(ind, countries)
            plt.legend(("freier Storage", "belegter Storage", "neue VM"), loc="upper left")

            plt.grid(True)

            c_rects = plt.bar( ind, kapazit_bar, align='center', alpha=0.0)

            def autolabel(rects):
                for rect in rects:
                    height = rect.get_height()
                    plt.text(rect.get_x() + rect.get_width()/2., height + 1, '%.1f' % float(height), ha='center', va='bottom')
            
            autolabel(c_rects)

            self.canvas.draw()
            testausgabe = int(self.eingabe_kapazitaet_v.text()) + int(self.eingabe_neue_vm_v.text())
            # --------Testausgabe----------------------------------------------------------------------------
            print("Eingabewerte")
            print("Ausgangsgröße:", self.eingabe_kapazitaet_v.text())
            print("Neue VM:", self.eingabe_neue_vm_v.text())
            print("freier Speicher:", self.eingabe_freier_speicher_v.text())
            # print(self.nm.text())  # achtung besondere schreibweise um an den Wert zu kommen
            # print("Test", testausgabe)
            print("Nach Berechnung")
            #print("Differenz:", differenz_v)
            print("% frei:", frei_prozent_vor_hinzufuegen_v)
            print("Belegter Speicher neu:", neu_belegter_speicher_v)
            print("Belegter Speicher:", neu_kapazitaet_v)
            print("% frei nach Erweierung:", frei_prozent_nach_hinzufuegen_v)
            print("vm_bar", vm_bar)
            print("belegter_speicher_bar", belegter_speicher_bar)
            print("kapazit_bar", kapazit_bar)
            print("IND", ind)
            print("Ende erreicht")

        if (self.eingabe_kapazitaet_v.text() == ""):
            QMessageBox.critical(self, "Warnung", "Fehlender Wert in Kapazität")
        elif (self.eingabe_freier_speicher_v.text() == ""):
            QMessageBox.critical(self, "Warnung", "Fehlender Wert in belegter Speicher")
        elif (int(self.eingabe_freier_speicher_v.text()) > int(self.eingabe_kapazitaet_v.text())):
            QMessageBox.critical(self, "Warnung", "Kapazitaet darf nicht kleiner sein")
        elif (self.eingabe_neue_vm_v.text() == ""):
            QMessageBox.critical(self, "Warnung", "Fehlender Wert in neue VM")
        else:
            testverarbeitung(self)

def main():
    app = QApplication(sys.argv)
    ex = storekalkulator()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
    # Aufgaben: falscheingabe abfangen. belegter platz darf nicht höher als Kapazität sein. dann msg. falscheingabe
    # % nach falscher wert
    # Ausgabefelder rechtsbümdig formatieren?
    # icon fenster
    # label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
    # + und - zeichen verhindern
