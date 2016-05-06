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

#迭代版算法
def lcs(a,b):
    n,m=len(a),len(b)
    pre,cur=[0]*(n+1),[0]*(n+1)
    for j in range(1,m+1):
        #第一层循环，序列a的每个元素
        pre,cur=cur,pre
        #互换上次循环操作的cur
        for i in range(1,n+1):
            #迭代序列b中每个元素，与a中一个元素比较
            if a[i-1] == b[j-1]:
                cur[i] = pre[i-1]
                #找到相同元素，则操作的cur[i]+1
            else:
                cur[i] = max(pre[i],cur[i-1])
                #没找到之前，会将cur的元素同化成pre，因为此时pre更大
                #找到后会同化成cur，因为此时cur已经加1
    return cur[n]
