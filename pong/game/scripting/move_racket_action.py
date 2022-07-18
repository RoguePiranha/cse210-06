from constants import *
from game.casting.point import Point
from game.scripting.action import Action


class MoveRacketAction(Action):

    def __init__(self, player):
        self._player = player

    def execute(self, cast, script, callback):
        racket = cast.get_first_actor(self._player)
        body = racket.get_body()
        velocity = body.get_velocity()
        position = body.get_position()
        y = position.get_y()
        
        position = position.add(velocity)

        if y < HUD_MARGIN + FONT_SMALL:
            position = Point(position.get_x(), HUD_MARGIN + FONT_SMALL)
        elif y > (SCREEN_HEIGHT - RACKET_HEIGHT):
            position = Point(position.get_x(), SCREEN_HEIGHT - RACKET_HEIGHT)
            
        body.set_position(position)
        