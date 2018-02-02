### 微信小游戏 大家来找茬 辅助

## 配置环境
- python 3.6
- pillow 4.3.0
- adb
- android 手机

## 使用方式
首先打开游戏界面，然后确认`adb`正常工作，使用`adb devices`可以看到手机，如图所示
![](http://oqyjccf1n.bkt.clouddn.com/20180202-172504.png)

尔后运行主程序,将会弹出包含了两幅图中不同的地方的画面
```bash
$ python3 find_diff.py
```

![](http://oqyjccf1n.bkt.clouddn.com/20180202-173120.png)







## todo

- [ ] 在图中直接圈出来有变化的地方，现在肉眼对应过去不直观





## 跋

健康游戏，合理作息。

程序未完善，有空再更。



2018年2月2日17:33:56