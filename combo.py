# モジュールのインポート
import tkinter as tk
import tkinter.ttk as ttk
import sqlite3
# --------------------------------
# ボタンが押下されたときのコールバック関数
def getitemcode(item_name):
    # データベースの接続
    c = sqlite3.connect("database.db")
    # SELECT文の発行 WHERE句には、変数item_nameをformat関数で代入する
    item_code = cur.execute("""
        SELECT item_code FROM item
        WHERE item_name = '{}'
        """.format(item_name))
    # SELECT文の結果をfetchoneメソッドで1つ表示する。
    # fethoneメソッドはタプルで返ってくるので、index0を取得し出力する。
    print(row[0])

	cur.close
	conn.close
# -------------------------------
# GUI部分の作成
root = tk.Tk()

combo = ttk.Combobox(root, state='readonly')
combo["values"] = ("食費","住宅費","光熱費")
combo.current(0)
combo.pack()

# コールバック関数にgetitemcodeを定義
button = tk.Button(text="表示",command=lambda:getitemcode(combo.get()))
button.pack()

root.mainloop()