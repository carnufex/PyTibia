from typing import Union

from .core.tasks.toggleTargetingWaypoint import ToggleTargetingWaypoint

from .core.tasks.goDownHoleWaypoint import GoDownHoleWaypointTask
from .core.tasks.useLadderWaypoint import UseLadderWaypointTask
from src.shared.typings import Waypoint
from .core.tasks.common.base import BaseTask
from .core.tasks.common.vector import VectorTask
from .core.tasks.depositGold import DepositGoldTask
from .core.tasks.depositItems import DepositItemsTask
from .core.tasks.dropFlasks import DropFlasksTask
from .core.tasks.logout import LogoutTask
from .core.tasks.lure import LureWaypointTask
from .core.tasks.refill import RefillTask
from .core.tasks.refillChecker import RefillCheckerTask
from .core.tasks.singleWalk import SingleWalkTask
from .core.tasks.useRopeWaypoint import UseRopeWaypointTask
from .core.tasks.useShovelWaypoint import UseShovelWaypointTask
from .core.tasks.walkToWaypoint import WalkToWaypointTask
from .core.tasks.useHole import UseHoleTask


# TODO: add unit tests
def resolveTasksByWaypoint(waypoint: Waypoint) -> Union[BaseTask, VectorTask]:
    if waypoint['type'] == 'depositGold':
        return DepositGoldTask()
    elif waypoint['type'] == 'depositItems':
        return DepositItemsTask(waypoint)
    elif waypoint['type'] == 'dropFlasks':
        return DropFlasksTask()
    elif waypoint['type'] == 'logout':
        return LogoutTask()
    elif waypoint['type'] == 'lure':
        return LureWaypointTask(waypoint)
    elif waypoint['type'] == 'moveDown':
        return SingleWalkTask(waypoint['type'], waypoint['options']['direction'])
    elif waypoint['type'] == 'moveUp':
        return SingleWalkTask(waypoint['type'], waypoint['options']['direction'])
    elif waypoint['type'] == 'refill':
        return RefillTask(waypoint)
    elif waypoint['type'] == 'refillChecker':
        return RefillCheckerTask(waypoint)
    elif waypoint['type'] == 'useRope':
        return UseRopeWaypointTask(waypoint)
    elif waypoint['type'] == 'useShovel':
        return UseShovelWaypointTask(waypoint)
    elif waypoint['type'] == 'useLadder':
        return UseLadderWaypointTask(waypoint)
    elif waypoint['type'] == 'goDownHole':
        return GoDownHoleWaypointTask(waypoint)
    elif waypoint['type'] == 'toggleTargeting':
        return ToggleTargetingWaypoint(waypoint['options']['setTargeting'])
    elif waypoint['type'] == 'walk':
        return WalkToWaypointTask(waypoint['coordinate'])
