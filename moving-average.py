from pydub import AudioSegment
import numpy as np
import matplotlib.pyplot as plt


audio = AudioSegment.from_wav("voz.wav")
samples = np.frombuffer(audio.raw_data, np.int64)/2**63
frameRate = audio.frame_rate
time = np.linspace(0., len(samples) / frameRate, len(samples))

filteredSamples = []
M = 1000

# y[n] = y[n-1] + (x[n] - x[n-M])/M

for index in range(len(samples)):
    if index == 0:
        filteredSamples.append(samples[index]/M)
    elif index < M:
        filteredSamples.append(filteredSamples[index-1] + samples[index]/M)
    else:
        filteredSamples.append(
            filteredSamples[index-1] + (samples[index] - samples[index-M])/M)

fig, ax = plt.subplots(1, 1, figsize=(8, 4))
ax.plot(time, samples, lw=1, label="Original")
ax.plot(time, filteredSamples, lw=1, alpha=.7,
        label="Filtrado com M " + str(M))
leg = ax.legend(loc='upper right')
ax.set_ylim(-1, 1)
plt.show()
