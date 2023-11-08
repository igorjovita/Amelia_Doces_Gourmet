import streamlit as st


def show():
    if "lista" not in st.session_state:
        st.session_state.lista = []

    def incluir_lista():

        if st.session_state.nova_lista:
            st.session_state.lista.append(
                {
                    "description": st.session_state.nova_lista.capitalize(),
                    "done": False,
                }
            )

    # # Show widgets to add new TODO.

    st.text_input("Adicione um item a lista", on_change=incluir_lista, key="nova_lista").capitalize()
    mostrar_lista(st.session_state.lista)

    # Show all TODOs.


def mostrar_lista(lista):
    "Display the todo list (mostly layout stuff, no state)."
    st.write("")

    for i, item in enumerate(lista):
        col1, col2, _ = st.columns([0.05, 0.8, 0.15])
        done = col1.checkbox("a", item["done"], key=str(i), label_visibility="hidden")
        if done:
            format_str = (
                '<span style="color: grey; text-decoration: line-through;">{}</span>'
            )
        else:
            format_str = "{}"

        col2.markdown(
            format_str.format(item["description"]),
            unsafe_allow_html=True,
        )


if __name__ == "__main__":
    show()
