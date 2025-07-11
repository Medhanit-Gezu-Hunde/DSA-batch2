n = int(input())
arr = list(map(int, input().split()))

unique_arr = list(set(arr))
unique_arr.sort(reverse=True)

runner_up = unique_arr[1]
print(runner_up)
