import pygame
import time
from render import draw_graph
from generation import generate_random_points, generate_hamiltonian_cycle, generate_distance_matrix
from optimization import simulated_annealing_step

# Configuracion de Pygame
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TSP")

# Generacion de puntos y aristas
## Lista de puntos (x, y)
points = generate_random_points(50, WIDTH, HEIGHT)
## Lista de aristas (índices de los puntos que conectan)
edges = generate_hamiltonian_cycle(points)
## Matriz de distancias entre los puntos
distance_matrix = generate_distance_matrix(points)

# Parametros
## Temperatura inicial
T = 500
## Factor de enfriamiento
cf = 0.9998

# Bucle principal
running = True
iter = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Actualizar aristas
    edges, T = simulated_annealing_step(points,edges,T,cf,distance_matrix)

    # Dibujar el grafo
    if iter % 100 == 0:
        draw_graph(screen, points, edges, T)

    if T < 0.005:
        running = False

    iter+=1


draw_graph(screen, points, edges, T, final=True)
time.sleep(5)
# Terminar el programa
pygame.quit()