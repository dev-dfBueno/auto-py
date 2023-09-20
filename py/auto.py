# Importar dependências#
import pyautogui as bot
import time
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import pickle
# Importar dependências#
# ============================================================================================

# Variáveis globais para armazenar o diretório de imagens, e-mail e senha
diretorio_imagens = ""
email = ""
senha = ""
# Variáveis globais para armazenar o diretório de imagens, e-mail e senha
# ============================================================================================

# Função para configurar o diretório de imagens
def configurar_diretorio():
    global diretorio_imagens
    diretorio_imagens = filedialog.askdirectory()
    print("Diretório de imagens configurado:", diretorio_imagens)
# Função para configurar o diretório de imagens
# ============================================================================================

# Função para configurar e-mail e senha
def configurar_credenciais():
    global email, senha
    janela_credenciais = tk.Tk()
    janela_credenciais.title("Configurar Credenciais")
# Função para configurar e-mail e senha
# ============================================================================================

# Defina um tamanho maior para a janela de configuração de e-mail
    largura_janela_credenciais = 400
    altura_janela_credenciais = 200
# Defina um tamanho maior para a janela de configuração de e-mail
# ============================================================================================

# Obtenha as dimensões da tela
    largura_tela = janela_credenciais.winfo_screenwidth()
    altura_tela = janela_credenciais.winfo_screenheight()
# Defina um tamanho maior para a janela de configuração de e-mail
# ============================================================================================

# Calcule a posição x e y para centralizar a janela
    pos_x = (largura_tela - largura_janela_credenciais) // 2
    pos_y = (altura_tela - altura_janela_credenciais) // 2
# Defina um tamanho maior para a janela de configuração de e-mail
# ============================================================================================

# Configure a geometria da janela de configuração de e-mail
    janela_credenciais.geometry(f"{largura_janela_credenciais}x{altura_janela_credenciais}+{pos_x}+{pos_y}")
# Configure a geometria da janela de configuração de e-mail
# ============================================================================================

# Configuração das credenciais
    label_email = tk.Label(janela_credenciais, text="E-mail:")
    label_email.pack()
    entry_email = tk.Entry(janela_credenciais)
    entry_email.pack()

    label_senha = tk.Label(janela_credenciais, text="Senha:")
    label_senha.pack()
    entry_senha = tk.Entry(janela_credenciais, show='*')
    entry_senha.pack()
# Configuração das credenciais
# ============================================================================================


# Carregar as credenciais do arquivo, se existirem
    try:
        with open("credenciais.pkl", "rb") as arquivo_credenciais:
            credenciais_salvas = pickle.load(arquivo_credenciais)
            email, senha = credenciais_salvas
            entry_email.insert(0, email)
            entry_senha.insert(0, senha)
    except FileNotFoundError:
        pass
# Carregar as credenciais do arquivo, se existirem
# ============================================================================================

# Salvar credenciais
    def salvar_credenciais():
        global email, senha
        email = entry_email.get()
        senha = entry_senha.get()
        print("Credenciais configuradas com sucesso!")

        # Salvar as credenciais em um arquivo
        with open("credenciais.pkl", "wb") as arquivo_credenciais:
            pickle.dump([email, senha], arquivo_credenciais)

        janela_credenciais.destroy()

    botao_salvar = ttk.Button(janela_credenciais, text="Salvar", command=salvar_credenciais)
    botao_salvar.pack()

    janela_credenciais.mainloop()
# Salvar credenciais    
# ============================================================================================
    
# Defina um ícone para a janela (substitua 'icone.ico' pelo caminho do seu ícone)
    janela_credenciais.iconbitmap('bug.ico')
# Defina um ícone para a janela (substitua 'icone.ico' pelo caminho do seu ícone)
# ============================================================================================

# Função para iniciar o projeto
def iniciar_projeto():
    janela_aceitacao.destroy()
# Função para iniciar o projeto    
# ============================================================================================

# Abertura do chrome
    time.sleep(2)
    bot.keyDown('shift')
    bot.click(966, 1054)
    bot.keyUp('shift')
# Abertura do chrome
# ============================================================================================

# Chrome visitante
    time.sleep(2)
    bot.moveTo(579, 850)
    time.sleep(2)
    bot.click()
# Chrome visitante
# ============================================================================================

# Link Facebook Business
    bot.write('https://business.facebook.com', interval=0.10)
    time.sleep(1)
    bot.press('Enter')
# Link Facebook Business
# ============================================================================================

# "Entrar com o Facebook"
    time.sleep(4)
    bot.moveTo(485, 585)
    bot.click()
# "Entrar com o Facebook"
# ============================================================================================

# Realiza o login com o e-mail e senha configurados
    time.sleep(2)
    bot.write(email, interval=0.10)
    bot.press('Tab')
    bot.write(senha, interval=0.10)
    bot.press('Enter')
# Realiza o login com o e-mail e senha configurados
# ============================================================================================

# Clica em "Criar Story"
    time.sleep(10)
    bot.moveTo(1227, 229)
    time.sleep(2)
    bot.click()
# Clica em "Criar Story"
# ============================================================================================

# Clica em "Adicionar mídia"
    time.sleep(2)
    bot.moveTo(524, 567)
    time.sleep(1)
    bot.click()
# Clica em "Adicionar mídia"
# ============================================================================================

# Clica na barra de pesquisa do Explorer
    time.sleep(2)
    bot.moveTo(476, 49)
    time.sleep(1)
    bot.click()
# Clica na barra de pesquisa do Explorer
# ============================================================================================

# Navega até o diretório configurado
    time.sleep(2)
    bot.write(diretorio_imagens)
    time.sleep(1)
    bot.press('Enter')
# Navega até o diretório configurado
# ============================================================================================

# Seleciona todas as imagens do diretório configurado
    time.sleep(2)
    bot.moveTo(931, 312)
    time.sleep(1)
    bot.click()
    bot.keyDown('ctrl')
    bot.keyDown('a')
    bot.keyUp('ctrl')
    bot.keyUp('a')
# Seleciona todas as imagens do diretório configurado
# ============================================================================================

# Clica em "Abrir" no Explorer após selecionar as imagens
    time.sleep(2)
    bot.moveTo(792, 505)
    time.sleep(1)
    bot.click()
# Clica em "Abrir" no Explorer após selecionar as imagens   
# ============================================================================================

# Clica em "Compartilhar story"
    time.sleep(10)
    bot.moveTo(1412, 869)
    time.sleep(10)
    bot.click()
# Clica em "Compartilhar story"
# ============================================================================================

# Criar a janela de aceitação
janela_aceitacao = tk.Tk()
janela_aceitacao.title("Iniciar Postagens")
# Criar a janela de aceitação
# ============================================================================================

# Defina um estilo para os botões
estilo = ttk.Style()
estilo.configure('Estilo.TButton', font=('Helvetica', 12))
# Defina um estilo para os botões
# ============================================================================================

# Defina o tamanho da janela
largura_janela = 750
altura_janela = 150
# Defina o tamanho da janela
# ============================================================================================

# Obtenha as dimensões da tela
largura_tela = janela_aceitacao.winfo_screenwidth()
altura_tela = janela_aceitacao.winfo_screenheight()
# Obtenha as dimensões da tela
# ============================================================================================

# Calcule a posição inicial para que a janela fique no centro
pos_x = (largura_tela - largura_janela) // 2
pos_y = (altura_tela - altura_janela) // 2
# Calcule a posição inicial para que a janela fique no centro
# ============================================================================================

# Configure a geometria da janela
janela_aceitacao.geometry(f"{largura_janela}x{altura_janela}+{pos_x}+{pos_y}")
# Configure a geometria da janela
# ============================================================================================

# Impedir que o usuário redimensione a janela
janela_aceitacao.resizable(False, False)
# Impedir que o usuário redimensione a janela
# ============================================================================================


# Etiqueta de aviso
label_aviso = tk.Label(janela_aceitacao, text="Você deseja iniciar as postagens?", font=('Helvetica', 14))
label_aviso.pack(pady=10)
# Etiqueta de aviso
# ============================================================================================

# Frame para os botões (para colocá-los lado a lado)
frame_botoes = tk.Frame(janela_aceitacao)
frame_botoes.pack()
# Frame para os botões (para colocá-los lado a lado)
# ============================================================================================

# Botão de aceitação
botao_aceitar = ttk.Button(frame_botoes, text="Sim", style='Estilo.TButton', command=iniciar_projeto)
botao_aceitar.pack(side=tk.LEFT, padx=20, pady=10)
# Botão de aceitação
# ============================================================================================

# Botão de configuração de diretório
botao_configurar = ttk.Button(frame_botoes, text="Configurar Diretório", style='Estilo.TButton', command=configurar_diretorio)
botao_configurar.pack(side=tk.LEFT, padx=20, pady=10)
# Botão de configuração de diretório
# ============================================================================================

# Botão de configuração de e-mail e senha
botao_configurar_credenciais = ttk.Button(frame_botoes, text="Configurar Credenciais", style='Estilo.TButton', command=configurar_credenciais)
botao_configurar_credenciais.pack(side=tk.LEFT, padx=20, pady=10)
# Botão de configuração de e-mail e senha
# ============================================================================================

# Botão de recusa
botao_recusar = ttk.Button(frame_botoes, text="Não", style='Estilo.TButton', command=janela_aceitacao.destroy)
botao_recusar.pack(side=tk.LEFT, pady=10)
# Botão de recusa
# ============================================================================================

# Defina um ícone para a janela (substitua 'icone.ico' pelo caminho do seu ícone)
janela_aceitacao.iconbitmap('bug.ico')
# Defina um ícone para a janela (substitua 'icone.ico' pelo caminho do seu ícone)
# ============================================================================================


# Iniciar a janela de aceitação
janela_aceitacao.mainloop()
# Iniciar a janela de aceitação
# ============================================================================================