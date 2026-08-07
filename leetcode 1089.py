arr = [1,0,2,3,0,4,5,0]
n=len(arr)
zeros = arr.count(0)

read = len(arr)-1
write = len(arr)+zeros-1

while read < write:
    if write < n:
        arr[write] = arr[read]
    if arr[read] == 0:
        write -= 1
        if write < n:
            arr[write] = 0
    read = read-1
    write = write-1
print(arr)