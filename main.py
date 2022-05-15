import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.scatter import Scatter
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition, SlideTransition
from kivy.lang import Builder
from kivy.properties import NumericProperty
from kivy.uix.scrollview import ScrollView


Builder.load_string("""
<StartingScreen>:
    name:'starting'
    BoxLayout:
        orientation: 'vertical'
        Label:
            text:'Press START to continue'
            font_size:'30'
            canvas.before:
                Rectangle:
                    pos: self.pos
                    size: self.size
                    source: 'wallpaper1.jpg'
            
        Button:
            text:'START'
            color: 1,1,1,1
            size_hint: 1, 1
            background_normal: ''
            background_color: 0,0,0,0
            on_release:root.manager.current = 'levels'
            on_release:root.manager.transition.direction = 'left'
            canvas.before:
                Rectangle:
                    pos: self.pos
                    size: self.size
                    source: 'Charge.jpg'


<LevelsScreen>:
    name:'levels'
    BoxLayout:
        orientation: 'horizontal'
        Button:
            text:'Go back'
            pos: 50, 50
            color: 1,0,0,1
            background_normal: ''
            background_color: .0,.0,.0,.0
            size_hint_x: .4
            size_hint_y: .2
            on_release:root.manager.current = 'starting'
            on_release:root.manager.transition.direction = 'right'
            canvas.before:
                Rectangle:
                    pos: self.pos
                    size: self.size
                    source: 'Back.jpg'
        ScrollView:
            canvas.before:
                Rectangle:
                    pos: self.pos
                    size: self.size
                    source: 'wallpaper2.jpg'
            do_scroll_x: False
            do_scroll_y: True
            GridLayout:
                cols: 1
                size_hint_y: None
                height: self.minimum_height
                
                Button:
                    text:'Level 1'
                    color: 1,0,0,1
                    background_normal: ''
                    background_color: .7,.7,.0,.0
                    size_hint_x: 1
                    size_hint_y: None
                    on_release:root.manager.current = 'level1'
                    on_release:root.manager.transition.direction = 'left'  
                Button:
                    text:'Level 2'
                    color: 1,0,0,1
                    background_normal: ''
                    background_color: .0,.0,.0,.0
                    size_hint_x: 1
                    size_hint_y: None
                    on_release:root.manager.current = 'level2'
                    on_release:root.manager.transition.direction = 'left'
                Button:
                    text:'Level 3'
                    color: 1,0,0,1
                    background_normal: ''
                    background_color: .0,.0,.0,.0
                    size_hint_x: 1
                    size_hint_y: None
                    on_release:root.manager.current = 'level3'
                    on_release:root.manager.transition.direction = 'left'
                Button:
                    text:'Level 4'
                    color: 1,0,0,1
                    background_normal: ''
                    background_color: .0,.0,.0,.0
                    size_hint_x: 1
                    size_hint_y: None
                    on_release:root.manager.current = 'level4'
                    on_release:root.manager.transition.direction = 'left'
                Button:
                    text:'Level 5'
                    color: 1,0,0,1
                    background_normal: ''
                    background_color: .0,.0,.0,.0
                    size_hint_x: 1
                    size_hint_y: None
                    on_release:root.manager.current = 'level5'
                    on_release:root.manager.transition.direction = 'left'
                Button:
                    text:'Level 6'
                    color: 1,0,0,1
                    background_normal: ''
                    background_color: .0,.0,.0,.0
                    size_hint_x: 1
                    size_hint_y: None
                    on_release:root.manager.current = 'level6'
                    on_release:root.manager.transition.direction = 'left'
                Button:
                    text:'Level 7'
                    color: 1,0,0,1
                    background_normal: ''
                    background_color: .0,.0,.0,.0
                    size_hint_x: 1
                    size_hint_y: None
                    on_release:root.manager.current = 'level7'
                    on_release:root.manager.transition.direction = 'left'
                Button:
                    text:'Level 8'
                    color: 1,0,0,1
                    background_normal: ''
                    background_color: .0,.0,.0,.0
                    size_hint_x: 1
                    size_hint_y: None
                    on_release:root.manager.current = 'level8'
                    on_release:root.manager.transition.direction = 'left'
                Button:
                    text:'Level 9'
                    color: 1,0,0,1
                    background_normal: ''
                    background_color: .0,.0,.0,.0
                    size_hint_x: 1
                    size_hint_y: None
                    on_release:root.manager.current = 'level9'
                    on_release:root.manager.transition.direction = 'left'
                Button:
                    text:'Level 10'
                    color: 1,0,0,1
                    background_normal: ''
                    background_color: .0,.0,.0,.0
                    size_hint_x: 1
                    size_hint_y: None
                    on_release:root.manager.current = 'level10'
                    on_release:root.manager.transition.direction = 'left'

<Level1>:
    name:'level1'
    BoxLayout:
        orientation: 'vertical'
        Button:
            text:'Go  back'
            pos: 50, 50
            size_hint: .2, .3
            on_release:root.manager.current = 'levels'
            on_release:root.manager.transition.direction = 'right'
        Label:
            text:'Question 1'
        BoxLayout:
            orientation: 'horizontal'
            Button:
                text:'Answer 1'
            Button:
                text:'Answer 2'
        BoxLayout:
            orientation: 'horizontal'
            Button:
                text:'Answer 3'
            Button:
                text:'Answer 4'


<Level2>:
    name:'level2'
    BoxLayout:
        orientation: 'vertical'
        Button:
            text:'Go  back'
            pos: 50, 50
            size_hint: .2, .2
            on_release:root.manager.current = 'levels'
            on_release:root.manager.transition.direction = 'right'
        Label:
            text:'Question 2'
        BoxLayout:
            orientation: 'horizontal'
            Button:
                text:'Answer 1'
            Button:
                text:'Answer 2'
        BoxLayout:
            orientation: 'horizontal'
            Button:
                text:'Answer 3'
            Button:
                text:'Answer 4'

<Level3>:
    name:'level3'
    BoxLayout:
        orientation: 'vertical'
        Button:
            text:'Go  back'
            pos: 50, 50
            size_hint: .2, .2
            on_release:root.manager.current = 'levels'
            on_release:root.manager.transition.direction = 'right'
        Label:
            text:'Question 3'
        BoxLayout:
            orientation: 'horizontal'
            Button:
                text:'Answer 1'
            Button:
                text:'Answer 2'
        BoxLayout:
            orientation: 'horizontal'
            Button:
                text:'Answer 3'
            Button:
                text:'Answer 4'
<Level4>:
    name:'level4'
    BoxLayout:
        orientation: 'vertical'
        Button:
            text:'Go  back'
            pos: 50, 50
            size_hint: .2, .2
            on_release:root.manager.current = 'levels'
            on_release:root.manager.transition.direction = 'right'
        Label:
            text:'Question 4'
        BoxLayout:
            orientation: 'horizontal'
            Button:
                text:'Answer 1'
            Button:
                text:'Answer 2'
        BoxLayout:
            orientation: 'horizontal'
            Button:
                text:'Answer 3'
            Button:
                text:'Answer 4'
<Level5>:
    name:'level5'
    BoxLayout:
        orientation: 'vertical'
        Button:
            text:'Go  back'
            pos: 50, 50
            size_hint: .2, .2
            on_release:root.manager.current = 'levels'
            on_release:root.manager.transition.direction = 'right'
        Label:
            text:'Question 5'
        BoxLayout:
            orientation: 'horizontal'
            Button:
                text:'Answer 1'
            Button:
                text:'Answer 2'
        BoxLayout:
            orientation: 'horizontal'
            Button:
                text:'Answer 3'
            Button:
                text:'Answer 4'
<Level6>:
    name:'level6'
    BoxLayout:
        orientation: 'vertical'
        Button:
            text:'Go  back'
            pos: 50, 50
            size_hint: .2, .2
            on_release:root.manager.current = 'levels'
            on_release:root.manager.transition.direction = 'right'
        Label:
            text:'Question 6'
        BoxLayout:
            orientation: 'horizontal'
            Button:
                text:'Answer 1'
            Button:
                text:'Answer 2'
        BoxLayout:
            orientation: 'horizontal'
            Button:
                text:'Answer 3'
            Button:
                text:'Answer 4'
<Level7>:
    name:'level7'
    BoxLayout:
        orientation: 'vertical'
        Button:
            text:'Go  back'
            pos: 50, 50
            size_hint: .2, .2
            on_release:root.manager.current = 'levels'
            on_release:root.manager.transition.direction = 'right'
        Label:
            text:'Question 7'
        BoxLayout:
            orientation: 'horizontal'
            Button:
                text:'Answer 1'
            Button:
                text:'Answer 2'
        BoxLayout:
            orientation: 'horizontal'
            Button:
                text:'Answer 3'
            Button:
                text:'Answer 4'
<Level8>:
    name:'level8'
    BoxLayout:
        orientation: 'vertical'
        Button:
            text:'Go  back'
            pos: 50, 50
            size_hint: .2, .2
            on_release:root.manager.current = 'levels'
            on_release:root.manager.transition.direction = 'right'
        Label:
            text:'Question 8'
        BoxLayout:
            orientation: 'horizontal'
            Button:
                text:'Answer 1'
            Button:
                text:'Answer 2'
        BoxLayout:
            orientation: 'horizontal'
            Button:
                text:'Answer 3'
            Button:
                text:'Answer 4'
<Level9>:
    name:'level9'
    BoxLayout:
        orientation: 'vertical'
        Button:
            text:'Go  back'
            pos: 50, 50
            size_hint: .2, .2
            on_release:root.manager.current = 'levels'
            on_release:root.manager.transition.direction = 'right'
        Label:
            text:'Question 9'
        BoxLayout:
            orientation: 'horizontal'
            Button:
                text:'Answer 1'
            Button:
                text:'Answer 2'
        BoxLayout:
            orientation: 'horizontal'
            Button:
                text:'Answer 3'
            Button:
                text:'Answer 4'
<Level10>:
    name:'level10'
    BoxLayout:
        orientation: 'vertical'
        Button:
            text:'Go  back'
            pos: 50, 50
            size_hint: .2, .2
            on_release:root.manager.current = 'levels'
            on_release:root.manager.transition.direction = 'right'
        Label:
            text:'Question 10'
        BoxLayout:
            orientation: 'horizontal'
            Button:
                text:'Answer 1'
            Button:
                text:'Answer 2'
        BoxLayout:
            orientation: 'horizontal'
            Button:
                text:'Answer 3'
            Button:
                text:'Answer 4'
""")


class StartingScreen(Screen):
    pass


class LevelsScreen(Screen):
    pass


class Level1(Screen):
    pass


class Level2(Screen):
    pass


class Level3(Screen):
    pass


class Level4(Screen):
    pass


class Level5(Screen):
    pass


class Level6(Screen):
    pass


class Level7(Screen):
    pass


class Level8(Screen):
    pass


class Level9(Screen):
    pass


class Level10(Screen):
    pass


sm = ScreenManager(transition=SlideTransition())

sm.add_widget(StartingScreen(name='starting'))
sm.add_widget(LevelsScreen(name='levels'))
sm.add_widget(Level1(name='level1'))
sm.add_widget(Level2(name='level2'))
sm.add_widget(Level3(name='level3'))
sm.add_widget(Level4(name='level4'))
sm.add_widget(Level5(name='level5'))
sm.add_widget(Level6(name='level6'))
sm.add_widget(Level7(name='level7'))
sm.add_widget(Level8(name='level8'))
sm.add_widget(Level9(name='level9'))
sm.add_widget(Level10(name='level10'))


class MyQuizApp(App):

    def build(self):
        return sm


if __name__ == '__main__':
    MyQuizApp().run()

