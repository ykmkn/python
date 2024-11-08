import itertools

# 0から9までの数字をリストにする
numbers = list(range(10))

# 4つの数字の組み合わせを生成
combinations = itertools.combinations(numbers, 4)

# 結果を横に4つずつ並べて表示
count = 0
for combo in combinations:
    print(combo, end='  ')
    count += 1
    if count % 4 == 0:
        print()  # 4つごとに改行
