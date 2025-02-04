import streamlit as st


st.title('CALCULADORA')
st.divider()

sinal = st.text_input("Ola, que tipo de conta deseja fazer? multiplicação, divisão, soma, subtração. Digite o tipo de conta desejada: ")
a = st.number_input('Digite o primeiro numero:\n ')
b = st.number_input('Digite o segundo numero:\n ')




if sinal == "multiplicação":
  conta  = a * b
  st.write(f"O resultado de sua conta de multiplicação é de {conta}.")

elif sinal =="divisão":
 conta  = a / b
        
 st.write(f"O resultado de sua conta de divisão é de {conta}.")
 
elif sinal =="soma":
 conta  = a + b
        
 st.write(f"O resultado de sua conta de soma é de {conta}.")

elif sinal == "subtração":
 conta  = a - b
        
 st.write(f"O resultado de sua conta de subtração é de {conta}.")
     
else:
 st.write("Opção não encontrada!")
    
  
