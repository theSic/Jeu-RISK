import pygame, random #init modules
import objs #init files

def run(GUI, mode, loop, mainLoop, configFile, textlocking):
    regions = {}
    for i in pygame.event.get():
        if i.type == pygame.QUIT: loop, mainLoop = False, False
        elif i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                j = GUI.get_at(pygame.mouse.get_pos())
                if j == (219, 174, 0, 255): mode, textlocking = 'menu', 'null'
                elif j == (218, 174, 0, 255):
                    try: regions = objs.read_dico('game.save')
                    except: pass
                    else: mode, textlocking = 'server', 'null'
                elif j == (219, 174, 1, 255):
                    mode, textlocking = 'server', 'null'
                    regions = {
                        0: {'rgb': (0, 12, 255, 255), 'owner': 'null', 'army': {'null': {'infantry': 0, 'cavalry': 0, 'artillery': 0}}, 'resources': {'factories': 0, 'populations': {'max': 0, 'mobilized': 1, 'dead': 0}},
                        'border':
                            [(1, 'land'), (2, 'sea'), (3, 'land')]
                        },
                        1: {'rgb': (0, 12, 254, 255), 'owner': 'null', 'army': {'null': {'infantry': 0, 'cavalry': 0, 'artillery': 0}}, 'resources': {'factories': 0, 'populations': {'max': 0, 'mobilized': 1, 'dead': 0}},
                        'border':
                            [(0, 'land')]
                        },
                        2: {'rgb': (0, 13, 255, 255), 'owner': 'null', 'army': {'null': {'infantry': 0, 'cavalry': 0, 'artillery': 0}}, 'resources': {'factories': 0, 'populations': {'max': 0, 'mobilized': 1, 'dead': 0}},
                        'border':
                            [(0, 'sea'), (3, 'sea')]
                        },
                        3: {'rgb': (0, 13, 254, 255), 'owner': 'null', 'army': {'null': {'infantry': 0, 'cavalry': 0, 'artillery': 0}}, 'resources': {'factories': 0, 'populations': {'max': 0, 'mobilized': 1, 'dead': 0}},
                        'border':
                            [(0, 'land'), (2, 'sea')]
                        },
                    }
                    try:
                        for i in regions: regions[i]['army']['null'][random.choice(['infantry', 'cavalry', 'artillery'])] = 1
                    except: pass
                    for i in regions: regions[i]['resources']['factories'] = random.choice([0.25, 0.5, 0.75])
                    for i in regions: regions[i]['resources']['populations']['max'] = random.choice([1, 2, 3, 4, 5, 6])
                    objs.store('game.save', regions)
                elif j == (220, 174, 0, 255): textlocking = 'hostPort'
                else: textlocking = 'null'
                if textlocking != 'hostPort':
                    if configFile['port'] == '' or int(configFile['port']) > 65536: configFile['port'] = '33000'
                    configFile['port'] = int(configFile['port'])
                objs.store('game.config', configFile)
        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_ESCAPE: mode, textlocking = 'menu', 'null'
            elif textlocking == 'hostPort':
                configFile['port'] = str(configFile['port'])
                if i.unicode in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                    if len(configFile['port']) <= 4: configFile['port'] += i.unicode
                elif i.key == pygame.K_BACKSPACE: configFile['port'] = configFile['port'][:-1]
    return mode, loop, mainLoop, configFile, textlocking, regions