import matplotlib.pyplot as plt
import matplotlib.patches as patches


def draw_ipsec_logo_with_arrows(filename="ipsec_icon.png"):

    fig, ax = plt.subplots(figsize=(6, 6))

    # Dark blue circle background
    circle = patches.Circle((0.5, 0.5), 0.45, facecolor="#283747", edgecolor="none")
    ax.add_patch(circle)

    # White cylinder shape
    cylinder = patches.Ellipse((0.5, 0.5), 0.6, 0.2, facecolor="white", edgecolor="none")
    ax.add_patch(cylinder)

    # IPSec text
    ax.text(0.5, 0.5, "IPSec", ha="center", va="center", fontsize=30, fontweight="bold")

    # Left arrow (from cylinder)
    ax.arrow(0.2, 0.5, -0.1, 0, head_width=0.05, head_length=0.05, fc='white', ec='white')

    # Right arrow (from cylinder)
    ax.arrow(0.8, 0.5, 0.1, 0, head_width=0.05, head_length=0.05, fc='white', ec='white')

    # Limits and no axes
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    # Saving
    plt.savefig(filename, bbox_inches="tight", pad_inches=0.1)
    plt.show()


if __name__ == "__main__":
    draw_ipsec_logo_with_arrows()
