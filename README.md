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
### Python libraries
-   [Spacy](https://pypi.org/project/scapy/) Nlp library ```pip install scapy```
-   [wikipedia](https://pypi.org/project/wikipedia/) API For searching the contents ```pip install wikipedia``
-   Dispacy(Scapy) for displaying annoted text ```from spacy import dispacy
-   [Natural language Toolkit](https://pypi.org/project/nltk/)(nltk)
### Python notebook link
```https://colab.research.google.com/drive/1otlCff6l17yWoj8Q9I_q1vWkcA5S2F2X?usp=sharing```
### Project Live Url

## Execution
