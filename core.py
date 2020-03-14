from bs4 import BeautifulSoup
import requests
import csv
print("CHECKPOINT 0")


def rsid_finder(file):
    with open(file, 'r') as csv_file:    # opens file to alisis
        csv_reader = csv.DictReader(csv_file)

        # searches for RSID that is available in other databases (the RS one)
        gene_id = []

        for line in csv_reader:
            if line["rsid"][0] == "r":
                gene_id.append(line["rsid"])  # list that contains all RSIDs

        return gene_id


def get_response(gene_id_pos):
    gene_rs = gene_id_pos
    url = "https://www.ncbi.nlm.nih.gov/search/all/?term=" + gene_rs
    source = requests.get(url).text  # gets the source code of response from website
    soup = BeautifulSoup(source, "lxml")

    return soup


def get_from_web():
    main_content = soup.find("main")

    section = main_content.find("section", class_="usa-section gquery")
    section_two = section.find("section", class_="gq-feature-section")
    div_one = section_two.find("div", class_="usa-grid-full")
    div_two = div_one.find("div", class_="usa-width-two-thirds primary-content")
    div_three = div_two.find("div", class_="shadowbox-wrapper")
    div_four = div_three.find("div", class_="shadowbox")
    div_five = div_four.find("div", class_="ncbi-docsum")
    div_six = div_five.find("div")
    paragraph = div_six.find("p", class_="ncbi-doc-excerpt").text
    return paragraph


def write_dict(rsid, name):
    with open("dictionary.csv", "a", newline="") as new_file:
        csv_writer = csv.writer(new_file)
        # for rsid in dictionary:
        csv_writer.writerow([rsid, name])


file = input("Enter name of the file you want to open: ")
if file == "" or file == " " or file == "  " or file == "\t":
    print("File name empty.")
    file = "genome_zeeshan_usmani.csv"
    gene_id = rsid_finder(file)  # got a list with all RSIDs from file
else:
    try:
        file = "'" + file + "'"
        rsid_finder(file)
        gene_id = rsid_finder(file)  # got a list with all RSIDs from file
    except FileNotFoundError as e:
        print(e)


"""When list with RSIDS is loaded into memory - find all translations"""
print("CHECKPOINT 1")


"""finding paragraph with translation on the website of NCBI"""
for rs in gene_id:
    # getting entering NCBI website for each RSID
    get_response(rs)
    soup = get_response(rs)
    try:
        get_from_web()
        paragraph = get_from_web()

        # print("CHECKPOINT 2")
        if "in the" in paragraph:
            value = paragraph.split()
            write_dict(rsid=rs, name=value[5])
    except AttributeError as e:
        print(e)    # pops up if no RSID - GENE translation in database


