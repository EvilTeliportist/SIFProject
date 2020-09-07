import json, matplotlib, operator, re, nltk, sklearn
import pandas as pd
import numpy as np
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.decomposition import NMF, LatentDirichletAllocation
from sklearn.feature_extraction.text import TfidfVectorizer



# Load CSV data from JSON (I converted it previously for ease of access)
data = []
with open('data.json', 'r') as file:
    data = json.load(file)

# Clean string and stem words
def clean_string(content):
    clean1 = re.sub('[^a-zA-z]', ' ', content)
    clean = clean1.lower().split()
    stem = PorterStemmer()
    clean = [stem.stem(word) for word in clean if word not in set(stopwords.words("english"))]
    clean = " ".join(clean)
    return clean

def main():

    descriptions = []
    for video in data[:100]:
        # Clean descriptions, remove newline escape characters
        desc = clean_string(video['description'].replace("\\n", " "))
        descriptions.append(desc)

    # Initialize vectorizer, then fit it to the descriptions
    vectorizer = TfidfVectorizer()
    matrixTF = vectorizer.fit_transform(descriptions).toarray()

    # Make final matrix
    matrix = pd.DataFrame(np.array(matrixTF), columns = vectorizer.get_feature_names())

    # Proceed with Non-negative matrix factorization
    model = NMF(n_components = 10).fit(matrix)
    feature_names = vectorizer.get_feature_names()

    # Print topics
    for topic_id, topic in enumerate(model.components_):
        print("Topic %d:" % (topic_id + 1))
        text = " ".join([feature_names[i] for i in topic.argsort()[:-20:-1]])
        print(text)

if __name__ == '__main__':
    main()

'''
Topic 1:
http com www twitter facebook instagram youtub patreon nickelback org johnmaclean higatv dream meganbatoon offic articl buzzfe hellthyjunkfood snapchat
Topic 2:
goo gl http aquarium crack click com us petersripol wwe build viralhog truck licens video walk train eminem best
Topic 3:
bit ly http cb video nail music late new youtu show ebay cloth morn javal sunday corden lnk polish
Topic 4:
smarturl http amor eazi tbad avail music spotifi iqid hunter itun fosterthepeopl appl amazon com futurefriendspart yt lnk stream
Topic 5:
amzn http soni com tinyurl cream ice camera mm len video microphon ijustin gracehelbig www contain use kingston canon
Topic 6:
time playlist world list pl news xgzxi iran iraq dead said anoth peopl press least youtub lebron confer gave
Topic 7:
com http youtub watch lelepon rudymancuso instagram lele shot youtu video rudi inanna anwar maejor pon alesso anitta iisuperwomanii
Topic 8:
nfl game player rest seahawk seattl sherman richard critic three ask play day touchdown footbal schedul return nov us
Topic 9:
movi john fox director trailer jason sin th us reaction offici justic showman greatest centuri think bateman mcadam comedi
Topic 10:
tune inform stay littl dad givealittlebit hodgson shhhh roger rogerhodgson give christma magic creat help amazon town big see
'''
