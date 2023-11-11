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
cursor = mydb.cursor(buffered=True)

st.title('Venda')
col1, col2, col3 = st.columns(3)
with col1:
    data = st.date_input('Data da Venda', format='DD/MM/YYYY')
    quantidade = st.text_input('Quantidade Vendida')

with col2:
    tipo = st.selectbox('Tipo:', ['Turista', 'Local'])
    valor = st.text_input('Valor:')

with col3:
    cursor.execute("SELECT nome FROM sabores")
    chars = "'),([]"
    lista = str(cursor.fetchall()).translate(str.maketrans('', '', chars)).split()
    sabor = st.selectbox('Sabor:', options=lista)
    pagamento = st.selectbox('Forma de Pagamento', options=['Pix', 'Dinheiro', 'Debito', 'Credito'])
    cursor.execute(f"Select id from sabores where nome = '{sabor}'")
    id_produto = str(cursor.fetchone()).translate(str.maketrans('', '', chars))

if st.button('Lançar Venda'):
    mydb.connect()
    cursor.execute("insert into saida(id_produto, quantidade, data_saida, valor, tipo, pagamento) values (%s, %s, %s, %s, %s, %s)",
                   (id_produto, quantidade, data, valor, tipo,pagamento))
    mydb.commit()
    st.success('Venda lançada no sistema')
