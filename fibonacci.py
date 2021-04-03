#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 1 12:00:25 2021

@author: fjp.droge
"""

class Fibonacci:
    _fibonacci = {'0': 0, '1': 1, '2': 1}
    _history = None
    
    def __init__(self) -> None:
        self.set_history()
        for i in range(101):
            Fibonacci._fibonacci[str(i)] = self.return_n(i)
    
    def get_history(self) -> list:
        return Fibonacci._history
    
    def set_history(self) -> None:
        if Fibonacci._history is None:
            Fibonacci._history = []
    
    def clear_history(self) -> list:
        Fibonacci._history = []
        return Fibonacci._history

    def get_dict(self) -> dict:
        return Fibonacci._fibonacci
    
    def get_n(self, n: int) -> int:
        Fibo_n = self.return_n(n)
        Fibonacci._history.append(n)
        Fibonacci._fibonacci[str(n)] = Fibo_n
        return Fibo_n
    
    def return_n(self, n: int) -> int:
        if n == 0:
            return 0
        if str(n) in Fibonacci._fibonacci:
            return Fibonacci._fibonacci[str(n)]
        else:
            return self.return_n(n-1) + self.return_n(n-2)
    