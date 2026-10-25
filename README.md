# Proyecto final: Máquina de canicas

**Curso:** Fundamentos de Python  
**Tema:** Simulación, procesamiento de datos, modularidad y graficación.

## Descripción

Este proyecto simula el recorrido de 3,000 canicas por una máquina con 12 niveles. En cada nivel, cada canica toma aleatoriamente una decisión hacia la izquierda o hacia la derecha. El programa registra el contenedor final, cuenta las frecuencias y genera un histograma.

## Archivos

- `EMILIA_REYES_proyecto3.py`: código principal del proyecto.
- `requirements.txt`: dependencia necesaria para la gráfica.
- `histograma_canicas.png`: se genera al ejecutar el programa.

## Requisitos

- Python 3
- matplotlib

Instala la dependencia con:

```bash
python -m pip install -r requirements.txt
```

## Cómo ejecutar

Desde una terminal abierta en la carpeta del proyecto:

```bash
python EMILIA_REYES_proyecto3.py
```

## Funciones

- `simular_canica(niveles=12)`: simula una canica y devuelve su contenedor final.
- `simular_resultados(cantidad=3000, niveles=12)`: ejecuta las simulaciones y devuelve una lista con los resultados.
- `graficar_resultados(resultados, niveles=12)`: crea y guarda el histograma.
- `main()`: coordina el proceso completo.

## Resultado esperado

El programa muestra en la terminal el total de 3,000 canicas y el número de canicas que terminó en cada contenedor. También crea `histograma_canicas.png`.

Los resultados pueden variar entre ejecuciones porque las decisiones son aleatorias.

