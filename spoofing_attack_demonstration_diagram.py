import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox


def add_icon(ax, image_path, position, label, zoom=0.15, text_offset=-0.12):
    """
    Places icon at given position and labels it below icon.
    :param ax: Matplotlib Axes object
    :param image_path: Path to icon image
    :param position: (x, y) coordinates to place icon
    :param label: Text label for icon
    :param zoom: Scaling factor for icon image
    :param text_offset: Vertical offset for label
    """
    img = plt.imread(image_path)
    imagebox = OffsetImage(img, zoom=zoom)  # Scaling icon
    ab = AnnotationBbox(imagebox, position, frameon=False)
    ax.add_artist(ab)

    # Placing text label below or above icon
    ax.text(position[0], position[1] + text_offset, label,
            ha='center', va='top', fontsize=12, fontweight='bold')


def add_arrow(ax, start, end, label=None, label_offset=(0, 0.06)):
    """
    Draws an arrow from start to end, optionally placing a label near the midpoint.
    """
    ax.annotate("",
                xy=end, xycoords='data',
                xytext=start, textcoords='data',
                arrowprops=dict(arrowstyle="->", lw=2, color='gray'))
    if label:
        mid_x = (start[0] + end[0]) / 2
        mid_y = (start[1] + end[1]) / 2
        ax.text(mid_x + label_offset[0], mid_y + label_offset[1],
                label, ha='center', va='center', fontsize=10, color='black')


# Figure and Axes
fig, ax = plt.subplots(figsize=(12, 4))
ax.axis('off')

# Node positions for horizontal flow (all at y=0.5)
positions = {
    "Attacker": (0.1, 0.5),
    "Spoofed IPs": (0.3, 0.5),
    "Intermediate Server": (0.5, 0.5),
    "Victim": (0.8, 0.5)
}

# Placing icons at each node with individualized zoom levels
# adjusted manually as .png files are different sizes
add_icon(ax, "images/attacker.png", positions["Attacker"], 
         label="Attacker", zoom=0.15)
add_icon(ax, "images/ip_icon.png", positions["Spoofed IPs"], 
         label="Spoofed IPs", zoom=0.15)
add_icon(ax, "images/server_icon.png", positions["Intermediate Server"], 
         label="Server", zoom=0.05)
add_icon(ax, "images/victim_laptop.png", positions["Victim"], 
         label="Victim", zoom=0.40)

# Arrows to show attack flow
add_arrow(ax, positions["Attacker"], positions["Spoofed IPs"], label="Spoofing IPs")
add_arrow(ax, positions["Spoofed IPs"], positions["Intermediate Server"], label="Malicious Traffic")
add_arrow(ax, positions["Intermediate Server"], positions["Victim"], label="DoS Flood")

# Title at top
ax.text(0.5, 0.9, "IP Spoofing DoS Attack",
        ha='center', va='center', fontsize=14, fontweight='bold')

# Saving to file
plt.savefig("IP_spoofing_DoS_attack.png", bbox_inches='tight')
plt.show()
