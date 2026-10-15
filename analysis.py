import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

P_CUTOFF = 0.01

results = pd.read_csv("results/de_genes.csv")
hits = results[results["p_value"] < P_CUTOFF]
print(f"{len(hits)} genes pass p < {P_CUTOFF}")

points = results.sample(min(len(results), 5000), random_state=1)
plt.scatter(points["log2_fold_change"], -np.log10(points["p_value"]), s=4)
plt.savefig("figures/volcano.png", dpi=300)
