from PIL import Image
import math


# --------------------------------------------------
# Algoritmo DDA (copiado de clase)
# --------------------------------------------------

def dda(pixels, x0, y0, x1, y1, color, ancho, alto):
    """Traza una línea usando el algoritmo DDA."""

    dx, dy = x1 - x0, y1 - y0
    pasos = max(abs(dx), abs(dy))

    if pasos == 0:
        return

    x_inc = dx / pasos
    y_inc = dy / pasos

    x = x0
    y = y0

    for _ in range(int(pasos) + 1):
        px, py = round(x), round(y)

        if 0 <= px < ancho and 0 <= py < alto:
            pixels[px, py] = color

        x += x_inc
        y += y_inc


# --------------------------------------------------
# Rectángulo
# --------------------------------------------------

def dibujar_rectangulo(pixels, x0, y0, x1, y1, color, ancho, alto):
    dda(pixels, x0, y0, x1, y0, color, ancho, alto)
    dda(pixels, x1, y0, x1, y1, color, ancho, alto)
    dda(pixels, x1, y1, x0, y1, color, ancho, alto)
    dda(pixels, x0, y1, x0, y0, color, ancho, alto)


# --------------------------------------------------
# Triángulo
# --------------------------------------------------

def dibujar_triangulo(pixels, p1, p2, p3, color, ancho, alto):
    dda(pixels, p1[0], p1[1], p2[0], p2[1], color, ancho, alto)
    dda(pixels, p2[0], p2[1], p3[0], p3[1], color, ancho, alto)
    dda(pixels, p3[0], p3[1], p1[0], p1[1], color, ancho, alto)


# --------------------------------------------------
# Puerta
# --------------------------------------------------

def dibujar_puerta(pixels, x0, y0, x1, y1, color, ancho, alto):
    dibujar_rectangulo(pixels, x0, y0, x1, y1, color, ancho, alto)


# --------------------------------------------------
# Ventana
# --------------------------------------------------

def dibujar_ventana(
    pixels,
    x0, y0,
    x1, y1,
    color_marco,
    color_division,
    ancho,
    alto
):

    dibujar_rectangulo(
        pixels,
        x0, y0,
        x1, y1,
        color_marco,
        ancho,
        alto
    )

    x_centro = (x0 + x1) // 2
    y_centro = (y0 + y1) // 2

    dda(
        pixels,
        x_centro, y0,
        x_centro, y1,
        color_division,
        ancho,
        alto
    )

    dda(
        pixels,
        x0, y_centro,
        x1, y_centro,
        color_division,
        ancho,
        alto
    )


# --------------------------------------------------
# Sol
# --------------------------------------------------

def dibujar_sol(
    pixels,
    cx,
    cy,
    radio,
    n_rayos,
    color,
    ancho,
    alto
):

    for i in range(n_rayos):

        angulo = i * 2 * math.pi / n_rayos

        x = cx + int(radio * math.cos(angulo))
        y = cy + int(radio * math.sin(angulo))

        dda(
            pixels,
            cx,
            cy,
            x,
            y,
            color,
            ancho,
            alto
        )


# --------------------------------------------------
# Nube
# --------------------------------------------------

def dibujar_nube(pixels, x, y, color, ancho, alto):

    dda(pixels, x, y, x + 20, y - 10, color, ancho, alto)
    dda(pixels, x + 20, y - 10, x + 40, y, color, ancho, alto)

    dda(pixels, x + 40, y, x + 60, y - 10, color, ancho, alto)
    dda(pixels, x + 60, y - 10, x + 80, y, color, ancho, alto)

    dda(pixels, x + 80, y, x, y, color, ancho, alto)


# --------------------------------------------------
# Flor
# --------------------------------------------------

def dibujar_flor(pixels, cx, cy, ancho_img, alto_img):

    # Tallo verde
    dda(
        pixels,
        cx,
        cy,
        cx,
        cy + 30,
        (0, 150, 0),
        ancho_img,
        alto_img
    )

    # Pétalos rosados
    for i in range(8):

        angulo = i * math.pi / 4

        x = cx + int(10 * math.cos(angulo))
        y = cy + int(10 * math.sin(angulo))

        dda(
            pixels,
            cx,
            cy,
            x,
            y,
            (255, 182, 193),
            ancho_img,
            alto_img
        )


# --------------------------------------------------
# Programa principal
# --------------------------------------------------

ancho = 600
alto = 500

imagen = Image.new("RGB", (ancho, alto), "white")
pixels = imagen.load()


# Piso
dda(
    pixels,
    50, 400,
    550, 400,
    (0, 150, 0),
    ancho,
    alto
)


# Casa
dibujar_rectangulo(
    pixels,
    180, 220,
    420, 400,
    (139, 69, 19),
    ancho,
    alto
)


# Techo
dibujar_triangulo(
    pixels,
    (180, 220),
    (300, 120),
    (420, 220),
    (200, 0, 0),
    ancho,
    alto
)


# Puerta
dibujar_puerta(
    pixels,
    260, 320,
    340, 400,
    (120, 60, 0),
    ancho,
    alto
)

# Picaporte de la puerta
dda(
pixels,
325, 360,
328, 360,
(80, 40, 0),
ancho,
alto
)


# Ventana izquierda
dibujar_ventana(
    pixels,
    210, 260,
    260, 310,
    (101, 67, 33),
    (120, 120, 120),
    ancho,
    alto
)


# Ventana derecha
dibujar_ventana(
    pixels,
    340, 260,
    390, 310,
    (101, 67, 33),
    (120, 120, 120),
    ancho,
    alto
)


# Sol
dibujar_sol(
    pixels,
    500,
    100,
    60,
    8,
    (255, 200, 0),
    ancho,
    alto
)


# Nubes
dibujar_nube(
    pixels,
    70,
    100,
    (135, 206, 235),
    ancho,
    alto
)

dibujar_nube(
    pixels,
    170,
    80,
    (135, 206, 235),
    ancho,
    alto
)


# Flores
dibujar_flor(
    pixels,
    120,
    370,
    ancho,
    alto
)

dibujar_flor(
    pixels,
    480,
    370,
    ancho,
    alto
)

dibujar_flor(
    pixels,
    530,
    370,
    ancho,
    alto
)


# Guardar imagen
imagen.save("casa.png")

print("Imagen generada: casa.png")