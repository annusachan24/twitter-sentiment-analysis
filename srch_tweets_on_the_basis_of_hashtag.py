import twitter
import json
def twitter_search(twitter_api,q,max_result=200,**kw):
    search_results = twitter_api.search.tweets(q=q, count=100,**kw)
    statuses = search_results['statuses']
    max_results= min(1000, max_result)
    for _ in range(10):
        try:
            next_results=search_results['search_metadata']['next_results']
        except KeyError , e:
            break
        kwargs = dict([ kv.split('=') for kv in next_results[1:].split("&")])
        
        search_results = twitter_api.search.tweets(**kwargs)
        statuses += search_results['statuses']
        if len(statuses) > max_results:
            break

    return statuses
