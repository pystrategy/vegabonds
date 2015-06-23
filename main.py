from kivy.app import App
from kivy.config import Config

res_width = 1920 / 4
res_height = 1080 / 4

Config.set('graphics', 'width', str(res_width))
Config.set('graphics', 'height', str(res_height))

class VegabondsApp(App):
    pass

if __name__ == '__main__':
    VegabondsApp().run()
