def binary_search(left, right, times, n):
    while left < right:
        mid = (left + right) // 2

        result = 0
        for t in times:
            result += mid // t

        if result < n:
            left = mid + 1
        else:
            right = mid
    return left


def solution(n, times):
    answer = 0

    answer = binary_search(1, n * max(times), times, n)

    return answer
