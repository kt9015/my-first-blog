# -*- coding: utf-8 -*-

import mysql.connector

conn = mysql.connector.connect(
    host = '176.34.20.157',
    port = 3306,
    user = 'mqj',
    password = 'habitation',
    database = 'metatrader5',
)

connected = conn.is_connected()
print(connected)
if (not connected):
    conn.ping(True)
	
cur = conn.cursor()

strSql = "SELECT `ea_deal`.`login`,`ea_deal`.`Order`,`ea_deal`.`Profit`+ `ea_deal`.`Swap` as 'ProfitTotal'"
strSql = strSql + "FROM `metatrader5`.`ea_deal`"
strSql = strSql + "Where name like" + "'AI Dummy 1'" +";"
cur.execute(strSql)

for row in cur.fetchall():
    print(row[0],row[1],row[2])

cur.close
conn.close

