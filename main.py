import pygame
import time
from draw import draw_graph
from generation import generate_random_points, generate_hamiltonian_cycle
from optimization import simulated_annealing_step

# Configuracion de pygame
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TSP")

# Generacion de puntos y aristas
## Lista de puntos (x, y)
points = generate_random_points(20, WIDTH, HEIGHT)
## Lista de aristas (índices de los puntos que conectan)
edges = generate_hamiltonian_cycle(points)

# Parametros
## Temperatura inicial
T = 1000
## Factor de enfriamiento
cf = 0.99

# Bucle principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Actualizar aristas
    edges, T = simulated_annealing_step(points,edges,T,cf)

    # Dibujar el grafo
    draw_graph(screen, points, edges, T)

    if T < 0.005:
        running = False

    # Esperar
    time.sleep(0.005)


draw_graph(screen, points, edges, T, final=True)
time.sleep(5)
# Terminar el programa
pygame.quit()