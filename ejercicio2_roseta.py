from PIL import Image
import math

# Implementacion del algoritmo de Bresenham

# Funcion Bresenham para dibujar lineas
def bresenham(pixels, x0, y0, x1, y1, color, ancho, alto):
    """Bresenham generalizado."""

    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    sx = 1 if x0 < x1 else -1
    sy = 1 if y0 < y1 else -1
    err = dx - dy
    x = x0
    y = y0

    while True:
        if 0 <= x < ancho and 0 <= y < alto:
            pixels[x, y] = color
        if x == x1 and y == y1:
            break
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x += sx
        if e2 < dx:
            err += dx
            y += sy

# Genera puntos equiespaciados sobre una circunferencia

def generar_puntos_circulo(cx, cy, radio, n):

    puntos = []

    for i in range(n):

        angulo = 2 * math.pi * i / n
        x = cx + int(radio * math.cos(angulo))
        y = cy + int(radio * math.sin(angulo))

        puntos.append((x, y))
    return puntos

# Dibuja la roseta conectando todos los puntos

def dibujar_roseta(pixels, puntos, ancho, alto):
    n = len(puntos)

    for i in range(n):
        for j in range(i + 1, n):

            # Gradiente de color
            r = (i * 20) % 256
            g = (j * 10) % 256
            b = ((i + j) * 15) % 256
            color = (r, g, b)

            bresenham(
                pixels,
                puntos[i][0],
                puntos[i][1],
                puntos[j][0],
                puntos[j][1],
                color,
                ancho,
                alto
            )


# Programa principal

ancho = 700
alto = 700

for n in [12, 24, 36]:

    imagen = Image.new("RGB", (ancho, alto), "white")
    pixels = imagen.load()
    puntos = generar_puntos_circulo(
        350,
        350,
        300,
        n
    )

    dibujar_roseta(
        pixels,
        puntos,
        ancho,
        alto
    )

#crear el nombre del archivo con el numero de puntos en la roseta
    nombre_archivo = f"roseta_{n}.png"

# Guardar imagen
    imagen.save(nombre_archivo)
    print(f"Imagen generada: {nombre_archivo}")