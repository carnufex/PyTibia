import numpy as np
from src.gameplay.core.tasks.orchestrator import TasksOrchestrator
from src.repositories.battleList.typings import Creature as BattleListCreature
from src.repositories.gameWindow.typings import Creature as GameWindowCreature
from src.repositories.radar.typings import Waypoint

context = {
    'backpacks': {
        'main': '',
        'loot': '',
    },
    'battleList': {
        'beingAttackedCreatureCategory': None,
        'creatures': [],
    },
    'cavebot': {
        'enabled': True,
        'holesOrStairs': [],
        'isAttackingSomeCreature': False,
        'previousTargetCreature': None,
        'targetCreature': None,
        'waypoints': {
            'currentIndex': None,
            'points': np.array([
                ('', 'lure', (33158, 32317, 12), {}),
                # maior que X mobs ligar o target
                # habilitar o target ao tomar block
                # ('', 'lure', (33165, 32287, 12), {}),
                # ('', 'lure', (33139, 32287, 12), {}),
                # ('', 'lure', (33156, 32268, 12), {}),
                # ('', 'lure', (33171, 32237, 12), {}),
                # ('', 'lure', (33142, 32240, 12), {}),
                
                
                
                # werehyaena cave 1
                ('', 'walk', (33214, 32458, 8), {}),
                ('', 'moveUp', (33214, 32456, 8), {'direction': 'north'}),
                ('', 'walk', (33217, 32441, 7), {}),
                ('endOfCity', 'walk', (33215, 32406, 7), {}),
                ('', 'walk', (33218, 32377, 7), {}),
                ('', 'walk', (33212, 32359, 7), {}),
                ('', 'useShovel', (33212, 32358, 7), {}),
                ('', 'walk', (33227, 32358, 8), {}),
                ('', 'moveDown', (33227, 32358, 8), {'direction': 'east'}),
                ('', 'walk', (33222, 32355, 9), {}), # 10
                ('', 'moveDown', (33222, 32355, 9), {'direction': 'north'}), 
                ('caveStart', 'lure', (33207, 32353, 10), {}),
                ('', 'lure', (33189, 32348, 10), {}),
                ('', 'lure', (33193, 32366, 10), {}),
                ('', 'lure', (33208, 32367, 10), {}),
                ('', 'lure', (33223, 32387, 10), {}),
                ('', 'lure', (33200, 32389, 10), {}),
                ('', 'lure', (33196, 32398, 10), {}),
                ('', 'lure', (33210, 32373, 10), {}),
                ('', 'lure', (33221, 32351, 10), {}), # 20
                ('', 'dropFlasks', (33306, 32289, 7), {}),
                ('', 'refillChecker', (33306, 32289, 7), { # 22
                    'minimumOfManaPotions': 200,
                    'minimumOfHealthPotions': 200,
                    'minimumOfCapacity': 500,
                    'waypointLabelToRedirect': 'caveStart',
                }),
                ('', 'walk', (33221, 32353, 10), {}),
                ('', 'moveUp', (33221, 32353, 10), {'direction': 'south'}),
                ('', 'walk', (33229, 32358, 9), {}),
                ('', 'moveUp', (33229, 32358, 9), {'direction': 'west'}),
                ('', 'walk', (33212, 32358, 8), {}),
                ('', 'useRope', (33212, 32358, 8), {}),
                ('', 'walk', (33220, 32378, 7), {}),
                ('', 'walk', (33221, 32387, 7), {}), # 30
                ('', 'depositGold', (33221, 32387, 7), {}),
                ('', 'walk', (33215, 32422, 7), {}),
                ('', 'walk', (33213, 32454, 7), {}),
                ('', 'moveDown', (33213, 32454, 7), {'direction': 'south'}),
                ('', 'depositItems', (33214, 32456, 8), {'city': 'Darashia'}),
                ('', 'walk', (33214, 32456, 8), {}),
                ('', 'moveUp', (33214, 32456, 8), {'direction': 'north'}),
                ('', 'walk', (33217, 32403, 7), {}),
                ('', 'refill', (33217, 32403, 7), {
                    'waypointLabelToRedirect': 'endOfCity'
                }),
            ], dtype=Waypoint),
            'items': [],
            'state': None
        },
    },
    'chat': {
        'tabs': {}
    },
    'comingFromDirection': None,
    'comboSpells': {
        'enabled': True,
        'lastUsedSpell': None,
        'lastUsedSpellAt': None,
        'items': [],
    },
    'deposit': {
        'lockerCoordinate': None
    },
    'gameWindow': {
        'coordinate': None,
        'image': None,
        'previousGameWindowImage': None,
        'previousMonsters': [],
        'monsters': [],
        'players': [],
        'walkedPixelsInSqm': 0,
    },
    'healing': {
        'highPriority': {
            'healthFood': {
                'enabled': False,
                'hotkey': None,
                'hpPercentageLessThanOrEqual': None,
            },
            'manaFood': {
                'enabled': False,
                'hotkey': None,
                'manaPercentageLessThanOrEqual': None,
            },
            'swapRing': {
                'enabled': False,
                'tankRing': {
                    'hotkey': None,
                    'hpPercentageLessThanOrEqual': 0
                },
                'mainRing': {
                    'hotkey': None,
                    'hpPercentageGreaterThanOrEqual': 0
                },
                'tankRingAlwaysEquipped': False
            },
            'swapAmulet': {
                'enabled': False,
                'tankAmulet': {
                    'hotkey': None,
                    'hpPercentageLessThanOrEqual': 0
                },
                'mainAmulet': {
                    'hotkey': None,
                    'hpPercentageGreaterThan': 0
                },
                'tankAmuletAlwaysEquipped': False
            }
        },
        'potions': {
            'firstHealthPotion': {
                'enabled': False,
                'hotkey': None,
                'hpPercentageLessThanOrEqual': None,
                'manaPercentageGreaterThanOrEqual': None,
            },
            'firstManaPotion': {
                'enabled': False,
                'hotkey': None,
                'manaPercentageLessThanOrEqual': None,
            },
        },
        'spells': {
            'criticalHealing': {
                'enabled': False,
                'hotkey': None,
                'hpPercentageLessThanOrEqual': None,
                'spell': None
            },
            'lightHealing': {
                'enabled': False,
                'hotkey': None,
                'hpPercentageLessThanOrEqual': None,
                'spell': None
            },
            'utura': {
                'enabled': False,
                'hotkey': None,
                'spell': {
                    'name': 'utura',
                    'manaNeeded': '75'
                }
            },
            'uturaGran': {
                'enabled': False,
                'hotkey': None,
                'spell': {
                    'name': 'utura gran',
                    'manaNeeded': '165'
                }
            },
        },
        'eatFood': {
            'enabled': False,
            'hotkey': '',
            'eatWhenFoodIslessOrEqual': 0,
        }
    },
    'loot': {
        'corpsesToLoot': [],
    },
    'lastPressedKey': None,
    'pause': True,
    'radar': {
        'coordinate': None,
        'previousCoordinate': None,
        'lastCoordinateVisited': None,
    },
    'resolution': 1080,
    'statusBar': {
        'hpPercentage': None,
        'hp': None,
        'manaPercentage': None,
        'mana': None,
    },
    'targeting': {
        'enabled': False,
        'creatures': {},
        'canIgnoreCreatures': True,
        'hasIgnorableCreatures': False,
    },
    'tasksOrchestrator': TasksOrchestrator(),
    'screenshot': None,
    'way': None,
    'window': None
}
