import random
import math

# Tipo para los puntos (coordenadas x, y)
Point = tuple[int, int]
Edge = tuple[int, int]

def generate_random_points(num_points: int, width: int, height: int) -> list[Point]:
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

def generate_hamiltonian_cycle(points: list[Point]) -> list[Edge]:
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

def generate_distance_matrix(points: list[Point]) -> list[list[float]]:
    """
    Genera una matriz de distancias entre cada par de puntos utilizando la fórmula de la distancia euclidiana.
    \n
    :param points: Lista de puntos, cada uno representado como una tupla (x, y).
    :return: Una matriz de distancias donde cada elemento [i][j] representa la distancia entre los puntos i y j.
    """
    num_points = len(points)
    distance_matrix = []

    for i in range(num_points):
        row = []
        for j in range(num_points):
            if i == j:
                row.append(0.0)
            else:
                x1, y1 = points[i]
                x2, y2 = points[j]
                # Calcular la distancia euclidiana
                distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
                row.append(distance)
        distance_matrix.append(row)
    
    return distance_matrix