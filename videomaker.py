
#!/usr/bin/python3
import os
import json
import numpy as np
import pandas as pd
import wget

#Loading data
with open('dataVideo.json','r') as f:
    videos_dict = json.load(f)

#Manipulate data
df = pd.DataFrame.from_dict(videos_dict)
#df_shorter = df.drop(columns=['url','timeCreated','videoUsed','videoUsedDate'])
#columns_name = ['id','commentCount','likeCount','playCount','shareCount']
#df_shorter = df_shorter.head()
#df_shorter = df_shorter.reindex(columns=columns_name)

#dataNorm=((df_shorter-df_shorter.min())/(df_shorter.max()-df_shorter.min()))*1
#dataNorm["id"]=df_shorter["id"]
#print(dataNorm)
#TODO: calculate a score for all videos in order to select the x best videos

#Download videos localy
path = os.getcwd()
urls = df['url'].head()
#vid_dl = []
#for u in urls:
#    vid_dl.append(wget.download(u))
vid = wget.download(urls[0],path)
print(vid)
#print(vid_dl)
