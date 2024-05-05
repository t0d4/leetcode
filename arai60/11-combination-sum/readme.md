# [Combination Sum](https://leetcode.com/problems/combination-sum)

## Initial trial

### 考えたこと

- `candidates` の要素を重複を許して取り出していって、それらの和がちょうど `target` になったら答えのリストに追加する。
- それらの和が `target` を超えたら探索を中断する、ことでどのくらい枝刈りできるか...
- DFSで実装する

### 反省点

- Submissionは通ったが、さすがに探索範囲が広すぎたのかBeats 5% of solutions
- 組み合わせとして見ると重複しているものを大量に数えてしまっているのがもったいない
- tupleはイミュータブルなので `comb + (c,)` のところで再構築が走っているせいで重いのかもしれない

## Upsolve

- [解説動画](https://leetcode.com/problems/combination-sum)を視聴
- `candidate[i]`をcombinationに追加するときに、毎回その下に「`candidate[i]`をもう一度以上使うことを許す場合」と「`candidate[i]`をもう二度と使わない場合」の2通りの部分木が出来るように考えることで葉の部分に重複が生まれなくなるらしい
  - `candidate[i]`をもう一度以上使うことを許す場合
    - https://github.com/t0d4/leetcode/blob/2116a50e305b0f4092e160c4b970a21e964e25ca/arai60/11-combination-sum/solve_neetcode.py#L12-L14
  - `candidate[i]`をもう二度と使わない場合
    - https://github.com/t0d4/leetcode/blob/2116a50e305b0f4092e160c4b970a21e964e25ca/arai60/11-combination-sum/solve_neetcode.py#L15-L17

**復習必須**