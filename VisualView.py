#coding=utf-8

from pyecharts import Bar

bar = Bar("第一个图标")
bar.add("服装", ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"],
        [5, 20, 30, 35, 38,40])
bar.show_config()
bar.render()

