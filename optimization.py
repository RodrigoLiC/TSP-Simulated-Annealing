import random
import math
from typing import List, Tuple

Point = Tuple[int, int]
Edge = Tuple[int, int]

def distance(p1: Point, p2: Point) -> float:
    """
    Calcula la distancia entre dos puntos.
    """
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def total_path_length(points: List[Point], edges: List[Edge]) -> float:
    """
    Calcula la longitud total del ciclo.
    """
    return sum(distance(points[edge[0]], points[edge[1]]) for edge in edges)

def isValid(edges: List[Edge]) -> bool:
    """
    Verifica si es un ciclo hamiltoniano.
    """
    n = len(edges)
    visited = [False] * n
    current = edges[0][0]  # Empezar desde el primer nodo de la primera arista
    start_node = current   # Guardar el nodo inicial para verificar el cierre del ciclo

    # Marcar el nodo inicial como visitado
    visited[current] = True
    edge_count = 0

    maxiter = 0
    while edge_count < n and maxiter < n:
        maxiter += 1
        for edge in edges:
            if edge[0] == current and not visited[edge[1]]:
                current = edge[1]
                visited[current] = True
                edge_count += 1
                break
            elif edge[1] == current and not visited[edge[0]]:
                current = edge[0]
                visited[current] = True
                edge_count += 1
                break
    # Verificar que hemos visitado todos los nodos
    return all(visited)

def two_opt_swap(edges: List[Edge]) -> List[Edge]:
    """
    Realiza un intercambio 2-opt, y verifica que el resultado sea un ciclo hamiltoniano.
    """
    # Seleccionar dos aristas aleatorias que no compartan vertices
    verts = 0
    while verts < 4:
        i, j = random.sample(range(len(edges)), 2)
        verts = len(set([edges[i][0],edges[i][1],edges[j][0],edges[j][1]]))

    # Obtener las aristas seleccionadas
    edge1 = edges[i]
    edge2 = edges[j]

    new_edges1 = edges.copy()
    new_edges2 = edges.copy()
    # Intercambiar puntos (A-B C-D) -> (A-D C-B) o (A-C B-D)
    new_edges1[i] = (edge1[0], edge2[1])
    new_edges1[j] = (edge2[0], edge1[1])
    new_edges2[i] = (edge1[0], edge2[0])
    new_edges2[j] = (edge1[1], edge2[1])

    if isValid(new_edges1):
        return new_edges1
    else:
        return new_edges2
    

def simulated_annealing_step(points: List[Point], edges: List[Edge], T: float, cooling_factor: float) -> Tuple[List[Edge], float]:
    """
    Realiza un paso del algoritmo de Simulated Annealing utilizando 2-opt.

    :param points: Lista de puntos (x, y).
    :param edges: Lista de aristas (índices de puntos).
    :param T: Temperatura actual del algoritmo.
    :return: Una tupla con la lista de aristas optimizada y la nueva temperatura.
    """
    current_edges = edges[:]
    current_length = total_path_length(points, current_edges)

    # Generar un nuevo estado usando 2-opt
    new_edges = two_opt_swap(current_edges)
    new_length = total_path_length(points, new_edges)

    # Calcular la diferencia de longitud
    delta_length = new_length - current_length

    # Decidir si aceptamos el nuevo estado
    if delta_length < 0 or random.random() < math.exp(-delta_length / T):
        current_edges = new_edges
        current_length = new_length
        print(f"Mejora encontrada: ΔL = {delta_length:.2f}, Nueva longitud = {current_length:.2f}")

    # Reducir la temperatura
    T *= cooling_factor

    return current_edges, T