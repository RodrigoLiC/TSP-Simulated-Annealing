import random
import math
from numpy import linspace

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

def generate_uniform(num_points_x: int, num_points_y: int, width: int, height: int, margin: float = 0.8) -> list[Point]:
    """
    Generar una malla de puntos uniformemente distribuidos
    \n
    :param num_points_x: Número de puntos en el eje x.
    :param num_points_y: Número de puntos en el eje y.
    :param width: Ancho del área.
    :param height: Altura del área.
    :param margin: factor del tamaño del cuadrado para no tocar los bordes.
    :return: Lista de puntos (x, y).
    """
    square_size = min(width, height)*margin
    offset_x = (width - square_size) // 2
    offset_y = (height - square_size) // 2
    x_points = linspace(offset_x, offset_x + square_size, num_points_x)
    y_points = linspace(offset_y, offset_y + square_size, num_points_y)
    points = [(x, y) for x in x_points for y in y_points]
    return points

def import_points_and_matrix():
    """
    Importa los puntos y la matriz de distancias desde los archivos 'points.txt' y 'matrix.txt'.
    \n
    :return: Una tupla con la lista de puntos y la matriz de distancias.
    """
    points = []
    distance_matrix = []
    with open('points.txt', 'r') as file:
        for line in file:
            x, y = map(float, line.strip().split())
            points.append((x, y))
    
    with open('matrix.txt', 'r') as file:
        for line in file:
            row = list(map(float, line.strip().split()))
            distance_matrix.append(row)
    
    return points, distance_matrix


def export_points_and_matrix(points: list[Point], distance_matrix: list[list[float]]):
    """
    Exporta los puntos y la matriz de distancias a los archivos 'points.txt' y 'matrix.txt'.
    \n
    :param points: Lista de puntos (x, y).
    :param distance_matrix: Matriz de distancias entre los puntos.
    """
    with open('points.txt', 'w') as file:
        for point in points:
            # Escribir cada punto como una línea con formato 'x y'
            file.write(f"{point[0]} {point[1]}\n")
    
    with open('matrix.txt', 'w') as file:
        for row in distance_matrix:
            # Escribir cada fila de la matriz, separando los valores por espacio
            file.write(" ".join(f"{dist:.2f}" for dist in row) + "\n")