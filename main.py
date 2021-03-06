from kivy.app import App
from kivy.config import Config
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.core.window import Window

from kivy.graphics import *

from random import random 

import json
import os

res_width = 1920 / 2
res_height = 1080 / 2

Config.set('graphics', 'width', str(res_width))
Config.set('graphics', 'height', str(res_height))

Window.clearcolor = (0.5, 0.5, 0.5, 1)

class VegabondsView(FloatLayout):
    def __init__(self, **kwargs):
        super(VegabondsView, self).__init__(**kwargs)

        self.__load_map_scene('china')

    def __load_map_scene(self, map_name):
        scene_path = os.path.join('resources', 'maps', map_name, 'scene.json')
        scene_dict = json.load(open(scene_path))

        scene_width = 1080
        scene_height = 800
        layer_list = scene_dict['layers']
        first_layer_dict = layer_list[0]
        pivot_pos = (first_layer_dict['x'], first_layer_dict['y'])
        for layer_dict in reversed(layer_list[1:]):
            layer_pos = (layer_dict['x'] - pivot_pos[0], layer_dict['y'] - pivot_pos[1])
            layer_size = (layer_dict['w'], layer_dict['h'])
            layer_name = layer_dict['name'] 
            layer_path = os.path.join('resources', 'maps', map_name, 'images', layer_name + '.png')
            
            layer_color = [random(), random(), random(), 1]
            layer_image = Image(source=layer_path, pos=layer_pos, size=layer_size, pos_hint={}, size_hint=(None, None), color=layer_color)
	    with layer_image.canvas.before:
		layer_image.bg_rect = Line(rectangle=(layer_pos[0], layer_pos[1], layer_size[0], layer_size[1]))
            self.add_widget(layer_image)
            
            layer_label = Label(text="[color=000000]"+layer_name+"[/color]", pos=layer_pos, size=layer_size, pos_hint={}, size_hint=(None, None), markup=True)
            self.add_widget(layer_label)

	layer_label = Label(text="[color=000000]!!!![/color]", pos=(0, 0), pos_hint={}, size_hint=(None, None), markup=True)
	self.add_widget(layer_label)

class VegabondsApp(App):
    pass

if __name__ == '__main__':
    VegabondsApp().run()
