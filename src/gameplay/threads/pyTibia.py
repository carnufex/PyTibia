import pyautogui
from time import sleep, time
import traceback
from src.gameplay.cavebot import resolveCavebotTasks, shouldAskForCavebotTasks
from src.gameplay.combo import comboSpells
from src.gameplay.core.middlewares.battleList import setBattleListMiddleware
from src.gameplay.core.middlewares.chat import setChatTabsMiddleware
from src.gameplay.core.middlewares.gameWindow import setDirectionMiddleware, setHandleLootMiddleware, setGameWindowCreaturesMiddleware, setGameWindowMiddleware
from src.gameplay.core.middlewares.playerStatus import setMapPlayerStatusMiddleware
from src.gameplay.core.middlewares.radar import setRadarMiddleware, setWaypointIndexMiddleware
from src.gameplay.core.middlewares.screenshot import setScreenshotMiddleware
from src.gameplay.core.middlewares.tasks import setCleanUpTasksMiddleware
from src.gameplay.core.tasks.lootCorpse import LootCorpseTask
from src.gameplay.resolvers import resolveTasksByWaypoint
from src.gameplay.healing.observers.eatFood import eatFood
from src.gameplay.healing.observers.healingBySpells import healingBySpells
from src.gameplay.healing.observers.healingByPotions import healingByPotions
from src.gameplay.healing.observers.swapAmulet import swapAmulet
from src.gameplay.healing.observers.swapRing import swapRing
from src.gameplay.targeting import hasCreaturesToAttack
from src.repositories.gameWindow.creatures import getClosestCreature


pyautogui.FAILSAFE = False
pyautogui.PAUSE = 0


class PyTibiaThread:
    # TODO: add typings
    def __init__(self, context):
        self.context = context

    def mainloop(self):
        while True:
            try:
                if self.context.context['pause']:
                    continue
                try:
                    fps = 1 / (time() - loop_time)
                    print(f'FPS {fps}', flush=True)
                except:
                    pass
                loop_time = time()
                startTime = time()
                self.context.context = self.handleGameData(
                    self.context.context)
                self.context.context = self.handleGameplayTasks(
                    self.context.context)
                self.context.context = self.context.context['tasksOrchestrator'].do(
                    self.context.context)
                self.context.context['radar']['lastCoordinateVisited'] = self.context.context['radar']['coordinate']
                healingByPotions(self.context.context)
                healingBySpells(self.context.context)
                comboSpells(self.context.context)
                swapAmulet(self.context.context)
                swapRing(self.context.context)
                eatFood(self.context.context)
                endTime = time()
                diff = endTime - startTime
                sleep(max(0.045 - diff, 0))
            except:
                print('An exception occurred:', traceback.format_exc())

    def handleGameData(self, context):
        if context['pause']:
            return context
        context = setScreenshotMiddleware(context)
        context = setRadarMiddleware(context)
        context = setChatTabsMiddleware(context)
        context = setBattleListMiddleware(context)
        context = setGameWindowMiddleware(context)
        context = setDirectionMiddleware(context)
        context = setGameWindowCreaturesMiddleware(context)
        context = setHandleLootMiddleware(context)
        context = setWaypointIndexMiddleware(context)
        context = setMapPlayerStatusMiddleware(context)
        context = setCleanUpTasksMiddleware(context)
        return context

    def handleGameplayTasks(self, context):
        context['cavebot']['closestCreature'] = getClosestCreature(
            context['gameWindow']['monsters'], context['radar']['coordinate'])
        currentTask = context['tasksOrchestrator'].getCurrentTask(context)
        if currentTask is not None and currentTask.name == 'selectChatTab':
            return context
        if len(context['loot']['corpsesToLoot']) > 0:
            context['way'] = 'lootCorpses'
            if currentTask is not None and currentTask.rootTask is not None and currentTask.rootTask.name != 'lootCorpse':
                context['tasksOrchestrator'].setRootTask(context, None)
            if context['tasksOrchestrator'].getCurrentTask(context) is None:
                # TODO: get closest dead corpse
                firstDeadCorpse = context['loot']['corpsesToLoot'][0]
                context['tasksOrchestrator'].setRootTask(
                    context, LootCorpseTask(firstDeadCorpse))
            context['gameWindow']['previousMonsters'] = context['gameWindow']['monsters']
            return context
        if context['targeting']['enabled']:
            hasCreaturesToAttackAfterCheck = hasCreaturesToAttack(context)
            if hasCreaturesToAttackAfterCheck:
                if context['cavebot']['closestCreature'] is not None:
                    context['way'] = 'cavebot'
                else:
                    context['way'] = 'waypoint'
            else:
                context['way'] = 'waypoint'
            if hasCreaturesToAttackAfterCheck and shouldAskForCavebotTasks(context):
                currentRootTask = currentTask.rootTask if currentTask is not None else None
                isTryingToAttackClosestCreature = currentRootTask is not None and (
                    currentRootTask.name == 'attackClosestCreature')
                if not isTryingToAttackClosestCreature:
                    context = resolveCavebotTasks(context)
        else:
            context['way'] = 'waypoint'
        if context['way'] == 'waypoint':
            if context['tasksOrchestrator'].getCurrentTask(context) is None:
                currentWaypointIndex = context['cavebot']['waypoints']['currentIndex']
                currentWaypoint = context['cavebot']['waypoints']['items'][currentWaypointIndex]
                context['tasksOrchestrator'].setRootTask(
                    context, resolveTasksByWaypoint(currentWaypoint))
            # else:
                    # print("stuck here")
        context['gameWindow']['previousMonsters'] = context['gameWindow']['monsters']
        return context
