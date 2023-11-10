import streamlit as st
import mysql.connector
import os

st.write('''<style>

[data-testid="column"] {
    width: calc(33.3333% - 1rem) !important;
    flex: 1 1 calc(33.3333% - 1rem) !important;
    min-width: calc(33% - 1rem) !important;
}

</style>''', unsafe_allow_html=True)

mydb = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USERNAME"),
    passwd=os.getenv("DB_PASSWORD"),
    db=os.getenv("DB_NAME"),
    autocommit=True,
    ssl_verify_identity=False,
    ssl_ca=r"C:\users\acqua\downloads\cacert-2023-08-22.pem")
cursor = mydb.cursor()
chars = "'),([]"
chars2 = "')([]"

st.title('Amelia Doces Gourmet')

col1, col2 = st.columns(2)

mydb.connect()
cursor.execute("SELECT nome FROM sabores")
sabores = str(cursor.fetchall()).translate(str.maketrans('', '', chars2)).split(',')
mydb.close()

for sabor in sabores:
    with col1:
        st.subheader(sabor)
    with col2:
        mydb.connect()
        cursor.execute(f"SELECT id FROM sabores WHERE nome = '{sabor}'")
        id_produto = str(cursor.fetchone()).translate(str.maketrans('', '', chars))
        cursor.execute(f"SELECT quantidade FROM estoque WHERE id_produto = {id_produto}")
        quantidade = str(cursor.fetchall()).translate(str.maketrans('', '', chars2)).split(',')
        mydb.close()
        st.subheader(quantidade)

# with col1:
#     st.subheader('Ninho')
#     st.subheader('Nesquik')
#     st.subheader('Ferrero Rocher')
#     st.subheader('Prestigio')
#
# with col2:
#     cursor.execute('SELECT quantidade FROM estoque where id_produto = "1"')
#     resultado1 = cursor.fetchall()
#
#     cursor.execute('SELECT quantidade FROM estoque where id_produto = "2"')
#     resultado2 = cursor.fetchall()
#
#     cursor.execute('SELECT quantidade FROM estoque where id_produto = "3"')
#     resultado3 = cursor.fetchall()
#
#     cursor.execute('SELECT quantidade FROM estoque where id_produto = "4"')
#     resultado4 = cursor.fetchall()
#     chars = "'),([]"
#     var1 = str(resultado1).translate(str.maketrans('', '', chars))
#     var2 = str(resultado2).translate(str.maketrans('', '', chars))
#     var3 = str(resultado3).translate(str.maketrans('', '', chars))
#     var4 = str(resultado4).translate(str.maketrans('', '', chars))
#     st.subheader(f'{var1}')
#     st.subheader(f'{var2}')
#     st.subheader(f'{var3}')
#     st.subheader(f'{var4}')


