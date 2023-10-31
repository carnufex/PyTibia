# TODO: add types
# TODO: add unit tests
def loadContextFromConfig(config, context):
    # backpacks
    context['backpacks'] = config['backpacks'].copy()
    # cavebot
    context['cavebot']['enabled'] = config['cavebot']['enabled']
    context['cavebot']['waypoints']['items'] = config['cavebot']['waypoints']['items'].copy()
    context['cavebot']['ignoreCreatures'] = config['cavebot']['ignoreCreatures'].copy()
    # comboSpells
    context['comboSpells']['enabled'] = config['comboSpells']['enabled']
    for comboSpellsItem in config['comboSpells']['items']:
        comboSpellsItem['currentSpellIndex'] = 0
        context['comboSpells']['items'].append(comboSpellsItem)
    # healing
    context['healing'] = config['healing'].copy()
    return context
