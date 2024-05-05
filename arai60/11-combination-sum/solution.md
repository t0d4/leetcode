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
- 新しい数を答えのリストに追加するときに、毎回「`candidate[i]`をもう一度使うことを許す場合」と「`candidate[i]`をもう使わない場合」の2通りを考えているということのよう

**復習必須**