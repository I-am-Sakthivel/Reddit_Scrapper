
import praw
from dotenv import load_dotenv
import os
import csv
load_dotenv()
def best_comment(comf):
    max_up=0
    max_com=None
    for com in comf:
        if str(type(com))!="<class 'praw.models.reddit.comment.Comment'>":
            continue
        if com.score>=max_up:
            max_up=com.score
            max_com=com
    if max_com:
        return max_com.body
    return "[ERROR]"
def scrape(subname):
    reddit=praw.Reddit(client_id=os.getenv('client_id'),client_secret=os.getenv('client_secret'),user_agent=os.getenv('user_agent'),username=os.getenv('username'),password=os.getenv('password'))
    sub=reddit.subreddit(subname)
    d={}
    posts=[]
    #title + query + answer
    try:
        coll=sub.hot(limit=100)
    except:
        return "Sub Does not exist"
    try:
        for subs in coll:
            d={}
            if sub.title and subs.selftext and subs.num_comments > 0:
                d['title']=subs.title
                d['query']=subs.selftext
                d['answer']=best_comment(subs.comments)
                posts.append(d)
    except:
        return "Sub Does not exist"
    os.makedirs('/tmp',exist_ok=True)
    f=open('/tmp/'+sub.display_name+".csv",'w')
    if len(posts)>0:
        keys=posts[0].keys()
        cw=csv.DictWriter(f,keys)
        cw.writeheader()
        cw.writerows(posts)
        return str(os.path.abspath('tmp/'+sub.display_name+".csv"))
    return "Sub Does not exist"
