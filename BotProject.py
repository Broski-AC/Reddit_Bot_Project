from os.path import isfile
import praw
import pdb
import re
import os


reddit = praw.Reddit('bot1')

#print(reddit.user.me())

#Checks to see if a file exists within the operating system, else if it doesn't, we create a list known as replied posts.
if not os.path.isfile("replied_comments.txt"):
    replied_comments = []
else:
    #Define the open textfile as f in this context
    with open("replied_comments.txt","r") as f:
        #Explicitly defines the variable replied_posts as a way to read the file
        #Retrieves a specific string
        replied_comments = f.read()
        #Redefines the variable as a list created from the string which was split at newline characters
        replied_comments = replied_comments.split("\n")
        #Filters out empty values, and returns the result as a list because reasons
        replied_comments = list(filter(None, replied_comments))


subreddit = reddit.subreddit("UrodeleTestReddit")

#Prints to the terminal information from the subreddit listed above
for submission in subreddit.hot(limit=5):
    print("Title: ", submission.title)
    print("User: ", submission.author)
    
        #Want to search through comments and find book titles in quotation marks
        #"." will match any character except a newline character
        #\s matches whitespace characters
        #+matches one or more times
        #for comment in subreddit.comments():
            #if re.search("X", comment.body, re.IGNORECASE):


    #Searches through expressions for a specific keyword in the body of the comment ignoring case
    comments = submission.comments
    for comment in comments:
        if comment.id not in replied_comments:
            if re.search("testing", comment.body, re.IGNORECASE):
                    #Responds to prompt if we detect the keyword
                    comment.reply("Test Successful!")
                    #Lets us know on the terminal this worked correcly
                    print("Bot replied to: ", comment)
                    #Adds id to the list
                    replied_comments.append(comment.id)


#Writing all lists values into the text file. This is likely because the list will be cleared each time we run the code, so therefore we need a more permanent place to store the ids we replied to
with open("replied_comments.txt", "w") as f:
    for post_id in replied_comments:
        f.write(post_id + "\n")
