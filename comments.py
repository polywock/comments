import requests 
import json 
import argparse
from sys import argv
import key

parser = argparse.ArgumentParser(description='Get comments from a Youtube video.')
parser.add_argument('video_id', type=str, help='The youtube video ID.')
parser.add_argument('--pages', type=int, help='Every page we can get 100 comments.', default=100)

def crawl_video(video_id, max_pages):
  page_token = ""
  comments = []
  for i in range(max_pages):
    url = "https://www.googleapis.com/youtube/v3/commentThreads?key={}&textFormat=plainText&part=snippet&videoId={}&maxResults=100&pageToken={}".format(key.KEY, video_id, page_token)
    resp = requests.get(url)
    if not resp.ok:
      return print("Could not load comments.")
    data = resp.json() 
    for item in data["items"]:
      snippet = item["snippet"]["topLevelComment"]["snippet"]
      comments.append({
        "author_name": snippet["authorDisplayName"],
        "author_id": snippet["authorChannelId"]["value"],
        "author_img": snippet["authorProfileImageUrl"],
        "body": snippet["textDisplay"],
        "like_count": snippet["likeCount"],
        "published_at": snippet["publishedAt"],
        "reply_count": item["snippet"]["totalReplyCount"]
      })
    try:
      data["nextPageToken"]
    except KeyError:
      break  
    page_token = data["nextPageToken"]

  comments.sort(key=lambda v: v["like_count"], reverse=True)
  for c in comments:
    print("+{}  {} -> {}".format(c["like_count"], c["author_name"], c["author_id"]))
    print("{}".format(" ".join(c["body"].split())))
    print("-------------------------------")
    
      
def main():
  global parser 
  args = parser.parse_args()
  crawl_video(args.video_id, args.pages)
        
        
  


main() 
