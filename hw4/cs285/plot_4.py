import numpy as np
from matplotlib import pyplot as plt

a = np.loadtxt("../run_logs/run_mb_q5_reacher_horizon5_reacher-cs285-v0_02-11-2019_07-29-38-tag-Eval_AverageReturn.csv", skiprows=1, delimiter=",")
plt.plot(a[:,1], a[:,2], label="Horizon=5")
a = np.loadtxt("../run_logs/run_mb_q5_reacher_horizon15_reacher-cs285-v0_02-11-2019_07-29-50-tag-Eval_AverageReturn.csv", skiprows=1, delimiter=",")
plt.plot(a[:,1], a[:,2], label="Horizon=15")
a = np.loadtxt("../run_logs/run_mb_q5_reacher_horizon30_reacher-cs285-v0_02-11-2019_07-30-06-tag-Eval_AverageReturn.csv", skiprows=1, delimiter=",")
plt.plot(a[:,1], a[:,2], label="Horizon=30")
plt.title("Reacher - Horizon")
plt.legend()
plt.savefig("q41.png")
plt.close()

a = np.loadtxt("../run_logs/run_mb_q5_reacher_numseq100_reacher-cs285-v0_02-11-2019_07-30-19-tag-Eval_AverageReturn.csv", skiprows=1, delimiter=",")
plt.plot(a[:,1], a[:,2], label="Action seq=100")
a = np.loadtxt("../run_logs/run_mb_q5_reacher_numseq1000_reacher-cs285-v0_02-11-2019_07-30-32-tag-Eval_AverageReturn.csv", skiprows=1, delimiter=",")
plt.plot(a[:,1], a[:,2], label="Action seq=1000")
plt.title("Reacher - Num. Action Sequences")
plt.legend()
plt.savefig("q42.png")
plt.close()

a = np.loadtxt("../run_logs/run_mb_q5_reacher_ensemble1_reacher-cs285-v0_02-11-2019_19-23-08-tag-Eval_AverageReturn.csv", skiprows=1, delimiter=",")
plt.plot(a[:,1], a[:,2], label="Ensemble=1")
a = np.loadtxt("../run_logs/run_mb_q5_reacher_ensemble3_reacher-cs285-v0_02-11-2019_19-23-14-tag-Eval_AverageReturn.csv", skiprows=1, delimiter=",")
plt.plot(a[:,1], a[:,2], label="Ensemble=3")
a = np.loadtxt("../run_logs/run_mb_q5_reacher_ensemble5_reacher-cs285-v0_02-11-2019_19-23-20-tag-Eval_AverageReturn.csv", skiprows=1, delimiter=",")
plt.plot(a[:,1], a[:,2], label="Ensemble=5")
plt.title("Reacher - Num. Model Ensembles")
plt.legend()
plt.savefig("q43.png")
plt.close()