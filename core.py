try:
    from parse_data import *
    from get_from_website import *
except ModuleNotFoundError as e:
    print(e)
    exit()


"""Open file with RSID"""
print("CHECKPOINT 0")

file = input("Enter name of the file you want to open: ")
if file == "" or file == " " or file == "  " or file == "\t":
    print("File name empty.")
    file = "genome_zeeshan_usmani.csv"
else:
    try:
        file = "'" + file + "'"
        rsid_finder(file)
        gene_id = rsid_finder(file)  # got a list with all RSIDs from file
    except FileNotFoundError as e:
        print(e)


"""When list with RSIDS is loaded into memory - find all translations"""
print("CHECKPOINT 1")


translated = []

for rs in gene_id:
    # getting entering NCBI website for each RSID
    get_response(rs)
    soup = get_response(rs)
    try:
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

        if "in the" in paragraph:

            translated.append(rs)
            print(translated)
    except AttributeError:
        pass

