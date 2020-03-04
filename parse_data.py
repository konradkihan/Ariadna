import csv

with open('genome_zeeshan_usmani.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

# searches for RSID that is avaliable in other databases (the RS one)
    def rsid_finder():
        gene_id = []
        for line in csv_reader:
            if line["# rsid"][0] == "r":
                gene_id.append(line["# rsid"])  # ERROR - LIST ALWAYS EMPTY

        return gene_id

    rsid_finder()

    gene_id = rsid_finder()

    print(gene_id)