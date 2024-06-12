"""
Clase Coche base para el Examen de la UD4
Refactorización
Extrae una superclase Vehículo con los campos
    num_serie
    fabricante
    color
:autor: Jaime Rabasco
"""

class Vehiculo:
    """
    Clase Vehículo que contiene los campos color, fabricante, num_serie.

    Author: Jorge Pradillo Hinterberger
    """
    color = 'rojo';
    fabricante = 'seat';
    num_serie = 1;

    def __init__(self):
        """
        Constructor de la clase Vehículo.
        """
        pass;

class Coche(Vehiculo):
    """
    Clase Coche que deriva de la clase Vehículo que contiene además una cilindrada que por defecto es 1000.
    """

    cilindrada = 1000;

    def __init__(self, num_serie, cilindrada, fabricante, color):
        """
        Constructor de la clase Coche que recibe los parámetros num_serie, cilindrada, fabricante y color.
        :param num_serie: Recibe el número de serie del coche.
        :param cilindrada: Recibe la cilindrada del coche
        :param fabricante: Recibe el fabricante del coche.
        :param color: Recibe el color que le queramos dar al coche.
        """
        self.num_serie = num_serie;
        self.cilindrada = cilindrada;
        self.fabricante = fabricante;
        self.color = color;

    @property
    def num_serie(self):
        """
        Propiedad num_serie del coche.
        :return: Devuelve el número de serie.
        """
        return self.__num_serie

    @num_serie.setter
    def num_serie(self, value):
        """
        Setter del num_serie del coche.
        :param value: Recibe un valor que queramos asignarle al número de serie.
        :return: Devuelve el valor que le hayamos dado.
        """
        self.__num_serie = value

    @property
    def color(self):
        """
        Propiedad color del coche.
        :return: Devuelve el número de serie.
        """
        return self.__color

    @color.setter
    def color(self, value: int):
        """
        Setter del color del coche.
        :param value: Recibe un valor que queramos asignarle al color del coche.
        :return: Devuelve el valor que le hayamos dado.
        """
        self.__color = value

    @property
    def cilindrada(self):
        """
        Propiedad cilindrada del coche.
        :return: Devuelve la cilindrada del coche.
        """
        return self.__cilindrada

    @cilindrada.setter
    def cilindrada(self, value):
        """
        Setter de la cilindrada del coche.
        :param value: Recibe un valor que queramos asignarle a la cilindrada del coche.
        :return: Devuelve el valor que le hayamos dado.
        """
        self.__cilindrada = value

    @property
    def fabricante(self):
        """
        Propiedad fabricante del coche.
        :return: Devuelve el fabricante del coche.
        """
        return self.__fabricante

    @fabricante.setter
    def fabricante(self, value):
        """
        Setter del fabricante del coche.
        :param value: Recibe un valor que queramos asignarle al fabricante del coche.
        :return: Devuelve el valor que le hayamos dado.
        """
        self.__fabricante = value
