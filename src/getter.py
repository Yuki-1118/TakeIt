# Youtubeからサムネイルを取得する

import requests
import os

_base_url = 'https://img.youtube.com/vi/{0}/maxresdefault.jpg'
_save_folder_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Pictures') + '\\Youtube_Thumbnail'

# 動画IDを受け取りYoutubeからサムネイルを取得する
def get(movieId):
    # サムネイルを取得
    try :
        res = requests.get(_base_url.format(movieId))
    except requests.exceptions.RequestException :
        return -1
    except Exception:
        return -2
    
    #ステータスコードが200番台ではなかった場合　処理をスキップ
    if res.status_code == 200:
        r = _save(filename=movieId+'.png',data=res.content)
    else :
        return -3
    # 処理に成功し正常に保存できた場合0を返す
    return 0

#取得したサムネイルを保存 filename = 保存するファイル名 data = サムネイル画像のデータ本体
def _save(*,filename,data):

    if not os.path.exists(_save_folder_path):
        os.mkdir(_save_folder_path)
    
    if os.path.exists(_save_folder_path + '\\'+filename):
        print('すでに同じ名前のファイルが存在します\n上書きしますか?(y/n)')
        i = input()
        if i == 'n':
            return 0
        elif not i =='y':
            print('Plese input y or n')
            return 1
        
    # ファイルを保存
    with open(_save_folder_path +'\\' + filename,'wb') as f:
        f.write(data)

    return 0