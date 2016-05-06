#!/usr/bin/python
#-*- coding:utf-8 -*-

#递归、记忆体求LCS(最长共用子序列)
#从两个序列的最右边开始比较有无相同的元素，如果有就一同去掉
#否则就交叉比较，即一个序列的最右边和另一个的倒数第二个，这样交错递归，避免遗漏
#保证每个递归都返回最大共用子序列
def rec_lcs(a,b):
    @memo
    def L(i,j):
        if min(i,j)<0:return 0
        if a[i]==b[j]:return 1+L(i-1,j-1)
        #如果找到相同元素，则去掉两个元素
        return max(L(i-1,j),L(i,j-1))
        #如果不相同，则开始交错递归
    return L(len(a)-1,len(b)-1)

