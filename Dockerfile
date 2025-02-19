# Usa uma imagem base do Python para ARM 32 bits
FROM arm32v7/python:3.9-slim

# Instala dependências do sistema (ffmpeg e outras bibliotecas necessárias)
RUN apt-get update && apt-get install -y \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

# Define o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copia os arquivos necessários para o contêiner
COPY ./app .

# Instala as dependências do Python
RUN pip install --no-cache-dir flask yt-dlp

# Expõe a porta 5000 (porta padrão do Flask)
EXPOSE 5000

# Comando para rodar a aplicação
CMD ["python", "app.py"]