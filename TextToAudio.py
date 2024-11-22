import numpy as np
import wave
import struct

# converts a character into a frequency based on its position in the alphabet
def char_to_freq(character):
    return 440 + (ord(character) - ord('a')) * 20

# generates a sine wave for a given frequency and duration
def generate_sine_wave(frequency, duration, sample_rate=44100):
    time_points = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    sine_wave = 0.5 * np.sin(2 * np.pi * frequency * time_points)
    return sine_wave

# saves waveform data as a .wav audio file
def save_wave(file_name, wave_data, sample_rate=44100):
    num_samples = len(wave_data)
    wave_file = wave.open(file_name, 'w')
    num_channels = 1
    sample_width = 2
    num_frames = num_samples
    compression_type = "NONE"
    compression_name = "not compressed"
    wave_file.setparams((num_channels, sample_width, sample_rate, num_frames, compression_type, compression_name))

    for sample in wave_data:
        wave_file.writeframes(struct.pack('h', int(sample * 32767.0)))

    wave_file.close()

# main function to convert input string into a .wav audio file
def main():
    input_phrase = input("Enter a phrase: ")
    sample_rate = 44100
    character_duration = 0.5  # duration of each character in seconds
    waveform_data = np.array([], dtype=np.float32)

    for character in input_phrase:
        frequency = char_to_freq(character)
        character_waveform = generate_sine_wave(frequency, character_duration, sample_rate)
        waveform_data = np.concatenate((waveform_data, character_waveform))

    save_wave('output.wav', waveform_data, sample_rate)

if __name__ == "__main__":
    main()