from ...typings import Context
from .common.base import BaseTask


class EnableTargetingTask(BaseTask):
    def __init__(self):
        super().__init__()
        self.name = 'enableTargeting'


    def shouldIgnore(self, context: Context) -> bool:
        return False#(context['battleList']['creatures']) == 0

    def do(self, context: Context) -> Context:
        context['targeting']['enabled'] = True
        return context

    def did(self, context: Context) -> bool:
        return len(context['battleList']['creatures']) == 0
