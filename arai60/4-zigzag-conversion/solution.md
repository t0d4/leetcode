# [Zigzag Conversion](https://leetcode.com/problems/zigzag-conversion)

## Initial trial

### 考えたこと

- n文字目はf(n)行目に現れる、というような規則がないか考えたが、どうやらなさそう？
- 各行についてリストを持ち、`s`を1文字ずつ走査する過程で行を表すインデックスを増やしたり減らしたりしながらそれに入れていくことを考える

### 反省点

- `numRows`が1の場合はずっと同じ行に書き続けることになるのでdirectionが0でないといけないことになる。そこで `direction = 1 if numRows != 1 else 0` としているが、 `numRows == 1`のときに `direction == 0` でないといけないというのはなぜかすぐには伝わりにくいかもしれない
- 最後の `"".join(["".join(row) for row in mat])` は若干可読性に難あり？