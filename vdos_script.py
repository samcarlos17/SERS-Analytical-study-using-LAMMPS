import numpy as np
import matplotlib.pyplot as plt

# Load VACF data
time, vacf = np.loadtxt("C:\lammps\LAMMPS 64-bit 27Jun2024\projects\raman silver icosahedra\vacf_output.dat", unpack=True)

# Perform Fourier Transform
freq = np.fft.rfftfreq(len(vacf), d=(time[1] - time[0]))  # Frequency domain
spectrum = np.abs(np.fft.rfft(vacf))  # Power spectrum

# Plot
plt.plot(freq, spectrum)
plt.xlabel('Frequency (THz)')
plt.ylabel('Intensity')
plt.title('Vibrational Density of States')
plt.show()
