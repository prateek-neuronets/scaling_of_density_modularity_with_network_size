import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator


def plot_size_density(all_brain_networks):

    """Plot network size against density for a collection of brain networks.

        Parameters
        ----------
        all_brain_networks : dict
        Dictionary of NetworkX graph objects."""

    # Collect metrics
    sizes = []
    densities = []

    for name, G in all_brain_networks.items():
        sizes.append(G.number_of_nodes())
        densities.append(nx.density(G))

    # Create figure with two subplots
    fig, axes = plt.subplots(1, 2, figsize=(10, 4), dpi=500)

    for ax in axes:
        ax.scatter(
            sizes,
            densities,
            s=40,
            alpha=0.3,
        )

        # Labels and styling
        ax.set_xlabel("$N$", fontsize=20)
        ax.set_ylabel("$d$", fontsize=20)

        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)

        ax.xaxis.set_major_locator(MaxNLocator(nbins=4))
        ax.tick_params(axis='both', which='major', labelsize=18)

    # Apply scales
    axes[0].set_xscale("log")        # Semi-log (y only)
    axes[1].set_xscale("log")        # Log-log
    axes[1].set_yscale("log")

    plt.tight_layout()
    plt.show()