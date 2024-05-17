import unittest

import sys
sys.path.append("src")
from Controller import Control, SecretConfig
from Model.Juego_principal import TableroBatallaNaval
import psycopg2

class TestDataBase(unittest.TestCase):

    #Intentar eliminar una partida pero sin haber guardado una partida anteriormente
    def Eliminar_partida(self):
        try:
            Control.eliminar_partida()
            print("Partida eliminada exitosamente")
        except psycopg2.Error as Error_No_Existen_Partidas:
            print("Error al eliminar la partida:", Error_No_Existen_Partidas)



    

    #Cargar una partida sin haber guardado ninguna(no existe partida para cargar)
    #guardar una partida sin haber jugado ninguna