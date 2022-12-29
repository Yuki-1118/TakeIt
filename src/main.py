# Youtubeの動画IDを指定して起動すると指定した動画のサムネイルを取得して保存する

import getter
import sys

def main():
    args = sys.argv #コマンドライン引数を取得
    video_ids = []
# コマンドライン引数を作業用変数にコピー
    if 0 == len(args):
        video_ids.append(input())
    else :
        for tmp in args:
            video_ids.append(tmp)
    del args  #コマンドライン引数を解放

    pass

if __name__ == "main":
    main() 