# [Generate Parentheses](https://leetcode.com/problems/generate-parentheses)

## Initial trial [失敗]

### 考えたこと

- validなパターンとして `pattern` があったときに、さらにvalidなものを作るには以下の3つが有り得ると考えた。
  - ()`pattern`
  - `pattern`()
  - (`pattern`)
- これを再帰でどんどんくっつけていくように実装

### 反省点

- 上記の解法はn=4から合わない、なぜなら上の考え方では (()**)(**()) のように既存のパターン (()()) の中にさらに新たに2つの括弧 )( が入り込むケースを考慮できていないから。