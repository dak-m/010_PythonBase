# non-data дескрипторы имею только метод __get__, т.е. они не хранят никаких
# значений, которые можно было бы менять, а только отдают некоторые
# сгенерированные значения

from random import choice
from time import time


class Choice:
    def __init__(self, *choice_, gamename):
        # *choice это упаковка входящих аргументов в кортеж         
        self._choice = choice_
        self._gameName = gamename
        self._obj = None 
        print(f'{self._choice} {type(self._choice)}')
    
    def __get__(self, obj, owner):
        # хранить тут данные объектов класса Game это плохая идея!
        # так как self._obj будет один и тот же на все объекты        
        if self._obj is None:
            self._obj = obj
        print(f'{self._obj}')
        return choice(self._choice)


class Game:
    dice = Choice(*range(1, 7), gamename='dice')
    flip = Choice('Heads', 'Tails', gamename='flip')
    rock_paper_scissors = Choice('Rock', 'Paper', 'Scissors',
                                 gamename='rock_paper_scissors')
    

g1 = Game()
g2 = Game()


class GetTime:
    def __get__(self, instance, owner):
        print(f'self: {self}')
        print(f'instance: {instance}')
        print(f'owner class: {owner}')
        return time()


class TimeClient:
    now = GetTime()


t = TimeClient()
time_ = t.now
