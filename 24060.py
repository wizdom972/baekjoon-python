def merge_sort(arr, s, e):
    if (s < e):
        mid = (s + e) // 2

        merge_sort(arr, s, mid)
        merge_sort(arr, mid + 1, e)
        merge(arr, s, mid, e)

def merge(arr, s, m, e):
    global counter, result, k

    i, j, t = s, m+1, 0
    temp_arr = [0] * (e - s + 1)

    while i <= m and j <= e:
        if arr[i] <= arr[j]:
            temp_arr[t] = arr[i]
            t += 1
            i += 1
        else:
            temp_arr[t] = arr[j]
            t += 1
            j += 1

    while i <= m:
        temp_arr[t] = arr[i]
        t += 1
        i += 1

    while j <= e:
        temp_arr[t] = arr[j]
        t += 1
        j += 1

    for i in range(t):
        arr[s + i] = temp_arr[i]
        counter += 1
        
        if counter == k:
            result = arr[s + i]

n, k = map(int, input().split())
arr = list(map(int, input().split()))

result = -1
counter = 0
merge_sort(arr, 0, n-1)

print(result)