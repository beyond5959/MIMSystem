# -*- coding:utf-8 -*-
import os.path     
import tornado.web  
import tornado.ioloop
import MySQLdb
import datetime
from time import strptime,strftime

conn = MySQLdb.connect(host = "localhost",db = "mis",user = "root",passwd = "492228470leo",charset="utf8")

sql0="insert into history (number,name,count,time,comment) values (%s,%s,%s,%s,%s)"
class MainHandler(tornado.web.RequestHandler):
	def get(self):
		self.set_header("Content-Type", "text/html; charset=UTF-8")
		self.render("index.html")
class ComePageHandler(tornado.web.RequestHandler):
	def get(self):
		self.set_header("Content-Type", "text/html; charset=UTF-8")
		self.render("come_into.html")
	def post(self):
		jintian=datetime.date.today()
		name=self.get_argument("name")
		number=self.get_argument('num')
		count=int(self.get_argument("quantity"))
		inputtime=self.get_argument('time')
		cursor=conn.cursor()
		today_sql1="insert into today (number,name,time,in_count) values (%s,%s,%s,%s)"
		today_sql2="update today set in_count=%s where name=%s and time=%s"
		today_sql3="select in_count from today where name=%s and time=%s"
		sql1="insert into now (number,name,count,time) values (%s,%s,%s,%s)"
		sql3="update now set count=%s,time=%s where name=%s"
		try:
			sql4="select count from now where name=%s"
			cursor.execute(sql4,(name))
			counts=cursor.fetchone()
			cursor.execute(sql3,((int(counts[0])+count),inputtime,name))
		except:
			cursor.execute(sql1,(number,name,count,inputtime))
		cursor.execute(sql0,(number,name,count,inputtime,"入库"))
		ttime=strptime(inputtime,'%Y-%m-%d')
		try:
			if ttime.tm_year==jintian.year and ttime.tm_mon==jintian.month and ttime.tm_mday==jintian.day:
				cursor.execute(today_sql3,(name,jintian))
				shuliang=cursor.fetchone()
				if int(shuliang[0])==0:
					cursor.execute(today_sql2,(count,name,jintian))
				else:
					cursor.execute(today_sql2,((int(shuliang[0])+count),name,jintian))
			else:
				pass
		except:
			cursor.execute(today_sql1,(number,name,jintian,count))
		self.write("<span></span>")
		conn.commit()
		self.render("come_into.html")
class GoPageHandler(tornado.web.RequestHandler):
	def get(self):
		self.set_header("Content-Type", "text/html; charset=UTF-8")
		self.render("go_out.html")
	def post(self):
		name=self.get_argument("name")
		number=self.get_argument('num')
		count=int(self.get_argument("quantity"))
		inputtime=self.get_argument('time')
		jintian=datetime.date.today()
		cursor=conn.cursor()
		today_sql1="insert into today (number,name,time,out_count) values (%s,%s,%s,%s)"
		today_sql2="update today set out_count=%s where name=%s and time=%s"
		today_sql3="select out_count from today where name=%s and time=%s"
		sql="update now set count=%s where name=%s"
		sql2="select count from now where name=%s"
		sql3="delete from now where number=%s"
		ttime=strptime(inputtime,'%Y-%m-%d')
		try:
			cursor.execute(sql2,(name))
			counts=cursor.fetchone()
			if (int(counts[0])-count)==0:
				cursor.execute(sql3,(number))
				cursor.execute(sql0,(number,name,count,inputtime,"出库"))
				try:
					if ttime.tm_year==jintian.year and ttime.tm_mon==jintian.month and ttime.tm_mday==jintian.day:
						cursor.execute(today_sql3,(name,jintian))
						shuliang=cursor.fetchone()
						if int(shuliang[0])==0:
							cursor.execute(today_sql2,(count,name,jintian))
						else:
							cursor.execute(today_sql2,((int(shuliang[0])+count),name,jintian))	
					else:
						pass
				except:
					cursor.execute(today_sql1,(number,name,jintian,count))
				conn.commit()
				self.write("<span></span>")
			elif (int(counts[0])-count)<0:
				self.write("<span></span><span></span>")
			else:
				cursor.execute(sql,((int(counts[0])-count),name))
				cursor.execute(sql0,(number,name,count,inputtime,"出库"))
				try:
					if ttime.tm_year==jintian.year and ttime.tm_mon==jintian.month and ttime.tm_mday==jintian.day:
						cursor.execute(today_sql3,(name,jintian))
						shuliang=cursor.fetchone()
						cursor.execute(today_sql2,((int(shuliang[0])+count),name,jintian))
					else:
						pass
				except:
					cursor.execute(today_sql1,(number,name,jintian,count))
				conn.commit()
				self.write("<span></span>")
		except:
			self.write("<span></span><span></span><span></span>")
		self.render("go_out.html")
class NowPageHandler(tornado.web.RequestHandler):
	def get(self):
		self.set_header("Content-Type", "text/html; charset=UTF-8")
		self.render("nselect.html")
	def post(self):
		conn = MySQLdb.connect(host = "localhost",db = "mis",
			user = "root",passwd = "492228470leo",charset="utf8")	
		qsql1="select number,name,count,time from now where time>=%s and time<=%s"
		qsql2="select number,name,count,time from now where number=%s and time>=%s and time<=%s and name=%s"
		qsql3="select number,name,count,time from now where time>=%s and time<=%s and name=%s"
		qsql4="select number,name,count,time from now where time>=%s and time<=%s and number=%s"
		cursor=conn.cursor()
		try:
			bianma=self.get_argument("bianma")
			name=self.get_argument("name")
			time1=self.get_argument("time1")
			time2=self.get_argument("time2")
			if bianma!="" and name!='' and time1!='' and time2!='':
				cursor.execute(qsql2,(bianma,time1,time2,name))
			elif time1!='' and time2!='' and bianma!='' and name=='':
				cursor.execute(qsql4,(time1,time2,bianma))
			elif time1!='' and time2!='' and name!='' and bianma=='':
				cursor.execute(qsql3,(time1,time2,name))
			else:
				cursor.execute(qsql1,(time1,time2)) 				
		except:
			self.write("<center>系统有错！！</center>")
		records=cursor.fetchall()
		self.set_header("Content-Type", "text/html; charset=UTF-8")
		self.render("result1.html",title="当前库存查询结果",records=records)
class HistoryPageHandler(tornado.web.RequestHandler):
	def get(self):
		self.set_header("Content-Type", "text/html; charset=UTF-8")
		self.render("hselect.html")
	def post(self):
		conn = MySQLdb.connect(host = "localhost",db = "mis",
			user = "root",passwd = "492228470leo",charset="utf8")
		qsql1="select number,name,count,time,comment from history where time>=%s and time<=%s"
		qsql2="select number,name,count,time,comment from history where time>=%s and time<=%s and name=%s and number=%s"
		qsql3="select number,name,count,time,comment from history where time>=%s and time<=%s and name=%s"
		qsql4="select number,name,count,time,comment from history where time>=%s and time<=%s and number=%s"
		cursor=conn.cursor()
		try:
			bianma=self.get_argument("bianma")
			name=self.get_argument("name")
			time1=self.get_argument("time1")
			time2=self.get_argument("time2")
			if bianma!='' and name!='' and time1!=''and time2!='':
				cursor.execute(qsql2,(time1,time2,name,bianma))
			elif bianma!='' and time1!='' and time2!='' and name=='':
				cursor.execute(qsql4,(time1,time2,bianma))
			elif bianma=='' and time1!='' and time2!='' and name!='':
				cursor.execute(qsql3,(time1,time2,name))
			else:
				cursor.execute(qsql1,(time1,time2))
		except:
			self.write("<center>系统有错！！</center>")
		records=cursor.fetchall()
		self.set_header("Content-Type", "text/html; charset=UTF-8")
		self.render("result2.html",title="历史库存查询结果",records=records)
class TodayPageHandler(tornado.web.RequestHandler):
	def get(self):
		self.set_header("Content-Type", "text/html; charset=UTF-8")
		self.render("today.html")
	def post(self):
		conn = MySQLdb.connect(host = "localhost",db = "mis",
			user = "root",passwd = "492228470leo",charset="utf8")
		qqq="select number,name,time,in_count,out_count from today where time=%s"
		inputtime=self.get_argument('time')
		cursor=conn.cursor()
		cursor.execute(qqq,(inputtime))
		records=cursor.fetchall()
		self.set_header("Content-Type", "text/html; charset=UTF-8")
		self.render("result3.html",title="该日进出库情况",records=records)

	
settings = { 
    "template_path":os.path.join(os.path.dirname(__file__), "templates"),
    "static_path": os.path.join(os.path.dirname(__file__).decode('gbk'), "static"), 
    "debug": "true" 
}
application = tornado.web.Application( [(r"/",MainHandler),
	               						(r"/index",MainHandler),
	                					(r"/come", ComePageHandler),
	                					(r"/go",GoPageHandler),
	                					(r"/today",TodayPageHandler),
	                					(r"/nselect",NowPageHandler),
	                					(r"/hselect",HistoryPageHandler),], **settings)
if __name__ == "__main__": 
    application.listen(8888) 
    server = tornado.ioloop.IOLoop.instance() 
    tornado.ioloop.PeriodicCallback(lambda: None, 500, server).start() 
    server.start()