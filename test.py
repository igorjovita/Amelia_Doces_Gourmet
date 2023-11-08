import streamlit as st

lista = []
texto = st.text_input('Adicione a lista')

if st.button('Botao'):
    lista.append(texto)

for i, nome in enumerate(lista):
    check = st.checkbox(str(nome), key=str(i))

