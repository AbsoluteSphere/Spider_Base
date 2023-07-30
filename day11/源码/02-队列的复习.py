
from queue import Queue

q = Queue()

q.put('11111')  # 放入数据   队列是满的会进行等待    计数会加1
q.put_nowait('2222')  # 存入数据  不等待 直接插入   队列满的时候会报错
q.put_nowait('2222')  # 存入数据  不等待 直接插入   队列满的时候会报错
q.put_nowait('2222')  # 存入数据  不等待 直接插入   队列满的时候会报错
q.put_nowait('2222')  # 存入数据  不等待 直接插入   队列满的时候会报错
q.put_nowait('2222')  # 存入数据  不等待 直接插入   队列满的时候会报错
q.put_nowait('2222')  # 存入数据  不等待 直接插入   队列满的时候会报错
q.put_nowait('2222')  # 存入数据  不等待 直接插入   队列满的时候会报错

# 查看当前队列中是否有数据
print(q.qsize())

print(q.get())   #  取数据的时候  计数不会减一
# get 和 task_done 一起会把计数减一
q.task_done()
print(q.get_nowait())
q.task_done()
print(q.get_nowait())
q.task_done()
print(q.get_nowait())
q.task_done()
print(q.get_nowait())
q.task_done()
print(q.get_nowait())
q.task_done()
print(q.get_nowait())
q.task_done()
print(q.get_nowait())
q.task_done()
# 队列中有一个计数系统   计数   join 判断计数是否为0   如果不为0    就会阻塞代码
q.join()


