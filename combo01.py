# モジュールのインポート
import tkinter as tk
import tkinter.ttk as ttk
import mysql.connector

# --------------------------------
# データベースの接続
conn = mysql.connector.connect(
	host = '176.34.20.157',
	port = 3306,
	user = 'mqj',
	password = 'habitation',
	database = 'metatrader5',
)
cur = conn.cursor()

strSql = "SELECT distinct `ea_deal`.`name`"
strSql = strSql + " FROM `metatrader5`.`ea_deal`"
strSql = strSql + " Where name like 'AI %'"
cur.execute(strSql)

# -------------------------------
# GUI部分の作成
root = tk.Tk()
combo = ttk.Combobox(root, state='readonly')

for row in cur.fetchall():
	combo["values"] = (row[0])

combo.current(0)
combo.pack()

# コールバック関数にgetitemcodeを定義
button = tk.Button(text="表示",command=lambda:getitemcode(combo.get()))
button.pack()

root.mainloop()
cur.close
conn.close


