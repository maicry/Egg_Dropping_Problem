eggsDrop = dict()  # 用于记录重复的子问题的解


def dp(K, N):
    # base case
    if K == 1:
        return N
    if N == 0:
        return 0

    # 避免重复计算
    if (K, N) in eggsDrop:
        return eggsDrop[(K, N)]

    res = float('INF')

    # 穷举所有可能的选择
    for i in range(1, N + 1):
        res = min(res,
                  max(
                      dp(K, N - i),
                      dp(K - 1, i - 1)
                  ) + 1
                  )

    # 记入字典
    eggsDrop[(K, N)] = res

    return res


if __name__ == "__main__":
    k = eval(input())
    n = eval(input())
    print(dp(k, n))