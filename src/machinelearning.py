### imports reddit r/machinelearning into pocket

import praw
from api import p, archived

reddit = praw.Reddit(
    client_id='xh2pqR0uu5pO6w',
    client_secret='lGodWdutxNBwCckchynSwjosjmQ',
    user_agent='my user agent'
)

def run():
    ar = archived("machinelearning")

    for submission in reddit.subreddit('machinelearning').new(limit=10):
        url = submission.url
        if url in ar:
            print("Skipped\t", submission.title, submission.url)
        else:
            p.bulk_add(item_id=None, url=submission.url, tags=["autoadd", "machinelearning"])

    p.commit()

if __name__ == "__main__":
    run()