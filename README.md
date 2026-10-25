# Proyecto final: Máquina de Galton

**Curso:** Fundamentos de Python  
**Estudiante:** Emilia Reyes  
**Proyecto:** Simulación, procesamiento de datos, modularidad y gráfica.

## Objetivo

Simular el recorrido de 3,000 canicas por una Máquina de Galton de 12 niveles, registrar el contenedor final de cada canica y representar la distribución mediante un histograma.

## ¿Cómo funciona la Máquina de Galton?

Una Máquina de Galton tiene filas de clavijas. Al chocar con cada clavija, una canica puede desviarse a la izquierda o a la derecha. En este programa, cada decisión se representa con un valor aleatorio: `0` para izquierda y `1` para derecha. Después de 12 decisiones, la suma de los movimientos a la derecha determina el contenedor final, entre 0 y 12.

Al repetir el recorrido miles de veces, muchos resultados tienden a agruparse cerca de los contenedores centrales y menos canicas suelen llegar a los extremos. La distribución exacta cambia en cada ejecución porque las decisiones son aleatorias.

## Organización del código

- `simular_canica(niveles=12)`: simula una canica y devuelve el índice de su contenedor final.
- `simular_resultados(cantidad=3000, niveles=12)`: ejecuta la simulación para muchas canicas y guarda los resultados en una lista.
- `graficar_resultados(resultados, niveles=12)`: crea y guarda el histograma con título y etiquetas de los ejes.
- `main()`: coordina el programa, cuenta las frecuencias por contenedor e invoca la gráfica.

## Módulos utilizados

- `random`: permite elegir aleatoriamente la dirección de cada canica mediante `random.choice()`.
- `matplotlib.pyplot`: permite crear, etiquetar, guardar y mostrar el histograma.

## Cómo ejecutar el proyecto

1. Instala Python 3.
2. Abre una terminal en la carpeta donde están los archivos.
3. Instala la dependencia con:

   ```bash
   python -m pip install -r requirements.txt
   ```

4. Ejecuta el programa:

   ```bash
   python EMILIA_REYES_PROYECTOM3.py
   ```

El programa muestra el total de canicas y el conteo por contenedor. También guarda la gráfica como `histograma_canicas.png`.

## Histograma

La gráfica incluye:
- **Título:** Máquina de Galton: distribución de canicas.
- **Eje X:** Distribución de canicas.
- **Eje Y:** Cantidad de canicas.

## Reflexión: uso de funciones y módulos

Dividir el programa en funciones hace que el código sea más claro, organizado y fácil de probar. Cada función tiene una responsabilidad: simular una canica, repetir el proceso o representar los resultados. Esto evita concentrar toda la lógica en un solo bloque y facilita cambiar el número de canicas o de niveles.

Los módulos permiten reutilizar herramientas ya desarrolladas. `random` aporta las decisiones aleatorias y `matplotlib.pyplot` se encarga de la visualización, por lo que no es necesario programar estas capacidades desde cero. En conjunto, las funciones y los módulos hacen que el proyecto sea más mantenible y sencillo de ampliar.

## Archivos incluidos

- `EMILIA_REYES_PROYECTO3.py`: código principal.
- `README.md`: descripción, lógica, instrucciones y reflexión.
- `requirements.txt`: dependencia necesaria para generar la gráfica.

La imagen `histograma_canicas.png` se genera al ejecutar el programa.
