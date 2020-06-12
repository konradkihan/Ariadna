import csv
import requests
from bs4 import BeautifulSoup


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
        self.soup = BeautifulSoup(source, "html.parser")  # converting
        return self.soup

    # finds the translation for gene name on ncbi website while connected
    def get_from_web(self):
        self.paragraph = self.soup.find_all('p', class_="ncbi-doc-excerpt")
        return self.paragraph
    # creates the dictionary csv file where RSID and GENE NAMES are stored
    def write_dict(self, rsid, name, dictionary_file):
        with open(dictionary_file, "a", newline="") as new_file:
            csv_writer = csv.writer(new_file)
            csv_writer.writerow([rsid, name])

class WriteDct:
    global file
    file = "choroby.csv"

    def name_find(self, file=file):
        with open(file, "r") as csv_file:
            csv_reader = csv.reader(csv_file)

            next(csv_reader)

            self.gene = []

            for line in csv_reader:
                self.gene.append(line[0])
        return self.gene

    def corelation_find(self, file=file):
        with open(file, "r") as csv_file:
            csv_reader = csv.reader(csv_file)

            next(csv_reader)

            self.corel = []

            for line in csv_reader:
                self.corel.append(line[1])
        return self.corel

    def issue_find(self, file=file):
        with open(file, "r") as csv_file:
            csv_reader = csv.reader(csv_file)

            next(csv_reader)

            self.issue = []

            for line in csv_reader:
                self.issue.append(line[2])

        return self.issue


"""end of classes"""

"""When list with RSIDS is loaded into memory - find all translations
finding paragraph with translation on the website of NCBI"""

file = input("Enter name of the file you want to open: ")

gene_id = Core().rsid_finder(file)

dictionary = input("Enter name of dictionary file that will be created during the process: ") + ".csv"  # dictionary name

for rs in gene_id:
    # getting entering NCBI website for each RSID
    Core().get_response(rs)
    soup = Core().get_response(rs)

    try:
        paragraph = Core().get_from_web()
        paragraph = str(paragraph[0].split())
        # rejecting only paragraphs with variations
        if "in" in paragraph:
            value = paragraph[6]
            # rejecting multiple variations
            if "," not in value:
                Core().write_dict(rsid=rs, name=value, dictionary_file=dictionary)

            else:
                pass

    except AttributeError as e:
        print(e) # pops up if no RSID - GENE translation in database


name = WriteDct().name_find()
corel = WriteDct().corelation_find()
issue = WriteDct().issue_find()

# checks if issue was already printed out
is_appeard = []

try:
    filetoread = dictionary
    with open(filetoread, "r") as dictionary:
        csv_reader = csv.reader(dictionary)

        # line[1] - choroba
        # corelation_index - index choroby + 2
        # issue_index - jest taki sam jak corelation_index

        for line in csv_reader:
            if line in csv_reader:
                if line[1] in name:
                    # indexes from other tables
                    corelation_index = name.index(line[1])
                    issue_index = corelation_index

                    # thanks to this IF lines do not multiply
                    if line[1] not in is_appeard:
                        print(line[1], corel[corelation_index], issue[issue_index])
                        is_appeard.append(line[1])
                    else:
                        pass

except FileNotFoundError as e:
    print(e)





