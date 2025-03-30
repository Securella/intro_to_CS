import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox


def add_icon(ax, image_path, position, label, zoom=0.15, text_offset=-0.12):
    # Icon at right position and label below
    img = plt.imread(image_path)
    imagebox = OffsetImage(img, zoom=zoom)
    ab = AnnotationBbox(imagebox, position, frameon=False)
    ax.add_artist(ab)
    ax.text(position[0], position[1] + text_offset, label,
            ha='center', va='top', fontsize=10, fontweight='bold')


def add_arrow(ax, start, end, label=None, label_offset=(0, 0.06)):
    # Arrow from start to end and (optional) label near midpoint
    ax.annotate("",
                xy=end, xycoords='data',
                xytext=start, textcoords='data',
                arrowprops=dict(arrowstyle="->", lw=2, color='gray'))
    if label:
        mid_x = (start[0] + end[0]) / 2
        mid_y = (start[1] + end[1]) / 2
        ax.text(mid_x + label_offset[0], mid_y + label_offset[1],
                label, ha='center', va='center', fontsize=10, color='black')


# Figure and axis
fig, ax = plt.subplots(figsize=(10, 3))
ax.axis("off")

# Positions for each element along horizontal line
positions = {
    "User Browser": (0.1, 0.5),
    "Vulnerable Webpage": (0.4, 0.5),
    "Injected Script": (0.7, 0.5),
    "Attacker Server": (1.0, 0.5)
}

# Defined offset for arrows so they don't touch icons
arrow_offset = 0.12

# Icons with labels
add_icon(ax, "images/user_browser.png", positions["User Browser"], "User Browser", zoom=0.15)
add_icon(ax, "images/vulnerable_webpage.png", positions["Vulnerable Webpage"], "Vulnerable Webpage", zoom=0.08)
add_icon(ax, "images/injected_script.png", positions["Injected Script"], "Injected Script", zoom=0.05)
add_icon(ax, "images/attacker_server.png", positions["Attacker Server"], "Attacker Server", zoom=0.15)

# Arrows between elements with labels, applying arrow_offset to shorten them
add_arrow(ax,
          (positions["User Browser"][0] + arrow_offset, positions["User Browser"][1]),
          (positions["Vulnerable Webpage"][0] - arrow_offset, positions["Vulnerable Webpage"][1]),
          label="Cookie Data")

add_arrow(ax,
          (positions["Vulnerable Webpage"][0] + arrow_offset, positions["Vulnerable Webpage"][1]),
          (positions["Injected Script"][0] - arrow_offset, positions["Injected Script"][1]),
          label="Injected Code")

add_arrow(ax,
          (positions["Injected Script"][0] + arrow_offset, positions["Injected Script"][1]),
          (positions["Attacker Server"][0] - arrow_offset, positions["Attacker Server"][1]),
          label="Stolen Cookie")

# Title
plt.title("XSS Cookie Theft Flow", fontsize=14, pad=20)

# Saving and showing
plt.savefig("xss_cookie_theft_flow.png", bbox_inches='tight')
plt.show()
