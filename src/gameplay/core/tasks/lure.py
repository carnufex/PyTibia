from src.gameplay.core.waypoint import resolveGoalCoordinate
from src.gameplay.typings import Context
import src.repositories.gameWindow.creatures as gameWindowCreatures
from ...typings import Context
from .common.vector import VectorTask
from .walkToCoordinate import WalkToCoordinateTask
from src.utils.array import getNextArrayIndex
from time import time
from .setNextWaypoint import SetNextWaypointTask

# Tarefas:
# - Se algum bicho parar perto da coordenada, ligar o target
# - Se levar trap, ligar o target
class LureWaypointTask(VectorTask):
    # TODO: add types
    def __init__(self, waypoint):
        super().__init__()
        self.name = 'lureWaypoint'
        self.delayAfterComplete = 1
        self.isRootTask = True
        self.coordinate = waypoint['coordinate']

    def onBeforeStart(self, context: Context) -> Context:
        context['targeting']['enabled'] = False
        self.tasks = [
            WalkToCoordinateTask(self.coordinate).setParentTask(self).setRootTask(self),
            SetNextWaypointTask().setParentTask(self).setRootTask(self),
        ]
        return context
    
    def ping(self, context: Context) -> Context:
        return context
    
    def onComplete(self, context: Context) -> Context:
        if (gameWindowCreatures.isTrappedByCreatures(context['gameWindow']['monsters'], context['radar']['coordinate']) or
            context['radar']['coordinate'] == tuple(context['cavebot']['waypoints']['items'][context['cavebot']['waypoints']['currentIndex']]['coordinate'])):
            context['targeting']['enabled'] = True
        return context
    
    #     self.manuallyTerminable = True
    #     self.waypoint = waypoint
    #     self.startedAt = time()

    # def shouldManuallyComplete(self, context: Context) -> bool:
    #     currentWaypoint = context['cavebot']['waypoints']['items'][context['cavebot']['waypoints']['currentIndex']]['coordinate']
    #     if not context['radar']['coordinate'] == tuple(currentWaypoint):
    #         timePassed = time() - self.startedAt
    #         if timePassed > 5:
    #             # stuck?
    #             return True
    #     else:
    #         return True
    #     return False
    #     return len(context['battleList']['creatures']) == 0

    # def ping(self, context: Context) -> Context:
    #     if gameWindowCreatures.isTrappedByCreatures(context['gameWindow']['monsters'], context['radar']['coordinate']):
    #         context['targeting']['enabled'] = True
    #     return context

    # def onBeforeStart(self, context: Context) -> Context:
    #     context['targeting']['enabled'] = False
    #     self.tasks = [
    #         WalkToCoordinateTask(self.waypoint['coordinate']).setParentTask(self).setRootTask(self),
    #     ]
    #     return context

    # def onComplete(self, context: Context) -> Context:
    #     nextWaypointIndex = getNextArrayIndex(
    #         context['cavebot']['waypoints']['items'], context['cavebot']['waypoints']['currentIndex'])
    #     context['cavebot']['waypoints']['currentIndex'] = nextWaypointIndex
    #     # currentWaypoint = context['cavebot']['waypoints']['items'][context['cavebot']['waypoints']['currentIndex']]
    #     # context['cavebot']['waypoints']['state'] = resolveGoalCoordinate(context['radar']['coordinate'], currentWaypoint)
    #     return context