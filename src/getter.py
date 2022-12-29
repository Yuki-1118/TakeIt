# Youtubeからサムネイルを取得する

import requests
import os


_base_url = 'https://img.youtube.com/vi/{0}/maxresdefault.jpg'                                                             #サムネイルを取得するためのURLのテンプレート
_save_folder_path =os.path.join(os.path.join(os.path.join(os.environ['USERPROFILE']), 'Pictures'),'Youtube_Thumbnail')   #取得したサムネイルを保存するためのディレクトリのパス
_overwriteing_thumbnail = True                                                                                             #同じ名前のファイルが存在したときに上書きを行うかどうか

# サムネイルを保存したい動画の動画IDを受け取る
def DownloadSave(movieId):
    
    if not _isSaveFolder():
        _creat_save_folder()
    
    data = _download_thumbnail(movieId)
    _save_file(thumbnailDatas=data,movieId=movieId)
    pass

def _save_file(*,thumbnailDatas,movieId):
    filepath = _generate_save_path(movieId)

    
    if (_exist_file(filepath) and _overwriteing_thumbnail == False):
        return
    

    with open(filepath,'wb') as f:
        f.write(thumbnailDatas)
        print('ID:{0}を[{1}]に保存'.format(movieId,filepath))
    pass


def _download_thumbnail(movieId):
    request_url = _generate_url(movieId)
    try:
        respons = requests.get(request_url)
    except:
        return
    Thumbnail_data = respons.content
    return Thumbnail_data

# 動画IDをもとにサムネイルを取得するためのURLを生成
def _generate_url(movieID):
    url = _base_url.format(movieID)
    return url

def _generate_save_path(filename):
    path = _save_folder_path + '\\{0}.jpg'.format(filename) 
    return path

def _isSaveFolder():
    return os.path.exists(_save_folder_path)

def _creat_save_folder():
    os.mkdir(_save_folder_path)
    pass

def _exist_file(filepath):
    return os.path.exists(filepath)