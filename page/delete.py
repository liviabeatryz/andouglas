import streamlit as st

import controller.cliente as cliente

def deletar():
    st.title ('deletar dados')

    with st.form(key='insert'):
        input_mat = st.number_input(label= 'insira sua matricula', format='%d', step=1)
        bt_excluir = st.form_submit_button('excluir')

        if bt_excluir:
            cliente.deletar(input_mat)
            st.success('matricula deletada com sucesso')
