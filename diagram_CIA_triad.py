import matplotlib.pyplot as plt

# Triangle vertices (for drawing edges):
C_vertex = (0.5, 0.65)   # Top vertex
I_vertex = (0.15, 0.2)   # Bottom-left vertex
A_vertex = (0.85, 0.2)   # Bottom-right vertex

# Offsets for threat text boxes:
C_box = (0.5, 0.58)      # Slightly below top vertex
I_box = (0.12, 0.17)     # Slightly offset from bottom-left vertex
A_box = (0.88, 0.17)     # Slightly offset from bottom-right vertex

# Lists of threats:
threats = {
    'C': (
        "Phishing\n"
        "Network Snooping\n"
        "Data Leakage\n"
        "Insider Threat\n"
        "Credential Theft\n"
        "Unauthorized Access\n"
        "Eavesdropping\n"
        "Data Breach"
    ),
    'I': (
        "Man-in-the-Middle Attack\n"
        "Unauthorized Modification\n"
        "Malware Injection\n"
        "Data Corruption\n"
        "Data Forgery\n"
        "Ransomware\n"
        "File-Tampering Virus"
    ),
    'A': (
        "Denial of Service\n"
        "Distributed Denial of Service\n"
        "Network Congestion\n"
        "Ransomware\n"
        "System Crash\n"
        "Hardware Exploit"
    )
}

# Create figure and remove axes
fig, ax = plt.subplots(figsize=(12, 8))
ax.axis('off')


def midpoint(p1, p2):
    """Compute midpoint between two points."""
    return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)


# Triangle
xs = [C_vertex[0], I_vertex[0], A_vertex[0], C_vertex[0]]
ys = [C_vertex[1], I_vertex[1], A_vertex[1], C_vertex[1]]
ax.plot(xs, ys, color='black', linewidth=2)

# Add text boxes with threats at each offset position
ax.text(
    C_box[0], C_box[1], threats['C'],
    ha='center', va='center', fontsize=9,
    bbox=dict(facecolor='lightgreen', edgecolor='black', boxstyle='round,pad=0.5')
)
ax.text(
    I_box[0], I_box[1], threats['I'],
    ha='center', va='center', fontsize=9,
    bbox=dict(facecolor='lightpink', edgecolor='black', boxstyle='round,pad=0.5')
)
ax.text(
    A_box[0], A_box[1], threats['A'],
    ha='center', va='center', fontsize=9,
    bbox=dict(facecolor='lightblue', edgecolor='black', boxstyle='round,pad=0.5')
)

# Label each edge with CIA categories
mid_CI = midpoint(C_vertex, I_vertex)
mid_IA = midpoint(I_vertex, A_vertex)
mid_AC = midpoint(A_vertex, C_vertex)
vertical_offset = 0.02

ax.text(
    mid_CI[0], mid_CI[1] + vertical_offset, "Integrity",
    ha='center', va='center', fontsize=12, color='darkred', fontweight='bold'
)
ax.text(
    mid_IA[0], mid_IA[1] + vertical_offset, "Availability",
    ha='center', va='center', fontsize=12, color='darkblue', fontweight='bold'
)
ax.text(
    mid_AC[0], mid_AC[1] + vertical_offset, "Confidentiality",
    ha='center', va='center', fontsize=12, color='darkgreen', fontweight='bold'
)

# Place diagram label inside triangle (slightly above centroid)
# Exact centroid is at ( (0.5+0.15+0.85)/3, (0.65+0.2+0.2)/3 ) = (0.5, 0.35).
# Text a bit higher at y=0.4 to avoid overlapping with bottom boxes.
ax.text(
    0.5, 0.4, "CIA Triad Threats",
    ha='center', va='center', fontsize=16, color='black', fontweight='bold',
    bbox=dict(facecolor='white', alpha=0.7, edgecolor='black', boxstyle='round,pad=0.5')
)

# Saving to file
plt.savefig("cia_triad_threats.png", bbox_inches='tight')

# Display diagram
plt.show()
