import pygame
from pyautogui import size as screen_size

from root_object.root_object_manager import RootObjectManager
from state.state_manager import StateManager

size = (480, 720)
fps = 60

full_screen = False

window = None

recorded_size = size

render_enable = True


def resize(size_, root_object_manager, state_manager, resize_alert_class):
    global window, size

    size = size_

    if full_screen:
        window = pygame.display.set_mode(size, pygame.FULLSCREEN)
    else:
        window = pygame.display.set_mode(size, pygame.RESIZABLE)
    resize_objects(root_object_manager, state_manager)
    root_object_manager.add(resize_alert_class(*size, root_object_manager))


def resize_objects(root_object_manager: RootObjectManager, state_manager: StateManager):
    root_object_manager.window_resize(*size)
    state_manager.window_resize(*size)


def toggle_full_screen(root_object_manager: RootObjectManager, state_manager: StateManager):
    global full_screen, recorded_size, window, size

    full_screen = not full_screen

    if full_screen:
        recorded_size = size
        size = screen_size()
        window = pygame.display.set_mode(size, pygame.FULLSCREEN)
    else:
        window = pygame.display.set_mode(recorded_size, pygame.RESIZABLE)

    resize_objects(root_object_manager, state_manager)
