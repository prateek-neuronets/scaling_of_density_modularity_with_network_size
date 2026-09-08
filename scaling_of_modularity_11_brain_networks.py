import matplotlib.pyplot as plt

# Requires dicts: of network names mapping to networkx graph objects representing the brain networks; of Q-raw values of all networks; of Q-z; of Q-raw - Q-z; std of Q-null. 

def plot_size_modularity(all_brain_networks, all_brain_networks_raw, all_brain_networks_zscore):
    """Plot raw modularity and modularity Z-score against network size."""

    # Collect metrics
    sizes = []
    Qs_raw = []
    Q_z_scores = []

    for name, G in all_brain_networks.items():
        sizes.append(G.number_of_nodes())
        Qs_raw.append(all_brain_networks_raw[name])
        Q_z_scores.append(all_brain_networks_zscore[name])
        
    # Create side-by-side subplots
    fig, axes = plt.subplots(1, 2, figsize=(10, 4), dpi=300)

    # Raw modularity plot
    axes[0].scatter(sizes, Qs_raw, alpha=0.7)
        
    axes[0].set_xlabel("$N$", fontsize=20)
    axes[0].set_ylabel("$Q_{raw}$", fontsize=20)
    axes[0].spines['top'].set_visible(False)
    axes[0].spines['right'].set_visible(False)

    axes[0].tick_params(axis='both', which='both', labelsize=18)

    # Z-score plot
    axes[1].scatter(sizes, Q_z_scores, alpha=0.7)

    axes[1].set_xlabel("$N$", fontsize=20)
    axes[1].set_ylabel("$Q_{z}$", fontsize=20)
    axes[1].spines['top'].set_visible(False)
    axes[1].spines['right'].set_visible(False)

    axes[0].set_xscale('log') 
    axes[0].set_yscale('log') 
    axes[1].set_xscale('log') 
    axes[1].set_yscale('log')

    axes[1].tick_params(axis='both', which='both', labelsize=18)

    plt.tight_layout()
    plt.show()



def plot_size_modularity_difference(all_brain_networks, q_raw_mu_differences, stds):
    """Plot modularity difference and null-model standard deviation against network size."""

    # Collect metrics
    sizes = []
    Q_diff = []   # Q_emp - mu
    std_vals = [] # sigma_null

    for name, G in all_brain_networks.items():
        sizes.append(G.number_of_nodes())
        Q_diff.append(q_raw_mu_differences[name])
        std_vals.append(stds[name])

    # Create side-by-side subplots
    fig, axes = plt.subplots(1, 2, figsize=(10, 4), dpi=300)

    # Q - mu plot
    axes[0].scatter(sizes, Q_diff, alpha=0.7)
    axes[0].set_xlabel("$N$", fontsize=20)
    axes[0].set_ylabel("$Q - \\langle Q_{null} \\rangle$", fontsize=20)
    axes[0].spines['top'].set_visible(False)
    axes[0].spines['right'].set_visible(False)
    axes[0].tick_params(axis='both', which='both', labelsize=18)

    # std plot
    axes[1].scatter(sizes, std_vals, alpha=0.7)
    axes[1].set_xlabel("$N$", fontsize=20)
    axes[1].set_ylabel("$\\sigma_{null}$", fontsize=20)
    axes[1].spines['top'].set_visible(False)
    axes[1].spines['right'].set_visible(False)
    axes[1].tick_params(axis='both', which='both', labelsize=18)

    # Log scales
    axes[0].set_xscale('log')
    axes[0].set_yscale('log')
    axes[1].set_xscale('log')
    axes[1].set_yscale('log')

    plt.tight_layout()
    plt.show()