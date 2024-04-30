# [Search Insert Position](https://leetcode.com/problems/search-insert-position)

## Initial trial

### 考えたこと

- 普通に二分探索を行う
- 最終的に `c` は "リスト内に `target` を入れるならこの要素を右に/左にずらして入れるべき" となる要素を指しているので， `nums[c]` と `target` の大小を比較して `c` の位置に入れる（`nums[c]`を右にずらす）べきか `c+1` の位置に入れる（`nums[c]`の右に入れる）べきか判断する．