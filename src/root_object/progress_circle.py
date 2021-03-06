from pygame.surface import Surface

import constants
from font import Font
from root_object.circle import Circle
from root_object.text import Text


class ProgressCircle(Circle):
    def __init__(self, center_x, center_y, max_radius, width, color, initial_progress=0.0):
        super().__init__(center_x, center_y, max_radius, width, color, initial_progress)

        font = Font(constants.NANUMSQUARE_LIGHT_FONT, 72, constants.TEXT_COLOR)
        self.circle_progress = Text(0, self.center_y - font.size / 2, '', font)

    def set_color(self, circle_color, text_color):
        self.color = circle_color
        self.circle_progress.font.set_color(text_color)

    def tick(self):
        super().tick()

        self.circle_progress.set_text('%.3f%%' % (constants.progress * 100))
        self.circle_progress.center_x()

    def render(self, surface: Surface):
        super().render(surface)
        self.circle_progress.render(surface)

    def window_resize(self, width: int, height: int):
        super().window_resize(width, height)
        self.circle_progress.y = self.center_y - self.circle_progress.font.size / 2
