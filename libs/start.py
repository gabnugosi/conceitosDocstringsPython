""" arquivo de teste de conceitos """

from typing import Type, Union
from .atleta import Atleta 

def aggregation(element_1: Union[str, int], element_2: Union[str, int]) -> Union[str, int]: 
    """ create an agregatin with two elements
     :param - element_1: string with first element 
            - element_2: string with second element 
     :return - string with elements agregated """
    return element_1 + element_2

def receber_atleta(atleta: Type[Atleta]) -> None:
    print(atleta) 