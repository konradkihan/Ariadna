import csv


def rsid_finder(file):
    with open(file, 'r') as csv_file:    # opens file to alisis
        csv_reader = csv.DictReader(csv_file)

        # searches for RSID that is available in other databases (the RS one)
        gene_id = []

        for line in csv_reader:
            if line["rsid"][0] == "r":
                gene_id.append(line["rsid"])  # list that contains all RSIDs

        return gene_id

