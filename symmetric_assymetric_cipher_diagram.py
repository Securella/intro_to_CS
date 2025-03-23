import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox


def add_icon(ax, image_path, position, label, zoom=0.15, text_offset=-0.12):
    # Placing icons and labels at correct positions.
    img = plt.imread(image_path)
    imagebox = OffsetImage(img, zoom=zoom)
    ab = AnnotationBbox(imagebox, position, frameon=False)
    ax.add_artist(ab)
    ax.text(position[0], position[1] + text_offset, label,
            ha='center', va='top', fontsize=10, fontweight='bold')


def add_arrow(ax, start, end, label="", label_offset=(0, 0.06)):
    # Drawing arrow from start to end, placing label near midpoint.
    ax.annotate(
        "",
        xy=end, xycoords='data',
        xytext=start, textcoords='data',
        arrowprops=dict(
            arrowstyle="->",
            lw=1.5,
            color='gray',
            alpha=0.7,
            linestyle="--"  # Dashed line
        )
    )
    if label:
        mid_x = (start[0] + end[0]) / 2
        mid_y = (start[1] + end[1]) / 2
        ax.text(mid_x + label_offset[0], mid_y + label_offset[1],
                label, ha='center', va='center', fontsize=10, color='black')


# Figure
fig, ax = plt.subplots(figsize=(14, 6))
ax.axis('off')

############################################
# Asymmetric Cipher Flow (Top Row)
############################################

# Positions for each step (y = 0.75)
asym_positions = {
    "Sender": (0.1, 0.75),
    "Plaintext": (0.25, 0.75),
    "Public Key": (0.4, 0.75),
    "Ciphertext": (0.55, 0.75),
    "Private Key": (0.7, 0.75),
    # Split "Decrypted Plaintext Data" into 2 lines
    "Decrypted Plaintext": (0.85, 0.75),
    "Recipient": (0.95, 0.75)
}

# Icons with labels
add_icon(ax, "images/sender.png", asym_positions["Sender"], "Sender")
add_icon(ax, "images/plaintext.png", asym_positions["Plaintext"], "Plaintext Data", zoom=0.20)
add_icon(ax, "images/public_key.png", asym_positions["Public Key"], "Public Key", zoom=0.05)
add_icon(ax, "images/ciphered.png", asym_positions["Ciphertext"], "Ciphered Data", zoom=0.20)
add_icon(ax, "images/private_key.png", asym_positions["Private Key"], "Private Key", zoom=0.20)
add_icon(ax, "images/decrypted.png", asym_positions["Decrypted Plaintext"], "Decrypted \nPlaintext\nData", zoom=0.10)
add_icon(ax, "images/recipient.png", asym_positions["Recipient"], "Recipient", zoom=0.20)

# Arrows (left to right)
asym_flow = [
    ("Sender", "Plaintext", "Encrypt Input"),
    ("Plaintext", "Public Key", "Use Public Key"),
    ("Public Key", "Ciphertext", ""),
    ("Ciphertext", "Private Key", "Use Private Key"),
    ("Private Key", "Decrypted Plaintext", ""),
    ("Decrypted Plaintext", "Recipient", "Deliver")
]

for start_label, end_label, arrow_text in asym_flow:
    add_arrow(ax, asym_positions[start_label], asym_positions[end_label], label=arrow_text)

# Title for asymmetric flow
ax.text(0.5, 0.88, "Asymmetric Cipher Flow", ha='center', va='center',
        fontsize=14, fontweight='bold')

############################################
# Symmetric Cipher Flow (Bottom Row)
############################################

# Positions for each step (y = 0.35)
sym_positions = {
    "Sender": (0.1, 0.35),
    "Plaintext": (0.25, 0.35),
    "Shared Key Enc": (0.4, 0.35),
    "Ciphertext": (0.55, 0.35),
    # Splitting "Shared Key (Decryption)" into 2 lines
    "Shared Key Dec": (0.7, 0.35),
    # Splitting "Decrypted Plaintext Data" into 2 lines
    "Decrypted Plaintext": (0.85, 0.35),
    "Recipient": (0.95, 0.35)
}

# Icons with labels
add_icon(ax, "images/sender.png", sym_positions["Sender"], "Sender")
add_icon(ax, "images/plaintext.png", sym_positions["Plaintext"], "Plaintext Data", zoom=0.20)
add_icon(ax, "images/shared_key.png", sym_positions["Shared Key Enc"], "Shared Key \n(Encryption)", zoom=0.05)
add_icon(ax, "images/ciphered.png", sym_positions["Ciphertext"], "Ciphered Data", zoom=0.20)
add_icon(ax, "images/shared_key.png", sym_positions["Shared Key Dec"], "Shared Key\n(Decryption)", zoom=0.05)
add_icon(ax, "images/decrypted.png", sym_positions["Decrypted Plaintext"], "Decrypted \nPlaintext\nData", zoom=0.10)
add_icon(ax, "images/recipient.png", sym_positions["Recipient"], "Recipient", zoom=0.20)

# Draw arrows (left to right)
sym_flow = [
    ("Sender", "Plaintext", "Encrypt Input"),
    ("Plaintext", "Shared Key Enc", "Use Shared Key"),
    ("Shared Key Enc", "Ciphertext", ""),
    ("Ciphertext", "Shared Key Dec", "Use Shared Key"),
    ("Shared Key Dec", "Decrypted Plaintext", ""),
    ("Decrypted Plaintext", "Recipient", "Deliver")
]

for start_label, end_label, arrow_text in sym_flow:
    add_arrow(ax, sym_positions[start_label], sym_positions[end_label], label=arrow_text)

# Title for symmetric flow
ax.text(0.5, 0.48, "Symmetric Cipher Flow", ha='center', va='center',
        fontsize=14, fontweight='bold')

# Saving & showing
plt.savefig("sym_asym_cipher_flow_diagram.png", bbox_inches='tight')
plt.show()
