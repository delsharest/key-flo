import numpy as np
import matplotlib.pyplot as plt
import os

def generate_flower(filename, stage):
    # Parameter bunga
    theta = np.linspace(0, 2 * np.pi, 100)
    
    # Variasi bentuk bunga berdasarkan tahap
    r = 1 + 0.5 * np.sin(5 * theta) * (stage / 10)  # Mengubah jumlah tahap menjadi 10
    color = plt.cm.viridis(stage / 10)  # Menggunakan colormap untuk variasi warna

    # Gambar bunga
    plt.figure(figsize=(6, 6))
    plt.polar(theta, r, color=color, linewidth=2)
    plt.fill(theta, r, color=color, alpha=0.5)
    plt.title("flo")
    plt.axis('off')  # Matikan sumbu
    plt.savefig(filename, bbox_inches='tight')
    plt.close()

# Buat folder untuk menyimpan gambar jika belum ada
if not os.path.exists('static/flowers'):
    os.makedirs('static/flowers')

# Menghasilkan gambar untuk setiap tahap
for stage in range(1, 11):  # 10 tahap
    generate_flower(f'static/flowers/flower_stage_{stage}.png', stage)