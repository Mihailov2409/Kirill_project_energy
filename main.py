import kivy
from kivy.app import App
from kivy.lang.builder import Builder
from kivy.core.window import Window
from kivy.uix.modalview import ModalView
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
import save_json
import calc
Window.size = (1440/4, 2960/4)
speed = 0
class Solis(App):
    def build(self):
        return Builder.load_file('style.kv')
    def on_start(self):
        name, mass = save_json.pars_fail()
        self.root.ids.name.text = name
        self.root.ids.mass.text = str(mass)
    def source(self):
        march = self.root.ids.name_mar.text
        try:
            a, b, pos, march = save_json.pars_mar(march)
            self.root.current = 'library_bat'
            self.root.ids.a_bat.text = a
            self.root.ids.b_bat.text = b
            self.root.ids.position_bat.text = pos
            self.root.ids.name_path_bat.text = march
        except:
            pass
    def save(self):
        name = self.root.ids.name.text
        mass = self.root.ids.mass.text
        save_json.save_fail(name, mass)
    def dada(self):
        global speed
        ves = self.root.ids.mass.text
        km = self.root.ids.position_bat.text
        try:
            resul = calc.calculator(int(ves), str(speed), int(km))
            win = ModalView(auto_dismiss=True, size_hint=(1, 0.3), pos_hint={'x': .0, 'y': .0})
            b = Button(text=f"{resul}kk")
            win.add_widget(b)
            win.open()
        except:
            print("Speed?")
    def qwerty(self, x):
        global speed
        speed = str(x)
    def speed_speed(self):
        win = ModalView(auto_dismiss=True, size_hint=(1, 0.3), pos_hint={'x': .0, 'y': .0})
        box = BoxLayout(orientation='vertical')
        fkm = Button(text="4km|h")
        skm = Button(text="6km|h")
        ekm = Button(text="8km|h")
        box.add_widget(fkm)
        box.add_widget(skm)
        box.add_widget(ekm)
        win.add_widget(box)
        win.open()
        fkm.bind(on_press=lambda x: self.qwerty("4km|h"))
        skm.bind(on_press=lambda x: self.qwerty("6km|h"))
        ekm.bind(on_press=lambda x: self.qwerty("8km|h"))
    def pos_save(self):
        a = self.root.ids.a.text
        b = self.root.ids.b.text
        position = self.root.ids.position.text
        name_path = self.root.ids.name_path.text
        if name_path == '' or name_path == ' ':
            self.root.ids.name_path.text = 'Введи имя маршута'
        else:
            save_json.library_save(a, b, position, name_path)
    def back_save(self):
        self.root.ids.a.text = ''
        self.root.ids.b.text = ''
        self.root.ids.position.text = ''
        self.root.ids.name_path.text = ''
    def screen(self, x):
        self.root.current = x
if __name__ == '__main__':
    Solis().run()