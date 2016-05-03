#!/usr/bin/python
#-*- coding:utf-8 -*-
#计数器排序算法
#利用defaultdict进行快速排序


from collections import defaultdict
def counting_sort(A,key=lambda x:x):
    B,C=[],defaultdict(list)
    #传入无序列表A，构建defaultdict(list)字典，如果传入不存在的key，则返回[]
    for x in A:
        C[key(x)].append(x)
        #将每个数加入字典，key:value均为自身的值
    for k in range(min(C),max(C)+1):
        #从最小的key开始尝试获取字典内的value，如果不存在key，返回[]
        B.extend(C[k])
        #将获得的数或者[]合并到B，这样添加的顺序是从小到大的
    return B

print counting_sort([1234,3546,657])
