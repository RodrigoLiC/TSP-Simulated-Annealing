import random
import math
from collections import defaultdict

Point = tuple[int, int]
Edge = tuple[int, int]

def total_path_length(points: list[Point], edges: list[Edge], distanceMatrix:  list[list[float]]) -> float:
    """
    Calcula la longitud total del ciclo.
    """
    return sum(distanceMatrix[u][v] for u, v in edges)

def isValid(edges: list[Edge]) -> bool:
    """
    Verifica si es un ciclo hamiltoniano.
    """
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited = set()
    stack = [edges[0][0]]

    while stack:
        node = stack.pop()
        if node in visited:
            continue
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                stack.append(neighbor)

    # Verificamos si todos los nodos fueron visitados
    return len(visited) == len(edges)

def two_opt_swap(edges: list[Edge]) -> list[Edge]:
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

    new_edges1 = edges[:]
    new_edges2 = edges[:]
    # Intercambiar puntos (A-B C-D) -> (A-D C-B) o (A-C B-D)
    new_edges1[i] = (edge1[0], edge2[1])
    new_edges1[j] = (edge2[0], edge1[1])
    new_edges2[i] = (edge1[0], edge2[0])
    new_edges2[j] = (edge1[1], edge2[1])

    if isValid(new_edges1):
        return new_edges1
    else:
        return new_edges2
    

def simulated_annealing_step(points: list[Point], edges: list[Edge], temp: float, cooling_factor: float, distanceMatrix: list[list[float]]) -> tuple[list[Edge], float]:
    """
    Realiza un paso del algoritmo de Simulated Annealing utilizando 2-opt.
    \n
    :param points: Lista de puntos (x, y).
    :param edges: Lista de aristas (índices de puntos).
    :param T: Temperatura actual del algoritmo.
    :return: Una tupla con la lista de aristas optimizada y la nueva temperatura.
    """
    current_edges = edges[:]
    current_length = total_path_length(points, current_edges, distanceMatrix)

    # Generar un nuevo estado usando 2-opt
    new_edges = two_opt_swap(current_edges)
    
    new_length = total_path_length(points, new_edges, distanceMatrix)

    # Calcular la diferencia de longitud
    delta_length = new_length - current_length

    # Decidir si aceptamos el nuevo estado
    if delta_length < 0 or random.random() < math.exp(-delta_length / temp):
        current_edges = new_edges
        current_length = new_length
        print(f"Mejora encontrada: ΔL = {delta_length:.2f}, Nueva longitud = {current_length:.2f}")

    # Reducir la temperatura
    temp *= cooling_factor

    return current_edges, temp, current_length