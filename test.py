import csv

# 你的陣列
data = [['Name', 'Age'], ['Alex', 21], ['Bob', 22], ['Clarke', 23]]

# 開啟檔案，並設定模式為 'a'，表示追加模式
with open('data.csv', 'a', newline='') as f:
    writer = csv.writer(f)
    # 寫入陣列
    writer.writerows(data)