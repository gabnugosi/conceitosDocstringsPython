""" arquivo de teste de conceitos """

from typing import Type
from atleta import Atleta 

def aggregation(element_1: str, element_2: str) -> str: 
    """ create an agregatin with two elements
     :param - element_1: string with first element 
            - element_2: string with second element 
     :return - string with elements agregated """
    return element_1 + element_2

def receber_atleta(atleta: Type[Atleta]) -> None:
    print(atleta) 