# Web Scraping and Performing NER using NLP
It is a Simple project which using wikipedia API to perform NER over the search results. It was devloped in python using Spacy and Wikipedia API library and it was created in Streamlit web app framework and was deployed using Heroku an open source PAAS. This project is included with a Python Notebook File and each code instruction is given in comments.

## Breif Introduction
### Web Scraping/Text Scraping
Web scraping, web harvesting, or web data extraction is data scraping used for extracting data from websites. The web scraping software may directly access the World Wide Web using the Hypertext Transfer Protocol or a web browser.
### What is Named Entity Recognition?
NER systems have been created that use linguistic grammar-based techniques as well as statistical models such as machine learning. Hand-crafted grammar-based systems typically obtain better precision, but at the cost of lower recall and months of work by experienced computational linguists . Statistical NER systems typically require a large amount of manually annotated training data. Semisupervised approaches have been suggested to avoid part of the annotation effort
### Named Entity Recognition in NLP
A Simple NER (Named-entity recognition) web scraping app using language python and technology NLP. In natural language processing, named entity recognition (NER) is the problem of recognizing and extracting specific types of entities in text. Such as people or place names.NER is both an interesting problem in NLP and also has many applications.We can find many meaninful insights from the text data by using the NLP.
### Features
-   It has many specific use cases like specific use cases an important one is in web search. By understanding the entities in a query, search engines deliver better results. Google uses this approach.Keywords search is definitely very useful. However, it can be improved further by augmenting it with entity recognition. This uses, in addition, knowledge about the main entities found in the document together with judgments on how significant of a role they play in that document.
-   A Second use case is in extracting product names or other salient entities from online reviews in a retail setting. These reviews may be at eCommerce sites or at social media ones. Clearly it is useful to know which products and features are being discussed in a particular review. As an example, consider the review Building a structured database from a corpus is also a use case of it.
-   One of the major uses cases of Named Entity Recognition involves automating the recommendation process. Recommendation systems dominate how we discover new content and ideas in today’s worlds. The example of Netflix shows that developing an effective recommendation system can work wonders for the fortunes of a media company by making their platforms more engaging and event addictive.
### Methods
- #### Dictionary-based
This is one of the simplest. However, it won’t work when the dictionary is incomplete, as would be the case when we are trying to use entity recognition to build a rich dictionary in the first place. (See the use case Building a structured database from a corpus described earlier in this post.)

- #### Supervised binary classification
This is an attractive approach to this problem. A training instance would be a short phrase labeled as positive (instance of the entity) or negative (not an instance of the entity). We’d also choose appropriate features to extract from the input phrase. (More on this later.) An important consideration is how to choose the negative instances for the training set. The universe of negative instances is huge — all phrases up to a certain length (what should this be?). Randomly sampling from the universe may give us weak negatives. Consequently, the learned classifier may be weaker than we think it is, relative to our assessment on a train-test split of the labeled data set. Point being that the negative instances are not real — we constructed them via a certain process — and that process may not be representative of the actual negatives we get in the field, which would be sufficiently short phrases in the text that are not instances of this entity.

- #### Feature Engineering
Consider recognizing national park names, i.e. distinguishing them from other phrases. The examples we have seen suggest a for-purpose heuristic variant of bag-of-words as the features. Specifically, first, we tokenize the input into words, then combine the last two words into a bigram, together with capturing that they are the last two words. This is easiest illustrated with examples.
## Installation
### Dependencies
- Latest version of [Python](https://www.python.org/downloads/windows/) (64-bit)
- Collab notebook /[Anaconda Jupyter Notebook](https://www.anaconda.com/products/individual)
- Python IDE(Spyder,PyCharm) /Code Editor(VsCode)
- Latest version of Git
- Web framework [Streamlit](https://streamlit.io/) ```pip install streamlit```
- [Heroku](https://dashboard.heroku.com/apps) PAAS to host app live
### Python libraries
-   [Spacy](https://pypi.org/project/scapy/) Nlp library ```pip install scapy```
-   [wikipedia](https://pypi.org/project/wikipedia/) API For searching the contents ```pip install wikipedia``
-   Dispacy(Scapy) for displaying annoted text ```from spacy import dispacy
-   [Natural language Toolkit](https://pypi.org/project/nltk/)(nltk)
### Python notebook link
```https://colab.research.google.com/drive/1otlCff6l17yWoj8Q9I_q1vWkcA5S2F2X?usp=sharing```
### Project Live Url

## Execution
### Data Scraping using Wikipedia API
- Scraping Data in Python Notebook using the [Wikipedia API](https://pypi.org/project/wikipedia/), Giving the user input to search and then retrive his search and -  perform text scraping
- Using [SpaCy Cli](https://spacy.io/api/cli). It provides a range of helpful commands for downloading and training pipelines, converting data and debugging your config, data and installation 
```import spacy.cli ```
### Perfoming NER over Scraped data
- Download trained pipelines for spaCy. The downloader finds the best-matching compatible version and uses pip install to download the Python package. Direct downloads don’t perform any compatibility checks and require the pipeline name to be specified with its version (e.g. en_core_web_sm-3.0.0). spacy.cli.download("en_core_web_md")
- Using Spacy Built_in Visualizer Displacy for annoted text highlighting extract entities like city, person, organisation, Date, Geographical Entity, Product etc.
Visualized named entities
![Screenshot (1)](https://user-images.githubusercontent.com/69640533/111735990-fc113e00-88a2-11eb-8497-39718c27ab01.png)
## Desigining Front end of App using Web Framework (Streamlit)
- Installation of [Streamlit](https://streamlit.io/) web Framework for Python for deploying High end Machine learning Model
### Introduction to Streamlit
Streamlit is an open-source app framework for Machine Learning and Data Science teams. Streamlit turns data scripts into shareable web apps in minutes. All in Python. All for free. No front‑end experience required.

- Installing streamlit
- ```pip install streamlit```
- ```streamlit hello```
### Stream lit
- Create a python file name it as app.py
- Refer to [StreamlitDocs](https://docs.streamlit.io/en/stable/)
- After Sucessfully installing Streamlit framework we will start coding our main python file import ```streamlit as st```
- We will add our NLP libraries and various libraries of python and start building our front end of app.
- To give a good look to our web app we will add an external css to main app.py file
- After designing, Our webpage will looke like this:
![Screenshot (2)](https://user-images.githubusercontent.com/69640533/111736352-ab4e1500-88a3-11eb-8350-a919eda25986.png)
## Executing Project
- To execute our project we just have to direct to our directory in local computer 
- Run the file with:
```streamlit run [filename]```
- The project will execute on your local domain in your browser
- After typing our search query in Text area our NER system will extract entities like city, person, organisation, Date, Geographical Entity, Product etc and will annote them.
![Screenshot (3)](https://user-images.githubusercontent.com/69640533/111736586-231c3f80-88a4-11eb-9781-e337dd7a1071.png)
- It will clearly classify the search result into city, person, organisation, Date, Geographical Entity, Product etc.

## Deployment of Project
- Now the Deployment of the project is the last stage of Project we can deploy over publicly accessible location like on AWS, Heroku, PythonAnywhere, etc.
- We are using Deployment pleatform Heroku[https://dashboard.heroku.com/apps]
- We need to install Heroku Cli in Windows
### Heroku
- Heroku is a cloud platform as a service supporting several programming languages.
One of the first cloud platforms, Heroku has been in development since June 2007, when it supported only the Ruby programming language, but now supports Java, Node.js, Scala, Clojure, Python and PHP.
- You can learn more about it [Heroku Docs]()
- So, We will Deploy our model over url and make it publically availaible.
### Our Project is Ready
#### For any queries Feel free to reach @shivampandit22698@gmail.com
