import os  
from azure.storage.blob import BlobServiceClient  
import streamlit as st
from utils.Config import Config  

def upload_blob(file, file_name):
    try:
        connection_string = Config.AZURE_STORAGE_CONNECTION_STRING

        blob_service_client = BlobServiceClient.from_connection_string(connection_string)

        container_name = Config.AZURE_CONTAINER_NAME

        blob_client = blob_service_client.get_blob_client(container=container_name, blob=file_name)

        blob_client.upload_blob(file, overwrite=True)

        st.success(f"Arquivo '{file_name}' enviado com sucesso para o contêiner '{container_name}' no Azure Blob Storage.")
    except Exception as e:
        st.error(f"Erro ao enviar o arquivo: {e}")
