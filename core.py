"""
core.py is a part of a project 'Ariadna' developed by Olha Babicheva and Konrad Kihan
File reads user's genome -> translates rsid from genome into gene names basing on ncbi database->
-> save data into the file
More information in README file
"""

import csv  # reading and creating csv file
import requests  # getting respone from a website
from bs4 import BeautifulSoup  # finding content on a website


def rsid_finder(file):
    with open(file, 'r') as csv_file:    # opens file to alisis
        csv_reader = csv.DictReader(csv_file)

        # searches for RSID that is available in other databases (the RS one)
        gene_id = []

        for line in csv_reader:
            if line["rsid"][0] == "r":
                gene_id.append(line["rsid"])  # list that contains all RSIDs

        return gene_id


# connecting with a website
def get_response(gene_id_pos):
    gene_rs = gene_id_pos  # it specifies witch to witch rsid page need to connect
    url = "https://www.ncbi.nlm.nih.gov/search/all/?term=" + gene_rs  # full url
    source = requests.get(url).text  # gets the source code of response from website
    soup = BeautifulSoup(source, "html.parser")  # converting
    return soup


# finds the translation for gene name on ncbi website while connected
def get_from_web():
    paragraph = soup.find_all('p', class_="ncbi-doc-excerpt")


    return paragraph


# creates the dictionary csv file where RSID and GENE NAMES are stored
def write_dict(rsid, name, dictionary_file):
    with open(dictionary_file, "a", newline="") as new_file:
        csv_writer = csv.writer(new_file)
        csv_writer.writerow([rsid, name])


file = input("Enter name of the file you want to open: ")
if file == "" or file == " " or file == "  " or file == "\t":
    print("File name empty.")
    file = "genome_zeeshan_usmani.csv"
    gene_id = rsid_finder(file)  # got a list with all RSIDs from file
else:
    try:
        rsid_finder(file)
        gene_id = rsid_finder(file)  # got a list with all RSIDs from file
    except FileNotFoundError as e:
        print(e)



"""When list with RSIDS is loaded into memory - find all translations
finding paragraph with translation on the website of NCBI"""

dictionary = input("Enter name of dictionary file that will be created during the process: ") # dictionary name
dictionary = dictionary + ".csv"
for rs in gene_id:
    # getting entering NCBI website for each RSID
    get_response(rs)
    soup = get_response(rs)
    try:
        get_from_web()
        paragraph = get_from_web()
        paragraph = str(paragraph[0]).split()

        # rejecting only paragraphs with variations
        if "in" in paragraph:

            value = paragraph[6]
            # rejecting multiple variations
            if "," not in value:

                write_dict(rsid=rs, name=value, dictionary_file=dictionary)
            else:
                pass




    except AttributeError as e:
        print(e)    # pops up if no RSID - GENE translation in database"""



"""part of previous data_presenting.py"""


file = "choroby.csv"


def name_find(file=file):
    with open(file, "r") as csv_file:
        csv_reader = csv.reader(csv_file)

        next(csv_reader)

        gene = []


        for line in csv_reader:
            gene.append(line[0])

    return gene


def corelation_find(file=file):
    with open(file, "r") as csv_file:
        csv_reader = csv.reader(csv_file)

        next(csv_reader)

        corel = []

        for line in csv_reader:
            corel.append(line[1])

    return corel


def issue_find(file=file):
    with open(file, "r") as csv_file:
        csv_reader = csv.reader(csv_file)

        next(csv_reader)

        issue = []

        for line in csv_reader:
            issue.append(line[2])

    return issue


name = name_find()
corel = corelation_find()
issue = issue_find()



postioner = 0

# checks is issue was already printed out
is_appeard = []
try:
    filetoread = input("Enter name of your dictionary file: ")
    with open(filetoread, "r") as dictionary:
        csv_reader = csv.reader(dictionary)

        # line[1] - choroba
        # corelation_index - index choroby + 2
        # issue_index - jest taki sam jak corelation_index
        for line in csv_reader:
            if line[1] in name:
                # indexes from other tables
                corelation_index = name.index(line[1])
                issue_index = corelation_index

                # thanks to this IF lines dont multiply
                if line[1] not in is_appeard:
                    print(line[1], corel[corelation_index], issue[issue_index])
                    is_appeard.append(line[1])
                else:
                    pass
except FileNotFoundError as e:
    print(e)