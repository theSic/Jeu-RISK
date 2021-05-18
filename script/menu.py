import pygame #init modules
import objs #init files

def run(GUI, mode, loop, mainLoop, gfx):
    for i in pygame.event.get():
        if i.type == pygame.QUIT: loop, mainLoop = False, False
        elif i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                j = GUI.get_at(pygame.mouse.get_pos())
                if j == (220, 174, 0, 255) or j == (0, 12, 57, 255): mode = 'host'
                elif j == (219, 175, 0, 255) or j == (1, 12, 57, 255): print('join')
                elif j == (219, 174, 1, 255) or j == (0, 13, 57, 255): mode = 'settings'
                elif j == (218, 174, 0, 255) or j == (0, 12, 58, 255): escape = True
        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_ESCAPE: escape = True
        if 'escape' in locals():
            while escape:
                for i in pygame.event.get():
                    gfx['escapeBackground'].blit()
                    gfx['escapeYes'].blit()
                    gfx['escapeNo'].blit()
                    gfx['escapeRequest'].blit()
                    pygame.display.flip() #loop les blits
                    if i.type == pygame.QUIT: escape, loop, mainLoop = False, False, False
                    elif i.type == pygame.MOUSEBUTTONDOWN:
                        j = GUI.get_at(pygame.mouse.get_pos())
                        if j == (220, 174, 0, 255): escape, loop, mainLoop = False, False, False
                        elif j == (219, 175, 0, 255): escape = False
                    elif i.type == pygame.KEYDOWN:
                        if i.key == pygame.K_ESCAPE: escape = False
                        elif i.key == pygame.K_RETURN or i.key == pygame.K_KP_ENTER: escape, loop, mainLoop = False, False, False
    return mode, loop, mainLoop