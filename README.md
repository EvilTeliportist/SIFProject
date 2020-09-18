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
These outputs can show us a lot about the dataset. First, there are a lot of words that are not necessarily correlated to a topic, like "http", "com", "bit ly", "goo gl", "smartuld", and "click". These are all common words that would be found in a description regardless of topic because there are plenty of links and things like that in descriptions. However, many of the catagories do show topics. Topic 1, the most popular, has a lot of social medias but also some trending names. The social medias are also popular words, so they do not pertain to any topics. In Topic 5, however, we can see that there are mentions of cameras, iPhones, microphones, etc, which was probably because of the upcoming release of the iPhone 8. We also see topics that contain words about football, the Seahawks, and a new film, the Greatest Showman. Trending names such as Lele Pons, Rudy Mancuso, and IISuperwomanII, were also prevalent.

Techniques like these can be used in many applications, like news bots. These bots could assess the trending topics, the connotations surrounding them, and choose whether to buy or short a position based on that. I suspect that bots like those would need a ton of tweaking with many specific parameters, but could prove useful in processing news information faster than human traders.


# FOR SIF READERS
I talked to Uro in the September 17th meeting about a personal project that I'm working on with a friend, Koby Adu-Bonnah, who is also applying to SIF. Please understand that while we just recently started this project, we did NOT start the project with the intention of trying to use it to get into SIF. That said, the project is a lightweight public API called Stocket for getting minute data of the equities in the SMP500. We used asynchronous requests in python to scrape the data from marketwatch.com, the post it to an authenticated endpoint on the main web server written in Node.js. From there, the main web server deals with inputting data into the database (we will probably move this to the python scripts to keep load off of the server) as well as handling requests from our python package, [PyStocket](https://github.com/EvilTeliportist/pystocket). The data is stored in an SQL database using Microsoft's SQL dialect, as the entire project is hosted on Azure. Lastly, we added a small [frontend setup](https://rtstockdata.azurewebsites.net/) for users looking to create an account and recieve their access token and provide some basic information about Stocket. As of right now, you must create an account to see the information, but it is the same that is found in the PyStocket repo. Feel free to try it out, as you can easily use false credentials to make an account (we will probably add email verification in the future) and the passwords are stored encrypted in SHA256.

If SIF ever has any intention of establishing a minute data backend in the future, please feel free to reach out to us even if we don't end up getting in. We would be happy to collaborate and would hopefully give you guys a starting point instead of having to start from scratch. The email for Stocket is stocketapi@gmail.com and my personal email is bhoulton@terpmail.umd.edu.

Thank you all for your time, and I look forward to seeing where the project goes in the future.
