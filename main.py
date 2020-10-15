from pydub import AudioSegment
import numpy as np
import matplotlib.pyplot as plt


audio = AudioSegment.from_wav("dasd.wav")
x = np.frombuffer(audio.raw_data, np.int16)[24:] / 2.**15

fig, ax = plt.subplots(1, 1, figsize=(8, 4))
t = np.linspace(0., len(x) / audio.frame_rate, len(x))
ax.plot(t, x, lw=1)
plt.show()
