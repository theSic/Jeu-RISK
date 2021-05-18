# V.1.2
import ctypes  # console_hide console_show
import pickle  # read_dico store
import pygame  # Picture (__init__ blit) Text (__init__ blit get_height get_width)
import time  # time_clock time_day


class Picture:
    def __init__(self, gui, contents, size, coord=(0, 0)):  # pygame
        self.gui = gui
        self.contents = pygame.image.load(contents)
        self.size = size
        self.coord = coord

    def blit(self):  # pygame
        self.gui.blit(pygame.transform.scale(self.contents, self.size), self.coord)


class Text:
    def __init__(self, gui, contents, color, size, police='none', coord=(0, 0), escape = 1/3):  # pygame
        self.gui = gui
        self.contents = contents
        self.color = color
        self.size = size
        self.police = police
        self.coord = coord
        self.escape = escape
    
    def blit(self):  # pygame
        for i in range(len(self.contents.split('\n'))): self.gui.blit(pygame.font.SysFont(self.police, self.size).render(self.contents.split('\n')[i], True, self.color), (self.coord[0], self.coord[1] + self.size * (self.escape + 0.5) * i))
    
    def get_height(self):  # pygame
        return pygame.font.SysFont(self.police, self.size).render(self.contents, True, self.color).get_height()
    
    def get_width(self):  # pygame
        return pygame.font.SysFont(self.police, self.size).render(self.contents.split('\n')[0], True, self.color).get_width()


def clear(name):
    file = open(name, 'w')
    file.close()


def console_hide():  # ctypes
    ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)


def console_show():  # ctypes
    ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 4)


def read_dico(name):  # pickle
    with open(name, 'rb') as i:
        return pickle.Unpickler(i).load()


def read_list(name):
    with open(name, 'r') as i:
        return [n.rstrip('\n') for n in i]


def store(name, text):  # pickle
    with open(name, 'wb') as i:
        pickle.Pickler(i).dump(text)


def time_clock(epoch=time.time()):  # time
    return time.strftime('%H:%M:%S', time.localtime(epoch))


def time_day(epoch=time.time()):  # time
    return time.strftime('%y/%m/%d', time.localtime(epoch))


def write(name, text):
    file = open(name, 'a')
    file.write(text)
    file.close()
