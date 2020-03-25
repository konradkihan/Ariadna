import csv

"""
def name_finder(file="choroby.csv"):
    with open(file, 'r') as csv_file:    # opens file to alisis
        csv_reader = csv.DictReader(csv_file)

        gene = []

        for line in csv_reader:
            if line["gene_name"][0] == "r":
                gene.append(line["gene_name"])
                print(gene)
"""
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
    filetoread = input("Enter name of your dictionary file")
    resultfile = open('wynik.txt', 'a+')
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
                    result = line[1], corel[corelation_index], issue[issue_index]
                    resultfile.write(str(result))
                    is_appeard.append(line[1])
                else:
                    pass
except FileNotFoundError as e:
    print(e)