import pygame, random
from pygame.locals import *

#Inicio de Pygame
pygame.init()

#Tamaño pantalla, fps, fuente de letra, titulo e icono del juego
W, H = 500, 500
Pantalla = pygame.display.set_mode((W, H))
Reloj = pygame.time.Clock()
fuente = pygame.font.Font(None, 30)
pygame.display.set_caption("Snake Game")
icono = pygame.image.load("Imagenes/icono.png")
pygame.display.set_icon(icono)

#Creacion de posicion de la manzana
def comida():
    random_pos = random.randint(5,45)*10
    manzana_pos = [random_pos,random_pos]
    return manzana_pos

#Creacion de pantalla de juego
def IniciarPantalla(score):
    #Color de fondo
    Pantalla.fill((0, 128, 0))
    #Linea de arriba
    pygame.draw.line(Pantalla, (0, 0, 0), (0, 0), (500, 0), 75)
    #Linea de abajo
    pygame.draw.line(Pantalla, (0, 0, 0), (0, 500), (500, 500), 75)
    #Linea de derecha
    pygame.draw.line(Pantalla, (0, 0, 0), (500, 0), (500, 500), 75)
    #Linea de izquierda
    pygame.draw.line(Pantalla, (0, 0, 0), (0, 0), (0, 500), 75)
    #Nombre del juego
    nombre = fuente.render("Snake Game", 0, (255, 0, 0))
    Pantalla.blit(nombre, (25, 10))
    #Puntuacion
    pygame.draw.rect(Pantalla,(250,250,250),(350, 10, 100, 20))
    text = fuente.render(("Score: " + str(score)),0,(255,0,0))
    Pantalla.blit(text, (350,10))

#Movimiento y muerte de la serpiente
def snake(move,snake_body,snake_pos):
    if move == "Right":
        snake_pos[0] += 10
    elif move == "Left":
        snake_pos[0] -= 10
    elif move == "Up":
        snake_pos[1] -= 10
    elif move == "Down":
        snake_pos[1] += 10

    if snake_pos[0] <= 30 or snake_pos[0] >= 460:
        pygame.quit()
    elif snake_pos[1] <= 30 or snake_pos[1] >= 460:
        pygame.quit()

    for n in snake_body:
        if snake_pos == n:
            pygame.quit()

#Metodo main
def main():
    juego = True
    snake_pos = [100, 100]
    snake_body = [[100, 100], [90, 100], [80, 100]]
    manzana_pos = comida()
    move = "Right"
    score = 0

    #Inicio del juego
    while juego:
        for event in pygame.event.get():
            if event.type == QUIT:
                juego = False

        #Asignacion de teclas
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_RIGHT]:
            move = "Right"
        elif teclas[pygame.K_LEFT]:
            move = "Left"
        elif teclas[pygame.K_UP]:
            move = "Up"
        elif teclas[pygame.K_DOWN]:
            move = "Down"

        #LLamamiento de la serpiente
        snake(move, snake_body, snake_pos)

        #Crecimiento de la serpiente
        snake_body.insert(0, list(snake_pos))
        if snake_pos == manzana_pos:
            manzana_pos = comida()
            score += 1
        else:
            snake_body.pop()

        #Llamada de la funcion Iniciar Pantalla
        IniciarPantalla(score)

        #Dibujo de la serpiente
        for block in snake_body:
            pygame.draw.rect(Pantalla, (0,0,255), (block[0], block[1], 10, 10))

        #Dibujo de la manzana
        pygame.draw.rect(Pantalla,(255,0,0), (manzana_pos[0], manzana_pos[1],10,10))

        #Diseño de niveles
        if score <= 10:
            Reloj.tick(10)
        elif 10 < score <= 30:
            Reloj.tick(20)
        elif score > 30:
            Reloj.tick(30)

        pygame.display.flip()
        pygame.display.update()

main()