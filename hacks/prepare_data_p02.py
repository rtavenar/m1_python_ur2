import json
import csv
import random
import datetime as dt

places = json.load(open("places.json", "r"))
posts = json.load(open("posts.json", "r"))
persons = list(csv.DictReader(open("../modules_fournis/suspects.csv", "r"), delimiter=";"))

twitter_posts = []
snapchat_posts = []

random.seed(0)
for p in posts:
    destination_post = random.choice(["snap", "tw"])
    p["iso_date"] = dt.datetime(2022, 10, 8,
                                hour=int(p["time"].split(":")[0]),
                                minute=int(p["time"].split(":")[1])).isoformat()
    del p["time"]
    if destination_post == "snap":
        if "place" in p.keys():
            p["loc"] = places[p["place"]]
            del p["place"]
        p["author"] = [info["IDENTIFIANT_SNAPCHAT"] for info in persons if info["ID"] == p["id"]][0]
        del p["id"]
        snapchat_posts.append(p)
    else:
        if "place" in p.keys():
            p["coordinates"] = [places[p["place"]][k] for k in ["lat", "lng"]]
            del p["place"]
        p["author"] = [info["IDENTIFIANT_TWITTER"] for info in persons if info["ID"] == p["id"]][0]
        del p["id"]
        twitter_posts.append(p)

json.dump(twitter_posts, open("twitter_posts.json", "w"), indent=2)
json.dump(snapchat_posts, open("snapchat_posts.json", "w"), indent=2)
