#! python3
import praw
#import pandas as pd
import io
import os
'''
reddit = praw.Reddit(client_id='NTli6KHgZM2Tkg', \
                     client_secret='MtCNRF0pRClhMaTFx73Ax6Vm4w8', \
                     user_agent='Shower Thoughts Bot', \
                     username='nathanllee', \
                     password='Rose!234')

subreddit = reddit.subreddit('Showerthoughts')
results = 1000
top_subreddit = subreddit.top(limit=results)


#for submission in subreddit.top(limit=1):


#
#for entries in top_subreddit:
    #titles_dict.append(submission.title)
#print(entries.title, entries.id)
print (top_subreddit)

counter = 939
for entries in subreddit.top(limit=1000):
    print (entries.title)

    with open("file_" + str(counter) + ".txt", 'w', encoding='utf-8') as f:
        f.write(str(entries.title))
    print(str(counter))
    counter += 1
    f.close()
'''

path = 'C:\\Users\\Nathan Lee\\Documents\\RedditTest\\files'
wholetext = ''
for files in os.listdir(path):
    filename = str(path + '\\' + files)
    text = open(filename, 'r')
    print(text.read())
    wholetext = text + wholetext + '/n'
    files.close(path)

textfile = open('wholetext.txt', 'w+')
textfile.write(wholetext)
#file = open("alldata.txt", 'w', encoding='uft-8')
#file.write()



#print (titles_dict)
