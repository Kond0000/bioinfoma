from pathlib import Path
import os

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT / "data"
FIGURE_DIR = PROJECT_ROOT / "results" / "figures"
MPL_CONFIG_DIR = PROJECT_ROOT / ".matplotlib"
CACHE_DIR = PROJECT_ROOT / ".cache"

MPL_CONFIG_DIR.mkdir(parents=True, exist_ok=True)
CACHE_DIR.mkdir(parents=True, exist_ok=True)
os.environ.setdefault("MPLCONFIGDIR", str(MPL_CONFIG_DIR))
os.environ.setdefault("XDG_CACHE_HOME", str(CACHE_DIR))

import matplotlib.pyplot as plt


def main() -> None:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    FIGURE_DIR.mkdir(parents=True, exist_ok=True)

    counts = pd.DataFrame(
        {
            "gene": ["TP53", "MYC", "GAPDH", "ACTB", "IL6"],
            "control_1": [120, 300, 5000, 4200, 30],
            "control_2": [100, 280, 5100, 4000, 25],
            "treated_1": [300, 600, 5300, 4100, 200],
            "treated_2": [280, 650, 5200, 4300, 220],
        }
    ).set_index("gene")

    counts_path = DATA_DIR / "toy_counts.csv"
    counts.to_csv(counts_path)

    loaded_counts = pd.read_csv(counts_path, index_col=0)
    print("Count matrix:")
    print(loaded_counts)
    print()

    library_size = loaded_counts.sum(axis=0)
    print("Library size per sample:")
    print(library_size)
    print()

    treated_mean = loaded_counts[["treated_1", "treated_2"]].mean(axis=1)
    control_mean = loaded_counts[["control_1", "control_2"]].mean(axis=1)
    fold_change = (treated_mean + 1) / (control_mean + 1)
    top_gene = fold_change.sort_values(ascending=False).index[0]

    print(f"Treatedで増えていそうな遺伝子: {top_gene}")
    print(
        f"理由: control平均={control_mean[top_gene]:.1f}, "
        f"treated平均={treated_mean[top_gene]:.1f}, "
        f"fold change={fold_change[top_gene]:.2f}"
    )

    plt.figure(figsize=(6, 4))
    library_size.plot(kind="bar", color=["#4C78A8", "#4C78A8", "#F58518", "#F58518"])
    plt.ylabel("Total counts")
    plt.title("Library size per sample")
    plt.xticks(rotation=30, ha="right")
    plt.tight_layout()

    figure_path = FIGURE_DIR / "day1_library_size.png"
    plt.savefig(figure_path, dpi=150)
    print(f"\nSaved: {figure_path}")


if __name__ == "__main__":
    main()
