# [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters)

## Initial Trial (FAILED)

### 考え方

- Sliding Windowを使えば良い。右側のポインタを動かしていくたびに「既に見た文字の集合」に文字を追加していき、その集合に入っているものが再び現れたらそこまで左側のポインタを動かす。

### 反省点

- コードを書き直すたびに出てくる「通らないテストケース」に気を取られ、既に見た文字の集合に入っている文字が再び現れたときにそもそも何をしてなくてはいけないのかを落ち着いて考えられなかった。
  - failのコードだと単純に「再び現れた文字」まで左側のポインタを進める、としているため、 `abba` のようなケースで通らない
- 集合を上手く利用しようと思えたのは進歩ではある。この問題のような状況に応じた更新処理を伴う走査では紙に書いたりして考えたほうが良いかも

