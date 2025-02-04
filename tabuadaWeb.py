
import streamlit as st


st.title('TABUADA')
st.divider()


numerador = st.number_input("Qual o número que deseja a tabuada: ")

print("\n")
for i in range(1,11):
    result = i * numerador
    st.write(f"{int(numerador)} x {i} = {int(result)}")
    i = i + 1