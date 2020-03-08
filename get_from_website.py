from bs4 import BeautifulSoup
import requests

"creating and getting url"


def get_response(gene_id_pos):
    gene_rs = gene_id_pos
    url = "https://www.ncbi.nlm.nih.gov/search/all/?term=" + gene_rs
    source = requests.get(url).text  # gets the source code of response from website
    soup = BeautifulSoup(source, "lxml")

    return soup


"""finding paragraph with translation on the website of NCBI"""


def get_from_ncbi(soup):
    main_content = soup.find("main")
    # line_with_data = box_on_website.p
    section = main_content.find("section", class_="usa-section gquery")
    section_two = section.find("section", class_="gq-feature-section")
    div_one = section_two.find("div", class_="usa-grid-full")
    div_two = div_one.find("div", class_="usa-width-two-thirds primary-content")
    div_three = div_two.find("div", class_="shadowbox-wrapper")
    div_four = div_three.find("div", class_="shadowbox")
    div_five = div_four.find("div", class_="ncbi-docsum")
    div_six = div_five.find("div")
    paragraph = div_six.find("p", class_="ncbi-doc-excerpt").text

    if "in the" in paragraph:
        print(paragraph)

    return paragraph


"""finding translation result"""
"""not present"""

def biogps_result(paragraph):
    for i in range(len(paragraph)):
        if paragraph[i:i+7] == "in the ":
            print(paragraph[i+7:])


# testing
get_response("rs12564807")
soup = get_response("rs12564807")
get_from_ncbi(soup)