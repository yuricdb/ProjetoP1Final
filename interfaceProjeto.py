from PyQt5 import QtCore, QtGui, QtWidgets
import modulosProjeto
import os

class Ui_TelaInicial(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        '''
        Construtor da classe
        :param parent: a qual janela está "herdando"
        '''
        super(Ui_TelaInicial, self).__init__(parent)
        modulosProjeto.inicio()
        self.userUI = 'VISITANTE'
        self.setupUi(self)
        modulosProjeto.inicio()

    def setupUi(self, MainWindow):
        '''
        Configurações iniciais da janela
        :param MainWindow: chama a si individualmente quando cria um objeto (nesse caso a janela)
        :return:
        '''
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(520, 350)
        MainWindow.setMinimumSize(QtCore.QSize(520, 350))
        MainWindow.setMaximumSize(QtCore.QSize(520, 350))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setEnabled(True)
        self.widget.setGeometry(QtCore.QRect(70, 150, 391, 151))
        self.widget.setObjectName("widget")
        self.lineEditLogin = QtWidgets.QLineEdit(self.widget)
        self.lineEditLogin.setEnabled(True)
        self.lineEditLogin.setGeometry(QtCore.QRect(130, 20, 191, 22))
        iconTela = QtGui.QIcon()
        iconTela.addPixmap(QtGui.QPixmap("icones/icotela.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        MainWindow.setWindowIcon(iconTela)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.lineEditLogin.setFont(font)
        self.lineEditLogin.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEditLogin.setInputMask("")
        self.lineEditLogin.setFrame(True)
        self.lineEditLogin.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditLogin.setObjectName("lineEditLogin")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(50, 60, 69, 22))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setScaledContents(False)
        self.label_3.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(50, 20, 69, 22))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setScaledContents(False)
        self.label_4.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label_4.setObjectName("label_4")
        self.lineEditLogin_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEditLogin_2.setGeometry(QtCore.QRect(130, 60, 191, 22))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.lineEditLogin_2.setFont(font)
        self.lineEditLogin_2.setFrame(True)
        self.lineEditLogin_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditLogin_2.setObjectName("lineEditLogin_2")
        self.lineEditLogin_2.setEchoMode(QtWidgets.QLineEdit.Password) #linha que deixa a senha inserida como asterisco
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(130, 100, 121, 32))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(210, 0, 128, 151))
        self.label.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("icones\\iconeProjeto2menor.png")) #lembrar de alterar essa imagem pra que ela fique na pasta do projeto
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(False)
        self.label.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 520, 21))
        self.menubar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.menubar.setDefaultUp(False)
        self.menubar.setNativeMenuBar(True)
        self.menubar.setObjectName("menubar")
        self.menuAjuda = QtWidgets.QMenu(self.menubar)
        self.menuAjuda.setObjectName("menuAjuda")
        self.menuUsu_rio = QtWidgets.QMenu(self.menubar)
        self.menuUsu_rio.setObjectName("menuUsu_rio")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionYCB = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setItalic(False)
        self.actionYCB.setFont(font)
        self.actionYCB.setVisible(True)
        self.actionYCB.setObjectName("actionYCB")
        self.actionCRIAR_CAMPEONATO = QtWidgets.QAction(MainWindow)
        self.actionCRIAR_CAMPEONATO.setObjectName("actionCRIAR_CAMPEONATO")
        self.actionVISUALIZAR_TABELA = QtWidgets.QAction(MainWindow)
        self.actionVISUALIZAR_TABELA.setEnabled(True)
        self.actionVISUALIZAR_TABELA.setObjectName("actionVISUALIZAR_TABELA")
        self.actionINSERIR_PLACAR_DOS_JOGOS = QtWidgets.QAction(MainWindow)
        self.actionINSERIR_PLACAR_DOS_JOGOS.setObjectName("actionINSERIR_PLACAR_DOS_JOGOS")
        self.actionVISUALIZAR_PLACARES_DOS_JOGOS = QtWidgets.QAction(MainWindow)
        self.actionVISUALIZAR_PLACARES_DOS_JOGOS.setEnabled(True)
        self.actionVISUALIZAR_PLACARES_DOS_JOGOS.setObjectName("actionVISUALIZAR_PLACARES_DOS_JOGOS")
        self.actionVISUALIZAR_CLASSIFICA_O = QtWidgets.QAction(MainWindow)
        self.actionVISUALIZAR_CLASSIFICA_O.setObjectName("actionVISUALIZAR_CLASSIFICA_O")
        self.actionREMOVER_SENHA_DO_BANCO_DE_DADOS = QtWidgets.QAction(MainWindow)
        self.actionREMOVER_SENHA_DO_BANCO_DE_DADOS.setObjectName("actionREMOVER_SENHA_DO_BANCO_DE_DADOS")
        self.actionVISUALIZAR_REGISTROS = QtWidgets.QAction(MainWindow)
        self.actionVISUALIZAR_REGISTROS.setObjectName("actionVISUALIZAR_REGISTROS")
        self.actionSAIR_DA_CONTA = QtWidgets.QAction(MainWindow)
        self.actionSAIR_DA_CONTA.setObjectName("actionSAIR_DA_CONTA")
        self.actionCadastrar_novo_usu_rio = QtWidgets.QAction(MainWindow)
        self.actionCadastrar_novo_usu_rio.setObjectName("actionCadastrar_novo_usu_rio")
        self.menuAjuda.addAction(self.actionYCB)
        self.menuUsu_rio.addAction(self.actionVISUALIZAR_TABELA)
        self.menuUsu_rio.addAction(self.actionVISUALIZAR_PLACARES_DOS_JOGOS)
        self.menuUsu_rio.addAction(self.actionVISUALIZAR_CLASSIFICA_O)
        self.menuUsu_rio.addAction(self.actionCRIAR_CAMPEONATO)
        self.menuUsu_rio.addAction(self.actionINSERIR_PLACAR_DOS_JOGOS)
        self.menuUsu_rio.addAction(self.actionVISUALIZAR_REGISTROS)
        self.menuUsu_rio.addAction(self.actionREMOVER_SENHA_DO_BANCO_DE_DADOS)
        self.menuUsu_rio.addAction(self.actionCadastrar_novo_usu_rio)
        self.menuUsu_rio.addAction(self.actionSAIR_DA_CONTA)
        self.menubar.addAction(self.menuUsu_rio.menuAction())
        self.menubar.addAction(self.menuAjuda.menuAction())
        self.habilitaMenu(False)
        self.senhaInicial()

        self.logadoButton = self.pushButton.clicked.connect(self.recebeTxtLogin)
        self.actionVISUALIZAR_TABELA.triggered.connect(self.mostraTabelaUI) #teste conectar o menu para abrir uma janela, é pelo triggered
        self.actionSAIR_DA_CONTA.triggered.connect(self.logOut)
        self.actionCadastrar_novo_usu_rio.triggered.connect(self.exibeCadastroUi)
        self.actionCRIAR_CAMPEONATO.triggered.connect(self.telaCriaTorneio)
        self.actionINSERIR_PLACAR_DOS_JOGOS.triggered.connect(self.marcaPlacarUi)
        self.actionVISUALIZAR_CLASSIFICA_O.triggered.connect(self.exibeClassifica)
        self.actionVISUALIZAR_REGISTROS.triggered.connect(self.mostraRegistroUI)
        self.actionREMOVER_SENHA_DO_BANCO_DE_DADOS.triggered.connect(self.removeSenhaUI)
        self.actionVISUALIZAR_PLACARES_DOS_JOGOS.triggered.connect(self.jogosMarcados)
        self.actionYCB.triggered.connect(self.about)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        '''
        Define alguns nomes padrão para os recursos dentro da janela criada
        :param MainWindow: Recebe o nome do obj para qual a função realizará a ação de forma individual
        :return:
        '''
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Tela Inicial - "+ self.userUI))
        self.label_3.setText(_translate("MainWindow", "Senha:"))
        self.label_4.setText(_translate("MainWindow", "Usuário:"))
        self.pushButton.setText(_translate("MainWindow", "Login"))
        self.menuAjuda.setTitle(_translate("MainWindow", "Ajuda"))
        self.menuUsu_rio.setTitle(_translate("MainWindow", "Usuário"))
        self.actionYCB.setText(_translate("MainWindow", "Sobre"))
        self.actionCRIAR_CAMPEONATO.setText(_translate("MainWindow", "CRIAR CAMPEONATO"))
        self.actionVISUALIZAR_TABELA.setText(_translate("MainWindow", "VISUALIZAR TABELA"))
        self.actionINSERIR_PLACAR_DOS_JOGOS.setText(_translate("MainWindow", "INSERIR PLACAR DOS JOGOS"))
        self.actionVISUALIZAR_PLACARES_DOS_JOGOS.setText(_translate("MainWindow", "VISUALIZAR PLACARES DOS JOGOS"))
        self.actionVISUALIZAR_CLASSIFICA_O.setText(_translate("MainWindow", "VISUALIZAR CLASSIFICAÇÃO"))
        self.actionREMOVER_SENHA_DO_BANCO_DE_DADOS.setText(_translate("MainWindow", "REMOVER CONTA REGISTRADA"))
        self.actionVISUALIZAR_REGISTROS.setText(_translate("MainWindow", "VISUALIZAR REGISTROS"))
        self.actionSAIR_DA_CONTA.setText(_translate("MainWindow", "SAIR DA CONTA "))
        self.actionCadastrar_novo_usu_rio.setText(_translate("MainWindow", "CADASTRAR NOVO USUÁRIO"))


    def habilitaMenu(self, habilita):
        '''
        Define quais itens começarão habilitados no menu
        :param habilita: nome do obj
        :return:
        '''
        self.actionCRIAR_CAMPEONATO.setEnabled(habilita)
        self.actionINSERIR_PLACAR_DOS_JOGOS.setEnabled(habilita)
        self.actionREMOVER_SENHA_DO_BANCO_DE_DADOS.setEnabled(habilita)
        self.actionVISUALIZAR_REGISTROS.setEnabled(habilita)
        self.actionSAIR_DA_CONTA.setEnabled(habilita)
        self.actionCadastrar_novo_usu_rio.setEnabled(habilita)


    def senhaInicial(self):
        '''
        Verifica se o programa está sendo executado pela primeira vez, através do banco de senhas
        :return: se for o primeiro acesso, permitirá ao primeiro visitante criar cadastro, se falso só poderá criar cadastro quem já tiver uma conta cadastrada
        '''
        senhaVazia = modulosProjeto.primeiraSenha()
        if senhaVazia:
            self.actionCadastrar_novo_usu_rio.setEnabled(True)
        else:
            self.actionCadastrar_novo_usu_rio.setEnabled(False)

    def exibeCadastroUi(self):
        '''
        Inicializa a classe (para abrir a janela de cadastro)
        :return:
        '''
        self.CadastroUiLogin = Ui_EntraLogin() #deixando o obj na função fora do init, faz com que as informações sejam descartadas quando se fecha a janela
        self.CadastroUiLogin.show()

    def marcaPlacarUi(self):
        '''
        Se já tiver sido criado um campeonato inicializa a classe (para abrir a janela marcar placar)
        :return:
        '''
        if modulosProjeto.verificaArquivo('tabelacampeonato.csv'):
            self.marcaUi = Ui_Placar()
            self.marcaUi.show()
        else:
            self.statusbar.showMessage('Campeonato ainda não foi criado')

    def telaCriaTorneio(self):
        '''
        Inicializa a classe (para abrir a janela criar um torneio)
        :return:
        '''
        self.janelaTorneio = Ui_Torneio()
        self.janelaTorneio.show()

    def exibeClassifica(self):
        '''
        Verifica se existem partidas marcadas, se sim, inicializa a classe (para abrir a janela de classificação)
        :return:
        '''
        existeArq = os.listdir('peladeiros\\partidas\\')
        if len(existeArq) != 0:
            self.classificaUI = Ui_Classifica()
            self.classificaUI.show()
            modulosProjeto.log('Visualizou a classificação', self.userUI)
        else:
            self.statusbar.showMessage('Ainda não há jogos marcados para classificação')

    def mostraTabelaUI(self):
        '''
        Se um torneio já tiver sido criado, inicializa a classe (para abrir a janela mostrar tabela)
        :return:
        '''
        if modulosProjeto.verificaArquivo('tabelacampeonato.csv'):
            self.tabelaUI = Ui_TabelaVisual()
            self.tabelaUI.show()
            modulosProjeto.log('Visualizou a tabela', self.userUI)
        else:
            self.statusbar.showMessage('Campeonato ainda não foi criado')

    def mostraRegistroUI(self):
        '''
        Inicializa a classe (para abrir a janela de registros)
        :return:
        '''
        self.registroUI = Ui_RegistroUI()
        self.registroUI.show()
        modulosProjeto.log('Visualizou os registros', self.userUI)

    def removeSenhaUI(self):
        '''
        Inicializa a classe (para abrir a janela que remove conta)
        :return:
        '''
        self.mostraSenhasUI = Ui_RemoveSenha()
        self.mostraSenhasUI.show()

    def jogosMarcados(self):
        '''
        Se tiver jogos marcados, inicializa a classe (para abrir a janela que exibe os jogos marcados por rodada)
        :return:
        '''
        existeArq = os.listdir('peladeiros\\partidas\\')
        if len(existeArq) != 0:
            self.exibeMarcadosUI = Ui_JogosMarcados()
            self.exibeMarcadosUI.show()
        else:
            self.statusbar.showMessage('Não há partidas marcadas')

    def recebeTxtLogin(self):
        '''
        Verifica o login e senha do usuário para acesso ao programa como usuário gerenciador (habilita outras opções de acesso no menu)
        :return: se true entra na conta como gerente, se false mostra a msg acesso negado
        '''
        login = self.lineEditLogin.text()
        senha = self.lineEditLogin_2.text()
        resposta = modulosProjeto.acesso(login, senha)
        if resposta == True:
            self.statusbar.showMessage('Acesso permitido')
            self.widget.hide()
            self.habilitaMenu(True)
            self.userUI = login
            MainWindow.setWindowTitle('Tela Inicial - '+ self.userUI.upper())
            modulosProjeto.log(f'Entrou com a conta "{login}"', ui.userUI)
            return True
        else:
            self.statusbar.showMessage('Acesso negado')
            return False

    def logOut(self):
        '''
        Sai da conta logada
        :return:
        '''
        self.habilitaMenu(False)
        self.widget.show()
        self.lineEditLogin.setText('')
        self.lineEditLogin_2.setText('')
        self.userUI = 'VISITANTE'
        MainWindow.setWindowTitle('Tela Inicial - ' + self.userUI)
        modulosProjeto.log(f'Saiu da conta', ui.userUI)

    def about(self):
        '''
        Inicializa a classe (para abrir a janela de informações do programa)
        :return:
        '''
        self.sobre = Ui_About()
        self.sobre.show()


class Ui_EntraLogin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(Ui_EntraLogin, self).__init__(parent)
        self.setupUi(self)

    def setupUi(self, Form):
        '''
        Configurações iniciais da janela
        :param Form:
        :return: chama a si individualmente quando cria um objeto (nesse caso a janela)
        '''
        Form.setObjectName("Form")
        Form.resize(360, 180)
        Form.setMinimumSize(QtCore.QSize(360, 180))
        Form.setMaximumSize(QtCore.QSize(360, 180))
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 30, 69, 22))
        iconTela = QtGui.QIcon()
        iconTela.addPixmap(QtGui.QPixmap("icones/icotela.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        Form.setWindowIcon(iconTela)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setScaledContents(False)
        self.label.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label.setObjectName("label")
        self.lineEditLogin = QtWidgets.QLineEdit(Form)
        self.lineEditLogin.setGeometry(QtCore.QRect(110, 30, 215, 22))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.lineEditLogin.setFont(font)
        self.lineEditLogin.setObjectName("lineEditLogin")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(30, 70, 69, 22))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setScaledContents(False)
        self.label_2.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label_2.setObjectName("label_2")
        self.labelSenha = QtWidgets.QLabel(Form)
        self.labelSenha.setGeometry(QtCore.QRect(110, 60, 69, 41))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.labelSenha.setFont(font)
        self.labelSenha.setText("")
        self.labelSenha.setScaledContents(False)
        self.labelSenha.setAlignment(QtCore.Qt.AlignCenter)
        self.labelSenha.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.labelSenha.setObjectName("labelSenha")
        self.labelSenha_2 = QtWidgets.QLabel(Form)
        self.labelSenha_2.setGeometry(QtCore.QRect(0, 150, 360, 22))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.labelSenha_2.setFont(font)
        self.labelSenha_2.setText("")
        self.labelSenha_2.setScaledContents(False)
        self.labelSenha_2.setAlignment(QtCore.Qt.AlignCenter)
        self.labelSenha_2.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.labelSenha_2.setObjectName("labelSenha_2")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(120, 110, 120, 32))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.valida)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        '''
        Define alguns nomes padrão para os recursos dentro da janela criada
        :param Form: Recebe o nome do obj para qual a função realizará a ação de forma individual
        :return:
        '''
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Cadastro Usuário"))
        self.label.setText(_translate("Form", "Usuário:"))
        self.label_2.setText(_translate("Form", "Senha:"))
        self.pushButton.setText(_translate("Form", "Cadastrar"))

    def valida(self):
        '''
        Recebe o nome e verifica se o usuário já foi cadastrado
        :return: msg mostrando se foi ou não cadastrado com sucesso
        '''
        nomeLogin = self.lineEditLogin.text()
        respotaValida = modulosProjeto.cadastroUsuario(nomeLogin)
        if respotaValida == False:
            self.labelSenha_2.setText('Usuário já cadastrado!')
        else:
            self.labelSenha_2.setText('Usuário cadastrado com sucesso!')
            self.labelSenha.setText(respotaValida)
            modulosProjeto.log(f'Criou a conta "{nomeLogin}"', ui.userUI)


class Ui_Placar(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(Ui_Placar, self).__init__(parent)
        self.setupUi(self)

    def setupUi(self, Placar):
        '''
        Configurações iniciais da janela
        :param Placar: chama a si individualmente quando cria um objeto (nesse caso a janela)
        :return:
        '''
        Placar.setObjectName("Placar")
        Placar.resize(437, 415)
        self.tableWidget = QtWidgets.QTableWidget(Placar)
        self.tableWidget.setEnabled(True)
        self.tableWidget.setGeometry(QtCore.QRect(0, 70, 436, 200))
        iconTela = QtGui.QIcon()
        iconTela.addPixmap(QtGui.QPixmap("icones/icotela.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        Placar.setWindowIcon(iconTela)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.tableWidget.setFont(font)
        self.tableWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tableWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setTabKeyNavigation(False)
        self.tableWidget.setProperty("showDropIndicator", False)
        self.tableWidget.setDragDropOverwriteMode(False)
        self.tableWidget.setAlternatingRowColors(False)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tableWidget.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.tableWidget.setShowGrid(False)
        self.tableWidget.setGridStyle(QtCore.Qt.NoPen)
        self.tableWidget.setCornerButtonEnabled(True)
        self.tableWidget.setAlternatingRowColors(True)
        self.tempPlacarVazio()
        self.criaTabelaUI()
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(True)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setSortIndicatorShown(False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.pushButton_MarcaGol = QtWidgets.QPushButton(Placar)
        self.pushButton_MarcaGol.setGeometry(QtCore.QRect(196, 304, 41, 41))  #ok
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.pushButton_MarcaGol.setFont(font)
        self.pushButton_MarcaGol.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icones\\bolaico.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_MarcaGol.setIcon(icon)
        self.pushButton_MarcaGol.setIconSize(QtCore.QSize(39, 39))
        self.pushButton_MarcaGol.setFlat(True)
        self.pushButton_MarcaGol.setObjectName("pushButton_MarcaGol")
        self.label_Mandante = QtWidgets.QLabel(Placar)
        self.label_Mandante.setGeometry(QtCore.QRect(10, 308, 141, 31))  #ok
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_Mandante.setFont(font)
        self.label_Mandante.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_Mandante.setObjectName("label_Mandante")
        self.label_Visitante = QtWidgets.QLabel(Placar)
        self.label_Visitante.setGeometry(QtCore.QRect(280, 308, 141, 31))  #ok
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_Visitante.setFont(font)
        self.label_Visitante.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_Visitante.setObjectName("label_Visitante")
        self.lineEdit_GolCasa = QtWidgets.QLineEdit(Placar)
        self.lineEdit_GolCasa.setGeometry(QtCore.QRect(158, 310, 31, 31))  #ok
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_GolCasa.sizePolicy().hasHeightForWidth())
        self.lineEdit_GolCasa.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.lineEdit_GolCasa.setFont(font)
        self.lineEdit_GolCasa.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.lineEdit_GolCasa.setMaxLength(2)
        self.lineEdit_GolCasa.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_GolCasa.setObjectName("lineEdit_GolCasa")
        self.lineEdit_GolFora = QtWidgets.QLineEdit(Placar)
        self.lineEdit_GolFora.setGeometry(QtCore.QRect(242, 310, 31, 31))  #ok
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_GolFora.sizePolicy().hasHeightForWidth())
        self.lineEdit_GolFora.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.lineEdit_GolFora.setFont(font)
        self.lineEdit_GolFora.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.lineEdit_GolFora.setMaxLength(2)
        self.lineEdit_GolFora.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_GolFora.setObjectName("lineEdit_GolFora")
        self.pushButton_finalizarRodada = QtWidgets.QPushButton(Placar)
        self.pushButton_finalizarRodada.setGeometry(QtCore.QRect(240, 29, 151, 24))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.pushButton_finalizarRodada.setFont(font)
        self.pushButton_finalizarRodada.setObjectName("pushButton_finalizarRodada")
        self.pushButton_finalizarRodada.setEnabled(False)
        self.pushButton_dir = QtWidgets.QPushButton(Placar)
        self.pushButton_dir.setGeometry(QtCore.QRect(250, 360, 44, 40))  #ok
        self.pushButton_dir.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icones\\esqico.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_dir.setIcon(icon1)
        self.pushButton_dir.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_dir.setFlat(True)
        self.pushButton_dir.setObjectName("pushButton_dir")
        self.pushButton_esq = QtWidgets.QPushButton(Placar)
        self.pushButton_esq.setGeometry(QtCore.QRect(138, 360, 44, 40))  #ok
        self.pushButton_esq.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icones\\dirico.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_esq.setIcon(icon2)
        self.pushButton_esq.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_esq.setFlat(True)
        self.pushButton_esq.setObjectName("pushButton_esq")
        self.label_infoGol = QtWidgets.QLabel(Placar)
        self.label_infoGol.setGeometry(QtCore.QRect(176, 280, 80, 21))  #ok
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_infoGol.setFont(font)
        self.label_infoGol.setAlignment(QtCore.Qt.AlignCenter)
        self.label_infoGol.setObjectName("label_infoGol")
        self.label_infoMarcar = QtWidgets.QLabel(Placar)
        self.label_infoMarcar.setGeometry(QtCore.QRect(176, 370, 80, 21)) #ok
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_infoMarcar.setFont(font)
        self.label_infoMarcar.setAlignment(QtCore.Qt.AlignCenter)
        self.label_infoMarcar.setObjectName("label_infoMarcar")
        self.retranslateUi(Placar)
        QtCore.QMetaObject.connectSlotsByName(Placar)
        self.mostraComboRodadaUi()
        self.pushButton_MarcaGol.clicked.connect(self.marcaJogoUI)
        self.iniciajogo()
        self.pushButton_dir.clicked.connect(self.avancaJogoDir)
        self.pushButton_esq.clicked.connect(self.avancaJogoEsq)
        self.comboBox_rodada.currentTextChanged.connect(self.mudaRodadaUi)
        self.jogoIndex = 0 #valor inicia index do jogo
        self.pushButton_finalizarRodada.clicked.connect(self.guardaPartidaUI)

    def retranslateUi(self, Placar):
        '''
        Define alguns nomes padrão para os recursos dentro da janela criada
        :param Placar: Recebe o nome do obj para qual a função realizará a ação de forma individual
        :return:
        '''
        _translate = QtCore.QCoreApplication.translate
        Placar.setWindowTitle(_translate("Placar", "Marcar Placar"))
        self.pushButton_finalizarRodada.setText(_translate("Placar", "Finalizar Rodada"))
        self.label_infoGol.setText(_translate("Placar", "Marcar"))
        self.label_infoMarcar.setText(_translate("Placar", "Jogo 1"))

    def tempPlacarVazio(self):
        '''
        Carrrega a classificação
        :return:
        '''
        tabelaCarregada = modulosProjeto.carregaTorneio()
        partidas = list(tabelaCarregada.values())
        self.rowTabela = len(partidas[0])
        self.placarTempUI = {}
        for i in range(0, self.rowTabela):
            self.placarTempUI[i] = []

    def criaTabelaUI(self):
        '''
        cria a tabela com as partidas, de acordo com o numero de jogo e rodadas de cada campeonato
        :return:
        '''
        tabelaCarregada = modulosProjeto.carregaTorneio()
        partidas = list(tabelaCarregada.values())
        self.qtdRodadasUI = len(partidas)
        self.rowTabela = len(partidas[0])
        self.columnTabela = len(partidas[0][0])

        self.tableWidget.setColumnCount(self.columnTabela)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setRowCount(self.rowTabela)
        self.tableWidget.setColumnWidth(0, 176)
        self.tableWidget.setColumnWidth(1, 32)
        self.tableWidget.setColumnWidth(2, 176)
        for i in range(0,self.rowTabela):
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setHorizontalHeaderItem(i, item)
            item.setTextAlignment(QtCore.Qt.AlignCenter)

        for i in range(0, self.columnTabela):
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setVerticalHeaderItem(i, item)
            item.setTextAlignment(QtCore.Qt.AlignCenter)

        for linha in range (0,self.rowTabela):
            for coluna in range (0,self.columnTabela):
                item = QtWidgets.QTableWidgetItem()
                agora = str(partidas[0][linha][coluna])
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                item.setText(agora)
                self.tableWidget.setItem(linha, coluna, item)

    def mostraComboRodadaUi(self):
        '''
        mostra os valores das rodadas no comboBox, de acordo com cada campeonato
        :return:
        '''
        tabelaCarregada = modulosProjeto.carregaTorneio()
        partidas = list(tabelaCarregada.values())
        self.qtdRodadasUI = len(partidas)
        self.rowTabela = len(partidas[0])
        self.columnTabela = len(partidas[0][0])

        self.comboBox_rodada = QtWidgets.QComboBox(self) #QUANDO for colocar no principal aqui placar tem que ser self
        self.comboBox_rodada.setGeometry(QtCore.QRect(20, 30, 120, 24))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.comboBox_rodada.setFont(font)
        self.comboBox_rodada.setObjectName("comboBox_rodada")
        for i in range(0,self.qtdRodadasUI):
            rodadaAtual = 'Rodada ' + str(i+1)
            self.comboBox_rodada.addItem(rodadaAtual)

    def marcaJogoUI(self):
        '''
        Recebe os valores dos gols das partidas para marcar nas rodadas
        :return:
        '''
        self.rodadaIndex = (self.comboBox_rodada.currentIndex())
        if self.lineEdit_GolCasa.text() != '' and self.lineEdit_GolFora.text() != '':
            self.placarTempUI[self.jogoIndex]=([self.lineEdit_GolCasa.text(), self.lineEdit_GolFora.text()])
            item = QtWidgets.QTableWidgetItem()
            golNaTabela = str(self.lineEdit_GolCasa.text())+ 'x' + str(self.lineEdit_GolFora.text())
            item.setText(golNaTabela)
            self.tableWidget.setItem(self.jogoIndex, 1, item)
            item.setTextAlignment(QtCore.Qt.AlignCenter)

        self.marcouTodos = self.verificaPartida()
        self.avancaJogoDir()
        if self.marcouTodos:
            self.pushButton_finalizarRodada.setEnabled(True)

    def mudaRodadaUi(self):
        '''
        troca os valores da tabela de acordo com a rodada
        :return:
        '''
        self.rodadaIndex = self.comboBox_rodada.currentIndex()
        tabelaCarregada = modulosProjeto.carregaTorneio()
        partidas = list(tabelaCarregada.values())
        for linha in range(0, self.rowTabela):
            for coluna in range(0, self.columnTabela):
                item = QtWidgets.QTableWidgetItem()
                agora = str(partidas[self.rodadaIndex][linha][coluna])
                item.setText(agora)
                self.tableWidget.setItem(linha, coluna, item)
                item.setTextAlignment(QtCore.Qt.AlignCenter)

        self.label_Mandante.setText(str(partidas[self.rodadaIndex][0][0])) #atualiza os labels de marcar jogo
        self.label_Visitante.setText(str(partidas[self.rodadaIndex][0][2]))
        self.jogoIndex = 0
        self.label_infoMarcar.setText('Jogo ' + str(self.jogoIndex+1))
        self.pushButton_finalizarRodada.setText('Finalizar Rodada')
        self.tempPlacarVazio()
        self.verificaPartida()
        self.lineEdit_GolCasa.setText('')
        self.lineEdit_GolFora.setText('')

    def iniciajogo(self):
        '''
        inicia com os valores do primeiro jogo e primeira rodada nos labels
        :return:
        '''
        tabelaCarregada = modulosProjeto.carregaTorneio()
        partidas = list(tabelaCarregada.values())
        self.label_Mandante.setText(str(partidas[0][0][0]))
        self.label_Visitante.setText(str(partidas[0][0][2]))

    def avancaJogoDir(self):
        '''
        muda para o próximo jogo, caso haja
        :return:
        '''
        tabelaCarregada = modulosProjeto.carregaTorneio()
        partidas = list(tabelaCarregada.values())
        self.rodadaIndex = self.comboBox_rodada.currentIndex()
        self.rowTabela = len(partidas[0])
        if self.jogoIndex < (self.rowTabela-1):
            self.jogoIndex += 1
        self.label_Mandante.setText(str(partidas[self.rodadaIndex][self.jogoIndex][0]))
        self.label_Visitante.setText(str(partidas[self.rodadaIndex][self.jogoIndex][2]))
        self.label_infoMarcar.setText('Jogo ' + str(self.jogoIndex+1))
        self.lineEdit_GolCasa.setText('')
        self.lineEdit_GolFora.setText('')

    def avancaJogoEsq(self,):
        '''
        muda para o jogo anterior, caso haja
        :return:
        '''
        tabelaCarregada = modulosProjeto.carregaTorneio()
        partidas = list(tabelaCarregada.values())
        self.rodadaIndex = self.comboBox_rodada.currentIndex()
        self.rowTabela = len(partidas[0])
        if  self.jogoIndex > 0:
            self.jogoIndex -= 1
        self.label_Mandante.setText(str(partidas[self.rodadaIndex][self.jogoIndex][0]))
        self.label_Visitante.setText(str(partidas[self.rodadaIndex][self.jogoIndex][2]))
        self.label_infoMarcar.setText('Jogo '+str(self.jogoIndex+1))
        self.lineEdit_GolCasa.setText('')
        self.lineEdit_GolFora.setText('')

    def guardaPartidaUI(self):
        '''
        se a rodada foi marcada de forma completa, guarda todas as informções
        :return:
        '''
        self.valoresTempPlacar = list(self.placarTempUI.values())
        rodada = (self.rodadaIndex + 1)
        modulosProjeto.marcarPlacar(rodada, self.valoresTempPlacar)
        self.pushButton_finalizarRodada.setText('Rodada Marcada')
        self.pushButton_finalizarRodada.setEnabled(False)
        modulosProjeto.log(f'Marcou a rodada "{rodada}"', ui.userUI)

    def verificaPartida(self):
        '''
        verifica se todas partidas da rodada foram marcadas, se sim habilita o botão finalizar rodada
        :return:
        '''
        self.valoresTempPlacar = list(self.placarTempUI.values())
        for i in self.valoresTempPlacar:
            if len(i) != 2:
                self.pushButton_finalizarRodada.setEnabled(False)
                return False
        return True


class Ui_Classifica(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(Ui_Classifica, self).__init__(parent)
        self.setupUi(self)

    def setupUi(self, Classifica):
        '''
        Configurações iniciais da janela
        :param Classifica: chama a si individualmente quando cria um objeto (nesse caso a janela)
        :return:
        '''
        Classifica.setObjectName("Classifica")
        Classifica.resize(642, 495)
        Classifica.setMinimumSize(QtCore.QSize(642, 495))
        Classifica.setMaximumSize(QtCore.QSize(642, 495))
        self.tableWidget = QtWidgets.QTableWidget(Classifica)
        self.tableWidget.setGeometry(QtCore.QRect(0, 80, 641, 268))
        self.tableWidget.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.tableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        iconTela = QtGui.QIcon()
        iconTela.addPixmap(QtGui.QPixmap("icones/icotela.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        Classifica.setWindowIcon(iconTela)
        self.tableWidget.setAutoScroll(True)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.setTabKeyNavigation(False)
        self.tableWidget.setProperty("showDropIndicator", False)
        self.tableWidget.setDragDropOverwriteMode(False)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.label_campeao = QtWidgets.QLabel(Classifica)
        self.label_campeao.setGeometry(QtCore.QRect(231, 450, 180, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.label_campeao.setFont(font)
        self.label_campeao.setAlignment(QtCore.Qt.AlignCenter)
        self.label_campeao.setObjectName("label_campeao")
        self.label_3 = QtWidgets.QLabel(Classifica)
        self.label_3.setGeometry(QtCore.QRect(271, 360, 100, 91))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("icones\\icoprimeiro.png"))
        self.label_3.setObjectName("label_3")
        self.pushButton_imprimir = QtWidgets.QPushButton(Classifica)
        self.pushButton_imprimir.setGeometry(QtCore.QRect(603, 459, 31, 31))
        self.pushButton_imprimir.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icones\\icoimprime.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_imprimir.setIcon(icon)
        self.pushButton_imprimir.setIconSize(QtCore.QSize(24, 24))
        self.pushButton_imprimir.setFlat(True)
        self.pushButton_imprimir.setObjectName("pushButton_imprimir")
        self.label_2 = QtWidgets.QLabel(Classifica)
        self.label_2.setGeometry(QtCore.QRect(160, 0, 300, 74))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("icones\\icofaaix.png"))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_rodada = QtWidgets.QLabel(Classifica)
        self.label_rodada.setGeometry(QtCore.QRect(230, 13, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label_rodada.setFont(font)
        self.label_rodada.setAlignment(QtCore.Qt.AlignCenter)
        self.label_rodada.setObjectName("label_rodada")
        self.criaTabelaUI()
        self.primeiroPos()
        self.pushButton_imprimir.clicked.connect(self.relatorioClassificacao)

        self.retranslateUi(Classifica)
        QtCore.QMetaObject.connectSlotsByName(Classifica)

    def retranslateUi(self, Classifica):
        '''
        Define nomes padrão para os recursos dentro da janela criada
        :param Classifica: Recebe o nome do obj para qual a função realizará a ação de forma individual
        :return:
        '''
        _translate = QtCore.QCoreApplication.translate
        Classifica.setWindowTitle(_translate("Classifica", "Classificação"))
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Classifica", "Time"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Classifica", "Pontos"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Classifica", "SG"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Classifica", "Vitória"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Classifica", "Derrota"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Classifica", "Empate"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Classifica", "Gol Pro"))

    def criaTabelaUI(self):
        '''
        cria uma tabela visual organiada com a classificação, nome do time, pontos, sg, etc
        :return:
        '''
        partidas = modulosProjeto.leClassificacao()
        self.qtdTimesUI = len(partidas)
        self.colunaTabela = len(partidas[0])
        self.tableWidget.setColumnCount(self.colunaTabela)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setRowCount(self.qtdTimesUI)
        self.tableWidget.setColumnWidth(0, 220)
        self.tableWidget.setColumnWidth(1, 68)
        self.tableWidget.setColumnWidth(2, 68)
        self.tableWidget.setColumnWidth(3, 68)
        self.tableWidget.setColumnWidth(4, 68)
        self.tableWidget.setColumnWidth(5, 68)
        self.tableWidget.setColumnWidth(6, 68)

        for i in range(0, self.qtdTimesUI):
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setHorizontalHeaderItem(i, item)

        for i in range(0, self.colunaTabela):
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setVerticalHeaderItem(i, item)

        for time in range(0, self.qtdTimesUI):
            for coluna in range(0, self.colunaTabela):
                item = QtWidgets.QTableWidgetItem()
                infoTimes = str(partidas[time][coluna])
                item.setText(infoTimes)
                self.tableWidget.setItem(time, coluna, item)
                item.setTextAlignment(QtCore.Qt.AlignCenter)

    def primeiroPos(self):
        '''
        verifica e mostra no label qual time está em primeiro lugar na classificação
        :return:
        '''
        partidas = modulosProjeto.leClassificacao()
        nomeCampeao = str(partidas[0][0])
        self.label_campeao.setText(nomeCampeao.upper())
        self.quantasRodadas = os.listdir('peladeiros\\partidas\\')
        if self.quantasRodadas == []:
            self.label_rodada.setText('Rodada 0')
        else:
            self.label_rodada.setText('Rodada '+str(len(self.quantasRodadas)))

    def relatorioClassificacao(self):
        '''
        cria um relatório organizado em csv para classficação
        :return:
        '''
        modulosProjeto.relatorioClassificacao()


class Ui_Torneio(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(Ui_Torneio, self).__init__(parent)
        self.setupUi(self)

    def setupUi(self, Form):
        '''
        Configurações iniciais da janela
        :param Form: chama a si individualmente quando cria um objeto (nesse caso a janela)
        :return:
        '''
        Form.setObjectName("Form")
        Form.resize(640, 445)
        Form.setMinimumSize(QtCore.QSize(640, 445))
        Form.setMaximumSize(QtCore.QSize(640, 450))
        self.labelSenha = QtWidgets.QLabel(Form)
        self.labelSenha.setGeometry(QtCore.QRect(110, 80, 69, 22))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.labelSenha.setFont(font)
        self.labelSenha.setText("")
        iconTela = QtGui.QIcon()
        iconTela.addPixmap(QtGui.QPixmap("icones/icotela.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        Form.setWindowIcon(iconTela)
        self.labelSenha.setScaledContents(False)
        self.labelSenha.setAlignment(QtCore.Qt.AlignCenter)
        self.labelSenha.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.labelSenha.setObjectName("labelSenha")
        self.labelSenha_2 = QtWidgets.QLabel(Form)
        self.labelSenha_2.setGeometry(QtCore.QRect(0, 160, 360, 22))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.labelSenha_2.setFont(font)
        self.labelSenha_2.setText("")
        self.labelSenha_2.setScaledContents(False)
        self.labelSenha_2.setAlignment(QtCore.Qt.AlignCenter)
        self.labelSenha_2.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.labelSenha_2.setObjectName("labelSenha_2")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(40, 290, 251, 111))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.label_QtTimes = QtWidgets.QLabel(self.groupBox)
        self.label_QtTimes.setGeometry(QtCore.QRect(73, 20, 91, 55))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(36)
        font.setBold(False)
        font.setWeight(50)
        self.label_QtTimes.setFont(font)
        self.label_QtTimes.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.label_QtTimes.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_QtTimes.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_QtTimes.setText("")
        self.label_QtTimes.setAlignment(QtCore.Qt.AlignCenter)
        self.label_QtTimes.setObjectName("label_QtTimes")
        self.pushButton_Confirmar = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_Confirmar.setGeometry(QtCore.QRect(80, 80, 75, 24))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.pushButton_Confirmar.setFont(font)
        self.pushButton_Confirmar.setObjectName("pushButton_Confirmar")
        self.pushButton_Confirmar.setEnabled(False)
        self.verticalScrollBar = QtWidgets.QScrollBar(self.groupBox)
        self.verticalScrollBar.setGeometry(QtCore.QRect(230, 20, 16, 80))
        self.verticalScrollBar.setMinimum(0)
        self.verticalScrollBar.setMaximum(20)
        self.verticalScrollBar.setSingleStep(1)
        self.verticalScrollBar.setPageStep(1)
        self.verticalScrollBar.setSliderPosition(20)
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setInvertedAppearance(False)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        self.pushButton_add = QtWidgets.QPushButton(Form)
        self.pushButton_add.setGeometry(QtCore.QRect(300, 30, 47, 43))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.pushButton_add.setFont(font)
        self.pushButton_add.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icones\\icoadd.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_add.setIcon(icon)
        self.pushButton_add.setIconSize(QtCore.QSize(35, 35))
        self.pushButton_add.setAutoDefault(False)
        self.pushButton_add.setDefault(False)
        self.pushButton_add.setFlat(True)
        self.pushButton_add.setObjectName("pushButton_add")
        self.listWidget_2 = QtWidgets.QListWidget(Form)
        self.listWidget_2.setGeometry(QtCore.QRect(70, 130, 180, 104))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.listWidget_2.setFont(font)
        self.listWidget_2.setFrameShape(QtWidgets.QFrame.Panel)
        self.listWidget_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.listWidget_2.setLineWidth(2)
        self.listWidget_2.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.listWidget_2.setAlternatingRowColors(False)
        self.listWidget_2.setItemAlignment(QtCore.Qt.AlignRight)
        self.listWidget_2.setObjectName("listWidget_2")
        item = QtWidgets.QListWidgetItem()
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(110, 70, 65, 22))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.pushButton_GerarTabela = QtWidgets.QPushButton(Form)
        self.pushButton_GerarTabela.setGeometry(QtCore.QRect(380, 370, 160, 35))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.pushButton_GerarTabela.setFont(font)
        self.pushButton_GerarTabela.setObjectName("pushButton_GerarTabela")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(310, 60, 300, 300))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("icones\\icosorteio2.png"))
        self.label_2.setObjectName("label_2")
        self.pushButton_Confirmar_2 = QtWidgets.QPushButton(Form)
        self.pushButton_Confirmar_2.setEnabled(False)
        self.pushButton_GerarTabela.setEnabled(False)
        self.pushButton_add.setEnabled(False)
        self.pushButton_Confirmar_2.setGeometry(QtCore.QRect(120, 240, 75, 24))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.pushButton_Confirmar_2.setFont(font)
        self.pushButton_Confirmar_2.setObjectName("pushButton_Confirmar_2")
        self.label_numEquipe = QtWidgets.QLabel(Form)
        self.label_numEquipe.setGeometry(QtCore.QRect(180, 70, 31, 22))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_numEquipe.setFont(font)
        self.label_numEquipe.setText("")
        self.label_numEquipe.setAlignment(QtCore.Qt.AlignCenter)
        self.label_numEquipe.setObjectName("label_numEquipe")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(40, 36, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setFrame(False)
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.label_Info = QtWidgets.QLabel(Form)
        self.label_Info.setGeometry(QtCore.QRect(40, 420, 251, 22))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.label_Info.setFont(font)
        self.label_Info.setText("")
        self.label_Info.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Info.setObjectName("label_Info")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.times = []
        self.valorFinalScroll = self.verticalScrollBar.valueChanged.connect(self.funcaoScroll)
        self.pushButton_add.clicked.connect(self.addTimes)
        self.pushButton_Confirmar.clicked.connect(self.confirmaQtTimes)
        self.pushButton_GerarTabela.clicked.connect(self.geraTabelaUi)
        self.pushButton_Confirmar_2.clicked.connect(self.apagarLista)

    def apagarLista(self):
        '''
        apaga os nomes dos times temporarios que estão dentro do textbox
        :return:
        '''
        self.listWidget_2.clear()
        self.times = []
        tamanho = int(len(self.times))
        self.label_numEquipe.setText(str(tamanho + 1))
        self.pushButton_GerarTabela.setEnabled(False)
        modulosProjeto.log(f'Apagou a lista temporaria de times', ui.userUI)

    def geraTabelaUi(self):
        '''
        Cria um campeonato colocando os nomes dos times dentro da função geradora de campeonato
        :return:
        '''
        import modulosProjeto
        campeonatoCriado = modulosProjeto.sorteioMaster(int(self.label_QtTimes.text()), self.times)
        modulosProjeto.salvaTorneio(campeonatoCriado)
        self.pushButton_GerarTabela.setText('Tabela Gerada')
        self.pushButton_GerarTabela.setEnabled(False)
        modulosProjeto.log('Criou um campeonato', ui.userUI)


    def addTimes(self):
        '''
        recebe o nome dos times do campeonato de acordo com o numero inserido pelo usuário
        :return:
        '''
        tamanho = int(len(self.times))
        nmTime = self.lineEdit.text()
        if int(self.label_QtTimes.text()) > tamanho:  # Add os nomes na lista times
            self.times.append(nmTime)
            self.lineEdit.setText('')  # apaga o campo texto depois de inserir o nome
            self.label_numEquipe.setText(str(tamanho + 2))  # aumenta o valor no label time

            item = QtWidgets.QListWidgetItem()  # parte de colocar os nomes na lista
            self.listWidget_2.addItem(item)
            item = self.listWidget_2.item(tamanho)
            item.setText(nmTime)

            if int(self.label_QtTimes.text()) - tamanho == 1:
                self.pushButton_GerarTabela.setEnabled(True)
                self.label_numEquipe.setText("Ok!")

            if (tamanho + 1) > 0:
                self.pushButton_Confirmar_2.setEnabled(True)
            else:
                self.pushButton_Confirmar_2.setEnabled(False)
        else:
            self.label_Info.setText("Tamanho limite de times alcançado")

    def confirmaQtTimes(self):
        '''
        confirma os times inseridos para habilitar o botão gerar campeonato
        :return:
        '''
        if self.valorFinalScroll != 0:
            self.verticalScrollBar.setEnabled(False)
            self.pushButton_add.setEnabled(True)
            self.pushButton_Confirmar.setEnabled(False)
            self.label_numEquipe.setText('1')

    def funcaoScroll(self):
        '''
        Dispõe ao usuário um intervalo de 2 a 40 (aumentando de 2 em 2) times participantes
        (o intervalo poderia ser muito maior, mas foi escolha minha deixar esses valores) em forma de scroll
        :return:
        '''
        valorScroll = (20 - (self.verticalScrollBar.value())) * 2
        self.label_QtTimes.setText(str(valorScroll))
        if valorScroll != 0:
            self.pushButton_Confirmar.setEnabled(True)
        else:
            self.pushButton_Confirmar.setEnabled(False)

    def habilitaTorneio(self):
        '''
        Deixa os botões inicialmente como desabilitados
        :return:
        '''
        self.pushButton_Confirmar_2.setEnabled(False)
        self.pushButton_GerarTabela.setEnabled(False)
        self.pushButton_add.setEnabled(False)
        self.pushButton_Confirmar.setEnabled(False)

    def retranslateUi(self, Form):
        '''
        Define nomes padrão para os recursos dentro da janela criada
        :param Form: Recebe o nome do obj para qual a função realizará a ação de forma individual
        :return:
        '''
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Criar Campeonato"))
        self.groupBox.setTitle(_translate("Form", "Quantidade de Times:"))
        self.pushButton_Confirmar.setText(_translate("Form", "Confirmar"))
        __sortingEnabled = self.listWidget_2.isSortingEnabled()
        self.listWidget_2.setSortingEnabled(False)
        self.listWidget_2.setSortingEnabled(__sortingEnabled)
        self.label_3.setText(_translate("Form", "Equipe:"))
        self.pushButton_GerarTabela.setText(_translate("Form", "Gerar Tabela"))
        self.pushButton_Confirmar_2.setText(_translate("Form", "Limpar"))


class Ui_TabelaVisual(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(Ui_TabelaVisual, self).__init__(parent)
        self.setupUi(self)

    def setupUi(self, tabelaVisual):
        '''
        Configurações iniciais da janela
        :param tabelaVisual: chama a si individualmente quando cria um objeto (nesse caso a janela)
        :return:
        '''
        tabelaVisual.setObjectName("tabelaVisual")
        tabelaVisual.resize(430, 495)
        tabelaVisual.setMinimumSize(QtCore.QSize(430, 495))
        tabelaVisual.setMaximumSize(QtCore.QSize(430, 495))
        iconTela = QtGui.QIcon()
        iconTela.addPixmap(QtGui.QPixmap("icones/icotela.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        tabelaVisual.setWindowIcon(iconTela)
        self.tableWidget = QtWidgets.QTableWidget(tabelaVisual)
        self.tableWidget.setGeometry(QtCore.QRect(0, 100, 430, 361))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.tableWidget.setFont(font)
        self.tableWidget.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.tableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget.setAutoScroll(True)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setTabKeyNavigation(False)
        self.tableWidget.setProperty("showDropIndicator", False)
        self.tableWidget.setDragDropOverwriteMode(False)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.pushButton_imprimir = QtWidgets.QPushButton(tabelaVisual)
        self.pushButton_imprimir.setGeometry(QtCore.QRect(200, 460, 31, 31))
        self.pushButton_imprimir.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icones\\icoimprime.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_imprimir.setIcon(icon)
        self.pushButton_imprimir.setIconSize(QtCore.QSize(24, 24))
        self.pushButton_imprimir.setFlat(True)
        self.pushButton_imprimir.setObjectName("pushButton_imprimir")
        self.label_trofeu = QtWidgets.QLabel(tabelaVisual)
        self.label_trofeu.setGeometry(QtCore.QRect(178, 6, 74, 88))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label_trofeu.setFont(font)
        self.label_trofeu.setText("")
        self.label_trofeu.setPixmap(QtGui.QPixmap("icones\\icocup.png"))
        self.label_trofeu.setAlignment(QtCore.Qt.AlignCenter)
        self.label_trofeu.setObjectName("label_trofeu")
        self.pushButton_imprimir.hide() #O BOTÃO DE IMPRIMIR AQUI TA OCULTO, caso o prof queira gerar relatorio, basta habilitar e conectar a função que ta comentada no arquivo modulos do projeto

        self.carregaTabelaUI()

        self.retranslateUi(tabelaVisual)
        QtCore.QMetaObject.connectSlotsByName(tabelaVisual)

    def retranslateUi(self, tabelaVisual):
        '''
        Define nomes padrão para os recursos dentro da janela criada
        :param tabelaVisual: Recebe o nome do obj para qual a função realizará a ação de forma individual
        :return:
        '''
        _translate = QtCore.QCoreApplication.translate
        tabelaVisual.setWindowTitle(_translate("tabelaVisual", "Tabela Campeonato"))
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("tabelaVisual", "Mandante"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("tabelaVisual", "Visitante"))

    def carregaTabelaUI(self):
        '''
        Importa a tabela do campeonato e exibe numa tabela visual do form
        :return:
        '''
        import csv
        listaTabelaUI = []
        arqTabUI = open('.\Peladeiros\\tabelacampeonato.csv', 'r')
        leArqUI = csv.reader(arqTabUI)
        for i in leArqUI:
            listaTabelaUI.append(i)
        arqTabUI.close()

        self.columnTabela = len(listaTabelaUI[0])
        self.rowTabela = len(listaTabelaUI)

        self.tableWidget.setColumnCount(self.columnTabela)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setRowCount(self.rowTabela)
        self.tableWidget.setColumnWidth(0, 176)
        self.tableWidget.setColumnWidth(1, 32)
        self.tableWidget.setColumnWidth(2, 176)

        for linha in range(0, self.rowTabela):
            for coluna in range(0, self.columnTabela):
                item = QtWidgets.QTableWidgetItem()
                agora = str(listaTabelaUI[linha][coluna])
                item.setTextAlignment(QtCore.Qt.AlignCenter)  # ALINHA AS CELULAS AO CENTRO
                item.setText(agora)
                self.tableWidget.setItem(linha, coluna, item)


class Ui_RegistroUI(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(Ui_RegistroUI, self).__init__(parent)
        self.setupUi(self)

    def setupUi(self, tabelaVisual):
        '''
        Configurações iniciais da janela
        :param tabelaVisual: chama a si individualmente quando cria um objeto (nesse caso a janela)
        :return:
        '''
        tabelaVisual.setObjectName("registroUI")
        tabelaVisual.resize(720, 495)
        tabelaVisual.setMinimumSize(QtCore.QSize(720, 495))
        tabelaVisual.setMaximumSize(QtCore.QSize(720, 495))
        iconTela = QtGui.QIcon()
        iconTela.addPixmap(QtGui.QPixmap("icones/icotela.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        tabelaVisual.setWindowIcon(iconTela)
        self.tableWidget = QtWidgets.QTableWidget(tabelaVisual)
        self.tableWidget.setGeometry(QtCore.QRect(0, 100, 720, 361))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.tableWidget.setFont(font)
        self.tableWidget.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.tableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget.setAutoScroll(True)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setTabKeyNavigation(False)
        self.tableWidget.setProperty("showDropIndicator", False)
        self.tableWidget.setDragDropOverwriteMode(False)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.pushButton_imprimir = QtWidgets.QPushButton(tabelaVisual)
        self.pushButton_imprimir.setGeometry(QtCore.QRect(345, 460, 31, 31))
        self.pushButton_imprimir.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icones\\icoimprime.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_imprimir.setIcon(icon)
        self.pushButton_imprimir.setIconSize(QtCore.QSize(24, 24))
        self.pushButton_imprimir.setFlat(True)
        self.pushButton_imprimir.setObjectName("pushButton_imprimir")
        self.label_log = QtWidgets.QLabel(tabelaVisual)
        self.label_log.setGeometry(QtCore.QRect(325, 6, 70, 74))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label_log.setFont(font)
        self.label_log.setText("")
        self.label_log.setPixmap(QtGui.QPixmap("icones\\icolog.png"))
        self.label_log.setAlignment(QtCore.Qt.AlignCenter)
        self.label_log.setObjectName("label_trofeu")
        self.pushButton_imprimir.clicked.connect(self.relatorioLog)

        self.carregaTabelaUI()

        self.retranslateUi(tabelaVisual)
        QtCore.QMetaObject.connectSlotsByName(tabelaVisual)

    def retranslateUi(self, tabelaVisual):
        '''
        Define nomes padrão para os recursos dentro da janela criada
        :param tabelaVisual: Recebe o nome do obj para qual a função realizará a ação de forma individual
        :return:
        '''
        _translate = QtCore.QCoreApplication.translate
        tabelaVisual.setWindowTitle(_translate("tabelaVisual", "Registros"))
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("tabelaVisual", "Usuário"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("tabelaVisual", "Ação"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("tabelaVisual", "Hora/Data"))

    def carregaTabelaUI(self):
        '''
        carrega tabela do campeonato e exibe em uma tabela visual do form
        :return:
        '''
        listaTabelaUI = modulosProjeto.carregaLog()

        self.columnTabela = len(listaTabelaUI[0])
        self.rowTabela = len(listaTabelaUI)

        self.tableWidget.setColumnCount(self.columnTabela)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setRowCount(self.rowTabela)
        self.tableWidget.setColumnWidth(0, 120)
        self.tableWidget.setColumnWidth(1, 378)
        self.tableWidget.setColumnWidth(2, 200)

        for linha in range(0, self.rowTabela):
            for coluna in range(0, self.columnTabela):
                item = QtWidgets.QTableWidgetItem()
                agora = str(listaTabelaUI[linha][coluna])
                item.setTextAlignment(QtCore.Qt.AlignCenter)  # ALINHA AS CELULAS AO CENTRO
                item.setText(agora)
                self.tableWidget.setItem(linha, coluna, item)

    def relatorioLog(self):
        '''
        cria um relatório da tabela do campeonato de forma organizada
        :return:
        '''
        import csv
        logCarregado = modulosProjeto.carregaLog()
        logRelatorio = open('relatorioLog.csv', mode='w', newline='')
        cabecalho = ['Usuário', 'Ação', 'Hora/Data']
        writer = csv.DictWriter(logRelatorio, fieldnames=cabecalho)
        writer.writeheader()
        for i, j, k in logCarregado:
            writer.writerow({'Usuário': i, 'Ação': j, 'Hora/Data': k})


class Ui_RemoveSenha(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(Ui_RemoveSenha, self).__init__(parent)
        self.setupUi(self)

    def setupUi(self, tabelaVisual):
        '''
        Configurações iniciais da janela
        :param tabelaVisual: chama a si individualmente quando cria um objeto (nesse caso a janela)
        :return:
        '''
        tabelaVisual.setObjectName("senhasUI")
        tabelaVisual.resize(258, 445)
        tabelaVisual.setMinimumSize(QtCore.QSize(258, 445))
        tabelaVisual.setMaximumSize(QtCore.QSize(258, 445))
        iconTela = QtGui.QIcon()
        iconTela.addPixmap(QtGui.QPixmap("icones/icotela.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        tabelaVisual.setWindowIcon(iconTela)
        self.tableWidget = QtWidgets.QTableWidget(tabelaVisual)
        self.tableWidget.setGeometry(QtCore.QRect(0, 90, 259, 263))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        self.tableWidget.setFont(font)
        self.tableWidget.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.tableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget.setAutoScroll(True)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setTabKeyNavigation(False)
        self.tableWidget.setProperty("showDropIndicator", False)
        self.tableWidget.setDragDropOverwriteMode(False)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.pushButton_apagaLogin = QtWidgets.QPushButton(tabelaVisual)
        self.pushButton_apagaLogin.setGeometry(QtCore.QRect(71, 412, 116, 28))
        self.pushButton_apagaLogin.setText("Remover Conta")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icones\\icodeleta.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_apagaLogin.setIcon(icon)
        self.pushButton_apagaLogin.setIconSize(QtCore.QSize(16, 16))
        self.pushButton_apagaLogin.setFlat(True)
        self.pushButton_apagaLogin.setObjectName("pushButton_imprimir")
        self.label_cadeado = QtWidgets.QLabel(tabelaVisual)
        self.label_cadeado.setGeometry(QtCore.QRect(93, 2, 74, 88))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label_cadeado.setFont(font)
        self.label_cadeado.setText("")
        self.label_cadeado.setPixmap(QtGui.QPixmap("icones\\icosenhalogin.png"))
        self.label_cadeado.setAlignment(QtCore.Qt.AlignCenter)
        self.label_cadeado.setObjectName("label_trofeu")
        self.lineEdit_remove = QtWidgets.QLineEdit(tabelaVisual)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        self.lineEdit_remove.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_remove.setFont(font)
        self.lineEdit_remove.setGeometry(QtCore.QRect(69, 377, 120, 28))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_remove.sizePolicy().hasHeightForWidth())
        self.lineEdit_remove.setSizePolicy(sizePolicy)
        self.label_infoRemove = QtWidgets.QLabel(tabelaVisual)
        self.label_infoRemove.setGeometry(QtCore.QRect(1, 354, 258, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_infoRemove.setFont(font)
        self.label_infoRemove.setAlignment(QtCore.Qt.AlignCenter)
        self.label_infoRemove.setObjectName("label_infoGol")

        self.carregaSenhaUI()
        self.pushButton_apagaLogin.clicked.connect(self.verificaUI)
        self.habilitaBusca()

        self.retranslateUi(tabelaVisual)
        QtCore.QMetaObject.connectSlotsByName(tabelaVisual)

    def retranslateUi(self, tabelaVisual):
        '''
        Define nomes padrão para os recursos dentro da janela criada
        :param tabelaVisual: Recebe o nome do obj para qual a função realizará a ação de forma individual
        :return:
        '''
        _translate = QtCore.QCoreApplication.translate
        tabelaVisual.setWindowTitle(_translate("tabelaVisual", "Remover Conta"))
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("tabelaVisual", "LOGIN"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("tabelaVisual", "SENHA"))


    def carregaSenhaUI(self):
        '''
        Cria e exibe uma tabela visual com o login e senha dos usuários
        :return:
        '''
        self.listaTabelaUI = modulosProjeto.exibirSenhas()
        self.columnTabela = len(self.listaTabelaUI[0])
        self.rowTabela = len(self.listaTabelaUI)

        self.tableWidget.setColumnCount(self.columnTabela)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setRowCount(self.rowTabela)
        self.tableWidget.setColumnWidth(0, 168)
        self.tableWidget.setColumnWidth(1, 70)


        for linha in range(0, self.rowTabela):
            for coluna in range(0, self.columnTabela):
                item = QtWidgets.QTableWidgetItem()
                agora = str(self.listaTabelaUI[linha][coluna])
                item.setTextAlignment(QtCore.Qt.AlignCenter)  # ALINHA AS CELULAS AO CENTRO
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(11)
                font.setBold(False)
                item.setFont(font)
                item.setText(agora)
                self.tableWidget.setItem(linha, coluna, item)

    def verificaUI(self):
        '''
        Remove uma conta se existir pelo menos duas contas cadastradas no arquivo csv
        :return:
        '''
        pegaLogin = self.lineEdit_remove.text()
        if (len(self.listaTabelaUI) > 1):
            respostaUI = modulosProjeto.removeSenha(self.listaTabelaUI, pegaLogin)
            if respostaUI:
                self.lineEdit_remove.setText('')
                self.carregaSenhaUI()
                modulosProjeto.log(f'Removeu a conta "{pegaLogin}"', ui.userUI)
            else:
                self.label_infoRemove.setText((f'Usuário "{pegaLogin}" não existe!'))
        if (len(self.listaTabelaUI) == 1):
            self.pushButton_apagaLogin.setEnabled(False)

    def habilitaBusca(self):
        '''
        se houver ao menos duas contas cadastradas, o botão de remoção é habilitado
        :return:
        '''
        self.listaTabelaUI = modulosProjeto.exibirSenhas()
        if (len(self.listaTabelaUI) <= 1):
            self.pushButton_apagaLogin.setEnabled(False)


class Ui_JogosMarcados(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(Ui_JogosMarcados, self).__init__(parent)
        self.setupUi(self)

    def setupUi(self, placarUI):
        '''
        Configurações iniciais da janela
        :param placarUI: chama a si individualmente quando cria um objeto (nesse caso a janela)
        :return:
        '''
        self.qtArqPlacar = len(os.listdir('peladeiros\\partidas\\'))
        placarUI.setObjectName("tabelaVisual")
        placarUI.resize(480, 450)
        placarUI.setMinimumSize(QtCore.QSize(480, 450))
        placarUI.setMaximumSize(QtCore.QSize(480, 450))
        iconTela = QtGui.QIcon()
        iconTela.addPixmap(QtGui.QPixmap("icones/icotela.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        placarUI.setWindowIcon(iconTela)
        self.tableWidget = QtWidgets.QTableWidget(placarUI)
        self.tableWidget.setGeometry(QtCore.QRect(0, 100, 479, 260))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.tableWidget.setFont(font)
        self.tableWidget.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.tableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget.setAutoScroll(True)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setTabKeyNavigation(False)
        self.tableWidget.setProperty("showDropIndicator", False)
        self.tableWidget.setDragDropOverwriteMode(False)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setRowCount(0)

        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.pushButton_imprimir = QtWidgets.QPushButton(placarUI)
        self.pushButton_imprimir.setGeometry(QtCore.QRect(225, 410, 31, 31))
        self.pushButton_imprimir.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icones\\icoimprime.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_imprimir.setIcon(icon)
        self.pushButton_imprimir.setIconSize(QtCore.QSize(24, 24))
        self.pushButton_imprimir.setFlat(True)
        self.pushButton_imprimir.setObjectName("pushButton_imprimir")
        self.label_jogoMarcado = QtWidgets.QLabel(placarUI)
        self.label_jogoMarcado.setGeometry(QtCore.QRect(202, 6, 74, 88))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label_jogoMarcado.setFont(font)
        self.label_jogoMarcado.setText("")
        self.label_jogoMarcado.setPixmap(QtGui.QPixmap("icones\\icocheck.png"))
        self.label_jogoMarcado.setAlignment(QtCore.Qt.AlignCenter)
        self.label_jogoMarcado.setObjectName("label_trofeu")
        self.rodadaPlacar = 1
        self.pushButton_dir = QtWidgets.QPushButton(placarUI)
        self.pushButton_dir.setGeometry(QtCore.QRect(308, 370, 44, 40))
        self.pushButton_dir.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icones\\esqico.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_dir.setIcon(icon1)
        self.pushButton_dir.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_dir.setFlat(True)
        self.pushButton_dir.setObjectName("pushButton_dir")
        self.pushButton_esq = QtWidgets.QPushButton(placarUI)
        self.pushButton_esq.setGeometry(QtCore.QRect(138, 370, 44, 40))
        self.pushButton_esq.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icones\\dirico.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_esq.setIcon(icon2)
        self.pushButton_esq.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_esq.setFlat(True)
        self.pushButton_esq.setObjectName("pushButton_esq")
        self.label_infoRodada = QtWidgets.QLabel(placarUI)
        self.label_infoRodada.setGeometry(QtCore.QRect(180, 380, 130, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setPointSize(14)
        self.label_infoRodada.setFont(font)
        self.label_infoRodada.setAlignment(QtCore.Qt.AlignCenter)
        self.label_infoRodada.setObjectName("label_infoGol")
        self.pushButton_dir.clicked.connect(self.aumentaRodada)
        self.pushButton_esq.clicked.connect(self.diminuiRodada)
        self.pushButton_imprimir.clicked.connect(self.relatorioJogosMarcados)

        self.carregaTabelaUI()

        self.retranslateUi(placarUI)
        QtCore.QMetaObject.connectSlotsByName(placarUI)

    def retranslateUi(self, tabelaVisual):
        '''
        Define nomes padrão para os recursos dentro da janela criada
        :param tabelaVisual: Recebe o nome do obj para qual a função realizará a ação de forma individual
        :return:
        '''
        _translate = QtCore.QCoreApplication.translate
        tabelaVisual.setWindowTitle(_translate("tabelaVisual", "Jogos Marcados"))
        self.tableWidget.setSortingEnabled(False)

    def carregaTabelaUI(self):
        '''
        carrega placares marcados do torneio e exibe numa tabela visual a partir do numero de rodada escolhido nos botões
        :return:
        '''
        listaTabelaUI = modulosProjeto.carregaPlacar(self.rodadaPlacar)
        self.columnTabela = len(listaTabelaUI[0])
        self.rowTabela = len(listaTabelaUI)

        self.tableWidget.setColumnCount(self.columnTabela)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setRowCount(self.rowTabela)
        self.tableWidget.setColumnWidth(0, 150)
        self.tableWidget.setColumnWidth(1, 20)
        self.tableWidget.setColumnWidth(2, 20)
        self.tableWidget.setColumnWidth(3, 20)
        self.tableWidget.setColumnWidth(4, 150)

        for linha in range(0, self.rowTabela):
            for coluna in range(0, self.columnTabela):
                item = QtWidgets.QTableWidgetItem()
                agora = str(listaTabelaUI[linha][coluna])
                item.setTextAlignment(QtCore.Qt.AlignCenter)  # ALINHA AS CELULAS AO CENTRO
                item.setText(agora)
                self.tableWidget.setItem(linha, coluna, item)

        for i in range(0, self.columnTabela):
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setHorizontalHeaderItem(i, item)

        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText("Mandante")
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText("Visitante")

        self.label_infoRodada.setText('Rodada ' + str(self.rodadaPlacar))
        modulosProjeto.log(f'Visualizou a rodada {self.rodadaPlacar}', ui.userUI)

    def aumentaRodada(self):
        '''
        avança uma rodada se existir
        :return:
        '''
        partidasMarcadas = os.listdir('peladeiros\\partidas\\')
        if self.rodadaPlacar < len(partidasMarcadas):
            self.rodadaPlacar+=1
            self.carregaTabelaUI()

    def diminuiRodada(self):
        '''
        volta uma rodada se existir
        :return:
        '''
        if self.rodadaPlacar > 1:
            self.rodadaPlacar-=1
            self.carregaTabelaUI()

    def relatorioJogosMarcados(self):
        '''
        Gera o relatorio de todos os jogos marcados
        :return:
        '''
        import csv
        qtArqMarcados = os.listdir('peladeiros//partidas')
        tamQtArqMarcados = len(qtArqMarcados) + 1
        arqJogoRelatorio = open('relatorioJogosMarcados.csv', mode='w', newline='')
        writer = csv.writer(arqJogoRelatorio)
        for i in range(1, tamQtArqMarcados):
            jogoRelatorio = modulosProjeto.carregaPlacar(i)
            writer.writerow([f'Rodada {i}'])
            for j, k, l, m, n in jogoRelatorio:
                writer.writerow([j.upper(), k, l.upper(), m, n.upper()])
        arqJogoRelatorio.close()


class Ui_About(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(Ui_About, self).__init__(parent)
        self.setupUi(self)

    def setupUi(self, About):
        '''
        Configurações iniciais da janela
        :param About: chama a si individualmente quando cria um objeto (nesse caso a janela)
        :return:
        '''
        About.setObjectName("Form")
        About.resize(500, 324)
        iconTela = QtGui.QIcon()
        iconTela.addPixmap(QtGui.QPixmap("icones/icotela.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        About.setWindowIcon(iconTela)
        self.label = QtWidgets.QLabel(About)
        self.label.setGeometry(QtCore.QRect(0, 0, 500, 324))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("icones/about1.png"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(About)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 500, 229))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("icones/about2.png"))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(About)
        self.pushButton.setGeometry(QtCore.QRect(460, 280, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setFlat(True)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(About)
        self.pushButton_2.setGeometry(QtCore.QRect(130, 280, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setFlat(True)
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_2.hide()
        self.pushButton.clicked.connect(self.direita)
        self.pushButton_2.clicked.connect(self.esquerda)

        self.retranslateUi(About)
        QtCore.QMetaObject.connectSlotsByName(About)

    def retranslateUi(self, Form):
        '''
        Define nomes padrão para os recursos dentro da janela criada
        :param Form: Recebe o nome do obj para qual a função realizará a ação de forma individual
        :return:
        '''
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Sobre"))
        self.pushButton.setText(_translate("Form", ">"))
        self.pushButton_2.setText(_translate("Form", "<"))

    def direita(self):
        '''
        mostra proximo label e esconde o atual
        :return:
        '''
        self.label.hide()
        self.label_2.show()

    def esquerda(self):
        '''
        mostra o label anterior e esconde o atual
        :return:
        '''
        self.label_2.hide()
        self.label.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_TelaInicial()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())