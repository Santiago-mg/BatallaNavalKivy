import unittest
import psycopg2
from unittest.mock import MagicMock, patch
from io import StringIO
import sys
import json
import sys
sys.path.append("src")
# Importa las funciones para probar
from Controller.Control import guardar_partida, eliminar_partida, cargar_partida
from Controller import Control
from Model.Juego_principal import TableroBatallaNaval

class TestFunciones(unittest.TestCase):

    # Prueba unitaria para la función guardar_partida
    @patch('psycopg2.connect')  # Mock para la conexión a la base de datos
    @patch('sys.stdout', new_callable=StringIO)  # Mock para la salida estándar
    def test_guardar_partida(self, mock_stdout, mock_connect):
        # Define datos de prueba
        jugador1 = "jugador1"
        jugador2 = "jugador2"
        tablero_jugador1 = {"fila1": [0, 0, 0], "fila2": [0, 0, 0], "fila3": [0, 0, 0]}
        tablero_jugador2 = {"fila1": [0, 0, 0], "fila2": [0, 0, 0], "fila3": [0, 0, 0]}
        
        # Llama a la función
        guardar_partida(jugador1, jugador2, tablero_jugador1, tablero_jugador2)

        # Verifica la salida esperada
        self.assertEqual(mock_stdout.getvalue().strip(), "Partida guardada exitosamente.")

    # Prueba unitaria para la función eliminar_partida
    @patch('psycopg2.connect')  # Mock para la conexión a la base de datos
    @patch('sys.stdout', new_callable=StringIO)  # Mock para la salida estándar
    def test_eliminar_partida(self, mock_stdout, mock_connect):
        # Llama a la función
        eliminar_partida()

        # Verifica la salida esperada
        self.assertEqual(mock_stdout.getvalue().strip(), "Partida eliminada exitosamente.")
    
    # Prueba unitaria para la función cargar_partida
    def test_cargar_partida(self):
        # Define los tableros de prueba
        tablero_jugador1 = TableroBatallaNaval(5,5)
        tablero_jugador2 = TableroBatallaNaval(5,5)        
        data_jugador1 = tablero_jugador1.tablero
        juego_jugador1 = json.dumps(data_jugador1) 
        data_jugador2 = tablero_jugador2.tablero
        juego_jugador2 = json.dumps(data_jugador2)
        jugador1 = "jugador1"
        jugador2 = "jugador2" 

        # Guarda la partida en la base de datos
        guardar_partida(jugador1, jugador2, juego_jugador1, juego_jugador2)
    
        # Carga la partida
        jugador_num1, jugador_num2 = cargar_partida()
        jugador_1 = json.loads(jugador_num1)
        jugador_2 = json.loads(jugador_num2)

        # Verifica la salida esperada
        self.assertEqual(jugador_1, tablero_jugador1.tablero)
        self.assertEqual(jugador_2, tablero_jugador2.tablero)

    # Función para asertrar la salida estándar
    def assert_stdout(self, expected_output, mock_stdout):
        cargar_partida()
        self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

    # Prueba unitaria para cargar_partida cuando no hay partidas guardadas
    def test_cargar_partida_sin_datos(self):
        expected_output = "No hay partidas guardadas."
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.assert_stdout(expected_output, mock_stdout)

    # Prueba unitaria para cargar_partida cuando no hay partidas guardadas
    def test_eliminar_partida_no_existente(self):
        expected_output = "Error al eliminar la partida: <psycopg2.errors.UndefinedTable 'Partidas' does not exist>"
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            with self.assertRaises(psycopg2.errors.UndefinedTable):
                eliminar_partida()

        self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

    # Prueba unitaria para cargar_partida cuando no hay partidas guardadas
    def test_cargar_partida_no_existente(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            jugador1, jugador2 = cargar_partida()

        self.assertIsNone(jugador1)
        self.assertIsNone(jugador2)
        self.assertEqual(mock_stdout.getvalue().strip(), "No hay partidas guardadas.")

if __name__ == '__main__':
    unittest.main()