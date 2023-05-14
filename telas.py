from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMessageBox

def entrar():
    user = tela1.usuario.text()
    password = tela1.senha.text()
    if user == '' or password == '':
        QMessageBox.about(tela1, 'Atenção', 'Preencha os campos solicitados!')
    elif user == 'admin' and password == '321':
        QMessageBox.about(tela1, 'Usuário OK', 'Usuário aceito.')
        tela2.show()
        tela1.close()
    else:
        QMessageBox.about(tela1, 'Atenção', 'Usuário e/ou senha inválido.')
    tela1.usuario.setText("")
    tela1.senha.setText("")

def cadastrar():
    tela3.show()
    tela1.close()

def cadastroFinal():
    name = tela3.nome.text()
    age = tela3.idade.text()
    email = tela3.email.text()

    if name == '' or age == '' or email == '':
        QMessageBox.about(tela3, 'Atenção', 'Preencha os campos solicitados!')
    elif not age.isdigit():
        QMessageBox.about(tela3, 'Atenção', 'Idade inválida.')
    else:
        if tela3.javascript.isChecked():
            QMessageBox.about(tela3, 'Curso', 'Curso Javascript selecionado.')
            QMessageBox.about(tela3, 'Cadastro OK', 'Cadastro realizado com sucesso.')
        elif tela3.python.isChecked():
            QMessageBox.about(tela3, 'Curso', 'Curso Python selecionado.')
            QMessageBox.about(tela3, 'Cadastro OK', 'Cadastro realizado com sucesso.')
        elif tela3.php.isChecked():
            QMessageBox.about(tela3, 'Curso', 'Curso PHP selecionado.')
            QMessageBox.about(tela3, 'Cadastro OK', 'Cadastro realizado com sucesso.')
        else:
            QMessageBox.about(tela3, 'Atenção', 'Selecione um curso.')

app = QtWidgets.QApplication([])
tela1 = uic.loadUi("tela-login.ui")
tela2 = uic.loadUi("tela-bem-vindo.ui")
tela3 = uic.loadUi("tela-cadastro.ui")
tela1.botaoAcessar.clicked.connect(entrar)
tela1.botaoCadastrar.clicked.connect(cadastrar)
tela3.botaoCadastroFinal.clicked.connect(cadastroFinal)
tela1.show()
app.exec()
