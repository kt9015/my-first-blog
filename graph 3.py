import numpy as np
import matplotlib.pyplot as plt
 
#一旦ここでグラフを描画。
step = np.random.choice([-1,1],500)
arr = np.cumsum(step)
x = np.arange(0, 500, 1)
plt.figure(figsize=(10,6))
lines, = plt.plot(x, arr) #グラフオブジェクトを受け取る
 
#1秒ごとに再描画
#set_dataメソッドで描画データを更新する
while True:
    step = np.random.choice([-1,1],500)
    arr = np.cumsum(step)
    lines.set_data(x, arr) #データ更新
    plt.ylim([arr.min()-1,arr.max()+1])
    plt.pause(1)