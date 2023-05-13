import os, sys
from kaki.app import App
import kivy
from kivy.factory import Factory
from kivy.resources import resource_add_path, resource_find
from kivy.core.window import Window
from kivy.config import Config

# from kivy.core.window import Window

Config.set("graphics", "resizable", 0)

from kivymd.app import MDApp


class MainApp(App, MDApp):
    DEBUG = True
    KV_FILES = {
        os.path.join(os.getcwd(), "VibelyAppDes.kv")
        # os.path.join('.', 'logic.screen_manager.kv')
    }
    CLASSES = {"vibelyApp": "VibelyApp"}

    #AUTORELOADER_PATHS = [(".", {"recursive": True})]
    #AUTORELOADER_IGNORE_PATTERNS = ['.db']
    def build_app(self):
        Window.size = (400, 775)
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Indigo"
        self.theme_cls.accent_palette = "Red"
        self.theme_cls.primary_hue = "900"

        return Factory.vibelyApp()


if hasattr(sys, "_MEIPASS"):
    resource_add_path(os.path.join(sys._MEIPASS))
MainApp().run()
