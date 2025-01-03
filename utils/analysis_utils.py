import librosa
import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft
from librosa.display import specshow

def load_audio(file_path):
    """
    Load an audio file.

    Parameters:
    - file_path: str, path to the audio file

    Returns:
    - audio: numpy array, audio time series
    - sr: int, sample rate of the audio
    """
    audio, sr = librosa.load(file_path, sr=None)  # sr=None to preserve the original sample rate
    return audio, sr

def plot_waveform(audio, sr, title):
    """
    Plot the waveform of an audio file.

    Parameters:
    - audio: numpy array, audio time series
    - sr: int, sample rate of the audio
    - title: str, title for the plot
    """
    plt.figure(figsize=(10, 4))
    plt.plot(np.linspace(0, len(audio)/sr, len(audio)), audio)
    plt.title(f"Waveform of {title}")
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.show()

def plot_frequency_spectrum(audio, sr, title):
    """
    Plot the frequency spectrum of an audio file.

    Parameters:
    - audio: numpy array, audio time series
    - sr: int, sample rate of the audio
    - title: str, title for the plot
    """
    n = len(audio)
    audio_fft = fft(audio)
    freqs = np.fft.fftfreq(n, 1/sr)
    magnitude = np.abs(audio_fft)
    
    plt.figure(figsize=(10, 4))
    plt.plot(freqs[:n//2], magnitude[:n//2])  # Show only positive frequencies
    plt.title(f"Frequency Spectrum of {title}")
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Magnitude')
    plt.show()

def plot_spectrogram(audio, sr, title):
    """
    Plot the spectrogram of an audio file.

    Parameters:
    - audio: numpy array, audio time series
    - sr: int, sample rate of the audio
    - title: str, title for the plot
    """
    plt.figure(figsize=(10, 4))
    D = librosa.amplitude_to_db(np.abs(librosa.stft(audio)), ref=np.max)
    specshow(D, x_axis='time', y_axis='log', sr=sr)
    plt.colorbar(format='%+2.0f dB')
    plt.title(f'Spectrogram of {title}')
    plt.show()

def plot_mfcc(audio, sr, title):
    """
    Plot the Mel-frequency cepstral coefficients (MFCC) of an audio file.

    Parameters:
    - audio: numpy array, audio time series
    - sr: int, sample rate of the audio
    - title: str, title for the plot
    """
    mfccs = librosa.feature.mfcc(y=audio, sr=sr, n_mfcc=13)
    plt.figure(figsize=(10, 4))
    plt.imshow(mfccs, aspect='auto', origin='lower', cmap='jet')
    plt.title(f'MFCC of {title}')
    plt.colorbar()
    plt.show()

def plot_pitch(audio, sr, title):
    """
    Extract and plot the pitch of an audio file.

    Parameters:
    - audio: numpy array, audio time series
    - sr: int, sample rate of the audio
    - title: str, title for the plot
    """
    pitch, voiced_flag, voiced_probs = librosa.pyin(audio, fmin=librosa.note_to_hz('C2'), fmax=librosa.note_to_hz('C7'))
    plt.figure(figsize=(10, 4))
    plt.plot(pitch)
    plt.title(f'Pitch of {title}')
    plt.xlabel('Time (s)')
    plt.ylabel('Frequency (Hz)')
    plt.show()

def analyze_audio(file_path, title):
    """
    Analyze an audio file by plotting various audio features.

    Parameters:
    - file_path: str, path to the audio file
    - title: str, title for the plot
    """
    audio, sr = load_audio(file_path)

    plot_waveform(audio, sr, title)
    plot_frequency_spectrum(audio, sr, title)
    plot_spectrogram(audio, sr, title)
    plot_mfcc(audio, sr, title)
    plot_pitch(audio, sr, title)

# the analysis on three audio files.
if __name__ == "__main__":
    # List of file paths and titles for the analysis
    file_paths = ['./audio/audio1.mp3', './audio/audio2.mp3', './audio/audio3.mp3']
    titles = ['Audio 1', 'Audio 2', 'Audio 3']

    for file_path, title in zip(file_paths, titles):
        analyze_audio(file_path, title)
