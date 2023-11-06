from src.repositories.skills.core import getHp, getMana
from src.repositories.statusBar.core import getManaPercentage, getHpPercentage, getIsParalyzed
from ...typings import Context


# TODO: add unit tests
def setMapPlayerStatusMiddleware(context: Context) -> Context:
    context['statusBar']['hp'] = getHp(context['screenshot'])
    context['statusBar']['hpPercentage'] = getHpPercentage(context['screenshot'])
    context['statusBar']['mana'] = getMana(context['screenshot'])
    context['statusBar']['manaPercentage'] = getManaPercentage(context['screenshot'])
    context['statusBar']['isParalyzed'] = getIsParalyzed(context['screenshot'])
    return context
