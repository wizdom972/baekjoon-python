def get_nums(lst, n):
    result = []

    for i in range(0, len(lst), n):
        num = "".join(lst[i : i + n])
        result.append(num)

    return result


T = int(input())
for test_case in range(1, T + 1):
    n, k = map(int, input().split())
    nums = list(input().strip())

    num_length = len(nums) // 4

    num_candi = []
    for i in range(len(nums)):
        num_candi += get_nums(nums, num_length)
        nums = [nums[-1]] + nums[: n - 1]

    num_candi = list(set(num_candi))
    num_candi.sort(reverse=True)

    print(f"#{test_case} {int(num_candi[k-1], base=16)}")
