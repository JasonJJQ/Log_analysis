import pandas as pd
import re

# 读取日志文件
with open("35kg_log.txt", "r", encoding="utf-8") as f:
    logs = f.readlines()

# 提取时间、操作类型、详细信息
data = []
for log in logs:
    time = re.search(r"\d{4}/\d{2}/\d{2} \d{2}:\d{2}:\d{2}\.\d{3}", log).group()
    event = log.split(">>")[-1].strip()
    data.append({"Time": pd.to_datetime(time), "Event": event})

df = pd.DataFrame(data)

# 标记关键操作类型
df["Operation"] = df["Event"].apply(lambda x: 
    "连接成功" if "Successful" in x else
    "连接失败" if "Unsuccessful" in x else
    "拍照请求" if "Car2_Request=1" in x else
    "触发拍照" if "相机触发拍照完成" in x else
    "点云存储" if "点云初始数据存储完成" in x else
    "后端计算" if "后端计算正常" in x else
    "坐标发送" if "坐标发送完成" in x else
    "错误" if "断电" in x or "触发失败" in x else "其他"
)

# 输出预处理后的数据
print(df.head())