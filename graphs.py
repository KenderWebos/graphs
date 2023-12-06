import pygame
import heapq

def dijkstra(grafo, fuente, destino):
    grafo = {
        'A':{'B':2, 'C':3,},
        'B':{'A':2, 'C':4, 'D':5},
        'C':{'A':3, 'B':4, 'D':6, 'E':7},
        'D':{'B':5, 'C':6, 'E':8, 'F':9},
        'E':{'C':7, 'D':8, 'F':10},
    }

pygame.init()