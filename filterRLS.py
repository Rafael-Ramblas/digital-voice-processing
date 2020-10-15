from pydub import AudioSegment
import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import write


audio = AudioSegment.from_wav("voz.wav")
samples = np.frombuffer(audio.raw_data, np.int64)/2**63
frameRate = audio.frame_rate
time = np.linspace(0., len(samples) / frameRate, len(samples))

filteredSamples = []
alfa = -0.99

# y[n] = alfa*y[n-1] +x[n]

for index in range(len(samples)):
    if index == 0:
        filteredSamples.append(samples[index])
    else:
        filteredSamples.append((alfa*filteredSamples[index-1])+samples[index])

fig, ax = plt.subplots(1, 1, figsize=(8, 4))
ax.plot(time, samples, lw=1, label="Original")
ax.plot(time, filteredSamples, lw=1, alpha=.7,
        label="Filtrado com alfa " + str(alfa))
leg = ax.legend(loc='upper right')
ax.set_ylim(-1, 1)
plt.show()

# write('rls-099.wav', frameRate, np.array(filteredSamples))
