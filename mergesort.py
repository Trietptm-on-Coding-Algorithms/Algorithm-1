#!/usr/bin/python
#-*- coding:utf-8 -*-
#�鲢����
#�ݹ�ֳ����룬lft��rgt���lft��rgt���ȴ���1���򻹿��Է֣�ֱ�����ݹ��յ㣬lft��rgtֻ��һ����
#�Ƚ�lft��rgt��С����������Ȼ������õ��б��ϴ�����һ����lft����rgt����һ���ٴαȽ�lft��rgt
#���бȽ�����Ȼ���ϴ����������ϴ���ֱ���ص����
#�����ص��ǽ���������õ������б�ϲ������Դ������б���������������߿�ʼ�Ƚϣ��ϴ��������res
#ֱ��һ���б�Ϊ�գ�˵����Ϊ�յ���һ���б��res���������С�����غϲ��б�(lft or rgt) + res


def mergesort(seq):
    mid=len(seq)/2
    lft,rgt=seq[:mid],seq[mid:]
    if len(lft)>1:lft=mergesort(lft)
    if len(rgt)>1:rgt=mergesort(rgt)
    res=[]
    while  lft and rgt:
        if lft[-1]>=rgt[-1]:
            res.append(lft.pop())
        else:
            res.append(rgt.pop())
    res.reverse()
    return (lft or rgt) + res
