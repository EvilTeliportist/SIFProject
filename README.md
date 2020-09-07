# SIF Data Analysis Project
For this project, I used the provided dataset of 2017 YouTube videos to show the top YouTube topic of the time period.
First, I converted the provided CSV file into a JSON for easy of access.
Then, I grabbed each of the descriptions of the YouTube videos and stored them in a list after cleaning them, meaning that I removed punctuation and stop words, and turned it all lowercase.
Then, I performed TFIDF (term frequency–inverse document frequency) on the descriptions to assign weights to represent importance to all words that were found.
After the TFIDF, I used NMF (non-negative matrix factorization) to extract the "features" of the dataset, which will sort out the topics from the TFIDF matrix.
Lastly, it's just a simple process of outputting the results, which can be seen here:
```Python
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
```
