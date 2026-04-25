# Bioinformatics RNA-seq Study Portfolio

このリポジトリは、RNA-seq解析を **ケーススタディとして学ぶための教材** です。  
読者は「データサイエンスは得意だが、生物学は初学者」という前提です。表、平均、分布、可視化の考え方には慣れている一方で、遺伝子、RNA、発現、実験条件といった生物学の言葉は最初から説明します。

この教材の目的は、単にコードを動かすことではありません。RNA-seqデータを見たときに、次のような判断ができるようになることを目指します。

- この表は何を測定したものか
- 条件間で比較してよいデータか
- 見かけの差と本当の発現差をどう区別するか
- どの遺伝子が変化したと言えるか
- その変化から、細胞の中で何が起きたと考えられるか

## Case Study

この教材は、次の研究課題を解き進める形で設計しています。

`炎症刺激を受けた細胞で、どの遺伝子群と生物学的経路が変化したのかを RNA-seq で明らかにする`

つまり、単に `PCA を学ぶ` のではなく、次の問いに答えるために PCA を使います。

- このデータは解析に進めてよい品質か
- 刺激群と対照群は全体として分かれているか
- どの遺伝子が本当に変化したのか
- それは炎症、ストレス応答、増殖のどれに近いのか
- その結果を、他人に伝わる解析レポートとしてどうまとめるか

## 学び方

各章は、教科書の章のように次の流れで読めるようにしています。

1. 研究上の問いを確認する
2. 必要な生物学の前提を理解する
3. データサイエンスとして表や図を読む
4. Colabで最小限のコードを動かす
5. 得られた結果から、次に何を判断するかを考える

この教材では、先に「なぜそれを学ぶのか」を説明してからコードに入ります。たとえば正規化は、単なる前処理ではありません。サンプルごとの総read数が違うと、見かけ上の差と本当の発現差が混ざるため、それを分けるために必要になります。

## 章構成

| Topic | 内容 | 具体的に解きたい問い | 身につける判断力 |
|---|---|---|---|
| `00_molecular_biology_primer` | 分子生物学の最小基礎 | `IL6` が増えたとは、細胞内で何が増えたという意味か | DNA、RNA、遺伝子発現の関係を説明できる |
| `01_count_matrix_qc` | count matrix の読み込みと基本QC | 刺激群と対照群で、遺伝子の使われ方を比べる準備ができているか | RNA-seqの表が何を数えているかを説明できる |
| `02_normalization` | 正規化と log 変換 | `IL6` の上昇は本当の発現差か、それとも測定量の差か | 生の count をそのまま比較してはいけない理由を判断できる |
| `03_exploratory_analysis` | PCA とヒートマップ | 刺激群と対照群は全体の発現パターンで分かれているか | 可視化から外れ値や条件差を読む |
| `04_differential_expression` | 差次的発現解析 | 刺激によって本当に変化した遺伝子はどれか | fold change と有意性を組み合わせて解釈する |
| `05_functional_interpretation` | 機能解釈 | 変化した遺伝子群は、どんな生物学的変化を示しているか | 遺伝子リストを生物学的な説明に変換する |
| `06_portfolio` | GitHub 公開用の整理 | この解析で何が分かったのかを他人にどう伝えるか | 解析の目的、方法、結果、解釈をまとめる |
| `07_experimental_design_metadata` | 実験設計とmetadata | 比較できるサンプル設計になっているか | replicate、condition、交絡を読む |
| `08_public_data_sra_geo` | 公共データの読み方 | GEO/SRAから解析に使えるデータを選べるか | 公開データの実験内容を読み解く |
| `09_fastq_quality_control` | FASTQとread QC | シーケンサー出力は解析に使える品質か | read quality とQC項目を理解する |
| `10_alignment_quantification` | アライメントと定量 | readをどの遺伝子由来として数えるのか | FASTQからcount matrixまでの流れを説明できる |
| `11_gene_annotation_ids` | 遺伝子IDとアノテーション | `ENSG...` と `TP53` はどう対応するか | 遺伝子IDを整理して解釈につなげる |
| `12_batch_effects_reproducibility` | バッチ効果と再現性 | 見えている差は刺激差か実験ロット差か | 条件差とバッチ効果を区別する |
| `13_pathway_enrichment_advanced` | pathway enrichment | 炎症関連遺伝子は偶然以上に多いか | gene set の偏りを読む |
| `14_reproducible_workflow` | 再現可能な解析 | 半年後に同じ結果を再現できるか | 解析を再実行可能な成果物にする |

## Colab

各トピックはトップREADMEから直接 Colab を開けます。

| Topic | Notebook | Open in Colab |
|---|---|---|
| `00_molecular_biology_primer` | [day0_molecular_biology_primer_colab.ipynb](notebooks/day0_molecular_biology_primer_colab.ipynb) | [Open](https://colab.research.google.com/github/Kond0000/bioinfoma/blob/main/notebooks/day0_molecular_biology_primer_colab.ipynb) |
| `01_count_matrix_qc` | [day1_count_matrix_qc_colab.ipynb](notebooks/day1_count_matrix_qc_colab.ipynb) | [Open](https://colab.research.google.com/github/Kond0000/bioinfoma/blob/main/notebooks/day1_count_matrix_qc_colab.ipynb) |
| `02_normalization` | [day2_normalization_colab.ipynb](notebooks/day2_normalization_colab.ipynb) | [Open](https://colab.research.google.com/github/Kond0000/bioinfoma/blob/main/notebooks/day2_normalization_colab.ipynb) |
| `03_exploratory_analysis` | [day3_exploratory_analysis_colab.ipynb](notebooks/day3_exploratory_analysis_colab.ipynb) | [Open](https://colab.research.google.com/github/Kond0000/bioinfoma/blob/main/notebooks/day3_exploratory_analysis_colab.ipynb) |
| `04_differential_expression` | [day4_differential_expression_colab.ipynb](notebooks/day4_differential_expression_colab.ipynb) | [Open](https://colab.research.google.com/github/Kond0000/bioinfoma/blob/main/notebooks/day4_differential_expression_colab.ipynb) |
| `05_functional_interpretation` | [day5_functional_interpretation_colab.ipynb](notebooks/day5_functional_interpretation_colab.ipynb) | [Open](https://colab.research.google.com/github/Kond0000/bioinfoma/blob/main/notebooks/day5_functional_interpretation_colab.ipynb) |
| `06_portfolio` | [day6_portfolio_colab.ipynb](notebooks/day6_portfolio_colab.ipynb) | [Open](https://colab.research.google.com/github/Kond0000/bioinfoma/blob/main/notebooks/day6_portfolio_colab.ipynb) |
| `07_experimental_design_metadata` | [day7_experimental_design_metadata_colab.ipynb](notebooks/day7_experimental_design_metadata_colab.ipynb) | [Open](https://colab.research.google.com/github/Kond0000/bioinfoma/blob/main/notebooks/day7_experimental_design_metadata_colab.ipynb) |
| `08_public_data_sra_geo` | [day8_public_data_sra_geo_colab.ipynb](notebooks/day8_public_data_sra_geo_colab.ipynb) | [Open](https://colab.research.google.com/github/Kond0000/bioinfoma/blob/main/notebooks/day8_public_data_sra_geo_colab.ipynb) |
| `09_fastq_quality_control` | [day9_fastq_quality_control_colab.ipynb](notebooks/day9_fastq_quality_control_colab.ipynb) | [Open](https://colab.research.google.com/github/Kond0000/bioinfoma/blob/main/notebooks/day9_fastq_quality_control_colab.ipynb) |
| `10_alignment_quantification` | [day10_alignment_quantification_colab.ipynb](notebooks/day10_alignment_quantification_colab.ipynb) | [Open](https://colab.research.google.com/github/Kond0000/bioinfoma/blob/main/notebooks/day10_alignment_quantification_colab.ipynb) |
| `11_gene_annotation_ids` | [day11_gene_annotation_ids_colab.ipynb](notebooks/day11_gene_annotation_ids_colab.ipynb) | [Open](https://colab.research.google.com/github/Kond0000/bioinfoma/blob/main/notebooks/day11_gene_annotation_ids_colab.ipynb) |
| `12_batch_effects_reproducibility` | [day12_batch_effects_reproducibility_colab.ipynb](notebooks/day12_batch_effects_reproducibility_colab.ipynb) | [Open](https://colab.research.google.com/github/Kond0000/bioinfoma/blob/main/notebooks/day12_batch_effects_reproducibility_colab.ipynb) |
| `13_pathway_enrichment_advanced` | [day13_pathway_enrichment_advanced_colab.ipynb](notebooks/day13_pathway_enrichment_advanced_colab.ipynb) | [Open](https://colab.research.google.com/github/Kond0000/bioinfoma/blob/main/notebooks/day13_pathway_enrichment_advanced_colab.ipynb) |
| `14_reproducible_workflow` | [day14_reproducible_workflow_colab.ipynb](notebooks/day14_reproducible_workflow_colab.ipynb) | [Open](https://colab.research.google.com/github/Kond0000/bioinfoma/blob/main/notebooks/day14_reproducible_workflow_colab.ipynb) |

## ディレクトリ構成

```text
notebooks/
  day0_molecular_biology_primer_colab.ipynb
  day1_count_matrix_qc_colab.ipynb
  day2_normalization_colab.ipynb
  day3_exploratory_analysis_colab.ipynb
  day4_differential_expression_colab.ipynb
  day5_functional_interpretation_colab.ipynb
  day6_portfolio_colab.ipynb
  day7_experimental_design_metadata_colab.ipynb
  day8_public_data_sra_geo_colab.ipynb
  day9_fastq_quality_control_colab.ipynb
  day10_alignment_quantification_colab.ipynb
  day11_gene_annotation_ids_colab.ipynb
  day12_batch_effects_reproducibility_colab.ipynb
  day13_pathway_enrichment_advanced_colab.ipynb
  day14_reproducible_workflow_colab.ipynb
topics/
  00_molecular_biology_primer/
  01_count_matrix_qc/
  02_normalization/
  03_exploratory_analysis/
  04_differential_expression/
  05_functional_interpretation/
  06_portfolio/
  07_experimental_design_metadata/
  08_public_data_sra_geo/
  09_fastq_quality_control/
  10_alignment_quantification/
  11_gene_annotation_ids/
  12_batch_effects_reproducibility/
  13_pathway_enrichment_advanced/
  14_reproducible_workflow/
README.md
```

## GitHub上での読み方

1. この `README.md` でケーススタディ全体を読む
2. `Colab` の表から各章を開く
3. 各トピックの `README.md` で、その章がどんな問いに対応するかを確認する
4. Colabノートブックで本文とコードを順に読む
5. 最後に、各章で何を判断できるようになったかを振り返る

## 現在の教材

- [day0_molecular_biology_primer_colab.ipynb](notebooks/day0_molecular_biology_primer_colab.ipynb)
- [day1_count_matrix_qc_colab.ipynb](notebooks/day1_count_matrix_qc_colab.ipynb)
- [day2_normalization_colab.ipynb](notebooks/day2_normalization_colab.ipynb)
- [day3_exploratory_analysis_colab.ipynb](notebooks/day3_exploratory_analysis_colab.ipynb)
- [day4_differential_expression_colab.ipynb](notebooks/day4_differential_expression_colab.ipynb)
- [day5_functional_interpretation_colab.ipynb](notebooks/day5_functional_interpretation_colab.ipynb)
- [day6_portfolio_colab.ipynb](notebooks/day6_portfolio_colab.ipynb)
- [day7_experimental_design_metadata_colab.ipynb](notebooks/day7_experimental_design_metadata_colab.ipynb)
- [day8_public_data_sra_geo_colab.ipynb](notebooks/day8_public_data_sra_geo_colab.ipynb)
- [day9_fastq_quality_control_colab.ipynb](notebooks/day9_fastq_quality_control_colab.ipynb)
- [day10_alignment_quantification_colab.ipynb](notebooks/day10_alignment_quantification_colab.ipynb)
- [day11_gene_annotation_ids_colab.ipynb](notebooks/day11_gene_annotation_ids_colab.ipynb)
- [day12_batch_effects_reproducibility_colab.ipynb](notebooks/day12_batch_effects_reproducibility_colab.ipynb)
- [day13_pathway_enrichment_advanced_colab.ipynb](notebooks/day13_pathway_enrichment_advanced_colab.ipynb)
- [day14_reproducible_workflow_colab.ipynb](notebooks/day14_reproducible_workflow_colab.ipynb)
