import json
import os
from pyecharts import options as opts
from pyecharts.charts import Page, Tree
from sql import *
class graph():
    def tree_base(self,data) -> Tree:
        c = (
            Tree()
            .add("", data,orient="TB",symbol_size=15)
            .set_global_opts(title_opts=opts.TitleOpts(title="拓扑图"))
            .set_series_opts(linestyle_opts=opts.LineStyleOpts(width=5))
        )
        c.render('./map1.html')
        return c
    def createTreeData(self,id='None'):
        Mysql = sql()
        result = Mysql.sqlread()
        results=json.loads(json.dumps(result))
        # print(results)
        sz = []
        for obj in results:
            if obj['father'] == id:
                sz.append({"name": obj["name"]+":"+obj["length"], "children": self.createTreeData(obj["ID"])})
        # print(sz)
        return sz


if __name__=="__main__":
    gra=graph()
    data1=gra.createTreeData()
    gra.tree_base(data1)
