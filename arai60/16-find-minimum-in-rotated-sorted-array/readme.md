# [Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array)

## Initial trial

### 考えたこと

- 9-search-in-rotated-sorted-arrayの考え方が引き継げそう
  - 「どちらがソートされているのかを見て、ソートされている方を基準に左右どちらに絞り込めばいいのかを判断する」
  - 今回は以下の通り
    1. `while l < r`
       1. `c = (l + r) // 2`
       2. もし`nums[c] > nums[r]`なら、つまり`nums[c], ..., nums[r]`がちゃんとソートされていないなら、この部分が例えば`7, 1, 2, 3`のようになっているはずで、右側に最小値がある => `l = c + 1`で更新
       3. そうでないなら、つまり`nums[c], ..., nums[r]`がちゃんとソートされているなら、最小値は`nums[c]`であるかもしくはもっと左にある数 => `r = c`で更新