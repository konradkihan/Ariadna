# Ariadna
Application that analyse the human genome, translates it's content to the gene parts and calculates
risk of suffering in one of a few genetic diseases. <br>
Data-set from: <br> 
* http://biogps.org <br>
* http://biogps.org/#goto=genereport&id=57695 <br>
* http://www.ensembl.org/ <br>


# Application info
**Language: Python 3.6** <br> <br>
**Modules / technologies used:**
* "csv" python module
* "requests" python module
* "BeautifulSoup" python module
* "kivy" python module


**Full application contains:**<br>
* core.py - core of the whole computing, responsible for reading file with genome, translating and interpreting provided data <br>
* kivygui.py & ariadnagui.kv - files responsible for nice and smooth GUI
* choroby.csv - CSV file with gene_name responsible for disease and its correlation. Used by core.py. Provides data for 
diseases such as: <br>
Alzheimer / Obesity / Down Syndrome / Cystic Fibrosis / Williams Syndrome <br>

**Prepare environment in CMD:**
```cmd
pip install csv
pip install response
pip install bs4
pip install docutils pygments pypiwin32 kivy.deps.sdl2 kivy.deps.glew
pip install kivy.deps.gstreamer
pip install kivy.deps.angle
pip install kivy
```

**Usage:**
1. Prepare your file with genome
2. Put all necessary program files in same destination
3. Run "Execution.py" file
4. Wait ;) <br>

Internet connection necessary

**Credits** 
Olha Babicheva (lead) <br>
Konrad Kihan <br>
<br>
Zespół Szkół im. Obrońców Poczty Polskiej in Gdańsku
