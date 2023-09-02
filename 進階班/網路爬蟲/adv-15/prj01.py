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
video_path = f'{title}.mp4'
if os.path.isfile(video_path):
    clip = VideoFileClip(video_path)
    print(f'影片長度:{length}秒')
    beg = int(input('切割開始(sec.)'))
    end = int(input('切割結束(sec.)'))
    clip = clip.subclip(beg, end)
    new_video_path = f'{title}{beg}~{end}.mp4'
    clip.write_videofile(new_video_path)
    print(f'儲存在{new_video_path}')
else:
    print('fail')

beg = int(input("請輸入要切割的開始時間(秒):"))
end = int(input("請輸入要切割的結束時間(秒):"))
result = "剪輯完成" if cut_video("2 綠色外星人.mp4", beg, end) else "剪輯失敗"
print(result)

#######################合併影片########################
file_name1 = "2 綠色外星人.mp4"
file_name2 = "2 綠色外星人.mp4"
file_name3 = "2 綠色外星人.mp4"
# 設定要合併的影片檔案
video1 = VideoFileClip(file_name1)
video2 = VideoFileClip(file_name2)
video3 = VideoFileClip(file_name3)
# 將影片檔案合併
final_clip = concatenate_videoclips([video1, video2,
                                     video3])  #[video1, video2, video3]list
# 儲存影片檔案
final_clip.write_videofile("合併影片.mp4")

file_name_list = ["影片1.mp4", "影片2.mp4", "影片3.mp4"]
result = "合併影片成功" if merge_video(file_name_list, "合併影片.mp4") else "合併影片失敗"
print(result)
#######################影片轉GIF########################
video_path = "2 綠色外星人.mp4"
gif_path = "2 綠色外星人.gif"
if os.path.isfile(video_path):

    clip = VideoFileClip(video_path)
    clip.write_gif(gif_path)
    print("影片轉GIF成功")

else:

    print("影片轉GIF失敗")


#######################模組化#######################
def cut_video(video_path: str, beg: int, end: int):
    if end <= beg:
        print("結束時間必須大於開始時間")
        return False
    if os.path.isfile(video_path):  # 判斷影片檔案是否存在
        clip = VideoFileClip(video_path)  # 讀取影片檔案
        length = clip.duration  # 影片長度
        print(f"影片長度:{length}秒")

        clip = clip.subclip(beg, end)  # 切割影片

        title = video_path.split(".")[0]  # 影片檔案名稱
        new_file_name = f"{title}-{beg}-{end}.mp4"
        clip.write_videofile(new_file_name)  # 儲存影片

        print(f"影片儲存於{new_file_name}")

        return True
    else:
        print("找不到影片檔案")
        return False


def merge_video(file_name_list: list, merge_file_name: str):
    for file_name in file_name_list:
        if not os.path.exists(file_name):
            print(f"錯誤: {file_name}不存在")
            return False
    video_list = []
    for file_name in file_name_list:
        video_list.append(VideoFileClip(file_name))
    final_clip = concatenate_videoclips(video_list)
    final_clip.write_videofile(merge_file_name)
    return True
