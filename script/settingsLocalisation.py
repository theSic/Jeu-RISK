import pygame #init modules
import objs #init files

def run(GUI, mode, loop, mainLoop, configFile):
    for i in pygame.event.get():
        if i.type == pygame.QUIT: loop, mainLoop = False, False
        elif i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                j = GUI.get_at(pygame.mouse.get_pos())
                if j == (220, 174, 0, 255) or j == (0, 12, 57, 255): configFile['language'], loop = 'ENG', False
                elif j == (0, 0, 0, 255) or j == (0, 12, 58, 255): pass
                elif j == (0, 0, 0, 255) or j == (0, 12, 56, 255): pass
                elif j == (219, 174, 0, 255) or j == (0, 13, 57, 255): configFile['language'], loop = 'FRA', False
                elif j == (0, 0, 0, 255) or j == (0, 13, 58, 255): pass
                elif j == (0, 0, 0, 255) or j == (0, 13, 56, 255): pass
                elif j == (0, 0, 0, 255) or j == (0, 11, 57, 255): pass
                elif j == (0, 0, 0, 255) or j == (0, 11, 58, 255): pass
                elif j == (0, 0, 0, 255) or j == (0, 11, 56, 255): pass
                elif j == (0, 0, 0, 255) or j == (1, 12, 57, 255): pass
                elif j == (0, 0, 0, 255) or j == (1, 12, 58, 255): pass
                elif j == (0, 0, 0, 255) or j == (1, 12, 56, 255): pass
                elif j == (0, 0, 0, 255) or j == (1, 13, 57, 255): pass
                elif j == (0, 0, 0, 255) or j == (1, 13, 58, 255): pass
                elif j == (0, 0, 0, 255) or j == (1, 13, 56, 255): pass
                elif j == (0, 0, 0, 255) or j == (1, 11, 57, 255): pass
                elif j == (0, 0, 0, 255) or j == (1, 11, 58, 255): pass
                elif j == (0, 0, 0, 255) or j == (1, 11, 56, 255): pass
                elif j == (0, 0, 0, 255) or j == (0, 12, 59, 255): pass
                elif j == (0, 0, 0, 255) or j == (0, 12, 55, 255): pass
                objs.store('game.config', configFile)
        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_ESCAPE: mode = 'settings'
    return mode, loop, mainLoop
'''
0, 12, 57  |  0, 12, 58
0, 12, 56  |  0, 13, 57
0, 13, 58  |  0, 13, 56
0, 11, 57  |  0, 11, 58
0, 11, 56  |  1, 12, 57
1, 12, 58  |  1, 12, 56
1, 13, 57  |  1, 13, 58
1, 13, 56  |  1, 11, 57
1, 11, 58  |  1, 11, 56
0, 12, 59  |  0, 12, 55
'''