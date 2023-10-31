from .typings import Context


# TODO: add unit tests
def hasCreaturesToAttack(context: Context) -> bool:
    context['targeting']['hasIgnorableCreatures'] = False
    if len(context['gameWindow']['monsters']) == 0:
        context['targeting']['canIgnoreCreatures'] = True
        return False
    if context['targeting']['canIgnoreCreatures'] == False:
        return True
    ignorableGameWindowCreatures = []
    for gameWindowCreature in context['gameWindow']['monsters']:
        # ignore creatures
        if (gameWindowCreature['name'] in context['cavebot']['ignoreCreatures']):
            shouldIgnoreCreature = context['targeting']['creatures'].get(gameWindowCreature['name'], { 'ignore': True })['ignore']
        else:
            shouldIgnoreCreature = context['targeting']['creatures'].get(gameWindowCreature['name'], { 'ignore': False })['ignore']
        
        if shouldIgnoreCreature:
            context['targeting']['hasIgnorableCreatures'] = True
            ignorableGameWindowCreatures.append(gameWindowCreature)
    return len(ignorableGameWindowCreatures) < len(context['gameWindow']['monsters'])
