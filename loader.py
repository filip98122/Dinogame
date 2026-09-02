from General_info import *
listofpics=[["walk",5],["idle",1]]
color="zb"
def load():
    textures={}
    for j in range(len(listofpics)):
        for i in range(listofpics[j][1]):
            for x in range(len(color)):
                notscalledpic=pygame.image.load(f"textures/{listofpics[j][0]}{i}{color[x]}.png")
                textures[f"r{listofpics[j][0]}{i}{color[x]}"]=pygame.transform.scale(notscalledpic,(WIDTH//(27.42857142857143*2),HEIGHT//(10.8*2)))
                textures[f"l{listofpics[j][0]}{i}{color[x]}"]=pygame.transform.flip(textures[f"r{listofpics[j][0]}{i}{color[x]}"],True,False)
    textures["cursorb"]=pygame.transform.scale(pygame.image.load("textures/cursorb.png"),(WIDTH//(128//1.5),HEIGHT//(36//1.5)))
    textures["cursorz"]=pygame.transform.scale(pygame.image.load("textures/cursorz.png"),(WIDTH//(128//1.5),HEIGHT//(36//1.5)))
    textures["startbutton"]=pygame.transform.scale(pygame.image.load("textures/start.png"),(WIDTH//(1920//200),HEIGHT//(1080//75)))
    textures["dinogame"]=pygame.transform.scale(pygame.image.load("textures/dinogame.png"),(WIDTH,HEIGHT))
    textures["game"]=pygame.transform.scale(pygame.image.load("textures/BG.png"),(WIDTH,HEIGHT))
    textures["barbedwire"]=pygame.transform.scale(pygame.image.load("textures/barbedwire.png"),(45,45))
    textures["boltu"]=pygame.transform.scale(pygame.image.load("textures/crossbowbolt.png"),(WIDTH//(128//1.5),HEIGHT//(36//1.5)))
    textures["boltr"]=pygame.transform.rotate(textures["boltu"],-90)
    textures["boltd"]=pygame.transform.rotate(textures["boltr"],-90)
    textures["boltl"]=pygame.transform.rotate(textures["boltd"],-90)
    textures["crossbowu"]=pygame.transform.scale(pygame.image.load("textures/crossbow.png"),(80,60))
    textures["crossbowr"]=pygame.transform.rotate(textures["crossbowu"],-90)
    textures["crossbowd"]=pygame.transform.rotate(textures["crossbowr"],-90)
    textures["crossbowl"]=pygame.transform.rotate(textures["crossbowd"],-90)
    textures["startplat"]=pygame.transform.scale(pygame.image.load("textures/platform.png"),(WIDTH//7,HEIGHT//9))
    textures["frame"]=pygame.transform.scale(pygame.image.load("textures/frame.png"),(WIDTH//(1707/135),HEIGHT//(1067/135)))
    textures["bomb"]=pygame.transform.scale(pygame.image.load("textures/bomb.png"),(WIDTH//(1707/45),HEIGHT//(1067/55)))
    return textures
textures=load()