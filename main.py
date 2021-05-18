import pygame, random #init modules
import init, objs, script.menu, script.host, script.settings, script.settingsLocalisation, server #init files

objs.console_hide()
mainLoop = True
while mainLoop:
    try: #initialization
        objs.clear('log.txt') #init log.txt
        objs.write('log.txt', 'game launch\n')
        configFile = init.loadGameConfig() #init configFile
        if configFile['ID'] == 'null': #init l'ID if empty
            configFile['ID'] = random.randint(1, 99999)
            objs.store('game.config', configFile) #store new ID
        tradFile = init.loadLocalisation(configFile['language']) #init tradFile
        objs.write('log.txt', 'loading pygame\n')
        pygame.init() #init pygame
        pygame.display.init()
        GUI = pygame.display.set_mode((configFile['screenWidth'], configFile['screenHeight'])) #init GUI
        pygame.display.set_icon(pygame.image.load('gfx/icon.png')) #init icon
        pygame.display.set_caption('je') #init text icon
        
        objs.write('log.txt', 'loading graphics\n')
        #mainBackground, menuButtons, menuTitle, menuHost, menuJoin, menuSettings, menuQuit = init.loadMenu(GUI, configFile, tradFile) #init menu
        
        #settingsButtons, settingsTitleName, settingsName, settingsResolution, settingsWidth, settingsHeight, settingsTrad, settingsQuit = init.loadSettings(GUI, configFile, tradFile) #init settings
        
        #settingsLocalisationButtons, settingsLocalisationENG, settingsLocalisationFRA = init.loadSettingsLocalisation(GUI, configFile, tradFile) #init settingsLocalisation
        
        #hostButtons, hostSave, hostNoSave, hostTitlePort, hostPort, hostQuit = init.loadHost(GUI, configFile, tradFile) #init host
        
        #escapeBackground, escapeRequest, escapeYes, escapeNo = init.loadEscape(GUI, configFile) #init escape
        
        #serverBackground, serverBackground2, serverBackground3, serverImage, serverTest, serverRegionsRegionFactories, serverRegionsRegionPopulations, serverRegionOwner, serverRegionsMove, serverRegionsAttack, serverRegionsTransferArmy, serverRegionsTransferRegion, serverOwner, serverInfantry, serverCavalry, serverArtillery, serverRegionsChoose, serverStartGame, serverChooseArmy, serverChooseArmyRequest, serverChooseArmyInfantry, serverChooseArmyCavalry, serverChooseArmyArtillery, serverChooseContinue, serverChooseCancel = init.loadServer(GUI, configFile) #init server
        
        gfx = init.loadGfx(GUI, configFile, tradFile)
        
    except Exception as e:
        mainLoop = False
        pygame.quit() #stop pygame
        try: objs.write('log.txt', 'ERROR: game launch has failed (exact error :"' + str(e) + '")')
        except:
            objs.clear('log.txt')
            objs.write('log.txt', 'ERROR: game launch has failed (exact error :"' + str(e) + '")')
    else:
        objs.write('log.txt', 'loaded game')
        loop = True
        textlocking = 'null'
        mode = 'menu'
        configFile_screenWidth = str(configFile['screenWidth'])
        configFile_screenHeight = str(configFile['screenHeight'])
        while loop:
            if mode == 'menu':
                gfx['mainBackground'].blit()
                gfx['menuButtons'].blit()
                gfx['menuTitle'].blit()
                gfx['menuHost'].blit()
                gfx['menuJoin'].blit()
                gfx['menuSettings'].blit()
                gfx['menuQuit'].blit()
                pygame.display.flip() #loop les blits
                mode, loop, mainLoop = script.menu.run(GUI, mode, loop, mainLoop, gfx)
            elif mode == 'settings':
                gfx['settingsName'].contents = configFile['name']
                gfx['settingsName'].coord = (configFile['screenWidth'] / 2 - gfx['settingsName'].get_width() / 2, configFile['screenHeight'] * 0.25 - gfx['settingsName'].get_height() / 2)
                
                gfx['settingsWidth'].contents = configFile_screenWidth
                gfx['settingsWidth'].coord = (configFile['screenWidth'] / 2 - configFile['screenWidth'] / 15 - gfx['settingsWidth'].get_width() / 2, configFile['screenHeight'] * 0.5 - gfx['settingsWidth'].get_height() / 2)
                
                gfx['settingsHeight'].contents = configFile_screenHeight
                gfx['settingsHeight'].coord = (configFile['screenWidth'] / 2 + configFile['screenWidth'] / 15 - gfx['settingsHeight'].get_width() / 2, configFile['screenHeight'] * 0.5 - gfx['settingsWidth'].get_height() / 2)
                
                gfx['mainBackground'].blit()
                gfx['settingsButtons'].blit()
                gfx['settingsTitleName'].blit()
                gfx['settingsName'].blit()
                gfx['settingsResolution'].blit()
                gfx['settingsWidth'].blit()
                gfx['settingsHeight'].blit()
                gfx['settingsTrad'].blit()
                gfx['settingsQuit'].blit()
                pygame.display.flip() #loop les blits
                mode, loop, mainLoop, configFile_screenWidth, configFile_screenHeight, configFile, textlocking = script.settings.run(GUI, mode, loop, mainLoop, configFile_screenWidth, configFile_screenHeight, configFile, textlocking)
            elif mode == 'settingsLocalisation':
                gfx['mainBackground'].blit()
                gfx['settingsLocalisationButtons'].blit()
                gfx['settingsLocalisationENG'].blit()
                gfx['settingsLocalisationFRA'].blit()
                pygame.display.flip() #loop les blits
                mode, loop, mainLoop = script.settingsLocalisation.run(GUI, mode, loop, mainLoop, configFile)
            elif mode == 'host': #hostButtons, hostSave, hostNoSave, hostTitlePort, hostQuit
                hostPort.contents = str(configFile['port'])
                hostPort.coord = (configFile['screenWidth'] / 2 - hostPort.get_width() / 2, configFile['screenHeight'] * 0.7 - hostPort.get_height() / 2)
                
                gfx['mainBackground'].blit()
                gfx['hostButtons'].blit()
                try: objs.read_dico('game.save')
                except: gfx['hostSave'].color = (167, 155, 113)
                else: gfx['hostSave'].color = (218, 174, 0)
                gfx['hostSave'].blit()
                gfx['hostNoSave'].blit()
                gfx['hostTitlePort'].blit()
                gfx['hostPort'].blit()
                gfx['hostQuit'].blit()
                pygame.display.flip() #loop les blits
                
                mode, loop, mainLoop, configFile, textlocking, regions = script.host.run(GUI, mode, loop, mainLoop, configFile, textlocking)
            elif mode == 'server':
                #serverBackground.blit()
                #pygame.display.flip() #loop les blits
                
                mode, loop, mainLoop = server.run(GUI, mode, loop, mainLoop, configFile, tradFile, regions, gfx)
        pygame.display.quit() #stop la fenètre
pygame.quit() #stop pygame
