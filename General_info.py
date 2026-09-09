import pygame
import copy
import random
pygame.init()
window=pygame.display.set_mode((0,0),pygame.FULLSCREEN)
currentwannabeh=window.get_height()
currentwannabew=window.get_width()
WIDTH,HEIGHT=window.get_width(),window.get_height()
clock=pygame.time.Clock()
def Sc2il(a,b):
    return [WIDTH//(currentwannabew/a),HEIGHT//(currentwannabeh/b)]
def Sc2fl(a,b):
    return WIDTH/(currentwannabew/a),HEIGHT/(currentwannabeh/b)
def Sciwl(a):
    return WIDTH//(currentwannabew/a)
def Scfwl(a):
    return WIDTH/(currentwannabew/a)
def Scihl(a):
    return HEIGHT//(currentwannabeh/a)
def Scfhl(a):
    return HEIGHT/(currentwannabeh/a)
def Sc2i(a,b):
    return WIDTH//(currentwannabew/a),HEIGHT//(currentwannabeh/b)
def Sc2f(a,b):
    return WIDTH/(currentwannabew/a),HEIGHT/(currentwannabeh/b)
def Sciw(a):
    return WIDTH//(currentwannabew/a)
def Scfw(a):
    return WIDTH/(currentwannabew/a)
def Scih(a):
    return HEIGHT//(currentwannabeh/a)
def Scfh(a):
    return HEIGHT/(currentwannabeh/a)