import matplotlib.pyplot as plt

labels = ['Confidentiality', 'Integrity', 'Availability']
threats = [
    "Phishing\nSpyware",
    "Ransomware\nFile-Tampering",
    "DDoS\nSystem Crash"
]

fig, ax = plt.subplots(figsize=(6,4))
ax.axis('off')

# Plot CIA triad as 3 connected boxes
for i, (label, threat) in enumerate(zip(labels, threats)):
    ax.text(0.5, 0.8-0.3*i, f"{label}\n---\n{threat}", 
            fontsize=12, ha='center', bbox=dict(facecolor='lightblue', edgecolor='black'))

plt.title("CIA Triad Threat Examples", fontsize=14)
plt.show()
