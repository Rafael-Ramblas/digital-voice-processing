from pydub import AudioSegment
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sg
from scipy.io.wavfile import write


audio = AudioSegment.from_wav("voz.wav")
frameRate = audio.frame_rate
samples = np.frombuffer(audio.raw_data, np.int64)/2**63
time = np.linspace(
    0., len(samples) / frameRate, len(samples))

audioSliced = audio[2000:3000]
samplesSliced = np.frombuffer(audioSliced.raw_data, np.int64)/2**63
timeSliced = np.linspace(
    0., len(samplesSliced) / frameRate, len(samplesSliced))


filteredSamples = sg.correlate(
    samples, samplesSliced, mode='full', method='direct')
filteredTime = np.linspace(
    0., len(filteredSamples) / frameRate, len(filteredSamples))


fig, axs = plt.subplots(3, 1, figsize=(8, 4))
axs[0].plot(time, samples, lw=1)
axs[1].plot(timeSliced, samplesSliced, lw=1)
axs[2].plot(filteredTime, filteredSamples, lw=1)

plt.show()


# write('rls.wav', frameRate, filteredSamples)
