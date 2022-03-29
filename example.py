

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy_garden.ebs.clocks import SimpleDigitalClock


class ClockExampleApp(App):
    def build(self):
        w = BoxLayout(size=(500, 200))
        clock = SimpleDigitalClock()
        clock.start()
        w.add_widget(clock)
        return w


ClockExampleApp().run()
