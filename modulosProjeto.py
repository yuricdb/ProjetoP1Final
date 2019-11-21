import random
import os
import csv
from datetime import datetime

def sorteioMaster(ntimes, clubesSortidos): #UIOK
    '''
    Cria a tabela de pontos corridos (todos contra todos, sem repetir partidas, e com os clubes jogando apenas uma vez por rodada)
    :param ntimes: quantidade de times do campeonato
    :param clubesSortidos: lista de times participantes
    :return: dicionário com as partidas criadas
    '''

    apagaArqAntigos('resultados')
    clubes = sorteioTimes(clubesSortidos)
    numTimes = ntimes
    metade = int((numTimes / 2))
    timescima = []
    timesbaixo = []
    ultimoIndex = int(metade - 1)
    qtdJogos = int(ntimes-1)
    dicRodadas = {}
    for i in range(0, metade):
        timescima.append(i)
    for j in range(metade, numTimes):
        timesbaixo.append(j)

    for k in range(0, qtdJogos):
        redonda = timescima[:] + timesbaixo[:]

        aux = int(timescima[ultimoIndex])
        for i in range(2, metade):
            ind = int(int(i) - 1)
            timescima[i] = redonda[ind]
        timescima[1] = timesbaixo[0]

        tamtemp = metade+1
        tam = int(len(timesbaixo) - 1)
        for i in range(0, tam):
            tam2 = int(i) + tamtemp
            timesbaixo[i] = (int(redonda[tam2]))
        timesbaixo[ultimoIndex] = aux

        rodada = []
        for l in range(0, metade):
            jogo = [clubes[int(timescima[l])], 'x', clubes[int(timesbaixo[l])]]
            rodada.append(jogo)
        numDia = int(k) + 1
        dia = 'Jogo ' + str(numDia)
        dicRodadas[dia] = rodada

    return dicRodadas


def salvaTorneio(dici): #se for preciso gerar relatorio, basta copiar essa funçao outra vez dentro dela propria com o nome arqDici diferente
    '''
    Recebe o torneio criado através de uma lista e salva em csv
    :param dici: dicionário com o tornei criado
    :return: sem retorno
    '''
    import csv
    arqDici = open('.\peladeiros\\tabelacampeonato.csv', 'w', newline='')
    arqGuardaTorneio = csv.writer(arqDici)
    for i in dici.items():
        #a = int(len(i[1]))
        for j in i[1]:
            arqGuardaTorneio.writerow(j)
    arqDici.close()


def carregaTorneio():
    '''
    Carrega o torneio criado através do arquivo csv
    :return: Dicionário com o torneio carregado
    '''
    listaTime = []
    cont = 0
    arqLog2 = open('.\Peladeiros\\tabelacampeonato.csv', 'r')
    escreveLog2 = csv.reader(arqLog2)
    tabelaCarregada = {}
    contRodada = 0
    for i in escreveLog2:
        listaTime.append(i)
        cont += 1

    qtTimes = int(((1 + (4 * (cont * 2)) ** (1 / 2)) + 1) / 2)
    qtJogosRodada = int(cont / (qtTimes - 1))
    for k in range(0, cont, qtJogosRodada):
        contRodada += 1
        nomeRodada = 'Jogo '+ str(int(contRodada))
        h = int(qtJogosRodada + k)
        tabelaCarregada[nomeRodada] = listaTime[k:h]
    return tabelaCarregada


def sorteiaSenha():
    '''
    Cria uma senha de 4 dígitos sendo duas letras (maiusculas ou minúsculas ou ambas) e dois números
    :return: senha criada, exemplo 1yN4
    '''
    letras = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ' #depois pensar em melhorar aqui pra caracter com chr and ord
    algarismos = '0123456789'
    senhaTemp = []
    senhaFinal = ''
    for i in range (0, 2):
        char1Temp = random.choice(letras)
        senhaTemp.append(char1Temp)
        char2Temp = random.choice(algarismos)
        senhaTemp.append(char2Temp)
    for i in range(0, 4):
        charTemp = random.choice(senhaTemp)
        senhaTemp.remove(charTemp)
        senhaFinal += charTemp
    return senhaFinal


def cadastroUsuario(nomeUsuario):
    '''
    Cadastra um novo usuário e guarda como csv no sistema
    :param nomeUsuario: login desejado como string
    :return: senha criada para o login desejado
    '''
    import csv
    senhaZero = primeiraSenha() #verifica se há algum arquivo de senha na pasta
    endSenhas = 'peladeiros\\senha\\senhas.csv'
    if senhaZero:
        loginExiste = False
    else:
        loginExiste = True
    while loginExiste:
        login = nomeUsuario
        loginExiste = False
        arqVerfica = open(endSenhas, 'r')
        leSenha = csv.reader(arqVerfica)
        for linha in leSenha:
            if linha[0] == login.upper():
                loginExiste = True
        if loginExiste:
            return False
    login = nomeUsuario
    senhaLogin = sorteiaSenha()
    guardar = (login.upper(), senhaLogin) #mudei de lista pra tuplas
    arqSalvar = open(endSenhas, 'a', newline='')
    salvando = csv.writer(arqSalvar)
    salvando.writerow(guardar)
    arqSalvar.close()
    return senhaLogin


def inicio():
    '''
    verifica e cria arquivos e ou pastas necessarias para o programa executar
    :return: nome da pasta principal do programa
    '''
    verPasta = 0
    cam = os.listdir()
    for ex in cam:
        if 'Peladeiros' == ex:
            verPasta += 1
    if verPasta == 0:
        os.mkdir('.\Peladeiros')
        os.mkdir('.\Peladeiros\partidas')
        os.mkdir('.\Peladeiros\senha')

    return 'Peladeiros\\'


def apagaArqAntigos(escolheApagar):
    '''
    Apaga arquivos dos resultados marcados
    :param escolheApagar: nome do arquivo
    :return: sem retorno
    '''

    if escolheApagar == 'resultados':
        partidasAntigas = os.listdir('peladeiros\\partidas\\')
        for i in partidasAntigas:
            os.remove('peladeiros\\partidas\\' + i)


def placar(listaPartida):
    '''
    Recebe e cria um dicionário com os resultados da rodada
    :param listaPartida: lista com os resultados separados por jogos
    :return: dicionário com os jogos organizados por nome
    '''
    resultado = {}
    tam = len(listaPartida)
    for i in range (0, tam):
        tempResultado = input(f'digite o placar da partida {listaPartida[i]}\n')
        casa = int(tempResultado[0])
        fora = int(tempResultado[2])
        chave = 'jogo' + str(int(i+1))
        resultado[chave] = [casa, fora]
    print(resultado)


def sorteioTimes(listTimes):
    '''
    Embaralha os times
    :param listTimes: lista de times
    :return: lista embaralhada
    '''
    copiaListTimes = listTimes[:]
    listaSorteada = []
    tamLista = int(len(copiaListTimes))
    while tamLista > 0:
        timeEscolhido = random.choice(copiaListTimes)
        listaSorteada.append(timeEscolhido)
        copiaListTimes.remove(timeEscolhido)
        tamLista = int(len(copiaListTimes))
    return listaSorteada


def acesso(login, senha):
    '''
    Tenta acessar o o login e senha
    :param login: login do usuário que deseja entrar
    :param senha: senha correspondente ao login inserido
    :return: um boolean, se corresponde ou não a senha com o login
    '''
    import csv
    acessoNegado = True
    while acessoNegado:
        localSenhas = 'peladeiros\\senha\\senhas.csv'
        entrada = [login.upper(), senha]
        arqLogin = open(localSenhas, 'r')
        leSenha = csv.reader(arqLogin)
        for linha in leSenha:
            if entrada == linha:
                return True
        if acessoNegado:
            return False


def log(acao, usuario='Visitante'):
    '''
    Grava em csv as ações do usuário visitante e usuário logado
    :param acao: descrição do que o usuário está fazendo
    :param usuario: nome do usuário caso esteja logado, ou visitante como padrão
    :return: sem retorno
    '''
    horaData = datetime.now()
    horaData = horaData.strftime('%H:%M:%S %d/%m/%Y')
    arqLog = open('log.csv', 'a', newline='')
    escreveLog = csv.writer(arqLog)
    escreveLog.writerow([usuario, acao, horaData])
    arqLog.close()


def carregaLog():
    '''
    Carrega as informações em csv dos registros gravados (log)
    :return: lista com as informações
    '''
    import csv
    listaLog = []
    caminho = 'log.csv'
    arqLog = open(caminho, mode='r', newline='')
    carregaLog = csv.reader(arqLog)
    for i in carregaLog:
        listaLog.append(i)
    arqLog.close()

    return listaLog


def marcarPlacar(rodada, listaResultados):
    '''
    Grava arquivos individualmente por rodada marcada, e atualiza a classificação
    :param rodada: numero da rodada
    :param listaResultados: lista com resultados dos jogos marcados
    :return: sem retorno
    '''
    import csv
    diciTorneio = carregaTorneio()
    index = 'Jogo ' + str(rodada)
    indexJunto = ''.join(index.lower().split())
    caminho = 'peladeiros\\partidas\\infopontos'+indexJunto+'.csv'
    arqPontos = open(caminho, mode='w', newline='')
    guardaPontos = csv.writer(arqPontos)
    cont = 0
    for i in diciTorneio[index]:
        placar1 = int(listaResultados[cont][0])
        placar2 = int(listaResultados[cont][1])
        guardaPontos.writerow([i[0], placar1, i[1], placar2, i[2]])
        cont += 1
    arqPontos.close()
    criaClassificacao()


def carregaPlacar(rodadaNumero):
    '''
    Carrega placar referente a rodada desejada
    :param rodadaNumero: numero da rodada
    :return: lista com os placares dos jogos
    '''

    import csv
    listaPlacar = []
    index = 'infopontosjogo' + str(rodadaNumero)
    caminho = 'peladeiros\\partidas\\' + index + '.csv'
    arqPlacar = open(caminho, mode='r', newline='')
    carregaResultado = csv.reader(arqPlacar)
    for i in carregaResultado:
        listaPlacar.append(i)
    arqPlacar.close()

    return listaPlacar


def exibirSenhas():
    '''
    Carrega as senhas e logins do arquivos csv
    :return: lista com login e senha
    '''
    import csv
    bancoSenhas = []
    caminho = 'peladeiros\\senha\\senhas.csv'
    arqSenha = open(caminho, mode='r', newline='')
    carregaSenhas = csv.reader(arqSenha)
    for i in carregaSenhas:
        bancoSenhas.append(i)
    arqSenha.close()

    return bancoSenhas


def removeSenha(listaSenhas, opcaoRemover):
    '''
    Remove login e senha do usuário, caso exista
    :param listaSenhas: lista com login e senhas
    :param opcaoRemover: opção do login do qual deseja-se remover
    :return: um boolean como confirmação de remoção
    '''
    import csv
    caminho = 'peladeiros\\senha\\senhas.csv'
    copiaSenhas = listaSenhas[:]
    cont = 0
    flag = True
    tamListaSenhas = int(len(listaSenhas))
    while (cont < tamListaSenhas) and flag:
        if listaSenhas[cont][0] == opcaoRemover.upper():
            del (copiaSenhas[cont])
            flag = False
        cont += 1
    tamCopiaSenhas = int(len(copiaSenhas))

    if tamCopiaSenhas != tamListaSenhas:
        arqSenha = open(caminho, 'w', newline='')
        atualizaSenhas = csv.writer(arqSenha)
        for i in copiaSenhas:
            atualizaSenhas.writerow(i)
        arqSenha.close()
        return True
    else:
        return False


def calculaPontos():
    '''
    Calcula todas as informações de cada times (pontos, saldo de gol, vitórias, empates, etc)
    :return: dicionário com todas as informções referentes a cada time
    '''
    dir = os.listdir('peladeiros\\partidas\\')
    tamDir = int(len(dir))+1
    resultados = []

    for i in range(1, tamDir): #carrega todos os jogos marcados (com gols) e insere dentro de uma lista
        placarAtual = carregaPlacar(i)
        resultados.append(placarAtual)
    nomes = []
    diciTeste = {}
    for i in resultados[0]: #guarda todos os nomes dos times para usar num dicionario
        if not(i[0] in nomes):
            nomes.append(i[0])
            diciTeste[i[0]] = [0, 0, 0, 0, 0, 0] #[pontos, saldo de gols, vitoria, derrota, empate, gols pro]
        if not(i[4] in nomes):
            nomes.append(i[4])
            diciTeste[i[4]] = [0, 0, 0, 0, 0, 0]

    for i in resultados:
        for j in i:
            if j[0] in nomes:
                if j[1] > j[3]: #verifica se o primeiro valor do gol é maior que o segundo (ou seja o time da casa ganhou)
                    diciTeste[j[0]][2] += 1
                    diciTeste[j[4]][3] += 1
                    diciTeste[j[0]][0] += 3 #time casa recebe 3 pontos pela vitoria
                elif j[1] < j[3]:  #verifica se o primeiro valor do gol é menor que o segundo (ou seja o time VISITANTE ganhou)
                    diciTeste[j[4]][2] += 1
                    diciTeste[j[4]][0] += 3  # time visitante recebe 3 pontos pela vitoria
                    diciTeste[j[0]][3] += 1
                else: #não sendo os casos anteriores, então só pode ter sido placar igual (ou seja, empate)
                    diciTeste[j[0]][4] += 1
                    diciTeste[j[4]][4] += 1
                    diciTeste[j[0]][0] += 1
                    diciTeste[j[4]][0] += 1
                diciTeste[j[0]][1] += (int(j[1]) - int(j[3])) #aqui o clube da casa recebe o valor do primeiro valor gol marcado pelo usuário
                diciTeste[j[4]][1] += (int(j[3]) - int(j[1])) #aqui o visitante recebe o valor do segundo valor de gol marcado pelo usuário
                diciTeste[j[0]][5] += (int(j[1])) #guarda a quantidade de gols do time da casa
                diciTeste[j[4]][5] += (int(j[3])) #guarda os gols do time visitante

    return diciTeste

def criaClassificacao():
    '''
    Cria e grava em csv uma classificação organizada necessariamente na seguinte ordem
    Pontos marcados, saldo de gols, gols marcados, vitoria, derrota, ordem alfabetica.
    :return: sem retorno
    '''
    import csv
    diciPontos = calculaPontos()
    tempValores = diciPontos.values()
    listaValores = []
    for i in tempValores:
        listaValores.append(i[:])
    listaNomesClubes = diciPontos.keys()
    cont = 0
    tempPeso = []

    for i in listaNomesClubes: #os pesos aqui são o seguinte, pontos, saldo de gol, gol pro, vitoria, derrota, e depois na ordenação abaixo sem peso vem ordem alfabetica
        posicao = (listaValores[cont][0])*(10**6)+(listaValores[cont][1])*(10**5)+(listaValores[cont][2])*(10**3)+(listaValores[cont][3])*(10**2)+(listaValores[cont][5])*(10**4)
        tempPeso.append([i, posicao])
        cont += 1

    a = int(len(tempPeso))
    for i in range(0, a): # agora ordena pelos valores numericos (com os pesos de pontos, saldo de gols etc)
        if i != 0:
            for j in range((i - 1), -1, -1):
                k = j + 1 #(seguinte do j) usado pra comparar o j com o próximo depois do j, ou seja j+1
                if tempPeso[j][1] > tempPeso[k][1]:
                    numtemp = tempPeso[:][j]
                    numtemp2 = tempPeso[:][k]
                    del tempPeso[j]
                    tempPeso.insert(j, numtemp2)
                    del tempPeso[k]
                    tempPeso.insert(k, numtemp)
                elif tempPeso[j][1] == tempPeso[k][1]: #compara se tem pontuação iguais (mesmo com todos os pesos calculados) se sim, o desempate vai por ordem alfabética
                    if tempPeso[j][0] < tempPeso[k][0]: #aqui troquei o maior pelo menor pois se tratava de nomes, assim o maior ia ficar depois, mas como eu gravo csv de trás pra frente, ele pega primeiro o menor
                        numtemp = tempPeso[:][j]
                        numtemp2 = tempPeso[:][k]
                        del tempPeso[j]
                        tempPeso.insert(j, numtemp2)
                        del tempPeso[k]
                        tempPeso.insert(k, numtemp)

    localDoArquivo = 'peladeiros\\Classificacao.csv'
    tamTempPeso = int(len(tempPeso))-1
    arqClassifica = open(localDoArquivo, 'w', newline='')
    escreveClassifica = csv.writer(arqClassifica)
    for i in range (tamTempPeso, -1, -1):
        escreveClassifica.writerow([(tempPeso[i][0]), *diciPontos[tempPeso[i][0]]]) #o asterisco em diciPontos é pra "abrir" a lista na hora de guardar no csv (feito o *args como parametro em funções)

    arqClassifica.close()


def leClassificacao():
    '''
    Carrega o arquivo csv referente a classificação
    :return: lista com a classificação dos clubes
    '''
    import csv
    lugarDoArquivo = 'peladeiros\\classificacao.csv'
    arqClassifica = open(lugarDoArquivo, 'r')
    leLinhas = csv.reader(arqClassifica)
    classifica = []
    for i in leLinhas:
        classifica.append(i)
    arqClassifica.close()
    return classifica


def primeiraSenha():
    '''
    Verifica se existe algum arquivo de senha criado
    :return: sem retorno
    '''
    existeSenha = os.listdir('peladeiros\\senha\\')
    if existeSenha == []:
        return True
    else:
        return False

def qtdDeJogosMarcados():
    '''
    verifica a quantidade de jogos marcados
    :return: quantidade de jogos marcados
    '''
    partidasMarcadas = os.listdir('peladeiros\\partidas\\')
    return partidasMarcadas

def verificaArquivo(nomeArquivo):
    '''
    Varre a pasta a procura do nome do arquivo solicitado
    :param nomeArquivo: arquivo que se quer descobrir se existe
    :return: retorna um boolean para existe ou nao existe arquivo
    '''
    existeArq = os.listdir('peladeiros\\')
    for i in existeArq:
        if i.upper() == nomeArquivo.upper():
            return True
    return False

def relatorioClassificacao():
    '''
    cria um csv organizado com a classificação da rodada
    :return:
    '''
    arqRelatorio = open('relatorioClassifica.csv', mode='w', newline='')
    cabecalho = ['Time', 'Pontos', 'Saldo de Gol', 'Vitoria', 'Derrota', 'Empate', 'Gols Marcados']
    writer = csv.DictWriter(arqRelatorio, fieldnames=cabecalho)
    writer.writeheader()
    classificacao = leClassificacao()
    for i, j, k, l, m, n, o in classificacao:
        writer.writerow(
            {'Time': i, 'Pontos': j, 'Saldo de Gol': k, 'Vitoria': l, 'Derrota': m, 'Empate': n, 'Gols Marcados': o})