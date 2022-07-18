from constants import *
from game.scripting.action import Action


class DrawHudAction(Action):

    def __init__(self, video_service, player_stats, player_score):
        self._video_service = video_service
        self._player_stats = player_stats
        self._player_score = player_score
        
    def execute(self, cast, script, callback):
        stats = cast.get_first_actor(self._player_stats)
        self._draw_label(cast, self._player_score, SCORE_FORMAT, stats.get_score())

    def _draw_label(self, cast, group, format_str, data):
        label = cast.get_first_actor(group)
        text = label.get_text()
        text.set_value(format_str.format(data))
        position = label.get_position()
        self._video_service.draw_text(text, position)