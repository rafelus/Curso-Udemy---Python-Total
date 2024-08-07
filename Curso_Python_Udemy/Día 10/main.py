import pygame
import random
import math
from pygame import mixer

# Inicializar Pygame
pygame.init()

# Crear la pantalla
pantalla = pygame.display.set_mode((1200, 800))

# Titulo e icono
pygame.display.set_caption("Invasión Imperio")
icono_juego = pygame.image.load("darthvader_87105.png")
pygame.display.set_icon(icono_juego)
fondo = pygame.image.load("starry-night-sky.jpg")

# Musica de fondo
mixer.music.load("Marcha Imperial.mp3")
mixer.music.set_volume(0.4)
mixer.music.play(-1)

# Variables del Jugador
img_jugador = pygame.image.load("Millenium_Falcon_-_02_35432.png")
jugador_x = 578
jugador_y = 0
jugador_x_cambio = 0
jugador_y_cambio = 0

# Variables enemigo
img_enemigo = []
enemigo_x = []
enemigo_y = []
enemigo_x_cambio = []
enemigo_y_cambio = []
cantidad_enemigos = 15

# Variables cantidad enemigos
for e in range(cantidad_enemigos):
    img_enemigo.append(pygame.image.load("Tie_Fighter_-_03_35417.png"))
    enemigo_x.append(random.randint(0, 1136))
    enemigo_y.append(random.randint(700, 746))
    enemigo_x_cambio.append(0.5)
    enemigo_y_cambio.append(-50)

# Variables bala
img_bala = pygame.image.load("bala.png")
bala_x = 0
bala_y = 0
bala_x_cambio = 0
bala_y_cambio = 1
bala_visible = False
cantidad_balas = 3

# Variable puntuación
puntuacion = 0
fuente = pygame.font.Font("STJEDISE.ttf", 20)
texto_x = 10
texto_y = 10

# Texto final juego
fuente_final = pygame.font.Font("STJEDISE.ttf", 35)


def texto_final_juego():
    texto_final = fuente_final.render("juego terminado", True, (255, 255, 255))
    texto = fuente.render(f"Naves destruidas : {puntuacion}", True, (255, 255, 255))
    pantalla.blit(texto_final, (425, 150))
    pantalla.blit(texto, (490, 200))


def mostrar_puntuacion(x, y):
    texto = fuente.render(f"Naves destruidas : {puntuacion}", True, (255, 255, 255))
    pantalla.blit(texto, (x, y))


# Funcion jugador
def jugador(x, y):
    pantalla.blit(img_jugador, (x, y))


# Funcion enemigo
def enemigo(x, y, enem):
    pantalla.blit(img_enemigo[enem], (x, y))


def dispara_bala(x, y):
    global bala_visible
    bala_visible = True
    pantalla.blit(img_bala, (x + 16, y + 10))


# Funcion detectar colisiones
def compr_colision_disparo(x_enemigo, y_enemigo, x_bala, y_bala):
    distancia = math.sqrt(math.pow(x_enemigo - x_bala, 2) + math.pow(y_enemigo - y_bala, 2))
    if distancia < 27:
        soni_enem_expl = mixer.Sound("enemigo_explosion.wav")
        soni_enem_expl.set_volume(0.2)
        soni_enem_expl.play()
        return True
    else:
        return False


# Loop del juego
se_ejecuta = True
while se_ejecuta:

    # RGB
    pantalla.blit(fondo, (0, 0))

    # Iterar eventos
    for evento in pygame.event.get():

        # Evento cerrar el juego
        if evento.type is pygame.QUIT:
            se_ejecuta = False

        # Evento si se pulsa una direccón
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                jugador_x_cambio = -0.3
            if evento.key == pygame.K_RIGHT:
                jugador_x_cambio = +0.3
            if evento.key == pygame.K_UP:
                jugador_y_cambio = -0.3
            if evento.key == pygame.K_DOWN:
                jugador_y_cambio = +0.3
            if evento.key == pygame.K_SPACE:
                if not bala_visible:
                    sonido_disparo = mixer.Sound("disparo.wav")
                    sonido_disparo.set_volume(0.2)
                    sonido_disparo.play()
                    bala_y = jugador_y
                    bala_x = jugador_x
                    dispara_bala(bala_x, bala_y)

        # Evento soltar dirección
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0
            if evento.key == pygame.K_UP or evento.key == pygame.K_DOWN:
                jugador_y_cambio = 0

    # Evento mover jugador
    jugador_x += jugador_x_cambio
    jugador_y += jugador_y_cambio

    # Evento limites de movimiento jugador
    if jugador_x <= 0:
        jugador_x = 0
    if jugador_x >= 1136:
        jugador_x = 1136
    if jugador_y <= 0:
        jugador_y = 0
    if jugador_y >= 500:
        jugador_y = 500

    # Evento mover enemigo
    for e in range(cantidad_enemigos):
        # Fin del juego
        if enemigo_y[e] <= 0:
            for nave in range(cantidad_enemigos):
                enemigo_y[nave] = -100
                jugador_x = 578
                jugador_y = 0
            texto_final_juego()
            break

        enemigo_x[e] += enemigo_x_cambio[e]

        # Evento limites de movimiento enemigo y movimiento automatico
        if enemigo_x[e] <= 0:
            enemigo_x_cambio[e] = 0.3
            enemigo_y[e] += enemigo_y_cambio[e]
        if enemigo_x[e] >= 1136:
            enemigo_x_cambio[e] = -0.3
            enemigo_y[e] += enemigo_y_cambio[e]

    # Movimiento bala
    if bala_y > 746:
        bala_y = jugador_y
        bala_visible = False
    if bala_visible:
        dispara_bala(bala_x, bala_y)
        bala_y += bala_y_cambio

    # Verificacion colision
    for e in range(cantidad_enemigos):
        colision = compr_colision_disparo(enemigo_x[e], enemigo_y[e], bala_x, bala_y)
        if colision:
            bala_y = jugador_y
            bala_x = jugador_x
            bala_visible = False
            puntuacion += 1
            enemigo_x[e] = random.randint(0, 1136)
            enemigo_y[e] = random.randint(700, 746)

    jugador(jugador_x, jugador_y)
    for e in range(cantidad_enemigos):
        enemigo(enemigo_x[e], enemigo_y[e], e)
    mostrar_puntuacion(texto_x, texto_y)

    # Actualizar
    pygame.display.update()
