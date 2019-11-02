#下面是一些堆的相关操作：
from heapq import nsmallest, nlargest
from heapq import *

heap = []
heappush(heap, item)#：将 item 元素加入堆。
heappop(heap)#：将堆中最小元素弹出。
heapify(heap)#：将堆属性应用到列表上。
heapreplace(heap, x)#：将堆中最小元素弹出，并将元素x 入堆。
merge(*iterables, key=None, reverse=False)#：将多个有序的堆合并成一个大的有序堆，然后再输出。
heappushpop(heap, item)#：将item 入堆，然后弹出并返回堆中最小的元素。
nlargest(n, iterable, key=None)#：返回堆中最大的 n 个元素。
nsmallest(n, iterable, key=None)#：返回堆中最小的 n 个元素。
