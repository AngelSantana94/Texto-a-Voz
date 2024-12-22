import os
from gtts import gTTS
from newspaper import Article

def texto_a_voz(texto,archivo_salida="salida.mp3", idioma="es"):
    """
    Convierte texto a voz y guarda el resultado en un archivo de audio.
    """
    try:
        print("Convirtiendo el texto a audio...")
        tts = gTTS(text=texto, lang=idioma)
        tts.save(archivo_salida)
        print(f"Audio generado exitosamente: {archivo_salida}")

        #Reproducir el archivo de audio
        if os.name == "nt": #Windows
            os.system(f"start {archivo_salida}")
        elif os.name == "posix": # Linux/Mac
            os.system(f"mpg321 {archivo_salida} || afplay {archivo_salida}")
        else:
            print("Sistema operativo no soportado para reproducción automática.")
    except Exception as e:
        print(f"Error al generar el audio: {e}")

def leer_texto_desde_url(url):
    """
    Extrae texto de un artículo desde una URL.
    """
    try:
        print("Descargando el artículo...")
        articulo = Article(url)
        articulo.download()
        articulo.parse()
        texto = articulo.text.strip()

        if not texto:
            raise ValueError("El artículo no contiene texto válido para procesar.")
        
        print("Texto extraído correctamente.")
        return texto
    except Exception as e:
        print(f"Error al procesar la URL: {e}")
        return ""
    
def main():
    print("Seleciona el modo de entrada:")
    print("1. Leer texto desde un archivo .txt")
    print("2. Ingresa texto manualmente.")
    print("3. Leer texto desde una URL")
    opcion= input("Elige una opcion (1, 2 o 3)").strip()

    if opcion =="1":
        archivo = input("Introduce la ruta del archivo .txt: ").strip()
        try:
            with open(archivo, "r", encoding="utf-8") as f:
                texto = f.read()
            texto_a_voz(texto)
        except FileNotFoundError:
            print("Archivo no encontrado.")
    elif opcion == "2":
        texto = input("Introduce el texto que deseas convertir a audio: ").strip()
        texto_a_voz(texto)
    elif opcion == "3":
        url = input("Introduce la URL del artículo: ").strip()
        texto = leer_texto_desde_url(url)
        if texto:
            texto_a_voz(texto)
    else:
        print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()
