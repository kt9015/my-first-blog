# モジュールのインポート
import tkinter as tk
import tkinter.ttk as ttk
import sqlite3
# --------------------------------
# ボタンが押下されたときのコールバック関数
def getitemcode(item_name):
	# データベースの接続
		conn = mysql.connector.connect(
		host = '176.34.20.157',
		port = 3306,
		user = 'mqj',
		password = 'habitation',
		database = 'metatrader5',
	)
	cur = conn.cursor()
    # SELECT文の発行 WHERE句には、変数item_nameをformat関数で代入する
	strSql = "SELECT distinct `ea_deal`.`Order`"
	strSql = strSql + " FROM `metatrader5`.`ea_deal`"
	strSql = strSql + " Where name ="+.format(item_name)+"'"
	item_code = cur.execute(strSql)
	
    # SELECT文の結果をfetchoneメソッドで1つ表示する。
    # fethoneメソッドはタプルで返ってくるので、index0を取得し出力する。
	for row in cur.fetchall():
		print(row[0])
	
	cur.close
	conn.close
# -------------------------------
# GUI部分の作成
root = tk.Tk()

combo = ttk.Combobox(root, state='readonly')
combo["values"] = ("Dummy 02","Dummy 03","Dummy 04")
combo.current(0)
combo.pack()

# コールバック関数にgetitemcodeを定義
button = tk.Button(text="表示",command=lambda:getitemcode(combo.get()))
button.pack()

root.mainloop()