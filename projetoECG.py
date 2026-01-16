import matplotlib.pyplot as plt
import numpy as np
import wfdb 

#Obtendo dados do MIT-BIH Noise Stress Test
print("Baixando registro 118e00...")

record = wfdb.rdrecord('118e00', sampfrom=0, sampto=5400, pn_dir='nstdb')

sinal_ruidoso = record.p_signal[:, 0] 
fs = record.fs
t = np.arange(len(sinal_ruidoso)) / fs  

#O FILTRO
M = 300 
janela = np.ones(M) / M
tendencia = np.convolve(sinal_ruidoso, janela, mode='same')
sinal_recuperado = sinal_ruidoso - tendencia

# Plotagem dos Gráficos
plt.rcParams.update(plt.rcParamsDefault)
plt.style.use('dark_background') 

def configurar_grid(ax):
    ax.set_facecolor('black')
    ax.grid(True, which='both', color='#004400', linestyle='-', linewidth=0.8)
    ax.minorticks_on()
    ax.grid(True, which='minor', color='#002200', linestyle=':', linewidth=0.5)

fig1 = plt.figure(num=1, figsize=(10, 6))
fig1.canvas.manager.set_window_title('Figura 1 - O Problema')
fig1.patch.set_facecolor('black')

ax1 = plt.gca() 
plt.title("Sinal Ruidoso", fontsize=14, fontfamily='monospace', color='#00FF00', loc='left')
plt.plot(t, sinal_ruidoso, color='yellow', linewidth=1.5, label='Sinal Bruto')
plt.plot(t, tendencia, color='white', linestyle='--', linewidth=2, alpha=0.9, label='Baseline Wander')
configurar_grid(ax1)
plt.legend(facecolor='black', edgecolor='#00FF00', labelcolor='white')
plt.xlabel("TIME (s)", color='#00FF00', fontfamily='monospace')
plt.tight_layout()

fig2 = plt.figure(num=2, figsize=(10, 6))
fig2.canvas.manager.set_window_title('Figura 2 - A Solução')
fig2.patch.set_facecolor('black')

ax2 = plt.gca()
plt.title("Sinal Limpo", fontsize=14, fontfamily='monospace', color='#00FF00', loc='left')
plt.plot(t, sinal_recuperado, color='#00FF00', linewidth=2, label='Sinal Processado')
configurar_grid(ax2)
plt.legend(facecolor='black', edgecolor='#00FF00', labelcolor='white')
plt.xlabel("TIME (s)", color='#00FF00', fontfamily='monospace')
plt.tight_layout()

fig3 = plt.figure(num=3, figsize=(16, 9))
fig3.canvas.manager.set_window_title('Figura 3 - Comparativo Final')
fig3.patch.set_facecolor('black')


ax3_top = plt.subplot(2, 1, 1)
plt.title("Comparativo sinal ruidoso", fontsize=12, fontfamily='monospace', color='#00FF00', loc='left')
plt.plot(t, sinal_ruidoso, color='yellow', linewidth=1.5, label='Sinal Bruto')
plt.plot(t, tendencia, color='white', linestyle='--', linewidth=2, alpha=0.9, label='Baseline Wander')
configurar_grid(ax3_top)
plt.legend(facecolor='black', edgecolor='#00FF00', labelcolor='white', loc='upper right')


ax3_bottom = plt.subplot(2, 1, 2)
plt.title("Comparativo sinal limpo", fontsize=12, fontfamily='monospace', color='#00FF00', loc='left')
plt.plot(t, sinal_recuperado, color='#00FF00', linewidth=2, label='Sinal Processado')
configurar_grid(ax3_bottom)
plt.xlabel("TIME (s)", color='#00FF00', fontfamily='monospace')

plt.tight_layout()
plt.show()