import requests
from bs4 import BeautifulSoup

from parse_data import gene_id

def find_gene_on_ncbi():
    url = "https://www.ncbi.nlm.nih.gov/search/all/?term=" + gene_rs  # variable that stores full url
    source = requests.get(url).text  # gets the source code of response from website
    soup = BeautifulSoup(source, "lxml")
    box_on_website = soup.find('div')
    line_with_data = box_on_website.p.text

for rs_num in gene_id:
    gene_rs = gene_id[rs_num]   # stores the position of from "gene_id" list from parse_data.py

    find_gene_on_ncbi()
