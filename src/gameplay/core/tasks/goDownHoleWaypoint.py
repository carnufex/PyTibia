from src.shared.typings import Waypoint
from .setNextWaypoint import SetNextWaypointTask
from .clickInCoordinate import ClickInCoordinateTask
from ...typings import Context
from .common.vector import VectorTask


class GoDownHoleWaypointTask(VectorTask):
    def __init__(self, waypoint: Waypoint):
        super().__init__()
        self.name = 'useGoDownHoleWaypoint'
        self.isRootTask = True
        self.waypoint = waypoint

    def onBeforeStart(self, context: Context) -> Context:
        self.tasks = [
            ClickInCoordinateTask(self.waypoint).setParentTask(self).setRootTask(self),
            SetNextWaypointTask().setParentTask(self).setRootTask(self),
        ]
        return context
