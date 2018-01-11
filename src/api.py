from pprint import pprint
from pocket import Pocket, PocketException

p = Pocket(
    consumer_key='73969-97b3dedc26da58ec74e67608',
    access_token='facbe785-b308-4f4b-fbd5-fdf1b3'
)

def archived(tag):
    last = p.retrieve(state="archive", tag=tag, count=1000, offset=0)
    if last['list']:
        return [value['resolved_url'] for value in last['list'].values()]
    else:
        return []



# # Fetch a list of articles
# try:
#     print(p.retrieve(offset=0, count=10))
# except PocketException as e:
#     print(e.message)

# Add an article
# p.add('https://pymotw.com/3/asyncio/')
