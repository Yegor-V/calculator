from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import uic
import sys


class MyForm(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        Form, Base = uic.loadUiType('calc.ui')
        self.form = Form()
        self.form.setupUi(self)

        self.form.b1.clicked.connect(self.handler)
        self.form.b2.clicked.connect(self.handler)
        self.form.b3.clicked.connect(self.handler)
        self.form.b4.clicked.connect(self.handler)
        self.form.b5.clicked.connect(self.handler)
        self.form.b6.clicked.connect(self.handler)
        self.form.b7.clicked.connect(self.handler)
        self.form.b8.clicked.connect(self.handler)
        self.form.b9.clicked.connect(self.handler)
        self.form.b0.clicked.connect(self.handler)

        self.form.b_dot.clicked.connect(self.handler)

        self.form.b_div.clicked.connect(self.handler)
        self.form.b_minus.clicked.connect(self.handler)
        self.form.b_mult.clicked.connect(self.handler)
        self.form.b_plus.clicked.connect(self.handler)

        self.form.b_eq.clicked.connect(self.handler)

        self.form.b_clear.clicked.connect(self.handler)

        self.form.lcdNumber.setNumDigits(10)

        self.number_one = None
        self.number_two = None
        self.operation = None

    def handler(self):
        # clicking on button results in assignment its text to text_button variable
        button = self.sender()
        text_button = button.text()  # text_button type is <str>

        if self.number_one is None and self.number_two is None and self.operation is None:
            if text_button in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
                self.number_one = ''
                self.number_one += text_button
                self.form.lcdNumber.display(self.number_one)
            if text_button in ['+', '-', '*', '/']:
                self.number_one = '0'
                self.operation = text_button

            if text_button == '.':
                self.number_one = '0.'
                self.form.lcdNumber.display(self.number_one)
            if text_button == 'C':
                pass
            if text_button == '=':
                self.form.lcdNumber.display('0')

        elif self.number_one is not None and self.number_two is None and self.operation is None:
            if text_button in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
                if self.number_one == '0' and text_button == '0':
                    pass
                elif len(self.number_one) > 6:
                    pass
                else:
                    self.number_one += text_button
                    self.form.lcdNumber.display(self.number_one)
            if text_button in ['+', '-', '*', '/']:
                self.operation = text_button
                self.form.lcdNumber.display(self.number_one)
            if text_button == '.':
                if '.' in self.number_one:
                    pass
                else:
                    self.number_one += text_button
                    self.form.lcdNumber.display(self.number_one)
            if text_button == 'C':
                self.number_one = None
                self.form.lcdNumber.display(int(0))
            if text_button == '=':
                self.form.lcdNumber.display(self.number_one)

        elif self.number_one is not None and self.number_two is None and self.operation is not None:
            if text_button in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
                self.number_two = ''
                self.number_two += text_button
                self.form.lcdNumber.display(self.number_two)

            if text_button in ['+', '-', '*', '/']:
                self.operation = text_button
                self.form.lcdNumber.display(self.number_one)

            if text_button == '.':
                self.number_two = '0.'
                self.form.lcdNumber.display(self.number_two)

            if text_button == 'C':
                self.number_one = None
                self.operation = None
                self.form.lcdNumber.display('0')

            if text_button == '=':
                self.operation = None
                self.form.lcdNumber.display(self.number_one)

        elif self.number_one is not None and self.number_two is not None and self.operation is not None:
            if text_button in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
                if self.number_two == '0' and text_button == '0':
                    pass
                if len(self.number_two) > 6:
                    pass
                else:
                    self.number_two += text_button
                    self.form.lcdNumber.display(self.number_two)

            if text_button in ['+', '-', '*', '/']:
                n1 = float(self.number_one)
                n2 = float(self.number_two)
                if self.operation == '/' and n2 == 0:
                    self.number_one = None
                    self.number_two = None
                    self.operation = None
                    self.form.lcdNumber.display('Error')
                else:
                    if self.operation == '+':
                        res = n1 + n2
                    if self.operation == '-':
                        res = n1 - n2
                    if self.operation == '*':
                        res = n1 * n2
                    if self.operation == '/':
                        res = n1 / n2
                        res = round(res, 6)
                    if int(res) == res:
                        res = int(res)
                        self.form.lcdNumber.display(res)
                    else:
                        self.form.lcdNumber.display(res)

                    self.number_one = str(res)
                    self.operation = text_button
                    self.number_two = None

            if text_button == '.':
                if '.' in self.number_two:
                    pass
                else:
                    self.number_two += text_button
                    self.form.lcdNumber.display(self.number_two)

            if text_button == '=':
                n1 = float(self.number_one)
                n2 = float(self.number_two)
                if self.operation == '/' and n2 == 0:
                    self.number_one = None
                    self.number_two = None
                    self.operation = None
                    self.form.lcdNumber.display('Error')
                else:


                    if self.operation == '+':
                        res = n1 + n2
                    if self.operation == '-':
                        res = n1 - n2
                    if self.operation == '*':
                        res = n1 * n2

                    if self.operation == '/':
                        res = n1 / n2
                        res = round(res, 6)

                    if int(res) == res:
                        res = int(res)
                        self.form.lcdNumber.display(res)
                    else:
                        self.form.lcdNumber.display(res)

                    self.number_one = str(res)
                    self.number_two = None
                    self.operation = None
        '''
        if text_button in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.'):
            if self.operation == '':
                self.text_number_one += text_button
                self.form.lcdNumber.display(self.text_number_one)
            else:
                self.text_number_two += text_button
                self.form.lcdNumber.display(self.text_number_two)
        elif text_button in ('+', '-', '*', '/'):
                self.operation = text_button
                self.form.lcdNumber.display(self.text_number_one)

        elif text_button == '=':
            if self.text_number_one == '':
                self.number_one = 0
            else:
                self.number_one = int(self.text_number_one)
            if self.text_number_two == '':
                self.number_two = 0
            else:
                self.number_two = int(self.text_number_two)
            res = 0
            if self.operation == '+':
                res = self.number_one + self.number_two
            if self.operation == '-':
                res = self.number_one - self.number_two
            if self.operation == '*':
                res = self.number_one * self.number_two
            if self.operation == '/':
                if self.number_two == 0:
                    res = 'Error'
                else:
                    res = self.number_one / self.number_two
                    res = round(res, 7)
            if self.operation == '':
                res = self.number_two

            self.form.lcdNumber.display(res)

            self.text_number_one = ''
            self.number_one = 0
            self.text_number_two = str(res)
            self.number_two = res
            self.operation = ''

        elif text_button == 'C':
            self.form.lcdNumber.display('0')
            self.number_one = 0
            self.number_two = 0
            self.text_number_one = ''
            self.text_number_two = ''
            self.operation = ''
        '''


def main():
    if __name__ == '__main__':
        app = QApplication(sys.argv)
        window = MyForm()
        window.show()
        sys.exit(app.exec_())

main()



