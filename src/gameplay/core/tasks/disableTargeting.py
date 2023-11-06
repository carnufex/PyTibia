from ...typings import Context
from .common.base import BaseTask


class DisableTargetingTask(BaseTask):
    def __init__(self):
        super().__init__()
        self.name = 'disableTargeting'


    def shouldIgnore(self, context: Context) -> bool:
        return False#(context['battleList']['creatures']) == 0

    def do(self, context: Context) -> Context:
        context['targeting']['enabled'] = False
        return context

    def did(self, context: Context) -> bool:
        return True
