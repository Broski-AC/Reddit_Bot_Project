from os.path import isfile
import praw
import pdb
import re
import os


reddit = praw.Reddit('bot1')

#print(reddit.user.me())

#Checks to see if a file exists within the operating system, else if it doesn't, we create a list known as replied posts.
if not os.path.isfile("replied_posts.txt"):
    replied_posts = []
else:
    #Define the open textfile as f in this context
    with open("replied_posts.txt","r") as f:
        #Explicitly defines the variable replied_posts as a way to read the file
        #Retrieves a specific string
        replied_posts = f.read()
        #Redefines the variable as a list created from the string which was split at newline characters
        replied_posts = replied_posts.split("\n")
        #Filters out empty values, and returns the result as a list because reasons
        replied_posts = list(filter(None, replied_posts))


subreddit = reddit.subreddit("UrodeleTestReddit")

#Prints to the terminal information from the subreddit listed above
for submission in subreddit.hot(limit=5):
    print("Title: ", submission.title)
    print("User: ", submission.author)

    #Check to see if id is already in our lists
    if submission.id not in replied_posts:

        #Searches through expressions for a specific keyword in the title, ignoring case
        if re.search("test", submission.title, re.IGNORECASE):
            #Responds to prompt if we detect the keyword
            submission.reply("Test Successful!")
            #Lets us know on the terminal this worked correcly
            print("Bot replied to: ", submission.title)

            #Adds id to the list
            replied_posts.append(submission.id)

#Writing all lists values into the text file. This is likely because the list will be cleared each time we run the code, so therefore we need a more permanent place to store the ids we replied to
with open("replied_posts.txt", "w") as f:
    for post_id in replied_posts:
        f.write(post_id + "\n")
