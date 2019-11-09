import pymysql
import json
class sql():
    def sqlread(self): #sql读取
      data=[]
      # 连接数据库
      db = pymysql.connect("地址","用户名","密码","数据库名" )
      # 获取可执行SQL语句的光标对象
      cursor = db.cursor()
      # 定义要执行的sql语句
      sql="SELECT * FROM Node "
      try:
            cursor.execute(sql)
            results=cursor.fetchall()
            for row in results:
                result={}
                result['ID']=str(row[0])
                result['name'] = row[1]
                result['father'] = str(row[2])
                result['length'] = str(row[3])
                result['firstChild'] = str(row[4])
                result['rightBrother'] = str(row[5])
                result['isVirtual'] = str(row[6])
                data.append(result)
            return data
      except :
            print("no people")
      cursor.close()
      db.close()

if __name__ == "__main__":
    sq = sql()
    data1 = []
    data1=sq.sqlread()
    print(data1)

