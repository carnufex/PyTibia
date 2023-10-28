from .walkToCoordinate import WalkToCoordinateTask
from .rightClickCoordinate import RightClickInCoordinateTask
from .setNextWaypoint import SetNextWaypointTask
import src.repositories.gameWindow.core as gameWindowCore
import src.repositories.gameWindow.slot as gameWindowSlot
from src.shared.typings import Waypoint
import src.utils.keyboard as keyboard
from ...typings import Context
from .common.vector import VectorTask


class UseLadderWaypointTask(VectorTask):
    def __init__(self, waypoint: Waypoint):
        super().__init__()
        self.name = 'useLadder'
        self.isRootTask = True
        self.waypoint = waypoint
        self.delayAfterComplete = 1


    def onBeforeStart(self, context: Context) -> Context:
        self.tasks = [
            WalkToCoordinateTask(self.waypoint['coordinate']).setParentTask(self).setRootTask(self),
            RightClickInCoordinateTask(self.waypoint['coordinate']).setParentTask(self).setRootTask(self),
            SetNextWaypointTask().setParentTask(self).setRootTask(self),
        ]
        return context
