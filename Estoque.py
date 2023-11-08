import streamlit as st
import mysql.connector
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

st.title('Amelia Doces Gourmet')

col1, col2 = st.columns(2)

with col1:
    st.subheader('Ninho')
    st.subheader('Nesquik')
    st.subheader('Ferrero Rocher')
    st.subheader('Prestigio')

with col2:
    resultado1 = cursor.execute('SELECT quantidade FROM estoque where id_produto = "1"')
    resultado1 = cursor.fetchall()

    resultado2 = cursor.execute('SELECT quantidade FROM estoque where id_produto = "2"')
    resultado2 = cursor.fetchall()

    resultado3 = cursor.execute('SELECT quantidade FROM estoque where id_produto = "3"')
    resultado3 = cursor.fetchall()

    resultado4 = cursor.execute('SELECT quantidade FROM estoque where id_produto = "4"')
    resultado4 = cursor.fetchall()
    chars = "'),([]"
    var1 = str(resultado1).translate(str.maketrans('', '', chars))
    var2 = str(resultado2).translate(str.maketrans('', '', chars))
    var3 = str(resultado3).translate(str.maketrans('', '', chars))
    var4 = str(resultado4).translate(str.maketrans('', '', chars))
    st.subheader(f'{var1} Unidades')
    st.subheader(f'{var2} Unidades')
    st.subheader(f'{var3} Unidades')
    st.subheader(f'{var4} Unidades')


