import pyttsx3
import speech_recognition as sr
import pyaudio
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia

# opciones de voz / idiomas
id1 = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-ES_HELENA_11.0"
id2 = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
id3 = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0"


# escuchar microfono y devolver audio como texto
def transf_audio_en_texto():
    # almacenar el recognizer en una variable
    r = sr.Recognizer()

    # config el mircofono
    with sr.Microphone() as origen:

        # tiempo de espera
        r.pause_threshold = 0.8

        # informar inicio grabacion
        print("ya puedes hablar")

        # guardar audio en una variable
        audio = r.listen(origen)

        try:
            # buscar en google
            pedido = r.recognize_google(audio, language="es-ES")

            # imprimir audio reconocido
            print(f"Dijiste: {pedido}")

            # devolver a pedido
            return pedido
        except sr.UnknownValueError:
            # prueba de que no comprendio el audio
            print("No se reconoce el audio")

            # devolver error
            return "sigo esperando"
        except sr.RequestError:
            # prueba de que no comprendio el audio
            print("No hay servicio")

            # devolver error
            return "sigo esperando"
        except:
            # prueba de que no comprendio el audio
            print("Algo ha salido mal")

            # devolver error
            return "sigo esperando"


# funcion para que el asistente pueda hablar
def hablar_asistente(mensaje):
    # encender el motor de pyttsx3
    engine = pyttsx3.init()
    engine.setProperty("voice", id1)

    # pronunciar mensaje
    engine.say(mensaje)
    engine.runAndWait()


# informar del dia de la semana
def pedir_dia():
    # crear variable con datos de hoy
    dia = datetime.datetime.today()

    # crear variable para el dia de la semana
    dia_semana = dia.weekday()

    # diccionario con nombres de dias de la semana
    dias_semana = {0: "Lunes",
                   1: "Martes",
                   2: "Miércoles",
                   3: "Jueves",
                   4: "Viernes",
                   5: "Sábado",
                   6: "Domingo"}

    # decir el dia de la semana
    hablar_asistente(f"Hoy es {dias_semana[dia_semana]}")


# informar que hora es
def pedir_hora():
    # crear una variable con datos de la hora
    hora = datetime.datetime.now()

    # decir la hora
    hora = f"Son las {hora.hour} y {hora.minute}"
    hablar_asistente(hora)


# saludo inicial
def saludo_inicial():
    # crear variable con datos de hora
    hora = datetime.datetime.now()
    if hora.hour < 6 or hora.hour > 21:
        momento = "buenas noches"
    elif 6 <= hora.hour <= 11:
        momento = "buenos días"
    elif 12 <= hora.hour <= 21:
        momento = "buenas tardes"

    # decir saludo
    hablar_asistente(f"Hola, {momento}, soy Dona tu asistente personal, ¿En que puedo ayudarte?")


# funcion central del asistente
def centro_peticiones():
    # acvitar el saludo inicial
    saludo_inicial()

    # variable de corte
    comenzar = True

    # loop central
    while comenzar:
        # activar el micro y guardar el pedido en un string
        pedido = transf_audio_en_texto().lower()

        if "abrir youtube" in pedido:
            hablar_asistente("Estoy abriendo Youtube")
            webbrowser.open("https://www.youtube.com/")
            continue
        elif "abrir navegador" in pedido:
            hablar_asistente("Estoy abriendo Google")
            webbrowser.open("https://www.goggle.es/")
            continue
        elif "qué día es hoy" in pedido:
            pedir_dia()
            continue
        elif "qué hora es" in pedido:
            pedir_hora()
            continue
        elif "chiste" in pedido:
            hablar_asistente(pyjokes.get_joke("es"))
        elif "precio de las acciones" in pedido:
            accion = pedido.split("de")[-1].strip()
            cartera = {"apple": "APPL",
                       "amazon": "AMZN",
                       "google": "GOOGL"}
            try:
                accion_buscada = cartera[accion]
                accion_buscada = yf.Ticker(accion_buscada)
                precio_actual = accion_buscada.info["regularMarketPrice"]
                hablar_asistente(f"La encontré, el precio de {accion} es {precio_actual}")
                continue
            except:
                hablar_asistente("Perdón, pero no la he encontrado")
                continue
        elif "adiós" in pedido:
            hablar_asistente("Ha sido un placer ayudarte, ¡Hasta la próxima!")
            break


centro_peticiones()
