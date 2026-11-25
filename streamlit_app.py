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

    {

        "titulo": "Minhas coisas favorita",

        "autor": "Gabriel Lucas",

        "texto": "Eu gosto muito de jogar futebol e de jogar videogame"

    },

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


    st.subheader("Publicações")


    # Campo de pesquisa

    pesquisa = st.text_input("Pesquisar publicações:")


    for post in POSTS:


        # Verifica se a publicação corresponde à pesquisa

        if pesquisa.lower() in post["titulo"].lower():


            with st.container(border=True):


                st.image(post["imagem"], use_container_width=True)


                st.subheader(post["titulo"])


                st.caption("Publicado por: " + post["autor"])


                st.write(post["texto"])


# ==========================================

# PÁGINA SOBRE

# ==========================================


elif pagina == "Sobre":


    st.header("Sobre o projeto")


    # ALTERE as informações abaixo

    st.write(

        "Este projeto foi desenvolvido como atividade final "

        "do Curso de Programação Web para Meninas."

    )


    st.subheader("Objetivo")


    st.write(

        "Apresente aqui o objetivo do seu projeto "

        "e explique para quem ele foi desenvolvido."

    )


    st.subheader("Sobre a autora")


    st.write(

        "Meu nome é SEU NOME e este é o meu projeto."

    )


# ==========================================

# PÁGINA CONTATO

# ==========================================


elif pagina == "Contato":


    st.header("Entre em contato")


    st.write("Preencha os campos abaixo.")


    with st.form("formulario_contato"):


        nome = st.text_input("Nome")


        email = st.text_input("E-mail")


        mensagem = st.text_area("Mensagem")


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

    f"© {datetime.now().year} | Desenvolvido por SEU NOME"

)

