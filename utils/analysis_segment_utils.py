import librosa
import numpy as np
import matplotlib.pyplot as plt
from librosa.display import specshow

def load_audio_segment(file_path, start_time, end_time):
    """
    Load a specific segment of an audio file.
    :param file_path: Path to the audio file
    :param start_time: Start time in seconds
    :param end_time: End time in seconds
    :return: Extracted audio segment and sample rate
    """
    audio, sr = librosa.load(file_path, sr=None)  # Preserve original sampling rate
    start_sample = int(start_time * sr)
    end_sample = int(end_time * sr)
    return audio[start_sample:end_sample], sr

def analyze_audio_segment(audio, sr, title):
    """
    Analyze an audio segment (waveform, frequency spectrum, spectrogram).
    :param audio: Audio data array
    :param sr: Sampling rate
    :param title: Title for the plots
    """
    # Plot waveform
    plt.figure(figsize=(10, 4))
    plt.plot(np.linspace(0, len(audio) / sr, len(audio)), audio)
    plt.title(f"Waveform of {title}")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.show()

    # Plot frequency spectrum
    n = len(audio)
    fft_audio = np.fft.fft(audio)
    freqs = np.fft.fftfreq(n, 1 / sr)
    magnitude = np.abs(fft_audio)

    plt.figure(figsize=(10, 4))
    plt.plot(freqs[:n // 2], magnitude[:n // 2])  # Display only positive frequencies
    plt.title(f"Frequency Spectrum of {title}")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Magnitude")
    plt.show()

    # Plot spectrogram
    plt.figure(figsize=(10, 4))
    spectrogram = librosa.amplitude_to_db(np.abs(librosa.stft(audio)), ref=np.max)
    specshow(spectrogram, sr=sr, x_axis="time", y_axis="log")
    plt.colorbar(format="%+2.0f dB")
    plt.title(f"Spectrogram of {title}")
    plt.show()

def main():
    """
    Main function to load and analyze a specific segment of an audio file.
    """
    file_path = './audio/audio3.mp3'
    titles = 'Audio 3'

    # Specify time range in seconds
    start_time = 56
    end_time = 64

    # Load the specified audio segment
    audio_segment, sr = load_audio_segment(file_path, start_time, end_time)

    # Analyze the audio segment
    analyze_audio_segment(audio_segment, sr, f"{titles} Segment from {start_time}s to {end_time}s")

if __name__ == "__main__":
    main()
