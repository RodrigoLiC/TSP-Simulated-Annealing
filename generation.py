import random
from typing import List, Tuple

# Tipo para los puntos (coordenadas x, y)
Point = Tuple[int, int]
Edge = Tuple[int, int]

def generate_random_points(num_points: int, width: int, height: int) -> List[Point]:
    """
    Genera una lista de puntos aleatorios dentro de las dimensiones especificadas.
    \n
    :param num_points: Número de puntos a generar.
    :param width: Ancho máximo del área.
    :param height: Altura máxima del área.
    :return: Lista de puntos (x, y).
    """
    points = [(random.randint(0, width), random.randint(0, height)) for _ in range(num_points)]
    return points

def generate_hamiltonian_cycle(points: List[Point]) -> List[Edge]:
    """
    Genera un ciclo hamiltoniano aleatorio para una lista de puntos.
    \n
    :param points: Lista de puntos, cada uno representado como una tupla (x, y).
    :return: Lista de aristas, cada una representada como una tupla de los índices de los puntos conectados.
    """
    # Crear una lista de índices de los puntos en orden aleatorio
    indices = list(range(len(points)))
    random.shuffle(indices)

    # Crear el ciclo hamiltoniano conectando los puntos en orden aleatorio
    edges = [(indices[i], indices[(i + 1) % len(indices)]) for i in range(len(indices))]
    return edges