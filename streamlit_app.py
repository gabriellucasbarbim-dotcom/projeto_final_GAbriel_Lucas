import os
import json
import streamlit as st
from datetime import datetime
from google.cloud import firestore
from google.oauth2 import service_account



# ==========================================
# CONEXÃO COM O FIREBASE
# ==========================================

@st.cache_resource
def conectar_firebase():
    dados = json.loads(os.environ["FIREBASE_CREDENTIALS"])
    credenciais = service_account.Credentials.from_service_account_info(dados)
    return firestore.Client(
        credentials=credenciais,
        project=dados["project_id"]
    )


# ==========================================
# FORMULÁRIO DE CONTATO
# ==========================================

st.header("📬 Contato")

with st.form("form_contato", clear_on_submit=True):
    nome = st.text_input("Nome")
    email = st.text_input("E-mail")
    mensagem = st.text_area("Mensagem")
    enviar = st.form_submit_button("Enviar mensagem")

    if enviar:
        if nome and email and mensagem:
            db = conectar_firebase()

            

import streamlit as st

from datetime import datetime


# ==========================================

# CONFIGURAÇÃO DO SITE

# ==========================================


# ALTERE o título da página

st.set_page_config(

    page_title="Meu Projeto Final",

    page_icon="💻",

    layout="wide"

)


# ==========================================

# INFORMAÇÕES DO PROJETO

# ==========================================


# ALTERE o nome e a descrição do seu site

NOME_SITE = "Meu Projeto Final"

DESCRICAO = "Este aqui é o meu projeto final, que vai falar sobre mim."


# ALTERE os textos e imagens das publicações

POSTS
dados ={
        "titulo": "Minhas coisas favorita",

        "autor": "Gabriel Lucas",

        "texto": "Eu gosto muito de jogar futebol e de jogar videogame"

    },
minhas_coisas = [
    {

        "titulo": "O que eu gosto de comer",

        "autor": "Gabriel Lucas",

        "texto": "Eu gosto muito de comer churrasco e um arroz pra acompanhar,de sobremesa eu gosto de sorvete ou um pave.",

        "imagem": "https://stock.adobe.com/br/search?k=%22churrasco+brasileiro%22"

    }

]


# ==========================================

# CABEÇALHO

# ==========================================


st.title(Projeto Final de Gabriel Lucas)

st.write(O que o Gabriel Gosta)

st.divider()


# ==========================================

# MENU DE NAVEGAÇÃO

# ==========================================


with st.sidebar:

    st.header("Menu")


    pagina = st.radio(

        "Escolha uma página:",

        ["Início", "Sobre", "Contato"]

    )


    st.divider()

    st.write("Projeto Final 2026")

    st.write("GRACE ICMC USP")


# ==========================================

# PÁGINA INICIAL

# ==========================================


if pagina == "Início":


    st.header("Bem-vindo ao meu site!")


    # ALTERE o texto de apresentação

    st.write(

        "Este é o meu projeto final do Curso de Programação Web. "

        "Aqui você encontrará conteúdos sobre mim."

    )


    

                


# ==========================================

# PÁGINA SOBRE

# ==========================================


elif pagina == "Sobre":


    st.header("Sobre o meu projeto ")


    # ALTERE as informações abaixo

    st.write(

        "Este projeto foi desenvolvido para falar sobre o Gabriel  "

        "Ele é uma pessoa muito Legal e companheira."

    )


    st.subheader("O objetivo ")


    st.write(

        "O objetivo é você conhecer maus o Gabriel  "

        "ele foi desenvolvido para o Gabriel mostrar a suas habilidades ."

    )


    st.subheader("Sobre o autpr")


    st.write(

        "Meu nome é Gabriel Lucas e esse é o meu projeto."

    )


# ==========================================

# PÁGINA CONTATO

# ==========================================


elif pagina == "Contato":


    st.header("Entre em contato")


    st.write("amiga o processo.")


    with st.form("formulario_contato"):


        nome = st.text_input("Gabriel Lucas ")


        email = st.text_input("gabriellucas.barbim")


        mensagem = st.text_area("Tenho uma duvida")


        enviar = st.form_submit_button("Enviar mensagem")


        if enviar:


            if nome and email and mensagem:


                # Neste primeiro modelo, os dados não

                # são armazenados em banco de dados.

                st.success(

                    "Formulário preenchido com sucesso! "

                    "Esta é uma demonstração."

                )


            else:

                st.warning("Preencha todos os campos.")


# ==========================================

# RODAPÉ

# ==========================================


st.divider()


# ALTERE o nome da autora

st.caption(

    f"© {datetime.now().year} | Desenvolvido por Gabriel Lucas"

)

