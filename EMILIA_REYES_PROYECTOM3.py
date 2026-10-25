"""
Proyecto final: Máquina de Galton.
Fundamentos de Python - Camp
"""
import random
import matplotlib.pyplot as plt


def simular_canica(niveles=12):
    """Simula una canica y devuelve el índice de su contenedor final."""
    contenedor = 0
    # En cada nivel, 0 representa izquierda y 1 representa derecha.
    for _ in range(niveles):
        contenedor += random.choice([0, 1])
    return contenedor


def simular_resultados(cantidad=3000, niveles=12):
    """Simula varias canicas y devuelve sus contenedores finales en una lista."""
    resultados = []
    # Repite la simulación y guarda el resultado de cada canica.
    for _ in range(cantidad):
        resultados.append(simular_canica(niveles))
    return resultados


def graficar_resultados(resultados, niveles=12):
    """Crea y guarda un histograma de la distribución de las canicas."""
    # Cada número entero representa un contenedor de la máquina.
    contenedores = list(range(niveles + 1))
    limites = [i - 0.5 for i in range(niveles + 2)]

    # Dibuja el histograma y añade título y nombres de los ejes.
    plt.figure(figsize=(10, 6))
    plt.hist(resultados, bins=limites, edgecolor="black", rwidth=0.9)
    plt.xticks(contenedores)
    plt.title("Máquina de Galton: distribución de canicas")
    plt.xlabel("Distribución de canicas")
    plt.ylabel("Cantidad de canicas")
    plt.grid(axis="y", alpha=0.3)
    plt.tight_layout()

    # Guarda una copia de la gráfica y la muestra en pantalla.
    plt.savefig("histograma_canicas.png", dpi=300)
    plt.show()


def main():
    """Coordina la simulación, el conteo y la creación del histograma."""
    cantidad_canicas = 3000
    niveles = 12

    # Simula las canicas y muestra el total procesado.
    resultados = simular_resultados(cantidad_canicas, niveles)
    print("SIMULACIÓN DE LA MÁQUINA DE GALTON")
    print(f"Total de canicas simuladas: {len(resultados)}")

    # Cuenta cuántas canicas terminaron en cada contenedor.
    frecuencias = [0] * (niveles + 1)
    for contenedor in resultados:
        frecuencias[contenedor] += 1

    # Muestra las frecuencias y genera el histograma.
    for contenedor, cantidad in enumerate(frecuencias):
        print(f"Contenedor {contenedor}: {cantidad} canicas")
    graficar_resultados(resultados, niveles)


if __name__ == "__main__":
    main()
