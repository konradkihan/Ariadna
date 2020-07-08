from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config
from kivy.utils import get_color_from_hex
from kivy.uix.image import Image, AsyncImage
from kivy.uix.textinput import TextInput
from kivy.core.window import Window


import csv



Config.set('graphics', 'resizable', 0)
Config.set('graphics', 'width', 1080)
Config.set('graphics', 'height', 720)
Window.clearcolor = get_color_from_hex("#1c1c24")

class Ariadna(App):
    def build(self):
        bl = BoxLayout(orientation = "vertical", padding = 10)
        gl = GridLayout(cols = 3, spacing = 20)

        self.img = Image(source='ariadna.png')
        bl.add_widget(self.img)

        self.file = TextInput(text="Source of genome file", size_hint=(.5, .2), multiline=False)
        gl.add_widget(self.file)
        self.dictionary = TextInput(text="Name of dictionary", size_hint=(.5, .2), multiline=False)
        gl.add_widget(self.dictionary)
        self.submit = Button(text="OK", background_color=get_color_from_hex("#1c1c24"), size_hint=(.2, .2))
        self.submit.bind(on_press=lambda x: self.runtime(self.file, self.dictionary))
        gl.add_widget(self.submit)

        bl.add_widget(gl)
        # w teorii tutaj ma już być plik z wynikami, ale przecież teraz robię gui bez funkcjonalności, więc have fun xD
        with open("endfile.csv") as f:
            contents = f.read()
        gl.add_widget(Label(text=contents, font_size = 20, size_hint=(1,1)))
        return bl

    def runtime(self, file, dictionary):
        from coreobject import WriteDct, Core
        file = file.text
        dictionary = dictionary.text


        gene_id = Core().rsid_finder(file)

        core = Core()

        for rs in gene_id:
            # getting entering NCBI website for each RSID

            try:
                paragraph = core.get_response(rs)
                paragraph = str(paragraph).split()

                # rejecting only paragraphs with variations
                if "in" in paragraph:
                    value = paragraph[6]
                    if value[-1] == ",":
                        value = value[0:-1]
                    # rejecting multiple variations
                    if "," not in value:
                        core.write_dict(rsid=rs, name=value, dictionary_file=dictionary)

                    else:
                        pass

            except AttributeError as e:
                print(e)  # pops up if no RSID - GENE translation in database

        WriteDct = WriteDct()

        name = WriteDct.name_find()
        corel = WriteDct.corelation_find()
        issue = WriteDct.issue_find()

        # checks if issue was already printed out
        is_appeard = []

        try:
            filetoread = dictionary
            with open(filetoread, "r") as dictionary:
                csv_reader = csv.reader(dictionary)

                # line[1] - choroba
                # corelation_index - index choroby + 2
                # issue_index - jest taki sam jak corelation_index
                endF = open("endfile.csv", "w")
                for line in csv_reader:
                    if line in csv_reader:
                        if line[1] in name:
                            # indexes from other tables
                            corelation_index = name.index(line[1])
                            issue_index = corelation_index

                            # thanks to this IF lines do not multiply
                            if line[1] not in is_appeard:
                                endF.write(f"{line[1], corel[corelation_index], issue[issue_index]}")
                                is_appeard.append(line[1])
                            else:
                                pass

        except FileNotFoundError as e:
            print(e)

if __name__ == '__main__':
    Ariadna().run()