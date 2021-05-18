import pickle, pygame #init modules
import objs #init files

def loadGameConfig(): #load et vérif game.config
    objs.write('log.txt', 'loading game.config\n')
    configFile = {
    'language': 'FRA',
    'port': 33000,
    'name': 'Player',
    'ID': 'null',
    'screenWidth': 800,
    'screenHeight': 600,
    }
    try: configFile = objs.read_dico('game.config')
    except EOFError:
        objs.store('game.config', configFile)
        objs.write('log.txt', 'ERROR: game.config file is empty, file reset\n')
    except pickle.UnpicklingError:
        objs.store('game.config', configFile)
        objs.write('log.txt', 'ERROR: game.config file is corrupted, file reset\n')
    except Exception as e:
        objs.store('game.config', configFile)
        objs.write('log.txt', 'ERROR: game.config file had to be deleted (exact error :"' + str(e) + '"), file reset\n')
    return configFile

def loadLocalisation(configFile_language): #load et vérif localisation
    objs.write('log.txt', 'loading localisations\n')
    tradFile = []
    try: tradFile = objs.read_list('localisation/' + configFile_language + '.trad')
    except Exception as e: objs.write('log.txt', 'ERROR: ' + configFile_language + '.trad file had to be deleted (exact error :"' + str(e) + '")\n')
    for i in range(7): tradFile.append('null') #nombre de ligne en trad
    return tradFile
"""
def loadMenu(GUI, configFile, tradFile):
    mainBackground = objs.Picture(GUI, 'gfx/interface/background.png', (configFile['screenWidth'], configFile['screenHeight']))
    
    menuButtons = objs.Picture(GUI, 'gfx/interface/buttons/menu.png', (configFile['screenWidth'], configFile['screenHeight']))
    
    menuTitle = objs.Text(GUI, 'gépété', (219, 174, 0), int(configFile['screenHeight'] / 6))
    menuTitle.coord = (configFile['screenWidth'] / 2 - menuTitle.get_width() / 2, configFile['screenHeight'] * 0.1 - menuTitle.get_height() / 2)
    
    menuHost = objs.Text(GUI, tradFile[0], (220, 174, 0), int(configFile['screenHeight'] / 8))
    menuHost.coord = (configFile['screenWidth'] / 2 - menuHost.get_width() / 2, configFile['screenHeight'] * 0.3 - menuHost.get_height() / 2)
    
    menuJoin = objs.Text(GUI, tradFile[1], (219, 175, 0), int(configFile['screenHeight'] / 8))
    menuJoin.coord = (configFile['screenWidth'] / 2 - menuJoin.get_width() / 2, configFile['screenHeight'] * 0.475 - menuJoin.get_height() / 2)
    
    menuSettings = objs.Text(GUI, tradFile[2], (219, 174, 1), int(configFile['screenHeight'] / 8))
    menuSettings.coord = (configFile['screenWidth'] / 2 - menuSettings.get_width() / 2, configFile['screenHeight'] * 0.65 - menuSettings.get_height() / 2)
    
    menuQuit = objs.Text(GUI, tradFile[3], (218, 174, 0), int(configFile['screenHeight'] / 8))
    menuQuit.coord = (configFile['screenWidth'] / 2 - menuQuit.get_width() / 2, configFile['screenHeight'] * 0.825 - menuQuit.get_height() / 2)
    
    return mainBackground, menuButtons, menuTitle, menuHost, menuJoin, menuSettings, menuQuit

def loadSettings(GUI, configFile, tradFile):
    settingsButtons = objs.Picture(GUI, 'gfx/icon.png', (configFile['screenWidth'], configFile['screenHeight']))
    
    settingsTitleName = objs.Text(GUI, tradFile[5], (218, 174, 0), int(configFile['screenHeight'] / 8))
    settingsTitleName.coord = (configFile['screenWidth'] / 2 - settingsTitleName.get_width() / 2, configFile['screenHeight'] * 0.15 - settingsTitleName.get_height() / 2)
    
    settingsName = objs.Text(GUI, configFile['name'], (220, 174, 0), int(configFile['screenHeight'] / 12))
    settingsName.coord = (configFile['screenWidth'] / 2 - settingsName.get_width() / 2, configFile['screenHeight'] * 0.25 - settingsName.get_height() / 2)
    
    settingsResolution = objs.Text(GUI, tradFile[4], (219, 173, 0), int(configFile['screenHeight'] / 8))
    settingsResolution.coord = (configFile['screenWidth'] / 2 - settingsResolution.get_width() / 2, configFile['screenHeight'] * 0.4 - settingsResolution.get_height() / 2)
    
    settingsWidth = objs.Text(GUI, str(configFile['screenWidth']), (219, 175, 0), int(configFile['screenHeight'] / 12))
    settingsWidth.coord = (configFile['screenWidth'] / 2 - configFile['screenWidth'] / 15 - settingsWidth.get_width() / 2, configFile['screenHeight'] * 0.5 - settingsWidth.get_height() / 2)
    
    settingsHeight = objs.Text(GUI, str(configFile['screenHeight']), (219, 174, 1), int(configFile['screenHeight'] / 12))
    settingsHeight.coord = (configFile['screenWidth'] / 2 + configFile['screenWidth'] / 15 - settingsHeight.get_width() / 2, configFile['screenHeight'] * 0.5 - settingsWidth.get_height() / 2)
    
    settingsTrad = objs.Text(GUI, tradFile[6], (220, 175, 0), int(configFile['screenHeight'] / 8))
    settingsTrad.coord = (configFile['screenWidth'] / 2 - settingsTrad.get_width() / 2, configFile['screenHeight'] * 0.65 - settingsResolution.get_height() / 2)
    
    settingsQuit = objs.Text(GUI, tradFile[3], (219, 174, 0), int(configFile['screenHeight'] / 8))
    settingsQuit.coord = (configFile['screenWidth'] / 2 - settingsQuit.get_width() / 2, configFile['screenHeight'] * 0.85 - settingsQuit.get_height() / 2)
    
    return settingsButtons, settingsTitleName, settingsName, settingsResolution, settingsWidth, settingsHeight, settingsTrad, settingsQuit

def loadSettingsLocalisation(GUI, configFile, tradFile):
    settingsLocalisationButtons = objs.Picture(GUI, 'gfx/interface/buttons/settingsLocalisation.png', (configFile['screenWidth'], configFile['screenHeight']))
    
    settingsLocalisationENG = objs.Text(GUI, tradFile[8], (220, 174, 0), int(configFile['screenHeight'] / 12))
    settingsLocalisationENG.coord = (configFile['screenWidth'] / 2 - configFile['screenWidth'] / 4 - settingsLocalisationENG.get_width() / 2, configFile['screenHeight'] * 0.05 - settingsLocalisationENG.get_height() / 2)
    
    settingsLocalisationFRA = objs.Text(GUI, tradFile[7], (219, 174, 0), int(configFile['screenHeight'] / 12))
    settingsLocalisationFRA.coord = (configFile['screenWidth'] / 2 + configFile['screenWidth'] / 4 - settingsLocalisationFRA.get_width() / 2, configFile['screenHeight'] * 0.15 - settingsLocalisationFRA.get_height() / 2)
    
    return settingsLocalisationButtons, settingsLocalisationENG, settingsLocalisationFRA

def loadHost(GUI, configFile, tradFile):
    hostButtons = objs.Picture(GUI, 'gfx/interface/buttons/host2.png', (configFile['screenWidth'], configFile['screenHeight']))
    
    hostSave = objs.Text(GUI, tradFile[11], (218, 174, 0), int(configFile['screenHeight'] / 8))
    hostSave.coord = (configFile['screenWidth'] / 2 - hostSave.get_width() / 2, configFile['screenHeight'] * 0.2 - hostSave.get_height() / 2)
    
    hostNoSave = objs.Text(GUI, tradFile[10], (219, 174, 1), int(configFile['screenHeight'] / 8))
    hostNoSave.coord = (configFile['screenWidth'] / 2 - hostNoSave.get_width() / 2, configFile['screenHeight'] * 0.4 - hostNoSave.get_height() / 2)
    
    hostTitlePort = objs.Text(GUI, tradFile[9], (219, 175, 0), int(configFile['screenHeight'] / 8))
    hostTitlePort.coord = (configFile['screenWidth'] / 2 - hostTitlePort.get_width() / 2, configFile['screenHeight'] * 0.6 - hostTitlePort.get_height() / 2)
    
    hostPort = objs.Text(GUI, str(configFile['port']), (220, 174, 0), int(configFile['screenHeight'] / 12))
    hostPort.coord = (configFile['screenWidth'] / 2 - hostPort.get_width() / 2, configFile['screenHeight'] * 0.7 - hostPort.get_height() / 2)
    
    hostQuit = objs.Text(GUI, tradFile[3], (219, 174, 0), int(configFile['screenHeight'] / 8))
    hostQuit.coord = (configFile['screenWidth'] / 2 - hostQuit.get_width() / 2, configFile['screenHeight'] * 0.85 - hostQuit.get_height() / 2)
    
    return hostButtons, hostSave, hostNoSave, hostTitlePort, hostPort, hostQuit

def loadEscape(GUI, configFile):
    escapeBackground = objs.Picture(GUI, 'gfx/icon.png', (round(configFile['screenWidth']*2/3), round(configFile['screenHeight']/3)), (configFile['screenWidth']*1/6, configFile['screenHeight']*1/3))
    
    escapeRequest = objs.Text(GUI, 'T sur de partir wsh ?', (219, 174, 0), int(configFile['screenHeight'] / 12))
    escapeRequest.coord = (configFile['screenWidth'] / 2 - escapeRequest.get_width() / 2, configFile['screenHeight']*2/5 - escapeRequest.get_height() / 2)
    
    escapeYes = objs.Text(GUI, 'Oui', (220, 174, 0), int(configFile['screenHeight'] / 8))
    escapeYes.coord = (configFile['screenWidth'] / 2 * 2/3 - escapeYes.get_width() / 2, configFile['screenHeight']*4/7 - escapeYes.get_height() / 2)
    
    escapeNo = objs.Text(GUI, 'Nope', (219, 175, 0), int(configFile['screenHeight'] / 8))
    escapeNo.coord = (configFile['screenWidth'] / 2 * 4/3 - escapeNo.get_width() / 2, configFile['screenHeight']*4/7 - escapeNo.get_height() / 2)
    
    return escapeBackground, escapeRequest, escapeYes, escapeNo

def loadServer(GUI, configFile):
    serverBackground = objs.Picture(GUI, 'gfx/interface/maprisk2.png', (configFile['screenWidth'], configFile['screenHeight']))
    serverBackground.contents = pygame.image.load('gfx/interface/droite.png')
    serverBackground.coord = (configFile['screenWidth']*2/3, 0)
    serverBackground.size = (round(configFile['screenWidth']/3), configFile['screenHeight'])
    
    serverBackground2 = objs.Picture(GUI, 'gfx/interface/gauche.png', (round(configFile['screenWidth']/3), configFile['screenHeight']))
    serverBackground3 = objs.Picture(GUI, 'gfx/interface/centre.png', (round(configFile['screenWidth']/3), configFile['screenHeight']), (configFile['screenWidth']*1/3, 0))
    
    serverImage = objs.Picture(GUI, 'gfx/icon.png', (round(configFile['screenWidth']/3), round(configFile['screenHeight']/3)), (0, configFile['screenHeight']*2/3))
    
    serverTest = objs.Text(GUI, 'null', (219, 174, 0), int(configFile['screenHeight'] / 20))
    #serverTest.coord = (configFile['screenWidth'] / 2 - serverTest.get_width() / 2, configFile['screenHeight'] * 0.6 - serverTest.get_height() / 2)
    
    serverRegionsRegionFactories = objs.Text(GUI, 'usines'+' : ', (219, 174, 0), int(configFile['screenHeight'] / 30))
    serverRegionsRegionFactories.coord = (configFile['screenWidth'] / 6 * 0.25 - serverRegionsRegionFactories.get_width() / 2, configFile['screenHeight'] * 0.75 - serverRegionsRegionFactories.get_height() / 2)
    
    serverRegionsRegionPopulations = objs.Text(GUI, 'pégus'+' : ', (219, 174, 0), int(configFile['screenHeight'] / 30))
    serverRegionsRegionPopulations.coord = (configFile['screenWidth'] / 6 * 0.75 - serverRegionsRegionPopulations.get_width() / 2, configFile['screenHeight'] * 0.75 - serverRegionsRegionPopulations.get_height() / 2)
    
    serverRegionOwner = objs.Text(GUI, 'owner'+' : ', (219, 174, 0), int(configFile['screenHeight'] / 30))
    serverRegionOwner.coord = (configFile['screenWidth'] / 6 * 1.25 - serverRegionOwner.get_width() / 2, configFile['screenHeight'] * 0.75 - serverRegionOwner.get_height() / 2)
    
    serverRegionsMove = objs.Text(GUI, 'déplacement', (219, 175, 0), int(configFile['screenHeight'] / 30))
    serverRegionsMove.coord = (configFile['screenWidth'] / 6 * 2/5 - serverRegionsMove.get_width() / 2, configFile['screenHeight'] * 0.7875 - serverRegionsMove.get_height() / 2)
    
    serverRegionsAttack = objs.Text(GUI, 'attaquer', (219, 174, 0), int(configFile['screenHeight'] / 25))
    serverRegionsAttack.coord = (configFile['screenWidth'] / 6 * 8/5 - serverRegionsAttack.get_width() / 2, configFile['screenHeight'] * 0.7875 - serverRegionsAttack.get_height() / 2)
    
    serverRegionsTransferArmy = objs.Text(GUI, 'TransferArmy', (219, 174, 0), int(configFile['screenHeight'] / 30))
    serverRegionsTransferArmy.coord = (configFile['screenWidth'] / 6 * 1 - serverRegionsTransferArmy.get_width() / 2, configFile['screenHeight'] * 0.7875 - serverRegionsTransferArmy.get_height() / 2)
    
    serverRegionsTransferRegion = objs.Text(GUI, 'TransferRegion', (219, 174, 0), int(configFile['screenHeight'] / 30))
    serverRegionsTransferRegion.coord = (configFile['screenWidth'] / 6 * 8/5 - serverRegionsTransferRegion.get_width() / 2, configFile['screenHeight'] * 0.7875 - serverRegionsTransferRegion.get_height() / 2)
    
    serverOwner = objs.Text(GUI, 'armies', (219, 174, 0), int(configFile['screenHeight'] / 30))
    serverOwner.coord = (configFile['screenWidth'] / 6 * 0.25 - serverOwner.get_width() / 2, configFile['screenHeight'] * 0.825 - serverOwner.get_height() / 2)
    
    serverInfantry = objs.Text(GUI, 'infantry', (219, 174, 0), int(configFile['screenHeight'] / 30))
    serverInfantry.coord = (configFile['screenWidth'] / 6 * 0.75 - serverInfantry.get_width() / 2, configFile['screenHeight'] * 0.825 - serverInfantry.get_height() / 2)
    
    serverCavalry = objs.Text(GUI, 'cavalry', (219, 174, 0), int(configFile['screenHeight'] / 30))
    serverCavalry.coord = (configFile['screenWidth'] / 6 * 1.25 - serverCavalry.get_width() / 2, configFile['screenHeight'] * 0.825 - serverCavalry.get_height() / 2)
    
    serverArtillery = objs.Text(GUI, 'artillery', (219, 174, 0), int(configFile['screenHeight'] / 30))
    serverArtillery.coord = (configFile['screenWidth'] / 6 * 1.75 - serverArtillery.get_width() / 2, configFile['screenHeight'] * 0.825 - serverArtillery.get_height() / 2)
    
    serverRegionsChoose = objs.Text(GUI, 'choisi moi fdp', (219, 175, 0), int(configFile['screenHeight'] / 25))
    serverRegionsChoose.coord = (configFile['screenWidth'] / 6 - serverRegionsChoose.get_width() / 2, configFile['screenHeight'] * 0.7875 - serverRegionsChoose.get_height() / 2)
    
    serverStartGame = objs.Text(GUI, 'start the game wsh', (220, 174, 0), int(configFile['screenHeight'] / 25))
    serverStartGame.coord = (configFile['screenWidth'] / 6 - serverStartGame.get_width() / 2, configFile['screenHeight'] / 2 - serverStartGame.get_height() / 2)
    
    serverChooseArmy = objs.Picture(GUI, 'gfx/icon.png', (round(configFile['screenWidth']*1/3), round(configFile['screenHeight']*1/3)), (configFile['screenWidth']*1/3, configFile['screenHeight']*1/6))
    
    serverChooseArmyRequest = objs.Text(GUI, 'CMB tu en prend frer', (219, 174, 0), int(configFile['screenHeight'] / 20))
    serverChooseArmyRequest.coord = (configFile['screenWidth'] / 2 - serverChooseArmyRequest.get_width() / 2, configFile['screenHeight'] / 2 * 2/5 - serverChooseArmyRequest.get_height() / 2)
    
    serverChooseArmyInfantry = objs.Text(GUI, '0', (219, 175, 0), int(configFile['screenHeight'] / 20))
    
    serverChooseArmyCavalry = objs.Text(GUI, '0', (220, 174, 0), int(configFile['screenHeight'] / 20))
    
    serverChooseArmyArtillery = objs.Text(GUI, '0', (218, 174, 0), int(configFile['screenHeight'] / 20))
    
    serverChooseContinue = objs.Text(GUI, 'continuer', (219, 173, 0), int(configFile['screenHeight'] / 20))
    serverChooseContinue.coord = (configFile['screenWidth'] / 2 * 15/18 - serverChooseContinue.get_width() / 2, configFile['screenHeight'] / 2 * 9/10 - serverChooseContinue.get_height() / 2)
    
    serverChooseCancel = objs.Text(GUI, 'annuler', (220, 175, 0), int(configFile['screenHeight'] / 20))
    serverChooseCancel.coord = (configFile['screenWidth'] / 2 * 21/18 - serverChooseCancel.get_width() / 2, configFile['screenHeight'] / 2 * 9/10 - serverChooseCancel.get_height() / 2)
    
    return serverBackground, serverBackground2, serverBackground3, serverImage, serverTest, serverRegionsRegionFactories, serverRegionsRegionPopulations, serverRegionOwner, serverRegionsMove, serverRegionsAttack, serverRegionsTransferArmy, serverRegionsTransferRegion, serverOwner, serverInfantry, serverCavalry, serverArtillery, serverRegionsChoose, serverStartGame, serverChooseArmy, serverChooseArmyRequest, serverChooseArmyInfantry, serverChooseArmyCavalry, serverChooseArmyArtillery, serverChooseContinue, serverChooseCancel
"""







def loadGfx(GUI, configFile, tradFile):

    #loadMenu(GUI, configFile, tradFile):
    
    mainBackground = objs.Picture(GUI, 'gfx/interface/background.png', (configFile['screenWidth'], configFile['screenHeight']))
    
    menuButtons = objs.Picture(GUI, 'gfx/interface/buttons/menu.png', (configFile['screenWidth'], configFile['screenHeight']))
    
    menuTitle = objs.Text(GUI, 'gépété', (219, 174, 0), int(configFile['screenHeight'] / 6))
    menuTitle.coord = (configFile['screenWidth'] / 2 - menuTitle.get_width() / 2, configFile['screenHeight'] * 0.1 - menuTitle.get_height() / 2)
    
    menuHost = objs.Text(GUI, tradFile[0], (220, 174, 0), int(configFile['screenHeight'] / 8))
    menuHost.coord = (configFile['screenWidth'] / 2 - menuHost.get_width() / 2, configFile['screenHeight'] * 0.3 - menuHost.get_height() / 2)
    
    menuJoin = objs.Text(GUI, tradFile[1], (219, 175, 0), int(configFile['screenHeight'] / 8))
    menuJoin.coord = (configFile['screenWidth'] / 2 - menuJoin.get_width() / 2, configFile['screenHeight'] * 0.475 - menuJoin.get_height() / 2)
    
    menuSettings = objs.Text(GUI, tradFile[2], (219, 174, 1), int(configFile['screenHeight'] / 8))
    menuSettings.coord = (configFile['screenWidth'] / 2 - menuSettings.get_width() / 2, configFile['screenHeight'] * 0.65 - menuSettings.get_height() / 2)
    
    menuQuit = objs.Text(GUI, tradFile[3], (218, 174, 0), int(configFile['screenHeight'] / 8))
    menuQuit.coord = (configFile['screenWidth'] / 2 - menuQuit.get_width() / 2, configFile['screenHeight'] * 0.825 - menuQuit.get_height() / 2)
    
    #def loadSettings(GUI, configFile, tradFile):
    
    settingsButtons = objs.Picture(GUI, 'gfx/icon.png', (configFile['screenWidth'], configFile['screenHeight']))
    
    settingsTitleName = objs.Text(GUI, tradFile[5], (218, 174, 0), int(configFile['screenHeight'] / 8))
    settingsTitleName.coord = (configFile['screenWidth'] / 2 - settingsTitleName.get_width() / 2, configFile['screenHeight'] * 0.15 - settingsTitleName.get_height() / 2)
    
    settingsName = objs.Text(GUI, configFile['name'], (220, 174, 0), int(configFile['screenHeight'] / 12))
    settingsName.coord = (configFile['screenWidth'] / 2 - settingsName.get_width() / 2, configFile['screenHeight'] * 0.25 - settingsName.get_height() / 2)
    
    settingsResolution = objs.Text(GUI, tradFile[4], (219, 173, 0), int(configFile['screenHeight'] / 8))
    settingsResolution.coord = (configFile['screenWidth'] / 2 - settingsResolution.get_width() / 2, configFile['screenHeight'] * 0.4 - settingsResolution.get_height() / 2)
    
    settingsWidth = objs.Text(GUI, str(configFile['screenWidth']), (219, 175, 0), int(configFile['screenHeight'] / 12))
    settingsWidth.coord = (configFile['screenWidth'] / 2 - configFile['screenWidth'] / 15 - settingsWidth.get_width() / 2, configFile['screenHeight'] * 0.5 - settingsWidth.get_height() / 2)
    
    settingsHeight = objs.Text(GUI, str(configFile['screenHeight']), (219, 174, 1), int(configFile['screenHeight'] / 12))
    settingsHeight.coord = (configFile['screenWidth'] / 2 + configFile['screenWidth'] / 15 - settingsHeight.get_width() / 2, configFile['screenHeight'] * 0.5 - settingsWidth.get_height() / 2)
    
    settingsTrad = objs.Text(GUI, tradFile[6], (220, 175, 0), int(configFile['screenHeight'] / 8))
    settingsTrad.coord = (configFile['screenWidth'] / 2 - settingsTrad.get_width() / 2, configFile['screenHeight'] * 0.65 - settingsResolution.get_height() / 2)
    
    settingsQuit = objs.Text(GUI, tradFile[3], (219, 174, 0), int(configFile['screenHeight'] / 8))
    settingsQuit.coord = (configFile['screenWidth'] / 2 - settingsQuit.get_width() / 2, configFile['screenHeight'] * 0.85 - settingsQuit.get_height() / 2)
    
    #def loadSettingsLocalisation(GUI, configFile, tradFile):
    
    settingsLocalisationButtons = objs.Picture(GUI, 'gfx/interface/buttons/settingsLocalisation.png', (configFile['screenWidth'], configFile['screenHeight']))
    
    settingsLocalisationENG = objs.Text(GUI, tradFile[8], (220, 174, 0), int(configFile['screenHeight'] / 12))
    settingsLocalisationENG.coord = (configFile['screenWidth'] / 2 - configFile['screenWidth'] / 4 - settingsLocalisationENG.get_width() / 2, configFile['screenHeight'] * 0.05 - settingsLocalisationENG.get_height() / 2)
    
    settingsLocalisationFRA = objs.Text(GUI, tradFile[7], (219, 174, 0), int(configFile['screenHeight'] / 12))
    settingsLocalisationFRA.coord = (configFile['screenWidth'] / 2 + configFile['screenWidth'] / 4 - settingsLocalisationFRA.get_width() / 2, configFile['screenHeight'] * 0.15 - settingsLocalisationFRA.get_height() / 2)
    
    #def loadHost(GUI, configFile, tradFile):
    
    hostButtons = objs.Picture(GUI, 'gfx/interface/buttons/host2.png', (configFile['screenWidth'], configFile['screenHeight']))
    
    hostSave = objs.Text(GUI, tradFile[11], (218, 174, 0), int(configFile['screenHeight'] / 8))
    hostSave.coord = (configFile['screenWidth'] / 2 - hostSave.get_width() / 2, configFile['screenHeight'] * 0.2 - hostSave.get_height() / 2)
    
    hostNoSave = objs.Text(GUI, tradFile[10], (219, 174, 1), int(configFile['screenHeight'] / 8))
    hostNoSave.coord = (configFile['screenWidth'] / 2 - hostNoSave.get_width() / 2, configFile['screenHeight'] * 0.4 - hostNoSave.get_height() / 2)
    
    hostTitlePort = objs.Text(GUI, tradFile[9], (219, 175, 0), int(configFile['screenHeight'] / 8))
    hostTitlePort.coord = (configFile['screenWidth'] / 2 - hostTitlePort.get_width() / 2, configFile['screenHeight'] * 0.6 - hostTitlePort.get_height() / 2)
    
    hostPort = objs.Text(GUI, str(configFile['port']), (220, 174, 0), int(configFile['screenHeight'] / 12))
    hostPort.coord = (configFile['screenWidth'] / 2 - hostPort.get_width() / 2, configFile['screenHeight'] * 0.7 - hostPort.get_height() / 2)
    
    hostQuit = objs.Text(GUI, tradFile[3], (219, 174, 0), int(configFile['screenHeight'] / 8))
    hostQuit.coord = (configFile['screenWidth'] / 2 - hostQuit.get_width() / 2, configFile['screenHeight'] * 0.85 - hostQuit.get_height() / 2)
    
    #def loadEscape(GUI, configFile):
    
    escapeBackground = objs.Picture(GUI, 'gfx/icon.png', (round(configFile['screenWidth']*2/3), round(configFile['screenHeight']/3)), (configFile['screenWidth']*1/6, configFile['screenHeight']*1/3))
    
    escapeRequest = objs.Text(GUI, 'T sur de partir wsh ?', (219, 174, 0), int(configFile['screenHeight'] / 12))
    escapeRequest.coord = (configFile['screenWidth'] / 2 - escapeRequest.get_width() / 2, configFile['screenHeight']*2/5 - escapeRequest.get_height() / 2)
    
    escapeYes = objs.Text(GUI, 'Oui', (220, 174, 0), int(configFile['screenHeight'] / 8))
    escapeYes.coord = (configFile['screenWidth'] / 2 * 2/3 - escapeYes.get_width() / 2, configFile['screenHeight']*4/7 - escapeYes.get_height() / 2)
    
    escapeNo = objs.Text(GUI, 'Nope', (219, 175, 0), int(configFile['screenHeight'] / 8))
    escapeNo.coord = (configFile['screenWidth'] / 2 * 4/3 - escapeNo.get_width() / 2, configFile['screenHeight']*4/7 - escapeNo.get_height() / 2)
    
    #def loadServer(GUI, configFile):
    
    serverBackground = objs.Picture(GUI, 'gfx/interface/maprisk2.png', (configFile['screenWidth'], configFile['screenHeight']))
    serverBackground.contents = pygame.image.load('gfx/interface/droite.png')
    serverBackground.coord = (configFile['screenWidth']*2/3, 0)
    serverBackground.size = (round(configFile['screenWidth']/3), configFile['screenHeight'])
    
    serverBackground2 = objs.Picture(GUI, 'gfx/interface/gauche.png', (round(configFile['screenWidth']/3), configFile['screenHeight']))
    serverBackground3 = objs.Picture(GUI, 'gfx/interface/centre.png', (round(configFile['screenWidth']/3), configFile['screenHeight']), (configFile['screenWidth']*1/3, 0))
    
    serverImage = objs.Picture(GUI, 'gfx/icon.png', (round(configFile['screenWidth']/3), round(configFile['screenHeight']/3)), (0, configFile['screenHeight']*2/3))
    
    serverTest = objs.Text(GUI, 'null', (219, 174, 0), int(configFile['screenHeight'] / 20))
    #serverTest.coord = (configFile['screenWidth'] / 2 - serverTest.get_width() / 2, configFile['screenHeight'] * 0.6 - serverTest.get_height() / 2)
    
    serverRegionsRegionFactories = objs.Text(GUI, 'usines'+' : ', (219, 174, 0), int(configFile['screenHeight'] / 30))
    serverRegionsRegionFactories.coord = (configFile['screenWidth'] / 6 * 0.25 - serverRegionsRegionFactories.get_width() / 2, configFile['screenHeight'] * 0.75 - serverRegionsRegionFactories.get_height() / 2)
    
    serverRegionsRegionPopulations = objs.Text(GUI, 'pégus'+' : ', (219, 174, 0), int(configFile['screenHeight'] / 30))
    serverRegionsRegionPopulations.coord = (configFile['screenWidth'] / 6 * 0.75 - serverRegionsRegionPopulations.get_width() / 2, configFile['screenHeight'] * 0.75 - serverRegionsRegionPopulations.get_height() / 2)
    
    serverRegionOwner = objs.Text(GUI, 'owner'+' : ', (219, 174, 0), int(configFile['screenHeight'] / 30))
    serverRegionOwner.coord = (configFile['screenWidth'] / 6 * 1.25 - serverRegionOwner.get_width() / 2, configFile['screenHeight'] * 0.75 - serverRegionOwner.get_height() / 2)
    
    serverRegionsMove = objs.Text(GUI, 'déplacement', (219, 175, 0), int(configFile['screenHeight'] / 30))
    serverRegionsMove.coord = (configFile['screenWidth'] / 6 * 2/5 - serverRegionsMove.get_width() / 2, configFile['screenHeight'] * 0.7875 - serverRegionsMove.get_height() / 2)
    
    serverRegionsAttack = objs.Text(GUI, 'attaquer', (219, 174, 0), int(configFile['screenHeight'] / 25))
    serverRegionsAttack.coord = (configFile['screenWidth'] / 6 * 8/5 - serverRegionsAttack.get_width() / 2, configFile['screenHeight'] * 0.7875 - serverRegionsAttack.get_height() / 2)
    
    serverRegionsTransferArmy = objs.Text(GUI, 'TransferArmy', (219, 174, 0), int(configFile['screenHeight'] / 30))
    serverRegionsTransferArmy.coord = (configFile['screenWidth'] / 6 * 1 - serverRegionsTransferArmy.get_width() / 2, configFile['screenHeight'] * 0.7875 - serverRegionsTransferArmy.get_height() / 2)
    
    serverRegionsTransferRegion = objs.Text(GUI, 'TransferRegion', (219, 174, 0), int(configFile['screenHeight'] / 30))
    serverRegionsTransferRegion.coord = (configFile['screenWidth'] / 6 * 8/5 - serverRegionsTransferRegion.get_width() / 2, configFile['screenHeight'] * 0.7875 - serverRegionsTransferRegion.get_height() / 2)
    
    serverOwner = objs.Text(GUI, 'armies', (219, 174, 0), int(configFile['screenHeight'] / 30))
    serverOwner.coord = (configFile['screenWidth'] / 6 * 0.25 - serverOwner.get_width() / 2, configFile['screenHeight'] * 0.825 - serverOwner.get_height() / 2)
    
    serverInfantry = objs.Text(GUI, 'infantry', (219, 174, 0), int(configFile['screenHeight'] / 30))
    serverInfantry.coord = (configFile['screenWidth'] / 6 * 0.75 - serverInfantry.get_width() / 2, configFile['screenHeight'] * 0.825 - serverInfantry.get_height() / 2)
    
    serverCavalry = objs.Text(GUI, 'cavalry', (219, 174, 0), int(configFile['screenHeight'] / 30))
    serverCavalry.coord = (configFile['screenWidth'] / 6 * 1.25 - serverCavalry.get_width() / 2, configFile['screenHeight'] * 0.825 - serverCavalry.get_height() / 2)
    
    serverArtillery = objs.Text(GUI, 'artillery', (219, 174, 0), int(configFile['screenHeight'] / 30))
    serverArtillery.coord = (configFile['screenWidth'] / 6 * 1.75 - serverArtillery.get_width() / 2, configFile['screenHeight'] * 0.825 - serverArtillery.get_height() / 2)
    
    serverRegionsChoose = objs.Text(GUI, 'choisi moi fdp', (219, 175, 0), int(configFile['screenHeight'] / 25))
    serverRegionsChoose.coord = (configFile['screenWidth'] / 6 - serverRegionsChoose.get_width() / 2, configFile['screenHeight'] * 0.7875 - serverRegionsChoose.get_height() / 2)
    
    serverStartGame = objs.Text(GUI, 'start the game wsh', (220, 174, 0), int(configFile['screenHeight'] / 25))
    serverStartGame.coord = (configFile['screenWidth'] / 6 - serverStartGame.get_width() / 2, configFile['screenHeight'] / 2 - serverStartGame.get_height() / 2)
    
    serverChooseArmy = objs.Picture(GUI, 'gfx/icon.png', (round(configFile['screenWidth']*1/3), round(configFile['screenHeight']*1/3)), (configFile['screenWidth']*1/3, configFile['screenHeight']*1/6))
    
    serverChooseArmyRequest = objs.Text(GUI, 'CMB tu en prend frer', (219, 174, 0), int(configFile['screenHeight'] / 20))
    serverChooseArmyRequest.coord = (configFile['screenWidth'] / 2 - serverChooseArmyRequest.get_width() / 2, configFile['screenHeight'] / 2 * 2/5 - serverChooseArmyRequest.get_height() / 2)
    
    serverChooseArmyInfantry = objs.Text(GUI, '0', (219, 175, 0), int(configFile['screenHeight'] / 20))
    
    serverChooseArmyCavalry = objs.Text(GUI, '0', (220, 174, 0), int(configFile['screenHeight'] / 20))
    
    serverChooseArmyArtillery = objs.Text(GUI, '0', (218, 174, 0), int(configFile['screenHeight'] / 20))
    
    serverChooseContinue = objs.Text(GUI, 'continuer', (219, 173, 0), int(configFile['screenHeight'] / 20))
    serverChooseContinue.coord = (configFile['screenWidth'] / 2 * 15/18 - serverChooseContinue.get_width() / 2, configFile['screenHeight'] / 2 * 9/10 - serverChooseContinue.get_height() / 2)
    
    serverChooseCancel = objs.Text(GUI, 'annuler', (220, 175, 0), int(configFile['screenHeight'] / 20))
    serverChooseCancel.coord = (configFile['screenWidth'] / 2 * 21/18 - serverChooseCancel.get_width() / 2, configFile['screenHeight'] / 2 * 9/10 - serverChooseCancel.get_height() / 2)
    
    return dict(filter(lambda i: i[0] not in list(globals().values())[-1].__code__.co_varnames[:list(globals().values())[-1].__code__.co_argcount], locals().items()))