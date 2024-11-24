# Use uma imagem base com suporte a Python
FROM python:3.9-slim

# Defina o diretório de trabalho dentro do container
WORKDIR /app

# Copie o arquivo de requisitos
COPY requirements.txt .

# Instale as dependências do projeto
RUN pip install --no-cache-dir -r requirements.txt

# Copie o código do projeto para o container
COPY . .

# Exponha a porta usada pelo Streamlit
EXPOSE 8501

# Comando para rodar o Streamlit
CMD ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]
