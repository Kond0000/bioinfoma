# 09 FASTQ and Read Quality Control

## この章の位置づけ

この章は、RNA-seqケーススタディ `炎症刺激を受けた細胞で、どの遺伝子群と生物学的経路が変化したのか` を解くための一部です。

## この章でまず問うこと

`FASTQ readは発現解析に使ってよい品質か`

この問いに答えられないまま次へ進むと、表や図は作れても、何を根拠に判断しているのかが曖昧になります。

## 何のための知識か

count matrixの前段階で低品質readやadapter混入があると、遺伝子への対応づけと定量が歪むため。

## 現実ではどこで役立つか

共同研究、公共データ再解析、ポートフォリオ作成の場面で、結果をただ出すのではなく「この比較は妥当か」「この図から何を言ってよいか」を説明するために役立ちます。

## この章で使う具体例

1本のFASTQ readと品質文字列

この教材では、いきなり巨大な実データに入らず、まず小さな表で考え方を固定します。小さな例で読み方を理解してから、実データや公共データに広げます。

## Colabで手を動かして確認すること

Phred quality scoreを計算し、Q20ラインとQC項目を読む。

コードは単なる作業手順ではなく、各セルで「いま何を確かめているのか」が分かるようにコメントと本文を入れています。

## この章で扱う概念

Colab内で、必要になった順に説明します。用語を先に暗記するのではなく、具体例を読めるようにするために使います。

## 読み取れるようになること

FASTQの4行構造とQCレポートの見方を説明できる。

## Colab

- [day9_fastq_quality_control_colab.ipynb](../../notebooks/day9_fastq_quality_control_colab.ipynb)
- [Open in Colab](https://colab.research.google.com/github/Kond0000/bioinfoma/blob/main/notebooks/day9_fastq_quality_control_colab.ipynb)
