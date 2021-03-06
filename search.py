import pandas as pd
import eel
import os
import sys

### デスクトップアプリ作成課題
def kimetsu_search(word, filename):
    # 検索対象取得
    #pyinstallerの実行場所が/users/userだったため、実行ファイル下の場所を取得
    current_dir = os.path.dirname(sys.argv[0])
    #実行環境で変更
    if current_dir == "":
        csvfile_path = "./" + filename
    else:
        csvfile_path = current_dir + "/" +filename

    if os.path.exists(filename) == True:
        pass
    else:
        back = "File:『{}』が存在しません".format(csvfile_path)
        return back

    df=pd.read_csv(csvfile_path)
    source=list(df["name"])

    # 検索
    if word in source:
        print("『{}』はあります".format(word))
        back = "『{}』はあります".format(word)
    else:
        print("『{}』はありません".format(word))
        back = "『{}』はありません".format(word)
        # 追加
        #add_flg=input("追加登録しますか？(0:しない 1:する)　＞＞　")
        #if add_flg=="1":
            #source.append(word)
    
    # CSV書き込み
    df=pd.DataFrame(source,columns=["name"])
    df.to_csv("./source.csv",encoding="utf_8-sig")
    print(source)

    return back
