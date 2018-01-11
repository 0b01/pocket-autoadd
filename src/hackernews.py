import requests as r
from json import loads
from random import random
from api import p, archived
length = 10

whitelist = [
    "bitcoin",
    "crypto",
    "china",
]

blacklist = [
    "meltdown",
    "spectre",
]

def ok(title):
    '''if whitelist words in title'''
    for word in whitelist:
        if word in title.lower():
            return True
    return False

def not_ok(title):
    for word in blacklist:
        if word in title.lower():
            return True
    return False


def run_new():
    ar = archived("hn_new")
    new_url = "https://hn.algolia.com/api/v1/search_by_date?tags=story&length={}&offset=0".format(length)
    articles = loads(r.get(new_url).text)
    hits = articles['hits']

    def send(title, url):
        if url in ar:
            print("Skipped\t", title, url)
        else:
            p.bulk_add(item_id=None, url=url, tags=["autoadd", "hn_new"])

    for hit in hits:
        title = hit['title']
        url = hit['url']

        tosend = False
        if ok(title):
            tosend = True
        elif not_ok(title):
            tosend = False
            continue
        elif random() > 0.9:
            tosend = True
        
        if tosend:
            send(title, url)
    p.commit()

def run_top():
    ar = archived("hn_top")
    top_url = "https://hn.algolia.com/api/v1/search?tags=front_page&length=48&offset=0"
    articles = loads(r.get(top_url).text)
    hits = articles['hits']

    def send(title, url):
        if url in ar:
            print("Skipped\t", title, url)
        else:
            p.bulk_add(item_id=None, url=url, tags=["autoadd", "hn_top"])

    for hit in hits:
        title = hit['title']
        url = hit['url']

        tosend = False
        if ok(title):
            tosend = True
        elif not_ok(title):
            tosend = False
            continue
        elif random() > 0.8:
            tosend = True
        
        if tosend:
            send(title, url)
    p.commit()

def run():
    run_new()
    run_top()

run()