import json, matplotlib, operator, re, nltk
import matplotlib.pyplot as plt
from nltk.corpus import stopwords

fig, ax1 = plt.subplots()
depth = 100

# Load from JSON
data = []
with open('data.json', 'r') as file:
    data = json.load(file)

def tags():
    ax2 = ax1.twinx()

    for video in data[:depth]:
        tags = video['tags'].split("|")
        ax1.scatter(len(tags), int(video['likes']) / int(video['views']), color='blue')
        ax2.scatter(len(tags), int(video['views']), color='red')

    plt.ticklabel_format(useOffset=False)
    ax1.set_xlabel('Number of Tags')
    ax1.set_ylabel('Like/View Ratio')
    ax2.set_ylabel('Views')
    fig.tight_layout()
    ax1.legend(['Ratio'], loc='upper left')
    ax2.legend(['Views'])
    plt.show()

def tag_words():

    words = {}
    stop_words = set(stopwords.words('english'))


    for video in data[:depth]:
        try:
            # Split tags from CSV formatting and clean
            words_in_tags = video['tags'].replace('"', '').replace(" ", "|").split("|")

            # Throw words into a dictionary
            for word in words_in_tags:

                # Remove punctuation and turn lowercase
                word = re.sub(r'[^\w\s]', '', word.lower())

                # Only add to dictionary if NOT a stop word
                if word not in stop_words:
                    if word in words.keys():
                        words[word] = words[word] + 1
                    else:
                        #Change encoding and strip string
                        words.update({str(word.encode('utf8'))[2:-1]: 1})
        except:
            pass

    # Sort by most used words
    words = sorted(words.items(), key=operator.itemgetter(1), reverse=True)
    print(words)

    w = []
    f = []
    for word in words[:50]:
        w.append(word[0])
        f.append(word[1])

    plt.bar(w, f)
    plt.xticks(rotation=50)
    plt.xlabel("Country of Origin")
    plt.ylabel("Number of Wines")
    plt.show()



tag_words()
