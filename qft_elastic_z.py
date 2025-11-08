import numpy as np
import matplotlib.pyplot as plt

# === PARÁMETROS ===
L = 32
dx = 1.0
m = 0.1
k = 1.0
eta = 0.9
t_recomb = 1e-3
t_start = 1e-6
t_zoom = 2e-3     # Zoom hasta poco después de recombinación
t_late = 2.0      # Hasta hoy
Nt_zoom = 5000
Nt_late = 5000

# === RED ===
phi = np.zeros((L, L, L))
phi_dot = np.zeros_like(phi)

def J(t):
    if t < t_start or t >= t_recomb:
        return 0.0
    return eta * 1000 * (t_recomb / t)**1.7

def laplacian(phi):
    return (np.roll(phi, 1, 0) + np.roll(phi, -1, 0) +
            np.roll(phi, 1, 1) + np.roll(phi, -1, 1) +
            np.roll(phi, 1, 2) + np.roll(phi, -1, 2) - 6*phi) / dx**2

# === FASE 1: ZOOM EN RECOMBINACIÓN ===
t = t_start
dt = (t_zoom - t_start) / Nt_zoom
E_zoom = []; t_zoom_list = []

for _ in range(Nt_zoom):
    phi_dot += dt * (-k * laplacian(phi) - m**2 * phi + J(t))
    phi += dt * phi_dot
    E = 0.5 * m**2 * np.mean(phi**2)
    E_zoom.append(E)
    t_zoom_list.append(t)
    t += dt

# === FASE 2: HASTA HOY (dt más grande) ===
dt_late = (t_late - t_zoom) / Nt_late
E_late = [E_zoom[-1]]; t_late_list = [t_zoom_list[-1]]

for _ in range(Nt_late):
    phi_dot += dt_late * (-k * laplacian(phi) - m**2 * phi)
    phi += dt_late * phi_dot
    E = 0.5 * m**2 * np.mean(phi**2)
    E_late.append(E)
    t_late_list.append(t)
    t += dt_late

# === GRÁFICAS ===
plt.figure(figsize=(14, 6))

plt.subplot(1, 2, 1)
plt.plot(t_zoom_list, E_zoom, 'b-', linewidth=2, label='Crecimiento elástico')
plt.plot(t_late_list, E_late, 'r--', linewidth=2, label='Congelado')
plt.axvline(t_recomb, color='orange', ls='--', label='Recombinación')
plt.xscale('log')
plt.xlabel('Tiempo (log)')
plt.ylabel('E(t)')
plt.title('Zoom: Memoria Cuántica del Espacio-Tiempo')
plt.legend()
plt.grid(alpha=0.3)

plt.subplot(1, 2, 2)
plt.imshow(phi[L//2, :, :], cmap='plasma', extent=[0, L, 0, L])
plt.colorbar(label='φ')
plt.title('Estado Coherente Final (t = 2.0)')

plt.tight_layout()
plt.show()

print(f"\nE(final) = {E_late[-1]:.6f}")