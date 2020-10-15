from pydub import AudioSegment
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sg
from scipy.io.wavfile import write


audio = AudioSegment.from_wav("dasd.wav")
samples = np.frombuffer(audio.raw_data, np.int32)/2**28
frameRate = audio.frame_rate
time = np.linspace(0., len(samples) / frameRate, len(samples))

fig, ax = plt.subplots(1, 1, figsize=(8, 4))
t = np.linspace(0., len(samples) / audio.frame_rate, len(samples))

filteredSamples = sg.savgol_filter(samples, 9, 1)

fig, ax = plt.subplots(1, 1, figsize=(8, 4))
ax.plot(time, samples, lw=1)
ax.plot(time, filteredSamples, lw=1)
# plt.show()

write('samples.wav', frameRate, filteredSamples)
