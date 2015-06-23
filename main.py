from kivy.app import App
from distutils.version import StrictVersion

import kivy

res_width = 1920 / 4
res_height = 1080 / 4

if StrictVersion(kivy.__version__) >= StrictVersion('1.9.0'):
    from kivy.config import Config
    Config.set('graphics', 'width', str(res_width))
    Config.set('graphics', 'height', str(res_height))
else:
    from kivy.core.window import Window
    Window.size = (res_width, res_height)

class VegabondsApp(App):
    pass

if __name__ == '__main__':
    VegabondsApp().run()
