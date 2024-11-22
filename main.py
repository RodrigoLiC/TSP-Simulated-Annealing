import pygame
import time
import matplotlib.pyplot as plt
import numpy as np
import keyboard
from render import draw_graph
from generation import *
from optimization import simulated_annealing_step

# Configuracion de Pygame
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TSP")

# Generacion de puntos y aristas
## Lista de puntos (x, y)
'''points = generate_random_points(30, WIDTH, HEIGHT)
points = generate_uniform(10, 10, WIDTH, HEIGHT)
## Matriz de distancias entre los puntos
distance_matrix = generate_distance_matrix(points)
## Lista de aristas (índices de los puntos que conectan)
export_points_and_matrix(points, distance_matrix)'''

points, distance_matrix = import_points_and_matrix()
edges = generate_hamiltonian_cycle(points)

# Parametros
## Temperatura inicial
temp = 400
## Factor de enfriamiento
cf = 0.9998

# Bucle principal
running = True
iter = 0
costs = []
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Actualizar aristas
    edges, temp, cost = simulated_annealing_step(points,edges,temp,cf,distance_matrix)
    costs.append(cost)

    # Dibujar el grafo
    if iter % 100 == 0:
        draw_graph(screen, points, edges, temp)

    if temp < 0.005:
        running = False

    iter+=1



iteraciones = np.arange(1, len(costs) + 1)
plt.plot(iteraciones, costs, linestyle='-', color='b', label='Distancia')
plt.xlabel('Iteraciones')
plt.ylabel('Distancia de la ruta')
plt.title('Evolucion de la ruta con 30 destinos')
plt.legend()
plt.grid(True)
plt.show()


time.sleep(3)
draw_graph(screen, points, edges, temp, final=True)
time.sleep(1)
# Terminar el programa
pygame.quit()