import pandas as pd
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
import string
from gensim import corpora
from nltk.tokenize import RegexpTokenizer

# If you haven't downloaded the stopwords dataset, do so now
import nltk
nltk.download('stopwords')
nltk.download('wordnet')

# Load the dataset
data = pd.read_csv("C:/Users/28905/Documents/PKU RA/gp-search-20240405-192705.csv", encoding='ISO-8859-1')

# Focus on the first 1000 patents
data = data.head(1001)

# Combine title and abstract for topic modeling
data['text'] = data['title'] + ' ' + data['assignee']

# Text preprocessing
tokenizer = RegexpTokenizer(r'\w+')
stop = set(stopwords.words('english'))
lemmatize = WordNetLemmatizer()
texts = []

for index, raw in data['text'].items():  # Using .items() for Series
    raw = raw.lower()
    tokens = tokenizer.tokenize(raw)
    stopped_tokens = [i for i in tokens if not i in stop]
    lemma_tokens = [lemmatize.lemmatize(i) for i in stopped_tokens]
    texts.append(lemma_tokens)

# Creating the term dictionary of our corpus, where every unique term is assigned an index
dictionary = corpora.Dictionary(texts)

# Converting list of documents (corpus) into Document Term Matrix using the dictionary
doc_term_matrix = [dictionary.doc2bow(text) for text in texts]
from gensim.models.ldamodel import LdaModel
from gensim.models.coherencemodel import CoherenceModel

def compute_coherence_values(dictionary, corpus, texts, limit, start=2, step=3):
    coherence_values = []
    model_list = []
    for num_topics in range(start, limit, step):
        model = LdaModel(corpus=corpus, id2word=dictionary, num_topics=num_topics)
        model_list.append(model)
        coherencemodel = CoherenceModel(model=model, texts=texts, dictionary=dictionary, coherence='c_v')
        coherence_values.append(coherencemodel.get_coherence())

    return model_list, coherence_values

# Can take a long time to run.
model_list, coherence_values = compute_coherence_values(dictionary=dictionary, corpus=doc_term_matrix, texts=texts, start=2, limit=40, step=6)

# Show graph
import matplotlib.pyplot as plt

limit=40; start=2; step=6;
x = range(start, limit, step)
plt.plot(x, coherence_values)
plt.xlabel("Num Topics")
plt.ylabel("Coherence score")
plt.legend(("coherence_values"), loc='best')
plt.show()

# Print the coherence scores
for m, cv in zip(x, coherence_values):
    print("Num Topics =", m, " has Coherence Value of", round(cv, 4))

# Select the model and print the topics
optimal_model = model_list[coherence_values.index(max(coherence_values))]
model_topics = optimal_model.show_topics(formatted=False)
optimal_model.print_topics(num_words=10)
