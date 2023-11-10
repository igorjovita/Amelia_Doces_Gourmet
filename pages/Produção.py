import streamlit as st
import mysql.connector
import pandas as pd
import os

mydb = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USERNAME"),
    passwd=os.getenv("DB_PASSWORD"),
    db=os.getenv("DB_NAME"),
    autocommit=True,
    ssl_verify_identity=False,
    ssl_ca=r"C:\users\acqua\downloads\cacert-2023-08-22.pem")
cursor = mydb.cursor()

st.title('Produção')
data = st.date_input('Data da Produção', format='DD/MM/YYYY')
mydb.connect()
cursor.execute("SELECT nome FROM sabores")
chars = "'),([]"
lista = str(cursor.fetchall()).translate(str.maketrans('', '', chars)).split()

sabor = st.selectbox('Sabor:', options=lista)

quantidade = st.text_input('Quantidade produzida')

col1, col2, col3 = st.columns(3)

with col1:
    if st.button('Lançar Produção'):
        cursor.execute(f"SELECT id from sabores where nome = {sabor} ")
        id_produto = str(cursor.fetchone()).translate(str.maketrans('', '', chars))

        cursor.execute("insert into entrada(id_produto, quantidade, data_entrada) values (%s, %s, %s) ", (id_produto, quantidade, data))
        mydb.commit()
        mydb.close()
        st.success('Produção lançada no sistema')



def click_button():
    st.session_state.button = not st.session_state.button


with col2:
    mydb.connect()
    cursor.execute("SELECT * FROM entrada")
    entrada = cursor.fetchall()
    mydb.close()

    if 'button' not in st.session_state:
        st.session_state.button = False
    st.button('Relatorio de Produção', type='primary', on_click=click_button)

if st.session_state.button:
    df = pd.DataFrame(entrada, columns=['Coluna 1', 'Coluna 2', 'Coluna 3', 'Coluna 4'])
    st.table(df)
else:
    pass
