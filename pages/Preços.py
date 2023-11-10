import mysql.connector
import streamlit as st
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


st.write('''<style>

[data-testid="column"] {
    width: calc(33.3333% - 1rem) !important;
    flex: 1 1 calc(33.3333% - 1rem) !important;
    min-width: calc(33% - 1rem) !important;
}

</style>''', unsafe_allow_html=True)





st.subheader('Compra')
chars = "'),([]"
col1, col2, col3 = st.columns(3)

with col1:
    data = st.date_input('Data da compra', format='DD/MM/YYYY')
    mercado = st.text_input('Mercado')

with col2:
    cursor.execute("SELECT nome FROM produto")
    produto = str(cursor.fetchall()).translate(str.maketrans('', '', chars)).split()
    quantidade_prod = st.text_input('Quantidade', key='quantidade1').replace(',', '.')
    valor_prod = st.text_input('Valor')
with col3:
    nome_prod = st.selectbox('Produto', produto)


cursor.execute(f"SELECT id from produto where nome = '{nome_prod}'")
id_prod = str(cursor.fetchall()).translate(str.maketrans('', '', chars))

if st.button('Lançar no Sistema'):
    cursor.execute("insert into preço (data_compra,id_produto, mercado, quantidade, valor) values (%s, %s, %s, %s,%s) ",
                   (data, id_prod, mercado, quantidade_prod, valor_prod))
    mydb.commit()
    st.success('Lançamento Feito!')

st.write('---')
st.subheader('Cadastro de Produtos')

col1, col2, col3 = st.columns(3)

with col1:
    nome = st.text_input('Nome do Produto').replace(' ', '_').capitalize()
with col2:
    quantidade = st.text_input('Quantidade')
with col3:
    valor = str(st.text_input('Preço do Produto')).replace(',', '.')


if st.button('Cadastrar Produto'):
    cursor.execute("INSERT INTO produto(nome, quantidade,valor) VALUES (%s,%s,%s)", (nome, quantidade, valor))
    mydb.commit()
    st.success('Produto Cadastrado com Sucesso')
st.write('---')
st.subheader('Registro de Preços')


nome_registro = st.selectbox('Lista', produto)
if st.button('Pesquisar no sistema'):
    cursor.execute(
        f"select preço.data_produto, produto.nome,preço.mercado, preço.quantidade, preço.valor from produto join preço on "
        f"preço.id_prod = produto.id where produto.nome ='{nome_registro}'")
    dados = cursor.fetchall()

    df = pd.DataFrame(dados, columns=['Data', 'Produto', 'Mercado', 'Quantidade', 'Preço'])

    st.dataframe(df)
