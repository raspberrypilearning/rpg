## 介绍：

在本项目中，你将设计并编写你自己的RPG（角色扮演游戏）迷宫游戏。 这个游戏的目标是收集物品并逃离房子，同时还要确保避开所有的怪物。

<div class="trinket">
  <iframe src="https://trinket.io/embed/python/d06adeb527?outputOnly=true&start=result" width="600" height="500" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen>
  </iframe>
  <img src="images/rpg-finished.png">
</div>

### 俱乐部导师的附加信息

如果您需要打印此项目，请使用[适合打印版本](https://projects.raspberrypi.org/en/projects/rpg/print) 。

## \--- collapse \---

## title: 俱乐部导师说明

## 介绍：

本项目通过开发一款RPG（角色扮演游戏）迷宫游戏来教授游戏设计。 在游戏中，玩家必须在一幢房子中收集物品并达到一个特定的房间，同时还要避开潜伏在某些房间中的怪物。 本游戏通过操纵数据字典和列表来实现。

## 在线资源

**本项目使用Python 3。**我们建议使用[trinket](https://trinket.io/)在线编写Python代码。 这个项目包含如下Trinket代码:

+ [RPG起始代码 - jumpto.cc/rpg-go](http://jumpto.cc/rpg-go)

还有一个包括已完成项目的Trinket：

+ [RPG完成的代码 -- trinket.io/python/d06adeb527](https://trinket.io/python/d06adeb527)

## 离线资源

如果你愿意，本项目可以[离线完成](https://www.codeclubprojects.org/en-GB/resources/python-working-offline/)。 你可以点击本项目的“项目资料”链接访问项目资源。 这个链接包含一个 “项目资源” 部分，里面有孩子们完成该项目所需的离线资源。 请确保每个孩子都能获得这些资源。 这部分包含如下文件：

+ rpg/rpg.py

你也可以在 “志愿者资源'”部分找到该项目的完成版本，里面包含：

+ rpg-finished/rpg.py

(上述所有资源也可以以`.zip`压缩包的形式下载。)

## 学习目标

+ 游戏设计
+ 编辑： 
    + 列表；
    + 字典。
+ 布尔表达式。

本项目涵盖[树莓派数字制作课程](http://rpf.io/curriculum)如下几方面内容：

+ [综合利用编程结构解决问题。](https://www.raspberrypi.org/curriculum/programming/builder)

## 挑战

+ 添加新的房间;
+ 添加可收集的物品;
+ 添加要躲开的怪物；
+ 开发你自己的游戏。

## 常见问题

+ 可能需要提醒孩子们字典或列表中的元素之间要用逗号分开。 例如，当向“rooms”字典中添加一个新的房间，在新加的房间和之前的房间之间需要添加一个逗号。
+ 在添加新房间的时候，孩子们可能会忘记将新的房间连接到一个现有的房间。 这意味着孩子可以离开一个房间，但不能进入这个新的房间。
+ 检查玩家是否已赢得游戏的代码需要缩进，以确保在玩家每次进入一个新的房间时该代码都被执行。 如果这段代码没有缩进，那么它将在游戏主循环代码之外并不会被执行。

\--- /collapse \---

## \--- collapse \---

## title: Project materials

## Project resources

+ [.zip file containing all project resources](resources/rpg-project-resources.zip)
+ [Online Trinket containing all 'RPG' project resources](http://jumpto.cc/rpg-go)
+ [rpg/rpg.py](resources/rpg-rpg.py)

## Club leader resources

+ [.zip file containing all completed project resources](resources/rpg-volunteer-resources.zip)
+ [Online completed Trinket project](https://trinket.io/python/d06adeb527)
+ [rpg-finished/rpg.py](resources/rpg-finished-rpg.py)

\--- /collapse \---