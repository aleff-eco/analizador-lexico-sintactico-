from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PyQt5.uic import loadUi
from ana_lex import analisis, tokens
from ana_sintac import verificar

class MiVentana(QMainWindow):
    def __init__(self):
        super(MiVentana, self).__init__()
        loadUi('ventana.ui', self)
        
        self.pushButton.clicked.connect(self.verificar)
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setHorizontalHeaderLabels(["Token", "Dato", "Posicion", "Status"])
        self.tableWidget.setColumnWidth(0, 240)
        self.tableWidget.setColumnWidth(1, 90)
        self.tableWidget.setColumnWidth(2, 85)
        self.tableWidget.setColumnWidth(3, 40)

    def verificar(self):
        self.CE.clear()  
        texto = self.textEdit.toPlainText()
        has_errors, tokens_lexico = analisis(texto)

        error_counter = 0
        self.tableWidget.setRowCount(0)

        for lexeme in tokens_lexico:
            parts = lexeme.split()
            tipo = parts[0]
            valor = parts[1]
            posicion = parts[2]

            rowPosition = self.tableWidget.rowCount()
            self.tableWidget.insertRow(rowPosition)

            self.tableWidget.setItem(rowPosition, 0, QTableWidgetItem(tipo))
            self.tableWidget.setItem(rowPosition, 1, QTableWidgetItem(valor))
        
            lexpos_value = posicion.split()[-1]
            self.tableWidget.setItem(rowPosition, 2, QTableWidgetItem(lexpos_value))

            if tipo == "ERROR":
                error_counter += 1
                self.tableWidget.setItem(rowPosition, 3, QTableWidgetItem("✕"))

        self.CE.addItem(str(error_counter))
        
        
        self.sintactico.clear()                      
        if (error_counter == 0):
            print("Análisis léxico correcto")
            syntax_result = verificar(texto)
            if syntax_result:
                print("Análisis sintáctico correcto")
                self.sintactico.addItem("Status: Sintaxis Correcta")
                #self.tableWidget_2.setItem("Status: Sintaxis Correcta")
            else:
                print("Error de sintaxis")
                self.sintactico.addItem("Status: error de sintaxis")
                #self.tableWidget_2.setItem("Status: Error de sintaxis")
        else:
            print("Análisis léxico con errores. Revise la tabla para más detalles.")
            self.sintactico.addItem("Status: Error de lexico.")
            #self.tableWidget_2.setItem("Status: Error en análisis léxico")



if __name__ == '__main__':
    app = QApplication([])
    ventana = MiVentana()
    ventana.show()
    app.exec_()
