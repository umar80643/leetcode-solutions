
nums1 = [1,2,3,4]
nums2 = [2,10,20,19]
k1 = 0
k2 = 0

diff = [abs(a - b) for a, b in zip(nums1, nums2)]
k = k1 + k2

if sum(diff) <= k:
    print(0)

left, right = 0, max(diff)

# Find the smallest level we can reduce all
# differences to using at most k operations.
while left < right:
    mid = (left + right) // 2
    operations = sum(max(0, x - mid) for x in diff)

    if operations <= k:
        right = mid
    else:
        left = mid + 1

level = left
operations = sum(max(0, x - level) for x in diff)
remaining = k - operations

ans = sum(min(x, level) ** 2 for x in diff)

# Use leftover operations to reduce some level values by 1.
ans -= remaining * (2 * level - 1)

print(ans)