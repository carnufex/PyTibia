from src.repositories.radar.core import getClosestWaypointIndexFromCoordinate, getCoordinate
from ...typings import Context


# TODO: add unit tests
def setRadarMiddleware(context: Context) -> Context:
    coord = getCoordinate(
        context['screenshot'], previousCoordinate=context['radar']['previousCoordinate'])
    if coord is not None:
        context['radar']['coordinate'] = coord
    return context


# TODO: add unit tests
def setWaypointIndexMiddleware(context: Context) -> Context:
    if context['cavebot']['waypoints']['currentIndex'] is None:
        context['cavebot']['waypoints']['currentIndex'] = getClosestWaypointIndexFromCoordinate(
            context['radar']['coordinate'], context['cavebot']['waypoints']['items'])
    return context
