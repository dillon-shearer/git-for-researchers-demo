import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

P_CUTOFF = 0.05

results = pd.read_csv("results/de_genes.csv")
hits = results[results["p_value"] < P_CUTOFF]
print(f"{len(hits)} genes pass p < {P_CUTOFF}")

plt.scatter(results["log2_fold_change"], -np.log10(results["p_value"]), s=4)
plt.savefig("figures/volcano.png", dpi=300)
