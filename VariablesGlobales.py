import pygame, sys, random, ctypes, os, glob

pygame.init()

fps = 60

run = True
white = (255,255,255)
negro = (0,0,0)
movex = 0
movey = 0
sizex = 0
sizey = 0
screen_size = (1920,1080)

mapa = {}
zoomv = 10
zoomvBase = 10

zoomList = [zoomv, zoomv*2, zoomv*4, zoomv*8]

clicking = {1 : False}

map_sizex = [0,2000] 
map_sizey = [0,1000] 

map_size = [map_sizex[1],map_sizey[1]]
tilesInMap = 0

#Cargamos las imagenes

class sizemap:
    def sizemap(imgsize, base_image):
        red_image = pygame.transform.scale(base_image, (imgsize, imgsize))
        return red_image

imagen = {}
start = "images/lowRes"
lista = os.listdir ( "images/lowRes" )


for i in lista:
    
    lista2 = os.listdir( start + '/' + i )
    imagen[i] = {}
    
    for j in lista2:
        lista3 = os.listdir ( start + '/' + i + '/' + j )
        imagen[i][j] = {}
        var = 0
        
        for k in lista3:    
            imagen[i][j][var] = {}
            #imagenDir = imagen
            
            baseImage = pygame.image.load(start + '/' + i + '/' + j + '/' + k)
            

            for size in zoomList:
                imagen[i][j][var][size] = sizemap.sizemap(size,baseImage)

            var = var + 1


'''
imagen = {0 : "images/lowRes/cities/city1.jpg", 1 : "images/lowRes/sea/sea2.jpg", 2 : "images/lowRes/forests/forest7.jpg", 3 : "images/lowRes/forests/forest6.jpg", 4 : "images/lowRes/winter/mountains/mountain3.jpg",

5 : "images/lowRes/floor/floor2.jpg", 6 : "images/lowRes/floor/floor4.jpg", 7 : "images/lowRes/mountains/mountain5.jpg", 8 : "images/lowRes/mountains/mountain4.jpg", 9: "images/lowRes/forests/forest9.jpg", 10 : "images/lowRes/forests/forest10.jpg"

}
'''
base_image = {}




'''
for image in range(len(imagen.keys())):
    baseImage = pygame.image.load(imagen[image])
    base_image[image] = {}
    
    for size in zoomList:
        base_image[image][size] = sizemap.sizemap(size,baseImage)
'''


mapDic = {}
mapDicXY = {}
mapTile = {}



#Raton

clicked = [0, 0]
clickedMap = [0, 0]
clickedMapOrigin = [0, 0]
unClicked = []
unClickedMap = []
selected = []
baseEleccion = []
selectedM = {}

untisDic = {}

vel_mov_mapa = [1, 1]

#menus

menus = {}
menusActivos = {}

#buttons

buttons = {}
buttonsActivos = {}

#Unidades

units = {}
unitsInGame = {}
armiesInGame = []
numberOfArmies = 0

#Texto

textActive = False

a = random.random()
print(a)
b = {1 : 1, 2 : 2}
id = 'army.' + str(len(b.keys()))
print(id)

class Test1:

    def __init__(self):
        self.var1=1
    

test1 = Test1()

dic1 = { "var1" : test1}

var2 = dic1["var1"]

var2.var1 = 3
a = list(dic1.keys())[0]

lista = [{9 : 1, 8 : 2 }, {2 : 3, 2 : 4}]

num = 0
for k in lista:
    
    for g in lista[num]:
        print(lista[num][g])
    num = num + 1
print(a)



print(test1.var1)