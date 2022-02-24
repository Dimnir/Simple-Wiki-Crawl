# - posts gallery of 2 images on reddit with a link
#   to a discord server to specified subreddits
#
# first it deletes all previous submissions and then posts new submissions to subreddits from 'subreddits' list
#
# the code can be inserted into a while loop and executed every X hours


import praw
import time



subreddits = ['cryptomooncoins', 'cryptocurrencyico',
                'cardanonfts', 'allcryptobets', 'openseamarket', 'openseanft',
                'satoshibets', 'openseamarket', 'freenfts']

# post title
title = 'Don''t forget to whitelist your wallets!'

# mini title for discord link
mini_title = 'JOIN DISCORD NOW'

# dc link
# link = insert link here 

# IMAGES
# insert images path here
# im_path =  
# im_path2 = 

insert redditor name
# reddit_name = ''

# insert reddit app info here
reddit = praw.Reddit(client_id='',
                     client_secret='',
                     password= '',
                     user_agent= '',
                     username=reddit_name)

redditor = reddit.redditor(reddit_name)


pics = [{"image_path": im_path, "caption": mini_title, "outbound_url": link},
        {"image_path": im_path2, "caption": mini_title, "outbound_url": link}]  # list of pics in gallery


# DELETE ALL PREVIOUS SUBMISSIONS
for submission in redditor.submissions.new():
  submission.delete()
print('previous submissions deleted')


# POST SUBMISSION
post_count = 0
for subreddit in subreddits:
    post_count += 1
    try:
        # reddit.subreddit(subreddit).submit(title=title, selftext=text, send_replies=False)
        reddit.subreddit(subreddit).submit_gallery(title=title, images=pics, send_replies=False) # submission
        print("Posted to", subreddit, "posts num:", post_count, 'of', len(subreddits))  # prints info

    # dealing with ratelimit exception in case it gets limited by reddit
    except praw.exceptions.RedditAPIException as exception:

        for subexception in exception.items:
            if subexception.error_type == "RATELIMIT" or "ratelimit": # if limited by time
            #figure out how long to wait before posting again
                exception_string = str(subexception) # turn exception to string

                if 'minute' in exception_string: # in case time limit = X minutes
                    for word in exception_string:
                        if word.isdigit():  # look up digits in string
                            wait = int(word) + 1 # add another minute just in case

                else: # if wait time is in seconds, wait for a minute
                    wait = 1

        print('waiting for', wait, 'minutes')
        time.sleep(wait*60)
        # try again after sleeping
        reddit.subreddit(subreddit).submit_gallery(title=title, images=pics, send_replies=False) # submission
        # reddit.subreddit(subreddit).submit(title=title, selftext=text, send_replies=False)
        print("Posted to", subreddit, "posts num:", post_count, 'of', len(subreddits))  # prints info


print("Finished posting")
