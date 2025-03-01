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

# Rota para a página do Twitter
@app.route("/twitter", methods=["GET", "POST"])
def twitter():
    informacoes = None  # Inicializa a variável de informações
    mensagem = None     # Mensagem de status do download

    if request.method == "POST":
        url = request.form.get("url")  # Pega a URL do formulário

        if "baixar_direto" in request.form:
            if url:
                try:
                    resolucao = request.form.get("resolucao")
                    if resolucao == "720p":
                        comando = [
                            "yt-dlp", "-S", "vcodec:h264", "-S", "acodec:aac", "-S", "res:576", "-o", "video_temp.mp4", url
                        ]
                    elif resolucao == "360p":
                        comando = [
                            "yt-dlp", "-S", "vcodec:h264", "-S", "acodec:aac", "-S", "res:480", "-o", "video_temp.mp4", url
                        ]
                    elif resolucao == "240p":
                        comando = [
                            "yt-dlp", "-S", "vcodec:h264", "-S", "acodec:aac", "-S", "res:320", "-o", "video_temp.mp4", url
                        ]
                    else:
                        mensagem = "Resolução inválida."
                        return render_template("twitter.html", informacoes=informacoes, mensagem=mensagem)

                    resultado = subprocess.run(comando, capture_output=True, text=True)
                    if resultado.returncode != 0:
                        mensagem = f"Erro ao baixar o vídeo:\n{resultado.stderr}"
                        return render_template("twitter.html", informacoes=informacoes, mensagem=mensagem)

                    return send_file("video_temp.mp4", as_attachment=True)

                except Exception as e:
                    mensagem = f"Ocorreu um erro: {e}"
                finally:
                    if os.path.exists("video_temp.mp4"):
                        os.remove("video_temp.mp4")
            else:
                mensagem = "Por favor, insira uma URL válida."

        elif "extrair" in request.form:
            if url:
                try:
                    comando = [
                        "yt-dlp", "-v", "-F", "-o", "%(id)s.%(ext)s", "--extractor-args", "twitter:api=graphql", url
                    ]
                    resultado = subprocess.run(comando, capture_output=True, text=True)

                    if resultado.returncode == 0:
                        informacoes = resultado.stdout
                    else:
                        informacoes = f"Erro ao extrair informações:\n{resultado.stderr}"
                except Exception as e:
                    informacoes = f"Ocorreu um erro: {e}"
            else:
                informacoes = "Por favor, insira uma URL válida."

        elif "baixar" in request.form:
            formato = request.form.get("formato")
            if url and formato:
                try:
                    nome_arquivo = "video_temp.mp4"
                    comando_yt_dlp = [
                        "yt-dlp", "-f", formato, "-o", nome_arquivo, url
                    ]
                    resultado_yt_dlp = subprocess.run(comando_yt_dlp, capture_output=True, text=True)

                    if resultado_yt_dlp.returncode != 0:
                        mensagem = f"Erro ao baixar o vídeo:\n{resultado_yt_dlp.stderr}"
                        return render_template("twitter.html", informacoes=informacoes, mensagem=mensagem)

                    return send_file(nome_arquivo, as_attachment=True)

                except Exception as e:
                    mensagem = f"Ocorreu um erro: {e}"
                finally:
                    if os.path.exists(nome_arquivo):
                        os.remove(nome_arquivo)
            else:
                mensagem = "Por favor, insira uma URL e um formato válidos."

    return render_template("twitter.html", informacoes=informacoes, mensagem=mensagem)

# Rota para a página do Tiktok
@app.route("/tiktok", methods=["GET", "POST"])
def tiktok():
    informacoes = None
    mensagem = None

    if request.method == "POST":
        url = request.form.get("url")

        if "baixar_direto" in request.form:
            if url:
                try:
                    resolucao = request.form.get("resolucao")
                    if resolucao == "1080p":
                        comando = [
                            "yt-dlp", "-S", "vcodec:h264", "-S", "acodec:aac", "-S", "res:1080", "-o", "video_temp.mp4", url
                        ]
                    elif resolucao == "720p":
                        comando = [
                            "yt-dlp", "-S", "vcodec:h264", "-S", "acodec:aac", "-S", "res:720", "-o", "video_temp.mp4", url
                        ]
                    elif resolucao == "576p":
                        comando = [
                            "yt-dlp", "-S", "vcodec:h264", "-S", "acodec:aac", "-S", "res:576", "-o", "video_temp.mp4", url
                        ]
                    else:
                        mensagem = "Resolução inválida."
                        return render_template("tiktok.html", informacoes=informacoes, mensagem=mensagem)

                    resultado = subprocess.run(comando, capture_output=True, text=True)
                    if resultado.returncode != 0:
                        mensagem = f"Erro ao baixar o vídeo:\n{resultado.stderr}"
                        return render_template("tiktok.html", informacoes=informacoes, mensagem=mensagem)

                    return send_file("video_temp.mp4", as_attachment=True)

                except Exception as e:
                    mensagem = f"Ocorreu um erro: {e}"
                finally:
                    if os.path.exists("video_temp.mp4"):
                        os.remove("video_temp.mp4")
            else:
                mensagem = "Por favor, insira uma URL válida."

        elif "extrair" in request.form:
            if url:
                try:
                    comando = [
                        "yt-dlp", "-v", "-F", "-o", "%(id)s.%(ext)s", url
                    ]
                    resultado = subprocess.run(comando, capture_output=True, text=True)

                    if resultado.returncode == 0:
                        informacoes = resultado.stdout
                    else:
                        informacoes = f"Erro ao extrair informações:\n{resultado.stderr}"
                except Exception as e:
                    informacoes = f"Ocorreu um erro: {e}"
            else:
                informacoes = "Por favor, insira uma URL válida."

        elif "baixar" in request.form:
            formato = request.form.get("formato")
            if url and formato:
                try:
                    nome_arquivo = "video_temp.mp4"
                    comando_yt_dlp = [
                        "yt-dlp", "-f", formato, "-o", nome_arquivo, url
                    ]
                    resultado_yt_dlp = subprocess.run(comando_yt_dlp, capture_output=True, text=True)

                    if resultado_yt_dlp.returncode != 0:
                        mensagem = f"Erro ao baixar o vídeo:\n{resultado_yt_dlp.stderr}"
                        return render_template("tiktok.html", informacoes=informacoes, mensagem=mensagem)

                    return send_file(nome_arquivo, as_attachment=True)

                except Exception as e:
                    mensagem = f"Ocorreu um erro: {e}"
                finally:
                    if os.path.exists(nome_arquivo):
                        os.remove(nome_arquivo)
            else:
                mensagem = "Por favor, insira uma URL e um formato válidos."

    return render_template("tiktok.html", informacoes=informacoes, mensagem=mensagem)

@app.route("/facebook", methods=["GET", "POST"])
def facebook():
    informacoes = None
    mensagem = None

    if request.method == "POST":
        url = request.form.get("url")

        if "baixar_direto" in request.form:
            if url:
                try:
                    resolucao = request.form.get("resolucao")
                    if resolucao == "hd":
                        # Comando para HD
                        comando_yt_dlp = [
                            "yt-dlp", "--youtube-skip-dash-manifest", "-f", "hd", "-g", url
                        ]
                    elif resolucao == "sd":
                        # Comando para SD
                        comando_yt_dlp = [
                            "yt-dlp", "--youtube-skip-dash-manifest", "-f", "sd", "-g", url
                        ]
                    else:
                        mensagem = "Resolução inválida."
                        return render_template("facebook.html", informacoes=informacoes, mensagem=mensagem)

                    # Executa o yt-dlp para obter a URL do vídeo
                    resultado_yt_dlp = subprocess.run(comando_yt_dlp, capture_output=True, text=True)
                    if resultado_yt_dlp.returncode != 0:
                        mensagem = f"Erro ao obter a URL do vídeo:\n{resultado_yt_dlp.stderr}"
                        return render_template("facebook.html", informacoes=informacoes, mensagem=mensagem)

                    url_video = resultado_yt_dlp.stdout.strip()

                    # Comando ffmpeg para processar o vídeo
                    comando_ffmpeg = [
                        "ffmpeg", "-i", url_video, "-c", "copy", "-reset_timestamps", "1",
                        "-avoid_negative_ts", "make_zero", "-f", "mp4", "video_temp.mp4"
                    ]
                    resultado_ffmpeg = subprocess.run(comando_ffmpeg, capture_output=True, text=True)
                    if resultado_ffmpeg.returncode != 0:
                        mensagem = f"Erro ao processar o vídeo:\n{resultado_ffmpeg.stderr}"
                        return render_template("facebook.html", informacoes=informacoes, mensagem=mensagem)

                    # Envia o arquivo para o usuário
                    return send_file("video_temp.mp4", as_attachment=True)

                except Exception as e:
                    mensagem = f"Ocorreu um erro: {e}"
                finally:
                    if os.path.exists("video_temp.mp4"):
                        os.remove("video_temp.mp4")
            else:
                mensagem = "Por favor, insira uma URL válida."

        elif "extrair" in request.form:
            if url:
                try:
                    comando = [
                        "yt-dlp", "-v", "-F", "-o", "%(id)s.%(ext)s", url
                    ]
                    resultado = subprocess.run(comando, capture_output=True, text=True)

                    if resultado.returncode == 0:
                        informacoes = resultado.stdout
                    else:
                        informacoes = f"Erro ao extrair informações:\n{resultado.stderr}"
                except Exception as e:
                    informacoes = f"Ocorreu um erro: {e}"
            else:
                informacoes = "Por favor, insira uma URL válida."

        elif "baixar" in request.form:
            formato = request.form.get("formato")
            if url and formato:
                try:
                    nome_arquivo = "video_temp.mp4"
                    comando_yt_dlp = [
                        "yt-dlp", "-f", formato, "-o", nome_arquivo, url
                    ]
                    resultado_yt_dlp = subprocess.run(comando_yt_dlp, capture_output=True, text=True)

                    if resultado_yt_dlp.returncode != 0:
                        mensagem = f"Erro ao baixar o vídeo:\n{resultado_yt_dlp.stderr}"
                        return render_template("facebook.html", informacoes=informacoes, mensagem=mensagem)

                    return send_file(nome_arquivo, as_attachment=True)

                except Exception as e:
                    mensagem = f"Ocorreu um erro: {e}"
                finally:
                    if os.path.exists(nome_arquivo):
                        os.remove(nome_arquivo)
            else:
                mensagem = "Por favor, insira uma URL e um formato válidos."

    return render_template("facebook.html", informacoes=informacoes, mensagem=mensagem)
    
# Rota para a página de Lista m3u8
@app.route("/m3u8", methods=["GET", "POST"])
def m3u8():
    mensagem = None

    if request.method == "POST":
        url = request.form.get("url")

        if url:
            try:
                nome_arquivo = "video_temp.mp4"
                comando_ffmpeg = [
                    "ffmpeg", "-i", url, "-c", "copy", "-reset_timestamps", "1", "-avoid_negative_ts", "make_zero", "-f", "flv", nome_arquivo
                ]

                resultado_ffmpeg = subprocess.run(comando_ffmpeg, capture_output=True, text=True)

                if resultado_ffmpeg.returncode != 0:
                    mensagem = f"Erro ao baixar o vídeo:\n{resultado_ffmpeg.stderr}"
                    return render_template("m3u8.html", mensagem=mensagem)

                return send_file(nome_arquivo, as_attachment=True)

            except Exception as e:
                mensagem = f"Ocorreu um erro: {e}"
            finally:
                if os.path.exists(nome_arquivo):
                    os.remove(nome_arquivo)
        else:
            mensagem = "Por favor, insira uma URL válida."

    return render_template("m3u8.html", mensagem=mensagem)

## main here
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)