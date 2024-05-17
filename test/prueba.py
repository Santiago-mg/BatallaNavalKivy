import unittest
import psycopg2
from unittest.mock import MagicMock, patch
from io import StringIO
import sys
import json
import sys
sys.path.append("src")
# Importa las funciones que quieres probar
from Controller.Control import guardar_partida, eliminar_partida, cargar_partida
from Controller import Control
from Model.Juego_principal import TableroBatallaNaval

class TestFunciones(unittest.TestCase):

    @patch('psycopg2.connect')
    @patch('sys.stdout', new_callable=StringIO)
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

    @patch('psycopg2.connect')
    @patch('sys.stdout', new_callable=StringIO)
    def test_eliminar_partida(self, mock_stdout, mock_connect):
        # Llama a la función
        eliminar_partida()

        # Verifica la salida esperada
        self.assertEqual(mock_stdout.getvalue().strip(), "Partida eliminada exitosamente.")
    
    def test_cargar_partida(self):
        tablero_jugador1 = TableroBatallaNaval(5,5)
        tablero_jugador2 = TableroBatallaNaval(5,5)        
        data_jugador1 =tablero_jugador1.tablero
        juego_jugador1 = json.dumps(data_jugador1) 
        data_jugador2 =tablero_jugador2.tablero
        juego_jugador2 = json.dumps(data_jugador2)
        jugador1 = "jugador1"
        jugador2 = "jugador2" 

        # Define el resultado esperado de la consulta a la base de datos
        guardar_partida(jugador1, jugador2, juego_jugador1, juego_jugador2)
    

        # Llama a la función
        jugador_num1, jugador_num2 = cargar_partida()
        jugador_1= json.loads(jugador_num1)
        jugador_2= json.loads(jugador_num2)
        # Convierte los tableros de string a diccionarios
        

        # Verifica la salida esperada
        self.assertEqual(jugador_1, tablero_jugador1.tablero)
        self.assertEqual(jugador_2, tablero_jugador2.tablero)
    def assert_stdout(self, expected_output, mock_stdout):
        cargar_partida()
        self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

    def test_cargar_partida_sin_datos(self):
        expected_output = "No hay partidas guardadas."
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.assert_stdout(expected_output, mock_stdout)

    def Eliminar_partida_no_EXISTENTE(self):
        try:
            eliminar_partida()
            print("Partida eliminada exitosamente")
            eliminar_partida()
            print("Partida eliminada exitosamente")
        except psycopg2.Error as Error_No_Existen_Partidas:
            print("Error al eliminar la partida:", Error_No_Existen_Partidas)

if __name__ == '__main__':
    unittest.main()
