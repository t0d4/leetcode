# [Maximum Subarray](https://leetcode.com/problems/maximum-subarray)

## Initial trial (FAILED)

### 考えたこと

- 求めるのは和だけで良い（どこからどこまでがmaxを与えるかを知る必要はない）
- 0未満の数が来た場合は必ず減る、そうでなければ必ず増える
- Sliding Windowアプローチを取る場合、右のポインタを更新しながらそこまでの和を更新していくのは簡単だがどのタイミングで左を更新すればいいのか分からない

### 解説の理解 (solve_with_answer.py)

- [解説動画](https://youtu.be/5WZl3MMT0Eg?si=SXHzImAJXhWBKuPJ)を視聴
- そもそもポインタを更新する必要がなかった、というのもl, rの場所はどうでもよく、今i番目にいる場合i-1番目までをsubarrayに含めるべきなのか否かだけ分かれば良いから
- 次を行う
  1. `max_subsum, cursum = nums[0], 0`で初期化
  2. `for i in range(len(nums))`
     1. `cursum < 0`なら（i番目より左が不要なら）i-1番目までは考慮しなくていいので`cumsum=0`
     2. `cursum += nums[i]`
     3. `max_subsum = max(max_subsum, cursum)`

## 2nd attempt

