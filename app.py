import streamlit as st
import google.generativeai as genai

# 1. Configuración de la página
st.title("Mi App con Google AI")
st.write("Escribe algo abajo y la IA te responderá.")

# 2. Capturar la API Key (esto se configura en la nube después)
# Se busca en los "secretos" de la configuración
api_key = st.secrets["GOOGLE_API_KEY"]

# 3. Configurar el modelo
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash') # O el modelo que hayas elegido

# 4. Interfaz de usuario
user_input = st.text_input("Ingresa tu consulta aquí:")

if st.button("Enviar"):
    if user_input:
        try:
            response = model.generate_content(user_input)
            st.write("### Respuesta:")
            st.write(response.text)
        except Exception as e:
            st.error(f"Hubo un error: {e}")
    else:
        st.warning("Por favor escribe algo antes de enviar.")
