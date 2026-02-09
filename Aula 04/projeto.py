#!/usr/bin/env python
# coding: utf-8

# Importando bibliotecas

# In[29]:


import os
import smtplib
import shutil
import pyautogui
import pywhatkit as kit
from time import sleep
from datetime import datetime
from email.message import EmailMessage
import win32com.client as win32


# Organizando arquivos

# In[30]:


arquivo_excel = "contas_processadas.xlsx"

pasta_base = "base"


# Verificando se o arquivo existe

# In[36]:


import os

if not os.path.exists(arquivo_excel):
    raise FileNotFoundError("Arquivo não localizado, verifique se o download foi concluído")

print("Arquivo encontrado")


# Criando a pasta base dentro da pasta Aula 04

# In[37]:


if not os.path.exists(pasta_base):
    os.makedirs(pasta_base)
    print('Pasta criada com sucesso')

else:
    print('Pasta Base já existe')


# Movendo arquivo para dentro da pasta Base

# In[38]:


destino = os.path.join(pasta_base, os.path.basename(arquivo_excel))

if not os.path.exists(destino):
    shutil.move(arquivo_excel, destino)
    print ('Arquivo movido com sucesso!')

else:
    print('Arquivo já existe na pasta base')


# Criando corpo do Email

# In[7]:


hoje = datetime.now().strftime("%d . %m . %Y | Hora %H:%M")  #| (data)
hoje

corpo_email = f"""
Platão, 

A realidade esta sendo moldada pela palavra e o pensamento em linguagem de codigos, me sinto aprendendo a ser um amo da caverna.

Dito isso, segue data de processamento: {hoje}

Abs, 
Fernando Cremm

"""


# Configurando OUTLOOK

# In[22]:


outlook = win32.Dispatch('Outlook.Application')

email = outlook.CreateItem(0)

email.To = 'fernando.cremm@jadlog.com.br'
email.subject = 'Relatório seculo 21 e contas processadas de Janeiro'
email.Body = corpo_email

email.attachments.Add(
    r"C:\Users\fernando.cremm\OneDrive - JADLOG LOGISTICA LTDA\Área de Trabalho\Curso Python1\Aula 04\base\contas_processadas.xlsx"
)

email.Send()
print('Email enviado com sucesso!')


# Alerta WhatsApp

# In[ ]:


telefone = "+5511975220779"

mensagem = "Agora a caverna esta de ZapZap, Relatorio enviado"

kit.sendwhatmsg_instantly(
    telefone,
    mensagem, 
    wait_time=20,
    tab_close=False
)

sleep(2)
pyautogui.press("enter")
print("Mensagem enviada ")



# Criando executável

# In[ ]:


#!pip install pyinstaller 
#get_ipython().system('jupyter nbconvert --to script projeto.ipynb')
#get_ipython().system('pyinstaller --onefile projeto.py')


# In[ ]:




