from flask import Flask, render_template, request, send_file
import subprocess
import os

app = Flask(__name__)

# Rota para a página inicial
@app.route("/")
def index():
    return render_template("index.html")

# Rota para a página do YouTube
@app.route("/youtube", methods=["GET", "POST"])
def youtube():
    informacoes = None  # Inicializa a variável de informações
    mensagem = None     # Mensagem de status do download

    if request.method == "POST":
        url = request.form.get("url")  # Pega a URL do formulário

        if "baixar_direto" in request.form:  # Se o botão "Baixar" for clicado
            if url:
                try:
                    # Define o comando yt-dlp com base na resolução escolhida
                    resolucao = request.form.get("resolucao")
                    if resolucao == "1080p":
                        comando = [
                            "yt-dlp",
                            "-S", "vcodec:h264",  # Seleciona vídeo h264
                            "-S", "acodec:aac",   # Seleciona áudio aac
                            "-S", "res:1080",     # Seleciona resolução 1080p
                            "-o", "video_temp.mp4",  # Nome do arquivo temporário
                            url
                        ]
                    elif resolucao == "720p":
                        comando = [
                            "yt-dlp",
                            "-S", "vcodec:h264",
                            "-S", "acodec:aac",
                            "-S", "res:720",
                            "-o", "video_temp.mp4",
                            url
                        ]
                    elif resolucao == "360p":
                        comando = [
                            "yt-dlp",
                            "-S", "vcodec:h264",
                            "-S", "acodec:aac",
                            "-S", "res:360",
                            "-o", "video_temp.mp4",
                            url
                        ]
                    elif resolucao == "240p":
                        comando = [
                            "yt-dlp",
                            "-S", "vcodec:h264",
                            "-S", "acodec:aac",
                            "-S", "res:240",
                            "-o", "video_temp.mp4",
                            url
                        ]
                    else:
                        mensagem = "Resolução inválida."
                        return render_template("youtube.html", informacoes=informacoes, mensagem=mensagem)

                    # Executa o comando yt-dlp
                    resultado = subprocess.run(comando, capture_output=True, text=True)
                    if resultado.returncode != 0:
                        mensagem = f"Erro ao baixar o vídeo:\n{resultado.stderr}"
                        return render_template("youtube.html", informacoes=informacoes, mensagem=mensagem)

                    # Envia o arquivo para o usuário como download
                    return send_file("video_temp.mp4", as_attachment=True)

                except Exception as e:
                    mensagem = f"Ocorreu um erro: {e}"
                finally:
                    # Remove o arquivo temporário após o envio
                    if os.path.exists("video_temp.mp4"):
                        os.remove("video_temp.mp4")
            else:
                mensagem = "Por favor, insira uma URL válida."

        elif "extrair" in request.form:  # Se o botão "Extrair Informações" for clicado
            if url:
                try:
                    # Comando yt-dlp para extrair informações
                    comando = [
                        "yt-dlp",
                        "-v",          # Modo verboso (opcional, para depuração)
                        "-F",          # Lista todos os formatos disponíveis
                        "-o", "%(id)s.%(ext)s",  # Define o padrão de nome do arquivo
                        url            # URL do vídeo
                    ]

                    # Executa o comando e captura a saída
                    resultado = subprocess.run(comando, capture_output=True, text=True)

                    # Verifica se o comando foi executado com sucesso
                    if resultado.returncode == 0:
                        informacoes = resultado.stdout  # Exibe as informações
                    else:
                        informacoes = f"Erro ao extrair informações:\n{resultado.stderr}"
                except Exception as e:
                    informacoes = f"Ocorreu um erro: {e}"
            else:
                informacoes = "Por favor, insira uma URL válida."

        elif "baixar" in request.form:  # Se o botão "Baixar" for clicado
            formato = request.form.get("formato")  # Pega o código do formato
            if url and formato:
                try:
                    # Gera um nome de arquivo temporário
                    nome_arquivo = "video_temp.mp4"

                    # Comando yt-dlp para baixar o vídeo diretamente
                    comando_yt_dlp = [
                        "yt-dlp",
                        "-f", formato,  # Formato selecionado
                        "-o", nome_arquivo,  # Nome do arquivo temporário
                        url
                    ]

                    # Executa o comando yt-dlp
                    resultado_yt_dlp = subprocess.run(comando_yt_dlp, capture_output=True, text=True)
                    if resultado_yt_dlp.returncode != 0:
                        mensagem = f"Erro ao baixar o vídeo:\n{resultado_yt_dlp.stderr}"
                        return render_template("youtube.html", informacoes=informacoes, mensagem=mensagem)

                    # Envia o arquivo para o usuário como download
                    return send_file(nome_arquivo, as_attachment=True)

                except Exception as e:
                    mensagem = f"Ocorreu um erro: {e}"
                finally:
                    # Remove o arquivo temporário após o envio
                    if os.path.exists(nome_arquivo):
                        os.remove(nome_arquivo)
            else:
                mensagem = "Por favor, insira uma URL e um formato válidos."

    # Renderiza a página HTML com as informações e mensagem
    return render_template("youtube.html", informacoes=informacoes, mensagem=mensagem)

# Rota para a página do Instagram
@app.route("/instagram", methods=["GET", "POST"])
def instagram():
    informacoes = None  # Inicializa a variável de informações
    mensagem = None     # Mensagem de status do download

    if request.method == "POST":
        url = request.form.get("url")  # Pega a URL do formulário

        if "baixar_direto" in request.form:  # Se o botão "Baixar" for clicado
            if url:
                try:
                    # Define o comando yt-dlp com base na resolução escolhida
                    resolucao = request.form.get("resolucao")
                    if resolucao == "1080p":
                        comando = [
                            "yt-dlp",
                            "-S", "vcodec:h264",  # Seleciona vídeo h264
                            "-S", "acodec:aac",   # Seleciona áudio aac
                            "-S", "res:1080",     # Seleciona resolução 1080p
                            "-o", "video_temp.mp4",  # Nome do arquivo temporário
                            url
                        ]
                    elif resolucao == "720p":
                        comando = [
                            "yt-dlp",
                            "-S", "vcodec:h264",
                            "-S", "acodec:aac",
                            "-S", "res:720",
                            "-o", "video_temp.mp4",
                            url
                        ]
                    elif resolucao == "360p":
                        comando = [
                            "yt-dlp",
                            "-S", "vcodec:h264",
                            "-S", "acodec:aac",
                            "-S", "res:360",
                            "-o", "video_temp.mp4",
                            url
                        ]
                    elif resolucao == "240p":
                        comando = [
                            "yt-dlp",
                            "-S", "vcodec:h264",
                            "-S", "acodec:aac",
                            "-S", "res:240",
                            "-o", "video_temp.mp4",
                            url
                        ]
                    else:
                        mensagem = "Resolução inválida."
                        return render_template("instagram.html", informacoes=informacoes, mensagem=mensagem)

                    # Executa o comando yt-dlp
                    resultado = subprocess.run(comando, capture_output=True, text=True)
                    if resultado.returncode != 0:
                        mensagem = f"Erro ao baixar o vídeo:\n{resultado.stderr}"
                        return render_template("instagram.html", informacoes=informacoes, mensagem=mensagem)

                    # Envia o arquivo para o usuário como download
                    return send_file("video_temp.mp4", as_attachment=True)

                except Exception as e:
                    mensagem = f"Ocorreu um erro: {e}"
                finally:
                    # Remove o arquivo temporário após o envio
                    if os.path.exists("video_temp.mp4"):
                        os.remove("video_temp.mp4")
            else:
                mensagem = "Por favor, insira uma URL válida."

        elif "extrair" in request.form:  # Se o botão "Extrair Informações" for clicado
            if url:
                try:
                    # Comando yt-dlp para extrair informações
                    comando = [
                        "yt-dlp",
                        "-v",          # Modo verboso (opcional, para depuração)
                        "-F",          # Lista todos os formatos disponíveis
                        "-o", "%(id)s.%(ext)s",  # Define o padrão de nome do arquivo
                        url            # URL do vídeo
                    ]

                    # Executa o comando e captura a saída
                    resultado = subprocess.run(comando, capture_output=True, text=True)

                    # Verifica se o comando foi executado com sucesso
                    if resultado.returncode == 0:
                        informacoes = resultado.stdout  # Exibe as informações
                    else:
                        informacoes = f"Erro ao extrair informações:\n{resultado.stderr}"
                except Exception as e:
                    informacoes = f"Ocorreu um erro: {e}"
            else:
                informacoes = "Por favor, insira uma URL válida."

        elif "baixar" in request.form:  # Se o botão "Baixar" for clicado
            formato = request.form.get("formato")  # Pega o código do formato
            if url and formato:
                try:
                    # Gera um nome de arquivo temporário
                    nome_arquivo = "video_temp.mp4"

                    # Comando yt-dlp para baixar o vídeo diretamente
                    comando_yt_dlp = [
                        "yt-dlp",
                        "-f", formato,  # Formato selecionado
                        "-o", nome_arquivo,  # Nome do arquivo temporário
                        url
                    ]

                    # Executa o comando yt-dlp
                    resultado_yt_dlp = subprocess.run(comando_yt_dlp, capture_output=True, text=True)
                    if resultado_yt_dlp.returncode != 0:
                        mensagem = f"Erro ao baixar o vídeo:\n{resultado_yt_dlp.stderr}"
                        return render_template("instagram.html", informacoes=informacoes, mensagem=mensagem)

                    # Envia o arquivo para o usuário como download
                    return send_file(nome_arquivo, as_attachment=True)

                except Exception as e:
                    mensagem = f"Ocorreu um erro: {e}"
                finally:
                    # Remove o arquivo temporário após o envio
                    if os.path.exists(nome_arquivo):
                        os.remove(nome_arquivo)
            else:
                mensagem = "Por favor, insira uma URL e um formato válidos."

    # Renderiza a página HTML com as informações e mensagem
    return render_template("instagram.html", informacoes=informacoes, mensagem=mensagem)

   
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
