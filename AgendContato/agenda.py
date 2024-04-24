import os
import csv
import datetime

lista_contatos=[]
aniversariantes = []
dataHoje = datetime.date.today()

def leitura_arquivo():
    
    with open("agenda.csv") as arquivo_csv:
        saida = csv.reader(arquivo_csv)
        for contato in saida:
            lista_contatos.append({"nome":contato[0],
                                    "tel":contato[1],
                                   "data":contato[2],
                                   "dataReg":contato[3]})
            contato_data=datetime.datetime.strptime(contato[2],"%Y-%m-%d")
            if contato_data.month == dataHoje.month and contato_data.day == dataHoje.day:
              aniversariantes.append(contato)

def mostrar_aniversariantes(aniver):
    for nome in aniver:
        idade = dataHoje.year - datetime.datetime.strptime(nome[2],"%Y-%m-%d").year
        print(f"{nome[0]} faz {idade} anos hoje!")

caminho = os.getcwd()
if os.path.isdir("Agenda"):
    os.chdir(caminho+"/Agenda")
    if (os.path.isfile("agenda.csv")):
        leitura_arquivo()
        mostrar_aniversariantes(aniversariantes)
else:
    os.mkdir("Agenda")
    os.chdir(caminho+"/Agenda")


def menu():
    ope = int(input("""
                        Menu de opções:
                        1 - Salvar Contato;
                        2 - Alterar Contato;
                        3 - Buscar Contato;
                        4 - Apagar Contato;
                        5 - Listar Contatos;
                        0 - Sair da Agenda.
    """))
    return ope

def salvaContato(**kwargs):
    lista_contatos.append(kwargs)
    print(f"Contato de {kwargs["nome"]} foi salvo com sucesso!")

def alteraContato(chave, **novo):
    for contato in lista_contatos:
        if contato["nome"]==chave:
            for key in contato.keys():
                if novo[key] is not None:
                    if key != "dataReg":
                        contato[key] = novo[key]
                    
    print(f"O contato {chave} foi alterado com os valores ({novo["nome"]},{novo["tel"]},{novo["data"]})")

def buscaContato(chave):
    lista_busca=[]
    for contato in lista_contatos:
        if contato["nome"]==chave:
            lista_busca.append(contato)
    return lista_busca

def apagaContato(chave):
    for contato in lista_contatos:
        if contato["nome"]==chave:
            lista_contatos.remove(contato)

    print(f"Os contatos {chave} foram apagados!")

def listaContatos():
    print(f"A quantidade de contato é {len(lista_contatos)}")
    for contato in lista_contatos:
        print(contato)

def salva_arquivo(agenda):
    contatos=[]
    for contato in agenda:
        contatos.append(contato.values())
    
    with open("agenda.csv", "w", newline="") as arquivo_csv:
        saida = csv.writer(arquivo_csv)
        saida.writerows(contatos)

while 1:

    valor=menu()

    if valor == 1:
        nome=input("Nome: ")
        tel = input("Telefone: ")
        print("Entre com sua data de nascimento: ")
        ano = int(input("Ano: "))
        mes = int(input("Mês: "))
        dia = int(input("Dia: "))
        data = datetime.date(year=ano, month = mes, day = dia)
        dataReg = datetime.datetime.now()
        salvaContato(nome=nome, tel=tel, data=data,dataReg = dataReg)
    elif valor == 2:
        chave = input("Qual contato você quer alterar: ")
        nome = input("Alterar nome: ")
        tel = input("Alterar telefone: ")
        data = input("Alterar aniversário: ")
        alteraContato(chave=chave, nome=nome, tel=tel, data=data)
    elif valor == 3:
        chave = input("Qual nome para buscar: ")
        for contato in buscaContato(chave):
            print(contato)
    elif valor==4:
        chave = input("Qual nome para apagar: ")
        apagaContato(chave)
    elif valor==5:
        listaContatos()
    elif valor==0:
        salva_arquivo(lista_contatos)
        break
