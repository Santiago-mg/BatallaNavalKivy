# BATALLA NAVAL

Este proyecto implementa el juego de Batalla Naval en Python. Consiste en un tablero de 10x10 celdas en el que se colocan barcos de diferentes tamaños y los jugadores intentan adivinar la ubicación de los barcos oponentes para hundirlos.

## Descripción del código

El código proporcionado consta de dos archivos principales:

### main.py 
Este archivo contiene la implementación del juego de Batalla Naval. Aquí se define la clase TableroBatallaNaval, que representa el tablero de juego y contiene métodos para colocar barcos, disparar y verificar el estado del tablero. Además, se definen excepciones personalizadas relacionadas con el juego.

### pruebas.py
Este archivo contiene pruebas unitarias para validar el funcionamiento del juego. Se utilizan las bibliotecas unittest y main para realizar las pruebas en la clase TableroBatallaNaval.

### Interfazz.py 
interfaz.py proporciona una experiencia interactiva para jugar al clásico juego de Batalla Naval en una interfaz gráfica de usuario.

## Funcionalidades principales 

### Colocar Naves: 
El método colocar_naves() de la clase TableroBatallaNaval coloca aleatoriamente barcos de diferentes tamaños en el tablero. 

### Disparar: 
El método disparar() permite al jugador disparar a una posición específica del tablero y determina si hubo un impacto en un barco o si fue un disparo al agua. 

### Imprimir Tablero: 
El método imprimir_tablero() muestra en la consola el estado actual del tablero. 

### Validaciones: 
Se realizan validaciones para verificar que las coordenadas de disparo estén dentro del rango válido y que no se dispare dos veces en la misma posición.

### Random: 
Utilizada para la generación de números aleatorios. colorama: Utilizada para imprimir texto con colores en la consola. Para instalar las dependencias, puedes utilizar el siguiente comando:

## Requisitos del sistema
Asegurate de tener instaladas las bibliotecas de colorama y kivy. Si no las tienes instaladas puedes ejecutar el siguiente codigo en la terminal de python: pip install colorama pip install kivy

## Instrucciones de Instalación
1. Abre una terminal(preferiblemente git bash)y clona el repositorio usando: `https://github.com/Santiago-mg/BatallaNavalKivy.git` .
2. Cambia/parate a la carpeta src usando: `cd BatallaNavalKivy/src`.

### Interfaz grafica

1. Cambia al directorio de interfaz usando: `cd Intefaz` .
2. Ejectuta el archivo usando: `py interfazz.py` .
3. Si deseas devolverte usa: `cd ..`

### Consola

1. Cambia al directorio de consola usando: `cd Batalla` .
2. Ejectuta el archivo usando: `py Juego_principal.py` .
3. Si deseas devolverte usa: `cd ..`
