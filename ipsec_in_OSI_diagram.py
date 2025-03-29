import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from matplotlib.offsetbox import OffsetImage, AnnotationBbox


def add_layer(ax, layer_name, color, center_x, center_y, width=0.4, height=0.08):
    # Rectangle for OSI layer with text in center.
    bottom_left_x = center_x - width / 2
    bottom_left_y = center_y - height / 2

    rect = Rectangle(
        (bottom_left_x, bottom_left_y),
        width, height,
        linewidth=1.5, edgecolor='black', facecolor=color
    )
    ax.add_patch(rect)

    ax.text(
        center_x, center_y, layer_name,
        ha='center', va='center', fontsize=11, fontweight='bold', color='black'
    )


def add_icon(ax, image_path, position, zoom=0.12):
    # IPSec icon at right position (x, y).
    img = plt.imread(image_path)
    imagebox = OffsetImage(img, zoom=zoom)
    ab = AnnotationBbox(imagebox, position, frameon=False)
    ax.add_artist(ab)


def add_curved_arrow(ax, start, end, label=None, curvature=-0.3):
    # Curved arrow from start to end. Optionally places label near midpoint.
    # 'curvature' parameter controls outward/inward arc
    ax.annotate(
        "",
        xy=end, xycoords='data',
        xytext=start, textcoords='data',
        arrowprops=dict(
            arrowstyle="->",
            lw=2,
            color='gray',
            connectionstyle=f"arc3,rad={curvature}"
        )
    )
    if label:
        mid_x = (start[0] + end[0]) / 2
        mid_y = (start[1] + end[1]) / 2
        ax.text(mid_x, mid_y + 0.02, label, ha='center', va='center', fontsize=10)


# Creating figure and axis
fig, ax = plt.subplots(figsize=(4, 8))
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')

# Defining vertical positions for each layer (bottom to top)
positions = {
    "Physical": 0.15,
    "Data Link": 0.27,
    "Network": 0.39,
    "Transport": 0.51,
    "Session": 0.63,
    "Presentation": 0.75,
    "Application": 0.87
}

# Adding layers (colorful)
add_layer(ax, "1 Physical Layer", "turquoise", 0.3, positions["Physical"])
add_layer(ax, "2 Data Link Layer", "turquoise", 0.3, positions["Data Link"])
add_layer(ax, "3 Network Layer", "plum", 0.3, positions["Network"])
add_layer(ax, "4 Transport Layer", "orange", 0.3, positions["Transport"])
add_layer(ax, "5 Session Layer", "lightgreen", 0.3, positions["Session"])
add_layer(ax, "6 Presentation Layer", "lightgreen", 0.3, positions["Presentation"])
add_layer(ax, "7 Application Layer", "lightgreen", 0.3, positions["Application"])

# Locating IPSec icon (right of Network Layer)
ipsec_icon_center = (0.7, positions["Network"])
add_icon(ax, "images/ipsec_icon.png", ipsec_icon_center, zoom=0.15)

# Arrow connecting edge of icon. Adjust offset_x if needed.
offset_x = 0.03
ipsec_icon_edge = (ipsec_icon_center[0] - offset_x, ipsec_icon_center[1])

# Right edge of Network Layer (width=0.4 => half=0.2, center_x=0.3 => right_edge=0.5)
network_right_edge = (0.5, positions["Network"])

# Curved arrow from Network Layer's right edge to icon's left edge
add_curved_arrow(
    ax, network_right_edge, ipsec_icon_edge,
    label="IPSec at Layer 3",
    curvature=-0.3
)

# Title
ax.text(0.5, 0.95, "OSI Model with IPSec",
        ha='center', va='center', fontsize=14, fontweight='bold')

# Saving and showing
plt.savefig("osi_model_ipsec.png", bbox_inches='tight')
plt.show()
