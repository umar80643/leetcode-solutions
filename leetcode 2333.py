import heapq

nums1 = [1,2,3,4]
nums2 = [2,10,20,19]
k1 = 0
k2 = 0

diff =[abs(a-b) for a,b in zip(nums1,nums2)]
k=k1+k2
if sum(diff) <=k:
    print(0)

heap =[-x for x in diff]
heapq.heapify(heap)

while k>0:
    largest = -heapq.heappop(heap)
    largest -= 1
    heapq.heappush(heap,largest)
    k -= 1


print( sum(x * x for x in diff) if False else sum((-x) ** 2 for x in diff))
