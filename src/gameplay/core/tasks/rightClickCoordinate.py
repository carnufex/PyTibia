import src.gameplay.utils as gameplayUtils
import src.repositories.gameWindow.core as gameWindowCore
import src.repositories.gameWindow.slot as gameWindowSlot
from src.shared.typings import Waypoint
from ...typings import Context
from .common.base import BaseTask


class RightClickInCoordinateTask(BaseTask):
    def __init__(self, waypoint: Waypoint):
        super().__init__()
        self.name = 'rightClickInCoordinate'
        self.delayBeforeStart = 2
        self.delayAfterComplete = 2
        self.waypoint = waypoint
        self.floorLevel = waypoint[2] - 1

    def do(self, context: Context) -> Context:
        slot = gameWindowCore.getSlotFromCoordinate(
            context['radar']['coordinate'], self.waypoint)
        gameWindowSlot.rightClickSlot(slot, context['gameWindow']['coordinate'])
        return context

    def did(self, context: Context) -> bool:
        return context['radar']['coordinate'][2] == self.floorLevel # ladder
