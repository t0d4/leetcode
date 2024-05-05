# [Permutations](https://leetcode.com/problems/permutations)

## Initial trial

### 考えたこと

- itertoolsを使えばすぐ出来る

## 2nd attempt (自力実装) solve2.py

### 考えたこと

- 再帰で考える。DFSを使う
- 例えば `[1, 2, 3]` があったら、仮に「先頭は1」と決めると `[2, 3]` をいろいろ並び替えて1の後ろにくっつけることになる。ここに再帰構造がある
- DFSの1本のパスによって構築されるpermutationを保持する `ans` と、いま使用可能な数字のリスト `nums` があるとき、$0 \le i < \mathrm{len}(\mathrm{nums})$について
  1. 【★】もし `len(nums) == 0` なら `ans` を求めるpermutationの1つとして記録してreturn
  2. そうでないなら
     1. `nums[i]` を `ans` の末尾に追加
     2. `nums` を `nums[:i]+nums[i+1:]` として（`nums` から `i`番目を除いて）、【★】に戻る

### 反省点

- 計算量がよくわからないまま書いてとりあえず通した感がある
  - `n := len(nums)` として $O(n! \times n)$といったところ？
    - `nums` の長さを1つずつ減らすので、内部のforの回る回数が1回ずつ減っていく => O(n!)
    - `nums[:i] + nums[i + 1 :]` のところでコピーが走る => (最悪の時点で) O(n)
- リストのslicingはcopyを伴うので `nums[:i] + nums[i + 1 :]` は計算量としては良くないが、制約上 `1 <= len(nums) <= 6` なので問題にはならない
  - https://wiki.python.org/moin/TimeComplexity