# Topics Overview

このディレクトリは、RNA-seq教材の各章をまとめた目次です。  
各章は独立したトピックではなく、1つのケーススタディを段階的に解くための章として並んでいます。

## ケーススタディ

`炎症刺激を受けた細胞で、どの遺伝子群と生物学的経路が変化したのかを RNA-seq で明らかにする`

この問いに答えるために、データの読み方、正規化、可視化、差次的発現解析、機能解釈、ポートフォリオ化を順番に学びます。

## 読み方

1. 番号の若いトピックから順に進める
2. 各 `README.md` で、その章の問いと背景を読む
3. トップREADMEの Colab リンクからノートブックを開く
4. 図や表を見て、その章で何を判断できるようになったかを確認する

## トピック一覧

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
