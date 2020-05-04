def dfs(nums, length, min_lim):
    # 返り値は、すべての数列の得点の最大値 ans です。
    # numsは数列の本体、lengthは数字の何個目まで決めたか、min_limは次の数字の最小値
    ans = 0
    if length == n:
        # 数列が完成したので、得点を計算します
        score_ret = 0
        for a, b, c, d in req:
            # nums[0]を捨てたので、nums[b-1]...としなくて済みます
            if nums[b] - nums[a] == c:
                score_ret += d
        return score_ret  # この数列の得点を返します
    else:
        # まだ数列が完成していません
        for nu in range(min_lim, m + 1):
            # 次の数字の下限はmin_limで、上限はmです
            new_nums = nums + [nu]  # 長さ1のリスト[nu]を連結します
            # lengthは1増えて、次の下限は今付け加えた数字nuです
            score = dfs(new_nums, length + 1, nu)
            ans = max(ans, score)  # 最大の得点を更新します

    # すべてが終わったので、答えを返します
    return ans


n, m, q = list(map(int, input().split()))

# 問題文のa,b,c,dの「リストのリスト」reqです。[[a1,b1,c1,d1],[a2,b2,c2,d2],[a3,b3,c3,d3]]のようになります。
req = [list(map(int, input().split())) for _ in range(q)]

# 最終的に答えが返ってくるようにします。処理はすべてdfsメソッドでやってもらいます。
# 数列の番号と添字を一致させたいので、適当な長さ1のリストを最初の状態にしておきます。
# 例えばサンプル1の1,3,4は[-1, 1, 3, 4]になります。
ans = dfs([-1], 0, 1)
print(ans)
