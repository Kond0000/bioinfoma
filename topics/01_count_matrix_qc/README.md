# 01 Count Matrix QC

## このトピックでやること

RNA-seq解析でよく受け取る `count matrix` を読み込み、サンプルごとの総カウント数を確認します。  
ただし、最初に「RNA-seqで何を数えているのか」から確認します。

## まず知ること

生物の細胞では、DNAに保存された遺伝子情報が、必要に応じてRNAとして読み出されます。  
ざっくり言うと、RNAが多い遺伝子ほど、その細胞でよく使われている可能性があります。

RNA-seqは、細胞中のRNAを細かく読んで、どの遺伝子由来のRNAがどれくらいあったかを数える実験です。

例:

```text
あるサンプルで TP53 由来のRNA断片が 120 個見つかった
別のサンプルで TP53 由来のRNA断片が 300 個見つかった
```

このように、遺伝子ごと・サンプルごとに数えた表が `count matrix` です。

## count matrix とは

`count matrix` は、行が遺伝子、列がサンプル、値がRNA断片の数になっている表です。

```text
gene   control_1  control_2  treated_1  treated_2
TP53         120        100        300        280
MYC          300        280        600        650
IL6           30         25        200        220
```

読み方:

- `gene`
  遺伝子名です。例: `TP53`, `MYC`, `IL6`
- `control_1`, `control_2`
  何も処理していない比較用サンプルです。
- `treated_1`, `treated_2`
  薬剤処理など、条件を変えたサンプルです。
- 数字
  その遺伝子に対応するRNA断片が何個読まれたかです。

例えば `IL6` は control では `30`, `25` ですが、treated では `200`, `220` です。  
これは「treated で IL6 のRNAが増えていそう」と考える入口になります。

ただし、この数字はそのまま最終結論にはしません。サンプルごとに読まれた総量が違うため、後で正規化や統計解析が必要です。

## 最小用語集

- 遺伝子
  体の中で働く分子を作るための設計情報です。例: `TP53`, `MYC`, `IL6`
- RNA
  DNAの情報が一時的に読み出されたものです。RNAが多い遺伝子は、その条件でよく使われている可能性があります。
- サンプル
  実験で測定した1つの材料です。例: controlの細胞1つ分、treatedの細胞1つ分
- control
  比較の基準になる条件です。薬剤を入れていない、処理していない、など。
- treated
  比較したい処理を加えた条件です。薬剤を入れた、刺激した、など。
- read
  シーケンサーが読んだ短いRNA由来の断片です。
- count
  ある遺伝子に対応するreadが何個あったかの数です。
- library size
  1サンプルで数えられたreadの合計です。

## 目的

- count matrix の形に慣れる
- サンプルごとの read 数の違いを見る
- いきなり遺伝子比較せず、まずQCを見る癖をつける

## 具体的に役立つ場面

RNA-seqの結果ファイルを受け取ったとき、最初に「これはそもそも何の表なのか」「比較に使えそうなサンプルなのか」を判断する場面で役立ちます。

## このトピックで解く課題

「treated で IL6 が高そうに見えるが、その前にこのデータ自体を信じて先へ進めてよいか」を判断するために、count matrix と library size を読み解きます。

## 入力

- `data/toy_counts.csv`

## 出力

- `results/figures/day1_library_size.png`

Google Colab で動かす場合:

- リポジトリ直下の [notebooks/day1_count_matrix_qc_colab.ipynb](../../notebooks/day1_count_matrix_qc_colab.ipynb) を開いて上から順に実行します
- GitHub から直接開く場合は [Open in Colab](https://colab.research.google.com/github/Kond0000/bioinfoma/blob/main/notebooks/day1_count_matrix_qc_colab.ipynb) を使います
- このノートブックは単体で動くので、追加のデータ配置なしで試せます

## このトピックにあるファイル

- `data/toy_counts.csv`
  練習用の小さな count matrix です。
- `results/figures/day1_library_size.png`
  サンプルごとの総カウント数を示す図です。
- `../../notebooks/day1_count_matrix_qc_colab.ipynb`
  Google Colab でそのまま実行できる学習用ノートブックです。

## ここで見るポイント

- count matrix は「遺伝子ごとにRNA断片を数えた表」
- `control_1` と `treated_1` で総カウント数が同じではない
- `IL6` は treated でかなり増えている
- この段階ではまだ正式な差次的発現解析ではない

## 今回の結果

- `treated_1` と `treated_2` は control より総カウント数がやや大きい
- `IL6` は treated で強く増えており、後続の解析で注目候補になる

## ゴール

「count matrix が何を表しているか」と「まず何を確認するべきか」を説明できるようになることです。
