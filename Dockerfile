# Usar a imagem base do Python
FROM python:3.9

# Definir o diretório de trabalho
WORKDIR /app

# Copiar os requisitos e instalar as dependências
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copiar o conteúdo da aplicação
COPY . .

# Comando para rodar a aplicação
CMD ["python", "app.py"]
