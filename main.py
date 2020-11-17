#!/bin/python3

from sense_hat import SenseHat
import schedule

sense = SenseHat()
#sense.clear()

f = open("data.txt", "r")
LEDON = f.readline()[2:-2]
LEDOFF = f.readline()[2:-2]
RGB = f.readline()[2:-2]
f.close()

ledon = LEDON[1:-1].split(", ")
ledoff = LEDOFF[1:-1].split(", ")
color = RGB[1:-1].split(", ")
print("LED ON: ",ledon)
print("LED OFF: ",ledoff)
print("RGB: ",color)

O = [int(color[0]), int(color[1]), int(color[2])]
Z = [0,0,0]

ALL_ON = [
O, O, O, O, O, O, O, O,
O, O, O, O, O, O, O, O,
O, O, O, O, O, O, O, O,
O, O, O, O, O, O, O, O,
O, O, O, O, O, O, O, O,
O, O, O, O, O, O, O, O,
O, O, O, O, O, O, O, O,
O, O, O, O, O, O, O, O
]

ALL_OFF = [
Z, Z, Z, Z, Z, Z, Z, Z,
Z, Z, Z, Z, Z, Z, Z, Z,
Z, Z, Z, Z, Z, Z, Z, Z,
Z, Z, Z, Z, Z, Z, Z, Z,
Z, Z, Z, Z, Z, Z, Z, Z,
Z, Z, Z, Z, Z, Z, Z, Z,
Z, Z, Z, Z, Z, Z, Z, Z,
Z, Z, Z, Z, Z, Z, Z, Z
]

ROOM ={ '1':{'x':0,'y':0},
        '2':{'x':0,'y':1},
        '3':{'x':0,'y':2},
        '4':{'x':0,'y':3},
        '5':{'x':0,'y':4},
        '6':{'x':0,'y':5},
        '7':{'x':0,'y':6},
        '8':{'x':0,'y':7},
        '9':{'x':1,'y':0},
        '10':{'x':1,'y':1},
        '11':{'x':1,'y':2},
        '10':{'x':1,'y':1},
        '11':{'x':1,'y':2},
        '12':{'x':1,'y':3},
        '13':{'x':1,'y':4},
        '14':{'x':1,'y':5},
        '15':{'x':1,'y':6},
        '16':{'x':1,'y':7},
        '17':{'x':2,'y':0},
        '18':{'x':2,'y':1},
        '19':{'x':2,'y':2},
        '20':{'x':2,'y':3},
        '21':{'x':2,'y':4},
        '22':{'x':2,'y':5},
        '23':{'x':2,'y':6},
        '24':{'x':2,'y':7},
        '25':{'x':3,'y':0},
        '26':{'x':3,'y':1},
        '27':{'x':3,'y':2},
        '28':{'x':3,'y':3},
        '29':{'x':3,'y':4},
        '30':{'x':3,'y':5},
        '31':{'x':3,'y':6},
        '32':{'x':3,'y':7},
        '33':{'x':4,'y':0},
        '34':{'x':4,'y':1},
        '35':{'x':4,'y':2},
        '36':{'x':4,'y':3},
        '37':{'x':4,'y':4},
        '38':{'x':4,'y':5},
        '39':{'x':4,'y':6},
        '40':{'x':4,'y':7},
        '41':{'x':5,'y':0},
        '42':{'x':5,'y':1},
        '43':{'x':5,'y':2},
        '44':{'x':5,'y':3},
        '45':{'x':5,'y':4},
        '46':{'x':5,'y':5},
        '47':{'x':5,'y':6},
        '48':{'x':5,'y':7},
        '49':{'x':6,'y':0},
        '50':{'x':6,'y':1},
        '51':{'x':6,'y':2},
        '52':{'x':6,'y':3},
        '53':{'x':6,'y':4},
        '54':{'x':6,'y':5},
        '55':{'x':6,'y':6},
        '56':{'x':6,'y':7},
        '57':{'x':7,'y':1},
        '58':{'x':7,'y':2},
        '59':{'x':7,'y':3},
        '60':{'x':7,'y':4},
        '61':{'x':7,'y':5},
        '62':{'x':7,'y':6},
        '63':{'x':7,'y':7},

    }


def main():
    for i in ledon:
        #print(type(i))
        if(i in ROOM):
            sense.set_pixel(ROOM[i]['x'],ROOM[i]['y'],int(color[0]),int(color[1]),int(color[2]))
        if i == '0':
            O = [0,0,0]
            sense.set_pixels(ALL_ON)
    for i in ledoff:
        #print(type(i))
        if(i in ROOM):
            sense.set_pixel(ROOM[i]['x'],ROOM[i]['y'],0,0,0)
        if i == '0':
            sense.set_pixels(ALL_OFF)

main()

