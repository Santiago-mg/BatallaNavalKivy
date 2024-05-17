import unittest
from unittest.mock import MagicMock, patch
from io import StringIO
import sys
import json
import sys
sys.path.append("src")
# Importa las funciones que quieres probar
from Controller.Control import guardar_partida, eliminar_partida, cargar_partida

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

    @patch('psycopg2.connect')
    @patch('sys.stdout', new_callable=StringIO)
    def test_cargar_partida(self, mock_stdout, mock_connect):
        # Define el resultado esperado de la consulta a la base de datos
        partida_guardada = ("jugador1", "jugador2", '{"jugador1": {"fila1": [0, 0, 0], "fila2": [0, 0, 0], "fila3": [0, 0, 0]}}', '{"jugador2": {"fila1": [0, 0, 0], "fila2": [0, 0, 0], "fila3": [0, 0, 0]}}')
        mock_cursor = MagicMock()
        mock_cursor.fetchone.return_value = partida_guardada
        mock_connect.return_value.cursor.return_value = mock_cursor

        # Llama a la función
        jugador1, jugador2 = cargar_partida()

        # Convierte los tableros de string a diccionarios
        tablero_jugador1 = json.loads(partida_guardada[2])
        tablero_jugador2 = json.loads(partida_guardada[3])

        # Verifica la salida esperada
        self.assertEqual(jugador1, tablero_jugador1["jugador1"])
        self.assertEqual(jugador2, tablero_jugador2["jugador2"])

if __name__ == '__main__':
    unittest.main()
