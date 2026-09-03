import pygame
import copy
pygame.init()
WIDTH,HEIGHT=WIDTH,HEIGHT = 1707,1067
window=pygame.display.set_mode((WIDTH,HEIGHT))
clock=pygame.time.Clock()
def Sc2il(a,b):
    return [WIDTH//(1707/a),HEIGHT//(1067/b)]
def Sc2fl(a,b):
    return WIDTH/(1707/a),HEIGHT/(1067/b)
def Sciwl(a):
    return WIDTH//(1707/a)
def Scfwl(a):
    return WIDTH/(1707/a)
def Scihl(a):
    return HEIGHT//(1067/a)
def Scfhl(a):
    return HEIGHT/(1067/a)
def Sc2i(a,b):
    return WIDTH//(1707/a),HEIGHT//(1067/b)
def Sc2f(a,b):
    return WIDTH/(1707/a),HEIGHT/(1067/b)
def Sciw(a):
    return WIDTH//(1707/a)
def Scfw(a):
    return WIDTH/(1707/a)
def Scih(a):
    return HEIGHT//(1067/a)
def Scfh(a):
    return HEIGHT/(1067/a)