from constants import *
from game.casting.sound import Sound
from game.scripting.action import Action


class CollideBordersAction(Action):

    def __init__(self, physics_service, audio_service, player1_stats, player2_stats):
        self._physics_service = physics_service
        self._audio_service = audio_service
        self._player1_stats = player1_stats    
        self._player2_stats = player2_stats 
        
    def execute(self, cast, script, callback):
        ball = cast.get_first_actor(BALL_GROUP)
        body = ball.get_body()
        position = body.get_position()
        x = position.get_x()
        y = position.get_y()
        bounce_sound = Sound(BOUNCE_SOUND)
        over_sound = Sound(OVER_SOUND)

        if x < FIELD_LEFT:
            statsp2 = cast.get_first_actor(self._player2_stats)
            statsp1 = cast.get_first_actor(self._player1_stats)
            statsp2.add_points(POINT_VALUE)
            
            if (statsp2.get_score() < MAXIMUM_SCORE) or (statsp2.get_score() < (statsp1.get_score() + (POINTS_TO_WIN))):
                callback.on_next(TRY_AGAIN) 
            else:
                callback.on_next(GAME_OVER)
                self._audio_service.play_sound(over_sound)

        if x > (FIELD_RIGHT - BALL_WIDTH):
            statsp2 = cast.get_first_actor(self._player2_stats)
            statsp1 = cast.get_first_actor(self._player1_stats)
            statsp1.add_points(POINT_VALUE)
            
            if (statsp1.get_score() < MAXIMUM_SCORE) or (statsp1.get_score() < (statsp2.get_score() + (POINTS_TO_WIN))):
                callback.on_next(TRY_AGAIN) 
            else:
                callback.on_next(GAME_OVER)
                self._audio_service.play_sound(over_sound)

        if y <  HUD_MARGIN + FONT_SMALL:
            ball.bounce_y()
            self._audio_service.play_sound(bounce_sound)

        if y > (FIELD_BOTTOM - BALL_WIDTH):
            ball.bounce_y()
            self._audio_service.play_sound(bounce_sound)