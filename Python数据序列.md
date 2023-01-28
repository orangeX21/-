<center>脚本告白</center>

**你不想发,我不想发,用服务器发**
利用==脚本自动化==方式，模拟手动触发,解决你我难题
软件:`TIM`
服务器:阿里云
语言:`python`
触发条件:

 - [x] 时间判断

操作内容：

 - [x] 转发指定内容，
 - [x] 识别回应信息，
 - [x] 反馈相应指令，
 - [x] 删除原代码，
 - [x] 重启云服务器，
 - [x] 待令 

最好后果：成功，有女朋友 :happy:💖

最差后果：失败，下一个更好🥳🥳🥳

## 方案:

触发条件:

```python
import random 
import datetime
result_1 = list(range(0,24))
result_2 = list(range(0,24))
result_shi = random.choice(result_1)
result_fen = random.choice(result_2)
now = datetime.datetime.now()
#"当前系统日期和时间是: 
result = now.strftime("%H:%M")
result_last = result_shi + ":" +result_fen
print (now.strftime("%H:%M"))
while result == result:
    #触发
```



1.消息操作 -准确定位TIM窗口
定位消息窗口，导入指针模块,定位坐标,引入剪切板，发消息(回车，简称`return`)， `API` 识别文字，利用逐字法，匹配白名单字符，反馈匹配字符 转3

![image-20220913203246521](C:\Users\29248\AppData\Roaming\Typora\typora-user-images\image-20220913203246521.png)

2.删除操作

触发：==祝福语：对不起，是我的问题，抱歉，祝你幸福！==

定位总窗口，导入指针模块,定位坐标，点击指令，二次循环，转3 

祝福语：对不起，是我的问题，抱歉，祝你幸福！



![image-20220913203654595](C:\Users\29248\AppData\Roaming\Typora\typora-user-images\image-20220913203654595.png)



3.删除代码，重启云服务器，待令

删除代码:

定位聊天文件夹，命令式删除

`d:\Administrator\Documents\Tencent Files\2924846542`

```python
import os
import shutil
from pathlib import path
if os.path.exist("d:\Administrator\Documents\Tencent Files\2924846542"):
    gef del_files0("d:\Administrator\Documents\Tencent Files\2924846542"):
        shutil.rmtree("d:\Administrator\Documents\Tencent Files\2924846542")
```

定位源码文件夹，命令式删除

`d:\Administrator\Desktop\10.1`

```python
import os
import shutil
from pathlib import path
if os.path.exist("d:\Administrator\Desktop\10.1"):
    gef del_files0("d:\Administrator\Desktop\10.1"):
        shutil.rmtree("d:\Administrator\Desktop\10.1")
```

重启云服务器

```python
import os
from os import system
#重启云服务器
os.system("shutdown -r -f -t 30 ")
```

待令

网易云还是网抑云

```python
import sys
import webbrowser
sys.path.append("libs")
url易 = "https://music.163.com/playlist?id=2765820785"
url抑 = "https://music.163.com/song?id=1977231916"
if ture:
    webbrowser.open(url)
    print(webbrowser.get())
else:
    webbrowser.open(url)
    print(webbrowser.get())
    

```

