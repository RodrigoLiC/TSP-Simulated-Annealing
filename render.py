import pygame

# Configuracion de pygame
pygame.init()

# Definiciones
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
Point = tuple[int, int]
Edge = tuple[int, int]
FONT = pygame.font.Font(None, 36)

def draw_graph(screen: pygame.Surface, points: list[Point], edges: list[Edge], temperatura: float, final = False) -> None:
    """
    Dibuja el grafo en la pantalla.
    \n
    :param screen: Superficie de Pygame donde se dibujará el grafo.
    :param points: Lista de puntos, cada uno representado como una tupla (x, y).
    :param edges: Lista de aristas, cada una representada como una tupla de los índices de los puntos conectados.
    :param temperatura: Temperatura actual del algoritmo.
    :return: None
    """
    # Vaciar la pantalla (rellenar de blanco)
    screen.fill(WHITE)
    # Dibujar aristas (líneas rojas)
    color = BLUE if final else RED
    for edge in edges:
        start_point = points[edge[0]]
        end_point = points[edge[1]]
        pygame.draw.line(screen, color, start_point, end_point, 3)

    # Dibujar puntos (círculos negros)
    for point in points:
        pygame.draw.circle(screen, BLACK, point, 8)

    # Configurar fuente y renderizar la temperatura
    text_surface = FONT.render(f"Temperature: {temperatura:.2f}", True, BLACK)
    
    # Obtener el tamaño de la pantalla y colocar el texto en la esquina inferior izquierda
    screen_height = screen.get_height()
    screen.blit(text_surface, (10, screen_height - text_surface.get_height() - 10))
    
    # Actualizar la pantalla
    pygame.display.flip()