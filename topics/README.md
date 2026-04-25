# Topics Overview

このディレクトリは、RNA-seq教材の各章をまとめた目次です。  
各章は独立したメモではなく、1つのケーススタディを段階的に解くための章として並んでいます。

## ケーススタディ

`炎症刺激を受けた細胞で、どの遺伝子群と生物学的経路が変化したのかを RNA-seq で明らかにする`

この問いに答えるために、分子生物学の基礎、実験設計、公共データ、FASTQ、アライメント、count matrix、正規化、可視化、差次的発現解析、機能解釈、再現性を順番に学びます。

## トピック一覧

### 00 Molecular Biology Primer

RNA-seqを理解するために必要な、DNA、RNA、遺伝子発現の最小限の生物学を学びます。  
ここでは「`IL6` が増えたと言うとき、細胞の中では何が増えたと考えているのか」を扱います。

詳細: [00_molecular_biology_primer/README.md](00_molecular_biology_primer/README.md)

### 01 Count Matrix QC

count matrix が何を数えた表なのかを理解し、比較に入る前に library size を確認します。  
ここでは「そもそもこの表は、刺激群と対照群を比べる出発点として使えるのか」を考えます。

詳細: [01_count_matrix_qc/README.md](01_count_matrix_qc/README.md)

### 02 Normalization

サンプルごとの総read数の違いを補正し、生の count を比較しやすい形に変換します。  
ここでは「`IL6` が高いのは本当の発現差なのか、単に多く読まれただけなのか」を考えます。

詳細: [02_normalization/README.md](02_normalization/README.md)

### 03 Exploratory Analysis

PCAやヒートマップで、データ全体の構造を見ます。  
ここでは「刺激群と対照群は全体として分かれているのか、外れ値はないのか」を考えます。

詳細: [03_exploratory_analysis/README.md](03_exploratory_analysis/README.md)

### 04 Differential Expression

条件間で本当に変化した遺伝子を調べます。  
ここでは「変化量が大きく、統計的にも信頼できる遺伝子はどれか」を考えます。

詳細: [04_differential_expression/README.md](04_differential_expression/README.md)

### 05 Functional Interpretation

差次的発現遺伝子を、生物学的な意味に結びつけます。  
ここでは「変化した遺伝子群は、炎症、ストレス応答、増殖のどれに関係していそうか」を考えます。

詳細: [05_functional_interpretation/README.md](05_functional_interpretation/README.md)

### 06 Portfolio

解析結果を、GitHubで第三者に伝わる形に整理します。  
ここでは「このケーススタディで何が分かったのかを、READMEと図でどう説明するか」を考えます。

詳細: [06_portfolio/README.md](06_portfolio/README.md)

### 07 Experimental Design and Metadata

サンプル数、条件、replicate、metadata が解析結果の信頼性をどう左右するかを学びます。  
ここでは「刺激群と対照群の差を信頼してよいと言うために、どのようなmetadataとreplicateが必要なのか」を考えます。

詳細: [07_experimental_design_metadata/README.md](07_experimental_design_metadata/README.md)

### 08 Public Data: SRA and GEO

公開RNA-seqデータを探し、実験内容とサンプル情報を読み取る方法を学びます。  
ここでは「GEOやSRAのページから、炎症刺激のRNA-seqデータとして使えるサンプルをどう選ぶのか」を考えます。

詳細: [08_public_data_sra_geo/README.md](08_public_data_sra_geo/README.md)

### 09 FASTQ and Read Quality Control

FASTQファイル、read quality、adapter、低品質readなど、count matrixの前段階を学びます。  
ここでは「シーケンサーから得られたreadは、遺伝子発現解析に使ってよい品質なのか」を考えます。

詳細: [09_fastq_quality_control/README.md](09_fastq_quality_control/README.md)

### 10 Alignment and Quantification

readをゲノムやトランスクリプトームに対応づけ、遺伝子ごとのcountに変換する流れを学びます。  
ここでは「短いreadを、どの遺伝子から来たRNA断片として数えるのか」を考えます。

詳細: [10_alignment_quantification/README.md](10_alignment_quantification/README.md)

### 11 Gene Annotation and IDs

遺伝子名、Ensembl ID、gene symbol、アノテーションの違いを学びます。  
ここでは「`ENSG00000141510` と `TP53` はどう対応し、解析ではどちらを使うべきか」を考えます。

詳細: [11_gene_annotation_ids/README.md](11_gene_annotation_ids/README.md)

### 12 Batch Effects and Reproducibility

条件差ではなく実験日や測定ロットで生じる差、つまりバッチ効果を学びます。  
ここでは「PCAでサンプルが分かれて見えるとき、それは炎症刺激の差なのか、実験日の差なのか」を考えます。

詳細: [12_batch_effects_reproducibility/README.md](12_batch_effects_reproducibility/README.md)

### 13 Pathway Enrichment

GOやpathway enrichmentを、遺伝子リストの偏りを読む手法として学びます。  
ここでは「上昇遺伝子群には、炎症応答に関係する遺伝子が偶然以上に多く含まれているのか」を考えます。

詳細: [13_pathway_enrichment_advanced/README.md](13_pathway_enrichment_advanced/README.md)

### 14 Reproducible Workflow

解析を他人が再実行できる形に整理するための、ファイル構成、記録、再現性を学びます。  
ここでは「半年後の自分や共同研究者が、同じ結果を再現できる解析になっているか」を考えます。

詳細: [14_reproducible_workflow/README.md](14_reproducible_workflow/README.md)
