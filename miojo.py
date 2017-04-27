#!/usr/bin/env python
# -*- coding: utf-8 -*-


def miojo(a1, a2):

    if 3 in (a1, a2):
        return 3
        
    t1, t2, t = a1, a2, 0
    if abs(t1 - t2) > 3:
        t = -3

    while True:
        while t1 and t2:
            t1 -= 1
            t2 -= 1
            t += 1
            
        if 3 in (t1, t2):
            return t + t1 + t2
            
        if not t1:
            t1 = a1
        if not t2:
            t2 = a2


def miojo2(ampulheta1, ampulheta2):

    if 3 in (ampulheta1, ampulheta2):
        return 3

    menor, maior = sorted((ampulheta1, ampulheta2))
    ampulheta = [menor, maior]
    acumulada = ampulheta[:]

    for da_vez in uma_ou_outra():
        esta = acumulada[da_vez]
        outra = acumulada[not da_vez]
        
        if abs(esta - outra) == 3:
            return outra
        elif esta < outra:
            acumulada[da_vez] += ampulheta[da_vez]


def uma_ou_outra():
    while True:
        yield 0
        yield 1
