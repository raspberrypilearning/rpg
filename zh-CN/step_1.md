## 介绍： 

你将在本项目中设计你自己的 RPG 迷宫游戏并编写相关代码。游戏的目标在于收集物体并逃离房子，同时确保避开所有的怪物！

<div class="trinket">
  <iframe src="https://trinket.io/embed/python/d06adeb527?outputOnly=true&start=result" width="600" height="500" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen>
  </iframe>
  <img src="images/rpg-finished.png">
</div>

### 更多俱乐部领导参考信息

如果你需要打印本项目，请使用 [适合打印机的版本](https://projects.raspberrypi.org/en/projects/rpg/print)。


--- collapse ---
---
title: 俱乐部领导备注
---


## 介绍：
本项目通过开发一款 RPG 迷宫游戏来教授游戏设计。在游戏中，玩家必须捡起一栋房子内的物体并到达特定房间，期间要躲避潜伏在一些房间内的怪物。此游戏通过操纵字典和列表来完成。

## 在线资源

__本项目使用 Python 3。__我们推荐使用 [trinket]（https://trinket.io/）在线编写 Python。本项目包含以下 Trinket：

+ [“RPG”起点 -- jumpto.cc/rpg-go](http://jumpto.cc/rpg-go)

还有一个 trinket 包含完整项目：

+ [“RPG”已完成 -- trinket.io/python/d06adeb527](https://trinket.io/python/d06adeb527)

## 离线资源
如果希望的话，本项目可[离线完成](https://www.codeclubprojects.org/en-GB/resources/python-working-offline/)。你可以通过单击此项目的“项目材料”链接来访问项目资源。此链接包含一个“项目资源”部分，其中包括孩子们离线完成本项目时所需的资源。确保每个孩子都能访问这些资源的副本。本节包括以下文件：

+ rpg/rpg.py

你还可以在“志愿者资源”部分中找到完整项目，其中包含：

+ rpg-finished/rpg.py

（以上所有的资源也可以作为项目和志愿者 `.zip` 文件下载。）

## 学习目标
+ 游戏设计；
+ 编辑：
	+ 列表；
	+ 字典。
+ 布尔表达式。

本项目包括 [Raspberry Pi 数字制作课程](http://rpf.io/curriculum) 以下几个部分的元素：

+ [结合编程结构解决问题。](https://www.raspberrypi.org/curriculum/programming/builder)

## 挑战
+ 添加新房间；
+ 添加需要收集的物品；
+ 添加需要躲避的敌人；
+ 开发你自己的游戏。

## 常见问题
+ 可能需要提醒孩子们字典／列表中的元素以逗号隔开。例如，向“房间”字典添加一个新房间时，需要在被添加的新房间和现有房间之间增加一个逗号。
+ 添加新房间时，孩子们可能会忘记向新创建的房间添加指向现有房间的链接。这就意味着孩子们能离开房间，但不能进入房间！
+ 检查玩家胜利或失败的代码需要进行缩进，以确保此次检查在进入每个新房间之后执行。如果未缩进该代码，那么代码会处于游戏主循环外部而永远无法运行。



--- /collapse ---


--- collapse ---
---
title: 项目材料
---
## 项目资源
* [包含所有项目资源的 .zip 文件](resources/rpg-project-resources.zip)
* [包含所有“RPG”项目资源的在线 Trinket](http://jumpto.cc/rpg-go)
* [rpg/rpg.py](resources/rpg-rpg.py)

## 俱乐部领导资源
* [包含所有已完成项目资源的 .zip 文件](resources/rpg-volunteer-resources.zip)
* [在线已完成 Trinket 项目](https://trinket.io/python/d06adeb527)
* [rpg-finished/rpg.py](resources/rpg-finished-rpg.py)

--- /collapse ---
