import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout


from kivy.uix.widget import Widget


class InputData(GridLayout):

    # stuff taken from ariadna.kv file    genomefile = ObjectProperty(None)
    newdict = ObjectProperty(None)


    def foo(self):
        print(self.genomefile.text, self.newdict.text)

        # clear input
        self.genomefile.text = ""
        self.newdict.text = ""



class AriadnaGui(App):

    def build(self):
        from kivy.config import Config
        Config.set("kivy", "window_icon", "logo.png")
        return InputData()


if __name__ == "__main__":
    AriadnaGui().run()
