import streamlit as st

import controller.cliente as cliente

def inserir():
    st.title('Inserir Dados')
    turmas = ['Matemática', 'português', 'geografia']
    
    with st.form(key='insert'):
        input_name = st.text_input(label='Insira o nome:')
        input_mat = st.number_input(label='Insira a matricula', format='%d', step=1)
        input_turmas = st.number_input(label='Insira a turma')
        input_email = st.text_input(label = 'insira seu e-mail' )
        buttom_submit = st.form_submit_button('Enviar')
        
        if buttom_submit:
            cliente.incluir(input_name, input_mat, int(input_turmas), input_email)
            st.success('Cliente incluido com sucesso')
