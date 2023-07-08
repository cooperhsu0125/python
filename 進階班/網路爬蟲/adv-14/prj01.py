#######################匯入模組########################
from moviepy.editor import *
from mod.mod import *
import sys
import os

#######################初始化########################
os.chdir(sys.path[0])

#######################取得影片資訊########################
u = "https://www.youtube.com/watch?v=BLYo63tsSek"
title, author, length, thumbnail, res = get_video_info(u)
print(res)
#######################下載影片########################
r = input("根據上面的資訊, 請輸入要下載的影片的解析度(720p/480p/360p/240p/144p):")
if download_video(u, r):
    print('下載完成')
else:
    print('找不到該解析度的影片')
#######################切割影片########################
beg = int(input('切割開始(秒):'))
end = int(input('切割結束(秒):'))
result = '完成' if cut_video(f"{title}.mp4", beg, end) else '失敗'
