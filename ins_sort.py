#!/usr/bin/python
#-*- coding:utf-8 -*-
#插入排序递归版
#算法实现过程与侏儒算法类似，也是发现前一个大于后一个，则将后者调正到前面合适位置
#后退式递归调用，每次只关注前i个数字，当达到终点也就是i=1时，开始往上级传递，针对该层关注的前i个数排序
#当然上层排序时，下层已经将前i-1个数字排好序，所以只需比较i-1与i
#回到最顶层时，所有的数字均排好顺序



def ins_sort_rec(seq,i):
    if i==0:return
    ins_sort_rec(seq,i-1)
    j=i
    while j>0 and seq[j-1]>seq[j]:
        seq[j-1],seq[j]=seq[j],seq[j-1]
        j-=1

ins_sort_rec([123,546,7,897,834,54,5,6,82],8)
