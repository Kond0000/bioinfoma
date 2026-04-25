# Bioinformatics RNA-seq Study Portfolio

RNA-seq解析を独学で身につけるための学習リポジトリです。  
目的は、解析の流れを理解すること、Google Colab で手を動かせること、GitHubで見せられる形に整理することです。

## このリポジトリでやっていること

- RNA-seq解析をトピックごとに分けて学ぶ
- 生物学初学者でも追えるように、解析前の生物学的な意味から説明する
- 各トピックで「目的」「入力」「出力」「Colabでの進め方」を明確にする
- 解析コードと図を残して、後から見返せる形にする

## 進捗

| Topic | 内容 | 状態 |
|---|---|---|
| `01_count_matrix_qc` | count matrix の読み込みと基本QC | 進行中 |
| `02_normalization` | 正規化と log 変換 | 未着手 |
| `03_exploratory_analysis` | PCA とヒートマップ | 未着手 |
| `04_differential_expression` | 差次的発現解析 | 未着手 |
| `05_functional_interpretation` | GO・経路解析 | 未着手 |
| `06_portfolio` | GitHub 公開用の整理 | 未着手 |

## Colab

各トピックはトップREADMEから直接 Colab を開けます。

| Topic | Notebook | Open in Colab |
|---|---|---|
| `01_count_matrix_qc` | [day1_count_matrix_qc_colab.ipynb](notebooks/day1_count_matrix_qc_colab.ipynb) | [Open](https://colab.research.google.com/github/Kond0000/bioinfoma/blob/main/notebooks/day1_count_matrix_qc_colab.ipynb) |
| `02_normalization` | [day2_normalization_colab.ipynb](notebooks/day2_normalization_colab.ipynb) | [Open](https://colab.research.google.com/github/Kond0000/bioinfoma/blob/main/notebooks/day2_normalization_colab.ipynb) |
| `03_exploratory_analysis` | [day3_exploratory_analysis_colab.ipynb](notebooks/day3_exploratory_analysis_colab.ipynb) | [Open](https://colab.research.google.com/github/Kond0000/bioinfoma/blob/main/notebooks/day3_exploratory_analysis_colab.ipynb) |
| `04_differential_expression` | [day4_differential_expression_colab.ipynb](notebooks/day4_differential_expression_colab.ipynb) | [Open](https://colab.research.google.com/github/Kond0000/bioinfoma/blob/main/notebooks/day4_differential_expression_colab.ipynb) |
| `05_functional_interpretation` | [day5_functional_interpretation_colab.ipynb](notebooks/day5_functional_interpretation_colab.ipynb) | [Open](https://colab.research.google.com/github/Kond0000/bioinfoma/blob/main/notebooks/day5_functional_interpretation_colab.ipynb) |
| `06_portfolio` | [day6_portfolio_colab.ipynb](notebooks/day6_portfolio_colab.ipynb) | [Open](https://colab.research.google.com/github/Kond0000/bioinfoma/blob/main/notebooks/day6_portfolio_colab.ipynb) |

## ディレクトリ構成

```text
notebooks/
  day1_count_matrix_qc_colab.ipynb
  day2_normalization_colab.ipynb
  day3_exploratory_analysis_colab.ipynb
  day4_differential_expression_colab.ipynb
  day5_functional_interpretation_colab.ipynb
  day6_portfolio_colab.ipynb
topics/
  01_count_matrix_qc/
  02_normalization/
  03_exploratory_analysis/
  04_differential_expression/
  05_functional_interpretation/
  06_portfolio/
README.md
```

各トピックには `README.md` を置き、次の4点がすぐ分かるようにしています。

- 何を学ぶのか
- なぜそれが必要か
- 何を実行するのか
- 何が出力されるのか

トピック一覧は [topics/README.md](topics/README.md) にまとめています。

## 最初に見る場所

現在の開始地点は [topics/01_count_matrix_qc/README.md](topics/01_count_matrix_qc/README.md) です。  
まず `count matrix とは何か` を読んでから Colab ノートブックを開きます。

Google Colab で試す場合:

- [day1_count_matrix_qc_colab.ipynb](notebooks/day1_count_matrix_qc_colab.ipynb)
- [Open in Colab](https://colab.research.google.com/github/Kond0000/bioinfoma/blob/main/notebooks/day1_count_matrix_qc_colab.ipynb)

## GitHubで公開するときの見せ方

GitHub上では、次の順番で読めると分かりやすいです。

1. この `README.md` で全体像を見る
2. `topics/README.md` で学習ステップを見る
3. 各トピックの `README.md` で目的と実行内容を見る
4. `notebooks/` で実際の教材を開く

## GitHub公開の最小手順

```bash
git init
git add .
git commit -m "Initialize RNA-seq study portfolio"
```

その後、GitHubで新しい公開リポジトリを作って push します。

## 現在の成果物

- [day1_count_matrix_qc_colab.ipynb](notebooks/day1_count_matrix_qc_colab.ipynb)
- [day2_normalization_colab.ipynb](notebooks/day2_normalization_colab.ipynb)
- [day3_exploratory_analysis_colab.ipynb](notebooks/day3_exploratory_analysis_colab.ipynb)
- [day4_differential_expression_colab.ipynb](notebooks/day4_differential_expression_colab.ipynb)
- [day5_functional_interpretation_colab.ipynb](notebooks/day5_functional_interpretation_colab.ipynb)
- [day6_portfolio_colab.ipynb](notebooks/day6_portfolio_colab.ipynb)
