방랑자들
========

여러 지역을 여행다니며 세력을 키워서 일인자가 되는 게임

환경
----

#### 가상 환경

    $ mkvirtualenv vegabonds

#### 모듈 설치

    $ pip install -r requirements.txt


리서치
------

#### 해상도 설정

* <http://stackoverflow.com/questions/14014955/how-to-change-window-size>

    * 윈도우 생성전 해상도 설정 (1.9.0 이상만 가능)

            import kivy
            kivy.require('1.9.0')

            from kivy.config import Config
            Config.set('graphics', 'width', '200')
            Config.set('graphics', 'height', '200')

    * 윈도우 생성 이후 해상도 설정

            Window.size = (300, 100)

* <http://kivy.org/docs/api-kivy.core.window.html#kivy.core.window.WindowBase>

         class WindowPygame(kivy.core.window.WindowBase)
         |  Method resolution order:
         |      WindowPygame
         |      kivy.core.window.WindowBase
         |      kivy._event.EventDispatcher
         |      kivy._event.ObjectWithUid
         |      __builtin__.object


         |  size
         |      Create a property with a custom getter and setter.
         |   
         |      If you don't find a Property class that fits to your needs, you can make
         |      your own by creating custom Python getter and setter methods.
         |   
         |      Example from kivy/uix/widget.py::
         |   
         |          def get_right(self):
         |              return self.x + self.width
         |          def set_right(self, value):
         |              self.x = value - self.width
         |          right = AliasProperty(get_right, set_right, bind=('x', 'width'))
         |   
         |      :Parameters:
         |          `getter`: function
         |              Function to use as a property getter
         |          `setter`: function
         |              Function to use as a property setter
         |          `bind`: list/tuple
         |              Properties to observe for changes, as property name strings
         |          `cache`: boolean
         |              If True, the value will be cached, until one of the binded elements
         |              will changes
         |   
         |      .. versionchanged:: 1.4.0
         |          Parameter `cache` added.
