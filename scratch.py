from bs4 import BeautifulSoup
import requests


gene_rs = "rs28359182"
url = "https://www.ncbi.nlm.nih.gov/search/all/?term=" + gene_rs

source = requests.get(url).text  # gets the source code of response from website
soup = BeautifulSoup(source, "lxml")

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
paragraph = div_six.find("p", class_="ncbi-doc-excerpt")

print(paragraph)

