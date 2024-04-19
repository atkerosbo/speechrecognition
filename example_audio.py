import wave
import matplotlib.pyplot as plt
import numpy as np
#audio signal parameters
# number_of_channels = 1
# sample_width = 2
# frame_rate = 44100
# number_of_channels = 2
# number_of_frames = 44100
# sample_width = 2


# #open the wave file
# file = wave.open("recorded.wav", "rb")

# print("Number of channels", file.getnchannels())
# print("framerate", file.getframerate())
# print("Number of frames", file.getnframes())
# print("Sample rate", file.getsampwidth())
# print("Wave params", file.getparams())

# file_time = file.getnframes() / file.getframerate()
# print("File time", file_time)

# frames = file.readframes(-1)
# print(type(frames))
# print(len(frames))

file = wave.open("recorded.wav", "rb")

n_samples = file.getframerate()
sample_freq = file.getnframes()

t_audio = n_samples / sample_freq

signal_wave = file.readframes(n_samples)
signal_array = np.frombuffer(signal_wave,dtype=np.int16)

times = np.linspace(0, n_samples/sample_freq, num=n_samples)



plt.figure(figsize=(15,5))
plt.plot(times, signal_array)
plt.title("Audio")
plt.ylabel("Signal Value")
plt.xlabel("time(s)")
plt.xlim(0, t_audio)
plt.show()


plt.figure(figsize=(15, 5))
plt.specgram(signal_array, Fs=sample_freq, vmin=-20, vmax=50)
plt.title('Left Channel')
plt.ylabel('Frequency (Hz)')
plt.xlabel('Time (s)')
plt.xlim(0, t_audio)
plt.colorbar()
plt.show()