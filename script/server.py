import pygame #init modules
import objs #init files

def coordCheck(configFile, zoom, contentsRight, originalSizeRight, contentsLeft, contentsUp, contentsDown, originalSizeDown, correctCoordX=0, correctCoordY=0):
    if contentsRight.coord[0] + contentsRight.size[0] < configFile['screenWidth']: correctCoordX = contentsRight.coord[0] - configFile['screenWidth'] + originalSizeRight * 1.1 ** zoom
    elif contentsLeft.coord[0] > 0: correctCoordX = contentsLeft.coord[0]
    if contentsUp.coord[1] > 0: correctCoordY = contentsUp.coord[1]
    elif contentsDown.coord[1] + contentsDown.size[1] < configFile['screenHeight']: correctCoordY = contentsDown.coord[1] - configFile['screenHeight'] + originalSizeDown * 1.1 ** zoom
    return correctCoordX, correctCoordY

def zoomIn(contents, configFile, zoom):
    if zoom > 15:
        return contents.coord[0] + (configFile['screenWidth'] / 2 - pygame.mouse.get_pos()[0]) / 10, contents.coord[1] + (configFile['screenHeight'] / 2 - pygame.mouse.get_pos()[1]) / 10
    contents.size = (round(contents.size[0] * 1.1), round(contents.size[1] * 1.1))
    return pygame.mouse.get_pos()[0] - (pygame.mouse.get_pos()[0] - contents.coord[0]) * 1.1, pygame.mouse.get_pos()[1] - (pygame.mouse.get_pos()[1] - contents.coord[1]) * 1.1

def zoomOut(contents, zoom, originalCoord=(0, 0)):
    if zoom >= 0:
        contents.size = (round(contents.size[0] / 1.1), round(contents.size[1] / 1.1))
        return pygame.mouse.get_pos()[0] - (pygame.mouse.get_pos()[0] - contents.coord[0]) / 1.1, pygame.mouse.get_pos()[1] - (pygame.mouse.get_pos()[1] - contents.coord[1]) / 1.1
    return originalCoord

def run(GUI, mode, server, loop, mainLoop, configFile, tradFile, textlocking, infosClients, regions, zoom, moving, regionlocking, gameStarted, regionSelected, selectArmy, armyMove, blockedRegion, gfx):
    for i in pygame.event.get():
        if moving == True:
            rel = pygame.mouse.get_rel()
            
            gfx['serverBackground'].coord = gfx['serverBackground'].coord[0] + rel[0], gfx['serverBackground'].coord[1] + rel[1]
            gfx['serverBackground2'].coord = gfx['serverBackground2'].coord[0] + rel[0], gfx['serverBackground2'].coord[1] + rel[1]
            gfx['serverBackground3'].coord = gfx['serverBackground3'].coord[0] + rel[0], gfx['serverBackground3'].coord[1] + rel[1]
            
        if i.type == pygame.QUIT: server, loop, mainLoop = False, False, False
        elif i.type == pygame.MOUSEBUTTONUP:
            if i.button == 2: moving, rel = False, pygame.mouse.get_rel()
        elif i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                j = GUI.get_at(pygame.mouse.get_pos())
                
                if armyMove and not selectArmy:
                    for k in regions[regionlocking]['border']:
                        if j == regions[k[0]]['rgb']:
                            if regions[k[0]]['owner'] == configFile['ID']:
                                armyMove = False
                                regions[regionlocking]['army'][configFile['ID']]['infantry'] -= int(gfx['serverChooseArmyInfantry'].contents)
                                regions[regionlocking]['army'][configFile['ID']]['cavalry'] -= int(gfx['serverChooseArmyCavalry'].contents)
                                regions[regionlocking]['army'][configFile['ID']]['artillery'] -= int(gfx['serverChooseArmyArtillery'].contents)
                                if regions[regionlocking]['army'][configFile['ID']] == {'infantry': 0, 'cavalry': 0, 'artillery': 0} and regions[regionlocking]['owner'] != configFile['ID']: del regions[regionlocking]['army'][configFile['ID']]
                                if configFile['ID'] in regions[k[0]]['army']:
                                    regions[k[0]]['army'][configFile['ID']]['infantry'] += int(gfx['serverChooseArmyInfantry'].contents)
                                    regions[k[0]]['army'][configFile['ID']]['cavalry'] += int(gfx['serverChooseArmyCavalry'].contents)
                                    regions[k[0]]['army'][configFile['ID']]['artillery'] += int(gfx['serverChooseArmyArtillery'].contents)
                                else:
                                    regions[k[0]]['army'][configFile['ID']]['infantry'] = int(gfx['serverChooseArmyInfantry'].contents)
                                    regions[k[0]]['army'][configFile['ID']]['cavalry'] = int(gfx['serverChooseArmyCavalry'].contents)
                                    regions[k[0]]['army'][configFile['ID']]['artillery'] = int(gfx['serverChooseArmyArtillery'].contents)
                                regionlocking = 'null'
                                blockedRegion.append(k[0])
                            elif regions[k[0]]['owner'] == 'null':
                                print('fdp')
                                armyMove = False
                            else:
                                print('pute mais non')
                                armyMove = False
                
                else:
                
                    if j == (219, 175, 0, 255):
                        if not regionSelected:
                            regionSelected = True
                            regions[regionlocking]['army'][configFile['ID']] = regions[regionlocking]['army']['null']
                            del regions[regionlocking]['army']['null']
                            regions[regionlocking]['owner'] = configFile['ID']
                            regionlocking = 'null'
                        elif selectArmy:
                            textlocking = 'infantry'
                            if int(gfx['serverChooseArmyInfantry'].contents) == 0: gfx['serverChooseArmyInfantry'].contents = ''
                        else:
                            armyMove = True
                            selectArmy = True
                            gfx['serverChooseArmyInfantry'].contents = '0'
                            gfx['serverChooseArmyCavalry'].contents = '0'
                            gfx['serverChooseArmyArtillery'].contents = '0'
                    elif j == (220, 174, 0, 255):
                        if not gameStarted: gameStarted = True
                        elif selectArmy:
                            textlocking = 'cavalry'
                            if int(gfx['serverChooseArmyCavalry'].contents) == 0: gfx['serverChooseArmyCavalry'].contents = ''
                    
                    elif j == (218, 174, 0, 255):
                        if selectArmy:
                            textlocking = 'artillery'
                            if int(gfx['serverChooseArmyArtillery'].contents) == 0: gfx['serverChooseArmyArtillery'].contents = ''
                    
                    elif j == (220, 175, 0, 255):
                        if selectArmy: armyMove, selectArmy = False, False
                    
                    elif j == (219, 173, 0, 255):
                        if int(gfx['serverChooseArmyInfantry'].contents) == 0 and int(gfx['serverChooseArmyCavalry'].contents) == 0 and int(gfx['serverChooseArmyArtillery'].contents) == 0: armyMove, selectArmy = False, False
                        else: selectArmy = False
                    
                    elif selectArmy: textlocking = 'null'
                    
                    else:
                        textlocking = 'null'
                        selectArmy = False
                        armyMove = False
                    
                        regionlocking = 'null'
                        for k in regions:
                            if j == regions[k]['rgb']: regionlocking = k
                        if regionlocking != 'null':
                            gfx['serverTest'].contents = tradFile[7+regionlocking]
                            gfx['serverTest'].coord = (configFile['screenWidth'] / 6 - gfx['serverTest'].get_width() / 2, configFile['screenHeight'] * 0.7 - gfx['serverTest'].get_height() / 2)
                            owner, infantry, cavalry, artillery = 'armies', 'infantry', 'cavalry', 'artillery'
                            if regions[regionlocking]['owner'] == 'null': gfx['serverRegionOwner'].contents = 'owner' + ' : ' + 'bot'
                            elif regions[regionlocking]['owner'] == int(configFile['ID']): gfx['serverRegionOwner'].contents = 'owner' + ' : ' + configFile['name']
                            else:
                                l = gfx['serverRegionOwner'].contents
                                for k in infosClients:
                                    if regions[regionlocking]['owner'] == int(k[2]): gfx['serverRegionOwner'].contents = 'owner' + ' : ' + k[3]
                                if gfx['serverRegionOwner'].contents == l: gfx['serverRegionOwner'].contents = 'owner' + ' : ' + str(regions[regionlocking]['owner'])
                            
                            gfx['serverRegionsRegionFactories'].contents = 'usines' + ' : ' + str(regions[regionlocking]['resources']['factories'])
                            
                            gfx['serverRegionsRegionPopulations'].contents = 'pégus' + ' : ' + str(int(regions[regionlocking]['resources']['populations']['max'] - regions[regionlocking]['resources']['populations']['mobilized'] - regions[regionlocking]['resources']['populations']['dead'])) + '/' + str(regions[regionlocking]['resources']['populations']['max'])
                            
                            for k in regions[regionlocking]['army']:
                                if k == 'null': owner += '\n bot'
                                elif k == int(configFile['ID']): owner += '\n ' + configFile['name']
                                else:
                                    l = owner
                                    for m in infosClients:
                                        if k == int(m[2]): owner += '\n ' + m[3]
                                    if owner == l: owner += '\n ' + str(k)
                                infantry += '\n ' + str(regions[regionlocking]['army'][k]['infantry'])
                                cavalry += '\n ' + str(regions[regionlocking]['army'][k]['cavalry'])
                                artillery +='\n ' +  str(regions[regionlocking]['army'][k]['artillery'])
                            gfx['serverOwner'].contents, gfx['serverInfantry'].contents, gfx['serverCavalry'].contents, gfx['serverArtillery'].contents = owner, infantry, cavalry, artillery
                
                if selectArmy:
                    if textlocking != 'infantry':
                        if gfx['serverChooseArmyInfantry'].contents == '': gfx['serverChooseArmyInfantry'].contents = '0'
                        elif int(gfx['serverChooseArmyInfantry'].contents) > regions[regionlocking]['army'][configFile['ID']]['infantry']: gfx['serverChooseArmyInfantry'].contents = str(regions[regionlocking]['army'][configFile['ID']]['infantry'])
                    if textlocking != 'cavalry':
                        if gfx['serverChooseArmyCavalry'].contents == '': gfx['serverChooseArmyCavalry'].contents = '0'
                        elif int(gfx['serverChooseArmyCavalry'].contents) > regions[regionlocking]['army'][configFile['ID']]['cavalry']: gfx['serverChooseArmyCavalry'].contents = str(regions[regionlocking]['army'][configFile['ID']]['cavalry'])
                    if textlocking != 'artillery':
                        if gfx['serverChooseArmyArtillery'].contents == '': gfx['serverChooseArmyArtillery'].contents = '0'
                        elif int(gfx['serverChooseArmyArtillery'].contents) > regions[regionlocking]['army'][configFile['ID']]['artillery']: gfx['serverChooseArmyArtillery'].contents = str(regions[regionlocking]['army'][configFile['ID']]['artillery'])
                
            elif i.button == 2: moving, rel = True, pygame.mouse.get_rel()
            elif i.button == 4:
                zoom += 1
                
                gfx['serverBackground'].coord = zoomIn(gfx['serverBackground'], configFile, zoom)
                gfx['serverBackground2'].coord = zoomIn(gfx['serverBackground2'], configFile, zoom)
                gfx['serverBackground3'].coord = zoomIn(gfx['serverBackground3'], configFile, zoom)
                
                if zoom > 15: zoom = 15
            elif i.button == 5:
                zoom -= 1
                
                gfx['serverBackground'].coord = zoomOut(gfx['serverBackground'], zoom, (configFile['screenWidth']*2/3, 0))
                gfx['serverBackground2'].coord = zoomOut(gfx['serverBackground2'], zoom)
                gfx['serverBackground3'].coord = zoomOut(gfx['serverBackground3'], zoom, (configFile['screenWidth']*1/3, 0))
                
                if zoom <= 0: zoom = 0
        elif i.type == pygame.KEYDOWN:
            if textlocking == 'infantry':
                if i.unicode in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                    gfx['serverChooseArmyInfantry'].contents += i.unicode
                    if int(gfx['serverChooseArmyInfantry'].contents) > regions[regionlocking]['army'][configFile['ID']]['infantry']: gfx['serverChooseArmyInfantry'].contents = str(regions[regionlocking]['army'][configFile['ID']]['infantry'])
                elif i.key == pygame.K_BACKSPACE: gfx['serverChooseArmyInfantry'].contents = gfx['serverChooseArmyInfantry'].contents[:-1]
            elif textlocking == 'cavalry':
                if i.unicode in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                    gfx['serverChooseArmyCavalry'].contents += i.unicode
                    if int(gfx['serverChooseArmyCavalry'].contents) > regions[regionlocking]['army'][configFile['ID']]['cavalry']: gfx['serverChooseArmyCavalry'].contents = str(regions[regionlocking]['army'][configFile['ID']]['cavalry'])
                elif i.key == pygame.K_BACKSPACE: gfx['serverChooseArmyCavalry'].contents = gfx['serverChooseArmyCavalry'].contents[:-1]
            elif textlocking == 'artillery':
                if i.unicode in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                    gfx['serverChooseArmyArtillery'].contents += i.unicode
                    if int(gfx['serverChooseArmyArtillery'].contents) > regions[regionlocking]['army'][configFile['ID']]['artillery']: gfx['serverChooseArmyArtillery'].contents = str(regions[regionlocking]['army'][configFile['ID']]['artillery'])
                elif i.key == pygame.K_BACKSPACE: gfx['serverChooseArmyArtillery'].contents = gfx['serverChooseArmyArtillery'].contents[:-1]
            elif i.key == pygame.K_ESCAPE:
                if selectArmy: armyMove, selectArmy = False, False
                elif regionlocking != 'null': regionlocking = 'null'
                else:
                    escape = True
                    while escape:
                        for i in pygame.event.get():
                            gfx['escapeBackground'].blit()
                            gfx['escapeYes'].blit()
                            gfx['escapeNo'].blit()
                            gfx['escapeRequest'].blit()
                            pygame.display.flip() #loop les blits
                            if i.type == pygame.QUIT: escape, mode, server = False, 'host', False
                            elif i.type == pygame.MOUSEBUTTONDOWN:
                                j = GUI.get_at(pygame.mouse.get_pos())
                                if j == (220, 174, 0, 255): escape, mode, server = False, 'host', False
                                elif j == (219, 175, 0, 255): escape = False
                            elif i.type == pygame.KEYDOWN:
                                if i.key == pygame.K_ESCAPE: escape = False
                                elif i.key == pygame.K_RETURN or i.key == pygame.K_KP_ENTER: escape, mode, server = False, 'host', False
        if moving == True or (i.type == pygame.MOUSEBUTTONUP and i.button == 2) or (i.type == pygame.MOUSEBUTTONDOWN and (i.button == 4 or i.button == 5)):
            correctCoord = coordCheck(configFile, zoom, gfx['serverBackground'], configFile['screenWidth']/3, gfx['serverBackground2'], gfx['serverBackground'], gfx['serverBackground2'], configFile['screenHeight'])
            
            gfx['serverBackground'].coord = (gfx['serverBackground'].coord[0] - correctCoord[0], gfx['serverBackground'].coord[1] - correctCoord[1])
            gfx['serverBackground2'].coord  = (gfx['serverBackground2'].coord[0] - correctCoord[0], gfx['serverBackground2'].coord[1] - correctCoord[1])
            gfx['serverBackground3'].coord  = (gfx['serverBackground3'].coord[0] - correctCoord[0], gfx['serverBackground3'].coord[1] - correctCoord[1])
            
    return mode, server, loop, mainLoop, textlocking, regions, zoom, moving, regionlocking, gameStarted, regionSelected, selectArmy, armyMove, blockedRegion, gfx