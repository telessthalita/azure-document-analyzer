import streamlit as st

def configure_interface():
    st.title("Upload de Arquivo - Fake Docs")
    
    uploaded_file = st.file_uploader("Escolha um arquivo", type=["pdf", "png", "jpeg"])
    
    if uploaded_file is not None:
        fileName = uploaded_file.name  
        st.write(f"Arquivo ({fileName}) enviado com sucesso para o Azure Blob Storage")
        
        credit_card_info = {"card_name": "João da Silva"}  
        blob_url = "https://exemplo.com/imagem.jpg"  

        show_image_and_validation(blob_url, credit_card_info)
    else:
        st.write("Nenhum arquivo foi enviado.")

def show_image_and_validation(blob_url, credit_card_info):
    st.image(blob_url, caption="Imagem enviada", use_column_width=True)
    st.write("Resultado da validação:")
    
    if credit_card_info and credit_card_info["card_name"]:
        st.markdown(
            "<h1 style='color: green;'>Cartão Válido</h1>",
            unsafe_allow_html=True
        )
        st.write(f"Nome do Titular: {credit_card_info['card_name']}")
    else:
        st.markdown(
            "<h1 style='color: red;'>Cartão Inválido</h1>",
            unsafe_allow_html=True
        )

if __name__ == "__main__":
    configure_interface()
