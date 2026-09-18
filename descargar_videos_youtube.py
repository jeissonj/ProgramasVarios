import yt_dlp


def descargar_video():
    # Pedir el enlace al usuario
    url = input("Por favor, pega el enlace del video de YouTube: ").strip()

    if not url:
        print("El enlace no puede estar vacío.")
        return

    # Configuración de descarga (Descarga la mejor calidad de video y audio combinados)
    opciones = {
        "format": "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best",
        "outtmpl": "%(title)s.%(ext)s",  # Guarda el archivo con el título del video
        "js_runtimes": {"deno": {}},  # <-- Fuerza el uso de Deno
    }

    print("\nIniciando la descarga... Por favor espera.")

    try:
        with yt_dlp.YoutubeDL(opciones) as ydl:
            ydl.download([url])
        print("\n¡Descarga completada con éxito!")
    except Exception as e:
        print(f"\nOcurrió un error al descargar el video: {e}")


if __name__ == "__main__":
    descargar_video()
