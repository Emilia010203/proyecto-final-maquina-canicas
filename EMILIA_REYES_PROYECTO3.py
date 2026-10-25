"""
Proyecto final: Simulación de una máquina de canicas.
Fundamentos de Python - Camp
"""

import random
import matplotlib.pyplot as plt


def simular_canica(niveles=12):
    """
    Simula el recorrido de una canica por la máquina.

    Args:
        niveles (int): Número de decisiones izquierda/derecha.

    Returns:
        int: Índice del contenedor final, comenzando en cero.
    """
    contenedor = 0

    # Cada decisión hacia la derecha avanza un contenedor.
    for _ in range(niveles):
        direccion = random.choice([0, 1])
        contenedor += direccion

    return contenedor


def simular_resultados(cantidad=3000, niveles=12):
    """
    Ejecuta múltiples simulaciones de canicas.

    Args:
        cantidad (int): Número de canicas que se simularán.
        niveles (int): Número de niveles de la máquina.

    Returns:
        list: Contenedores finales de todas las canicas.
    """
    resultados = []

    for _ in range(cantidad):
        resultado = simular_canica(niveles)
        resultados.append(resultado)

    return resultados


def graficar_resultados(resultados, niveles=12):
    """
    Genera un histograma de los contenedores finales.

    Args:
        resultados (list): Resultados de las simulaciones.
        niveles (int): Número de niveles de la máquina.
    """
    contenedores = list(range(niveles + 1))

    plt.figure(figsize=(10, 6))
    plt.hist(
        resultados,
        bins=[i - 0.5 for i in range(niveles + 2)],
        edgecolor="black",
        rwidth=0.9
    )

    plt.xticks(contenedores)
    plt.title("Distribución de canicas")
    plt.xlabel("Distribución de canicas")
    plt.ylabel("Cantidad de canicas")
    plt.grid(axis="y", alpha=0.3)
    plt.tight_layout()
    plt.savefig("histograma_canicas.png", dpi=300)
    plt.show()


def main():
    """Coordina la simulación, el conteo y la gráfica."""
    cantidad_canicas = 3000
    niveles = 12

    resultados = simular_resultados(cantidad_canicas, niveles)

    print("SIMULACIÓN DE LA MÁQUINA DE CANICAS")
    print(f"Total de canicas simuladas: {len(resultados)}")

    # Cuenta cuántas canicas terminaron en cada contenedor.
    frecuencias = [0] * (niveles + 1)

    for contenedor in resultados:
        frecuencias[contenedor] += 1

    for contenedor, cantidad in enumerate(frecuencias):
        print(f"Contenedor {contenedor}: {cantidad} canicas")

    graficar_resultados(resultados, niveles)


if __name__ == "__main__":
    main()
