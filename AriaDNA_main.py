from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config
from kivy.utils import get_color_from_hex
from kivy.uix.image import Image
from kivy.uix.textinput import TextInput
from kivy.core.window import Window


import csv
import requests
import os
from bs4 import BeautifulSoup


Config.set('graphics', 'resizable', 0)
Config.set('graphics', 'width', 1080)
Config.set('graphics', 'height', 720)
Window.clearcolor = get_color_from_hex("#1c1c24")

class Core:
    def rsid_finder(self, file):
        with open(file, 'r') as csv_file:  # opens file to alisis
            csv_reader = csv.DictReader(csv_file)

            # searches for RSID that is available in other databases (the RS one)
            self.gene_id = []

            for line in csv_reader:
                if line["rsid"][0] == "r":
                    self.gene_id.append(line["rsid"])  # list that contains all RSIDs
        return self.gene_id

    # connecting with a website
    def get_response(self, gene_id_pos):
        gene_rs = gene_id_pos  # it specifies witch to witch rsid page need to connect
        url = "https://www.ncbi.nlm.nih.gov/search/all/?term=" + gene_rs  # full url
        source = requests.get(url).text  # gets the source code of response from website
        soup = BeautifulSoup(source, "html.parser")  # converting
        self.paragraph = soup.find_all('p', class_="ncbi-doc-excerpt")
        return self.paragraph

    # creates the dictionary csv file where RSID and GENE NAMES are stored
    def write_dict(self, rsid, name, dictionary_file):
        with open(dictionary_file, "a", newline="") as new_file:
            csv_writer = csv.writer(new_file)
            csv_writer.writerow([rsid, name])



class WriteDct:
    file = "choroby.csv"

    def name_find(self, file=file):
        with open(file, "r") as csv_file:
            csv_reader = csv.reader(csv_file)

            next(csv_reader)

            gene = []

            for line in csv_reader:
                gene.append(line[0])
        return gene

    def corelation_find(self, file=file):
        with open(file, "r") as csv_file:
            csv_reader = csv.reader(csv_file)

            next(csv_reader)

            corel = []

            for line in csv_reader:
                corel.append(line[1])
        return corel

    def issue_find(self, file=file):
        with open(file, "r") as csv_file:
            csv_reader = csv.reader(csv_file)

            next(csv_reader)

            issue = []

            for line in csv_reader:
                issue.append(line[2])

        return issue

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
        gl.add_widget(Label(text='', font_size=20, size_hint=(1, 1)))
        return bl

    def runtime(self, file, dictionary):
        file = file.text
        dictionary = dictionary.text


        gene_id = Core().rsid_finder(file)

        core = Core()

        for rs in gene_id:
            # getting entering NCBI website for each RSID

            try:
                paragraph = core.get_response(rs)
                paragraph = str(paragraph)

                # rejecting only paragraphs with variations
                if "in" in paragraph:
                    value = paragraph[paragraph.find("<b>")+3:paragraph.find("</b>")]
                    if len(value) < 10:
                        core.write_dict(rsid=rs, name=value, dictionary_file=dictionary)
                    else: pass

            except AttributeError as e:
                print(e)  # pops up if no RSID - GENE translation in database

        writeDct = WriteDct()

        name = writeDct.name_find()
        corel = writeDct.corelation_find()
        issue = writeDct.issue_find()

        # checks if issue was already printed out
        is_appeard = []

        try:
            filetoread = dictionary
            with open(filetoread, "r") as dictionary:
                csv_reader = csv.reader(dictionary)
                # line[1] - choroba
                # corelation_index - index choroby + 2
                # issue_index - jest taki sam jak corelation_index
                choroby = open("choroby.csv")

                # skończyły mi się nazwy i gubię się w zmiennych :c
                geny_lista_czy_cos = []
                for line in csv_reader:
                    geny_lista_czy_cos.append(line)

                choroba = []
                for cline in choroby:
                    choroba.append(cline.split(","))

                choroba.pop(0)
                c = None
                l = []
                for i in range(len(geny_lista_czy_cos)):
                    if geny_lista_czy_cos[i] not in l:
                        l.append([choroba[0], choroba[1], choroba[2], geny_lista_czy_cos[i][0]])
                        c = choroba[0]

                result = []
                for i in range(len(l)):
                    for j in range(len(l[i])):
                        if l[i][j] not in result and type(l[i][j]) != str:
                            result.append(l[i][j])

                f = open('wynik.txt', 'a+')
                for i in result:
                    f.write(' '.join(i))
                f.close()
                os.system("wynik.txt")
                        # chyba koniec


        except FileNotFoundError as e:
            print(e)

if __name__ == '__main__':
    Ariadna().run()
