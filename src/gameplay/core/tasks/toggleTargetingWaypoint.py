from src.repositories.radar.typings import Coordinate
from ...typings import Context
from .common.vector import VectorTask
from .setNextWaypoint import SetNextWaypointTask
from .walkToCoordinate import WalkToCoordinateTask
from .disableTargeting import DisableTargetingTask
from .enableTargeting import EnableTargetingTask


class ToggleTargetingWaypoint(VectorTask):
    def __init__(self, onOff: str):
        super().__init__()
        self.name = 'toggleTargetingWaypoint'
        self.delayAfterComplete = 1
        self.isRootTask = True
        self.onOff = onOff

    def onBeforeStart(self, context: Context) -> Context:
        shouldEnable = True if self.onOff == 'on' else False
        if shouldEnable:
            action = EnableTargetingTask()
        else:
            action = DisableTargetingTask()

        self.tasks = [
            action.setParentTask(self).setRootTask(self),
            SetNextWaypointTask().setParentTask(self).setRootTask(self),
        ]
        return context
