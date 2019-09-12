from datetime import datetime

from pygame.surface import Surface

from src import Constants, Display
from src.root_object.ProgressCircle import ProgressCircle
from src.root_object.Time import Time
from src.state.State import State


class Clock(State):
    # noinspection SpellCheckingInspection
    def __init__(self):
        super().__init__()

        self.circle = ProgressCircle(0, 0, 190, 20, Constants.CIRCLE_COLOR)

        self.time = Time(0)

        self.window_resize(*Display.size)

    def tick(self):
        now = datetime.now()

        self.circle.progress = ((now.hour * 3600 + now.minute * 60 + now.second) + now.microsecond / 1000000) / 86400

        self.circle.tick()

        self.time.tick()

    def render(self, surface: Surface):
        super().render(surface)

        self.circle.render(surface)
        self.time.render(surface)

    def window_resize(self, width: int, height: int):
        self.circle.window_resize(width, height)
        self.time.window_resize(width, height)
