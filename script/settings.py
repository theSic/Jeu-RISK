import pygame #init modules
import objs #init files

def run(GUI, mode, loop, mainLoop, configFile_screenWidth, configFile_screenHeight, configFile, textlocking):
    for i in pygame.event.get():
        if i.type == pygame.QUIT: loop, mainLoop = False, False
        elif i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                j = GUI.get_at(pygame.mouse.get_pos())
                if j == (219, 174, 0, 255): mode, textlocking = 'menu', 'null'
                elif j == (220, 175, 0, 255): mode, textlocking = 'settingsLocalisation', 'null'
                elif j == (220, 174, 0, 255): textlocking = 'settingsName'
                elif j == (219, 175, 0, 255): textlocking = 'settingsWidth'
                elif j == (219, 174, 1, 255): textlocking = 'settingsHeight'
                else: textlocking = 'null'
                if textlocking != 'settingsWidth':
                    if configFile_screenWidth == '' or int(configFile_screenWidth) < 800: configFile_screenWidth = '800'
                if textlocking != 'settingsHeight':
                    if configFile_screenHeight == '' or int(configFile_screenHeight) < 600: configFile_screenHeight = '600'
                if textlocking != 'settingsName':
                    if configFile['name'] == '': configFile['name'] = 'Player'
                if textlocking == 'null':
                    if configFile['screenWidth'] != int(configFile_screenWidth) or configFile['screenHeight'] != int(configFile_screenHeight): configFile['screenWidth'], configFile['screenHeight'], loop = int(configFile_screenWidth), int(configFile_screenHeight), False
                    elif str(configFile['screenWidth']) != configFile_screenWidth or str(configFile['screenHeight']) != configFile_screenHeight: configFile['screenWidth'], configFile['screenHeight'], configFile_screenWidth, configFile_screenHeight = int(configFile_screenWidth), int(configFile_screenHeight), str(int(configFile_screenWidth)), str(int(configFile_screenHeight))
                objs.store('game.config', configFile)
        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_ESCAPE: mode, textlocking = 'menu', 'null'
            elif textlocking == 'settingsName':
                if i.unicode in ['a', 'A', 'b', 'B', 'c', 'C', 'd', 'D', 'e', 'E', 'f', 'F', 'g', 'G', 'h', 'H', 'i', 'I', 'j', 'J', 'k', 'K', 'l', 'L', 'm', 'M', 'n', 'N', 'o', 'O', 'p', 'P', 'q', 'Q', 'r', 'R', 's', 'S', 't', 'T', 'u', 'U', 'v', 'V', 'w', 'W', 'x', 'X', 'y', 'Y', 'z', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9','_','-']:
                    if len(configFile['name']) <= 14: configFile['name'] += i.unicode
                elif i.key == pygame.K_BACKSPACE: configFile['name'] = configFile['name'][:-1]
            elif textlocking == 'settingsWidth':
                if i.unicode in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                    if len(configFile_screenWidth) <= 5: configFile_screenWidth += i.unicode
                elif i.key == pygame.K_BACKSPACE: configFile_screenWidth = configFile_screenWidth[:-1]
            elif textlocking == 'settingsHeight':
                if i.unicode in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                    if len(configFile_screenHeight) <= 5: configFile_screenHeight += i.unicode
                elif i.key == pygame.K_BACKSPACE: configFile_screenHeight = configFile_screenHeight[:-1]
    return mode, loop, mainLoop, configFile_screenWidth, configFile_screenHeight, configFile, textlocking