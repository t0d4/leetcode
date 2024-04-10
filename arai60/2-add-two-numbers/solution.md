# [Add two numbers](https://leetcode.com/problems/add-two-numbers)

## Initial trial

### 考えたこと

- ノードは小さい桁の側から並んでいるので、 `l1` と `l2` がそれぞれ何桁の数なのかを最初に知る必要はなく都合が良い
- `l1` と `l2` の対応する各ノードの和を取り、10から溢れた分を繰り上がりとして持ち越せば良い

### 反省点

- 最後の `if carry > 0:` の部分は上の `while` の条件式を調整することで `while` ループの中に入れられたかも
- `divmod(l1_ptr.val + l2_ptr.val + carry)` のように書くのではなくて、一時変数を用意してまず `l1_ptr.val` を足して、次に `l2_ptr.val` を足して...とやっていけばもう少しコードが簡潔になったかも

## 2nd attempt

### 改善点

- `while` の条件式を調整してコードを簡潔にした。