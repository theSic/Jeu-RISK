import pygame, socket, select #init modules
import objs, script.server #init files

def connections(liaison, connectedClients, infosClients):
    requestLiaison, wlist, xlist = select.select([liaison], [], [], 0.05)
    for i in requestLiaison:
        establishingLiaison, infosClient = i.accept()
        connectedClients.append(establishingLiaison)
        print('new client connected, IP : ', infosClient[0], ':', infosClient[1], sep = '')
        establishingLiaison.sendto((infosClient[0] + ';' + str(infosClient[1])).encode(), (infosClient[0], infosClient[1]))
        getPackage = establishingLiaison.recv(1024).decode().split(';')
        for i in infosClients:
            if i[2] == getPackage[2]:
                establishingLiaison.sendto('sameID'.encode(), (infosClient[0], infosClient[1]))
                connectedClients[-1].close()
                del connectedClients[-1]
                print('client kicked (same ID), IP : ', infosClient[0], ':', infosClient[1], sep = '')
        try:
            establishingLiaison.sendto('singleID'.encode(), (infosClient[0], infosClient[1]))
        except:
            pass
        else:
            infosClients.append([infosClient[0], infosClient[1], getPackage[2], getPackage[3]])
    return connectedClients, infosClients

def packages(liaison, connectedClients, infosClients):
    getListPackage = []
    try:
        getListPackage, wlist, xlist = select.select(connectedClients, [], [], 0.05)
    except select.error:
        pass
    else:
        for i in getListPackage:
            try:
                getPackage = i.recv(1024).decode()
            except:
                for i in infosClients:
                    try :
                        liaison.sendto(('ping').encode(), (i[0], i[1]))
                    except:
                        connectedClients[infosClients.index(i)].close()
                        del connectedClients[infosClients.index(i)], infosClients[infosClients.index(i)]
                        print('client disconnected, IP : ', i[0], ':', i[1], sep = '')
            else:
                reply(i, getPackage, infosClients)
    return liaison, connectedClients

def reply(i, getPackage, infosClients):
    if getPackage.split(';')[1] == 'test':
        i.send((str(infosClients)).encode())
    else:
        print(getPackage)
        i.send(('wesh').encode())

def run(GUI, mode, loop, mainLoop, configFile, tradFile, regions, gfx):
    #objs.consoleShow() # montrer la console
    
    #menuBackground = objs.picture(GUI, 'gfx/interface/maprisk.png', (configFile['screenWidth'], configFile['screenHeight']))
    textlocking = 'null'
    zoom = 0
    moving = False
    regionlocking = 'null'
    gameStarted = False
    regionSelected = False
    for i in regions:
        if regions[i]['owner'] == configFile['ID']: regionSelected = True
    selectArmy = False
    armyMove = False
    blockedRegion = []
    
    liaison = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # init la co au saint internet
    liaison.bind(('', configFile['port'])) # init vers qui on s'adreese (pas d'IP donc on heberge à l'IP choisi)
    liaison.listen(5) #mdr je sais plus
    print('server open')
    server, connectedClients, infosClients = True, [], [] #server état # connectedClients infos pour socket (inutile) # infosClients ultra utile
    while server:
        
        connectedClients, infosClients = connections(liaison, connectedClients, infosClients) #invitez les nouveaux pégus
        
        liaison, connectedClients = packages(liaison, connectedClients, infosClients) #gerer les nouvelles requetes
        
        mode, server, loop, mainLoop, textlocking, regions, zoom, moving, regionlocking, gameStarted, regionSelected, selectArmy, armyMove, blockedRegion, gfx = script.server.run(GUI, mode, server, loop, mainLoop, configFile, tradFile, textlocking, infosClients, regions, zoom, moving, regionlocking, gameStarted, regionSelected, selectArmy, armyMove, blockedRegion, gfx)
        
        if not (gfx['serverBackground'].coord[0] > configFile['screenWidth'] or gfx['serverBackground'].coord[1] > configFile['screenHeight'] or gfx['serverBackground'].coord[0] + gfx['serverBackground'].size[0] < 0 or gfx['serverBackground'].coord[1] + gfx['serverBackground'].size[1] < 0): gfx['serverBackground'].blit()
        if not (gfx['serverBackground2'].coord[0] > configFile['screenWidth'] or gfx['serverBackground2'].coord[1] > configFile['screenHeight'] or gfx['serverBackground2'].coord[0] + gfx['serverBackground2'].size[0] < 0 or gfx['serverBackground2'].coord[1] + gfx['serverBackground2'].size[1] < 0): gfx['serverBackground2'].blit()
        if not (gfx['serverBackground3'].coord[0] > configFile['screenWidth'] or gfx['serverBackground3'].coord[1] > configFile['screenHeight'] or gfx['serverBackground3'].coord[0] + gfx['serverBackground3'].size[0] < 0 or gfx['serverBackground3'].coord[1] + gfx['serverBackground3'].size[1] < 0): gfx['serverBackground3'].blit()
        
        if not gameStarted:
            gfx['serverStartGame'].blit()
        if regionlocking != 'null':
            gfx['serverImage'].blit()
            gfx['serverTest'].blit()
            gfx['serverRegionsRegionFactories'].blit()
            gfx['serverRegionsRegionPopulations'].blit()
            gfx['serverRegionOwner'].blit()
            if not gameStarted and not regionSelected and regions[regionlocking]['owner'] == 'null':
                gfx['serverRegionsChoose'].blit()
            elif gameStarted and regionSelected:
                if configFile['ID'] in regions[regionlocking]['army'] and not regionlocking in blockedRegion:
                    gfx['serverRegionsMove'].blit()
                    gfx['serverRegionsTransferArmy'].blit()
                if regions[regionlocking]['owner'] == configFile['ID']:
                    gfx['serverRegionsTransferRegion'].blit()
                else:
                    gfx['serverRegionsAttack'].blit()
            gfx['serverOwner'].blit()
            gfx['serverInfantry'].blit()
            gfx['serverCavalry'].blit()
            gfx['serverArtillery'].blit()
        if selectArmy:
            gfx['serverChooseArmy'].blit()
            gfx['serverChooseArmyRequest'].blit()
            gfx['serverChooseArmyInfantry'].coord = (configFile['screenWidth'] / 2 * 7/9 - gfx['serverChooseArmyInfantry'].get_width() / 2, configFile['screenHeight'] / 2 * 2/3 - gfx['serverChooseArmyInfantry'].get_height() / 2)
            gfx['serverChooseArmyInfantry'].blit()
            gfx['serverChooseArmyCavalry'].coord = (configFile['screenWidth'] / 2 - gfx['serverChooseArmyCavalry'].get_width() / 2, configFile['screenHeight'] / 2 * 2/3 - gfx['serverChooseArmyCavalry'].get_height() / 2)
            gfx['serverChooseArmyCavalry'].blit()
            gfx['serverChooseArmyArtillery'].coord = (configFile['screenWidth'] / 2 * 11/9 - gfx['serverChooseArmyArtillery'].get_width() / 2, configFile['screenHeight'] / 2 * 2/3 - gfx['serverChooseArmyArtillery'].get_height() / 2)
            gfx['serverChooseArmyArtillery'].blit()
            gfx['serverChooseContinue'].blit()
            gfx['serverChooseCancel'].blit()
        
        pygame.display.flip() #loop les blits
    print('server shutdown')
    for i in connectedClients:
        i.send(('server shutdown').encode())
        i.close()
    liaison.close
    print('server closed')
    objs.store('game.save', regions)
    
    gfx['serverBackground'].size = (round(configFile['screenWidth']/3), configFile['screenHeight'])
    gfx['serverBackground'].coord = (configFile['screenWidth']*2/3, 0)
    
    gfx['serverBackground2'].size = (round(configFile['screenWidth']/3), configFile['screenHeight'])
    gfx['serverBackground2'].coord = (0, 0)
    
    gfx['serverBackground3'].size = (round(configFile['screenWidth']/3), configFile['screenHeight'])
    gfx['serverBackground3'].coord = (configFile['screenWidth']*1/3, 0)
    
    return mode, loop, mainLoop