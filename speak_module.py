import pyttsx3

engine = pyttsx3.init()

def hablar(texto):
    engine.say(texto)
    engine.runAndWait()

def cambiar_velocidad(velocidad):
    engine.setProperty("rate", velocidad)

def cambiar_volumen(volumen):
    # Entre 0.0 y 1.0
    engine.setProperty("volume", volumen)

def listar_voces():
    voces = engine.getProperty("voices")
    for i, voz in enumerate(voces):
        print(f"{i}: {voz.name}")

def cambiar_voz(indice):
    voces = engine.getProperty("voices")
    engine.setProperty("voice", voces[indice].id)

def guardar_audio(texto, archivo):
    engine.save_to_file(texto, archivo)
    engine.runAndWait()