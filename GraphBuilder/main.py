import pygame as pg
from pygame.locals import *
import sys
import os
import DFS
import pickle
from math import sqrt
from pygame_widgets.button import Button
from tkinter import filedialog
import random as ra
import numpy as np
import time
from collections import deque 

WHITE = (255, 255, 255)
RED = (255, 23, 62)
GREEN = (0, 139, 139)
BLUE = (255, 215, 0)
ONE = (255, 0, 215)

desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')

pg.init()
clock = pg.time.Clock()
FPS = 30
sc = pg.display.set_mode((800, 800))
r = 20
n = 1
apexs = {}
numbers = []
d_keys = {}
pre_a = (())

g = DFS.Graph()

icon = pg.image.load('icon.jpg')
pg.display.set_icon(icon)
pg.font.init()
font_obj = pg.font.Font('20339.ttf', 25)
pg.display.set_caption('Graph Drawer 2000-EXTREME')

buttons = (('New Graph', lambda: main(None)), ('Options', lambda: options()),
           ('Open Graph', lambda: main(1)), )
# 530 550

visited = list()


def menu():

    bg = pg.image.load('bg.jpg')
    sc.blit(bg, (0, 0))

    DFS_B = Button(
        sc, 70, 710, 200, 50, text='DFS Visual',
        font=font_obj,
        fontSize=25, margin=20,
        inactiveColour=(255, 0, 127),
        pressedColour=(75, 0, 130),
        hoverColour=(138, 43, 226),
        radius=100,
        onClick=lambda: main(2),
        textColour=(240, 255, 255)
    )

    NewGraph = Button(
        sc, 70, 500, 200, 50, text='New Graph',
        font=font_obj,
        fontSize=25, margin=20,
        inactiveColour=(255, 0, 127),
        pressedColour=(75, 0, 130),
        hoverColour=(138, 43, 226),
        radius=100,
        onClick=lambda: main(None),
        textColour=(240, 255, 255)
    )

    Options = Button(
        sc, 70, 570, 200, 50, text='Options',
        font=font_obj,
        fontSize=25, margin=20,
        inactiveColour=(255, 0, 127),
        pressedColour=(75, 0, 130),
        hoverColour=(138, 43, 226),
        radius=100,
        onClick=lambda: options(),
        textColour=(240, 255, 255)
    )

    Open_Graph = Button(
        sc, 70, 640, 200, 50, text='Open Graph',
        font=font_obj,
        fontSize=25, margin=20,
        inactiveColour=(255, 0, 127),
        pressedColour=(75, 0, 130),
        hoverColour=(138, 43, 226),
        radius=100,
        onClick=lambda: main(1),
        textColour=(240, 255, 255)
    )

    pg.display.flip()

    while True:
        for i in pg.event.get():

            keys = pg.key.get_pressed()
            print(keys)

            if i.type == pg.QUIT:
                sys.exit()

            # if i.type == pg.MOUSEBUTTONDOWN:
                # print(i.pos)

            NewGraph.listen(i)
            NewGraph.draw()
            Options.listen(i)
            Options.draw()
            Open_Graph.listen(i)
            Open_Graph.draw()
            DFS_B.listen(i)
            DFS_B.draw()

        pg.display.update()


def algorythm():
    global apexs, visited, d_keys
    els = list(apexs.keys())

    # arg = ra.randint(0, 1)
    arg = 1

    for i in range(len(els)):
        if arg == 0:
            if i+1 == len(els):
                draw_line(els[i][0][0], els[i][0][1], els[i][1],
                          els[0][0][0], els[0][0][1], els[0][1])
            else:
                draw_line(els[i][0][0], els[i][0][1], els[i][1],
                          els[i+1][0][0], els[i+1][0][1], els[i+1][1])
        else:
            el = els[ra.randint(0, len(els)-1)]
            draw_line(els[i][0][0], els[i][0][1], els[i][1],
                      el[0][0], el[0][1], el[1])

    d_keys = {}
    keys = list(apexs.keys())
    matrix = np.zeros(shape=(len(keys), len(keys)), dtype=int)
    num_coords = {}
    
    for key in keys:
        values = apexs.get(key)
        for val in values:
            matrix[key[1]-1][val[2]-1] = 1
            # num_coords.update(key[1]-1:)
    
    # pg.display.update()
    print(matrix)
    visited = set()
    first_node = keys[ra.randint(0, len(keys)-1)]
    pg.display.update()
    print(f'Починаю пошук з ноди номер: {first_node[1]}')
    #eulerian_cycle(keys)
    
    dfs_search(visited, apexs, first_node)
    print(f'Список відвіданих вершин: {visited}')
    print(f'Кількість відвіданих вершин: {len(visited)}')
    print(f'Загальна кількість вершин: {len(keys)}')
    if len(visited) < len(keys):
        print("Граф не зв'язний")
    else:
        print("Граф зв'язний")
    
    
def eulerian_cycle(keys):
    global apexs, visited, d_keys
    
    edges_amount = len(keys)
    cycle = deque()

    cur = 0
    while edges_amount > 0:
        choices = apexs[keys[cur]]

        while choices:
            cycle.append(cur)
            edges_amount -= 1
            cur = choices.pop()
            choices = apexs.get(keys[cur])

        if edges_amount == 0:
            break

        rotate = 0
        for cur in cycle:
            if graph[cur]:
                break
            rotate += 1

        cycle.rotate(-rotate)

    cycle.rotate(-cycle.index(0))
    cycle.append(0)


    return tuple(cycle)

def dfs_search(visited, graph, node):
    global d_keys, pre_a

    if type(node) is list:
        node = ((node[0], node[1]), node[2])
    if node[1] not in visited:
        # print(node)
        visited.add(node[1])
        pg.draw.circle(sc, GREEN, (node[0][0], node[0][1]), r)
        draw_number((node[0][0], node[0][1]), node[1])
        if len(pre_a) > 0:
            # print('yes')
            pg.draw.circle(sc, ONE, (pre_a[0][0], pre_a[0][1]), r)
            draw_number((pre_a[0][0], pre_a[0][1]), pre_a[1])
            pre_a = ((node[0][0], node[0][1]), node[1])
        else:
            pre_a = ((node[0][0], node[0][1]), node[1])
        time.sleep(2)
        pg.display.update()
        for neighbour in graph[node]:
            dfs_search(visited, graph, neighbour)
    pg.draw.circle(sc, ONE, (pre_a[0][0], pre_a[0][1]), r)
    draw_number((pre_a[0][0], pre_a[0][1]), pre_a[1])
 
def main(arg):
    global clock, FPS, RED, GREEN, BLUE, WHITE, r, n, apexs

    sc.fill(WHITE)

    if arg == 1:
        path = os.path.join(desktop, 'New Graph.pkl')
        file = open(path, 'rb')
        apexs_import = pickle.load(file)
        file.close()

        apexs_keys = list(apexs_import.keys())

        # print(apexs_keys)

        apexs = apexs_import.copy()
        for key in apexs_keys:
            values = apexs_import.get(key)
            draw_circle((float(key[0][0]), float(key[0][1])), int(key[1]))
            for val in values:
                draw_line(float(key[0][0]), float(key[0][1]),
                          int(key[1]), val[0], val[1], val[2])
                values.pop(values.index(val))

        n = apexs_keys[len(apexs_keys)-1][1]+1
    elif arg == 2:
        for i in range(1, ra.randint(5, 15)):
            x = ra.randint(100, 700)
            y = ra.randint(100, 700)
            if not intersection((x, y)):
                draw_circle((x, y), n)
                n += 1

    # bg = pg.image.load('graph.jpg')
    # sc.blit(bg, (0, 0))

    line = []

    while True:
        for i in pg.event.get():

            keys = pg.key.get_pressed()

            if i.type == pg.QUIT:
                sys.exit()

            if i.type == pg.MOUSEBUTTONDOWN:
                if i.button == 1:
                    if apexs:
                        p_coords = intersection(i.pos)
                        if p_coords:
                            line.append(p_coords)
                            if len(line) >= 2:
                                # print(line)
                                if [line[0][0],
                                    line[0][1], line[0][2]] in apexs[(line[1][0],
                                                                      line[1][1]), line[1][2]]:
                                    print('This connection already exists')
                                    pg.draw.circle(
                                        sc, RED, (line[0][0], line[0][1]), r)
                                    draw_number(
                                        (line[0][0], line[0][1]), line[0][2])
                                    line = []
                                else:
                                    if [line[1][0],
                                        line[1][1], line[1][2]] in apexs[(line[0][0],
                                                                          line[0][1]), line[0][2]]:
                                        del_line(line[0][0],
                                                 line[0][1],
                                                 line[0][2],
                                                 line[1][0],
                                                 line[1][1],
                                                 line[1][2])
                                    else:
                                        draw_line(line[0][0],
                                                  line[0][1],
                                                  line[0][2],
                                                  line[1][0],
                                                  line[1][1],
                                                  line[1][2])
                                    line = []
                            else:
                                pg.draw.circle(
                                    sc, GREEN, (line[0][0], line[0][1]), r)
                                draw_number(
                                    (line[0][0], line[0][1]), line[0][2])
                        else:
                            draw_circle(i.pos, n)
                            n += 1
                    else:
                        draw_circle(i.pos, n)
                        n += 1
                elif i.button == 2:
                    clear()
                    sc.fill(WHITE)
                elif i.button == 3:
                    line = []
                    dc = intersection(i.pos)
                    if dc:
                        values = apexs.pop(((dc[0], dc[1]), dc[2]))
                        pg.draw.circle(sc, WHITE, (dc[0], dc[1]), r)
            if i.type == pg.KEYDOWN:
                if i.key == pg.K_a:
                    print(apexs)
                if i.key == pg.K_p:
                    temp = apexs.copy()
                    keys = temp.keys()
                    for key in keys:
                        val = temp.get(key)
                        print(f'{key}:{val}')
                if i.key == pg.K_ESCAPE:
                    clear()
                    return
                if i.key == pg.K_s:
                    save_file()
                if i.key == pg.K_m:
                    algorythm()

        pg.display.update()
        clock.tick(FPS)
    return


def save_file():
    global apexs, desktop

    path = os.path.join(desktop, 'New Graph.pkl')
    file = open(path, 'wb')
    pickle.dump(apexs, file)
    file.close()
    print('Successfully Saved!')


def draw_line(x, y, n, x1, y1, n1):
    global apexs

    pg.draw.line(sc, RED, (x, y), (x1, y1))
    pg.draw.circle(sc, RED, (x, y), r)
    pg.draw.circle(sc, RED, (x1, y1), r)
    draw_number((x, y), n)
    draw_number((x1, y1), n1)
    apexs[(x, y), n].append([x1, y1, n1])
    apexs[(x1, y1), n1].append([x, y, n])


def del_line(x, y, n, x1, y1, n1):
    global apexs

    apexs[(x, y), n].remove([x1, y1, n1])
    pg.draw.line(sc, WHITE, (x, y), (x1, y1))
    pg.draw.circle(sc, RED, (x, y), r)
    pg.draw.circle(sc, RED, (x1, y1), r)
    draw_number((x, y), n)
    draw_number((x1, y1), n1)


def options():
    bg = pg.image.load('options.jpg')
    sc.blit(bg, (0, 0))
    Back = Button(
        sc, 300, 700, 200, 50, text='Back',
        font=font_obj,
        fontSize=25, margin=20,
        inactiveColour=(255, 0, 127),
        pressedColour=(75, 0, 130),
        hoverColour=(138, 43, 226),
        radius=100,
        onClick=lambda: menu(),
        textColour=(240, 255, 255)
    )
    while True:
        for i in pg.event.get():

            keys = pg.key.get_pressed()

            if i.type == pg.QUIT:
                sys.exit()

            # if i.type == pg.MOUSEBUTTONDOWN:
                # print(i.pos)

            Back.listen(i)
            Back.draw()

        pg.display.update()


def clear():
    global apexs, n

    bg = pg.image.load('bg.jpg')
    sc.blit(bg, (0, 0))
    n = 1
    apexs = {}


def draw_circle(coords, number):
    global sc, RED, r, n, apexs, BLUE, numbers

    pg.draw.circle(sc, RED, coords, r)
    apexs.setdefault((coords, n), [])

    draw_number(coords, number)


def draw_number(coords, num):

    if num < 100:
        font_size = 32
    else:
        font_size = 18
    number = pg.font.Font('freesansbold.ttf', font_size)
    n_obj = number.render(str(num), True, BLUE)
    n_rect_obj = n_obj.get_rect()
    n_rect_obj.center = (coords)
    sc.blit(n_obj, n_rect_obj)


def intersection(coords):
    global apexs

    keys = list(apexs.keys())

    for i in range(len(keys)):
        if sqrt((keys[i][0][0] - coords[0]) ** 2 + (keys[i][0][1] - coords[1]) ** 2) < 2 * r:
            return keys[i][0][0], keys[i][0][1], keys[i][1]


menu()