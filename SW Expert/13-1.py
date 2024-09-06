T = int(input())
for test_case in range(1, T + 1):
    dict = {
        "ZRO": 0,
        "ONE": 0,
        "TWO": 0,
        "THR": 0,
        "FOR": 0,
        "FIV": 0,
        "SIX": 0,
        "SVN": 0,
        "EGT": 0,
        "NIN": 0,
    }

    t_num, length = input().split()

    length = int(length)

    data = input().split()
    for i in range(length):
        dict[data[i]] += 1

    result = []

    for item in dict.items():
        key, val = item

        val = int(val)

        for i in range(val):
            result.append(key)

    result = " ".join(result)

    print(f"#{test_case} {result}")
