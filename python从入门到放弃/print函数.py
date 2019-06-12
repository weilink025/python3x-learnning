help(print)
"""
查看如何使用print
print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
"""
print('zhangwei','wade',sep='/',end=' ',flush=True)

"""
file:  a file-like object (stream); defaults to the current sys.stdout.     输出到什么文件
sep:   string inserted between values, default a space.   多少变量之间的间隔，默认是空格
end:   string appended after the last value, default a newline.  结束后，默认换行
flush: whether to forcibly flush the stream.       是否强制刷新，默认是False，只保存到内存
"""