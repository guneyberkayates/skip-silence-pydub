import sys
from pydub import AudioSegment
from pydub.silence import split_on_silence



def remove_silence(mp3_file_path, silence_thresh=-50, min_silence_len=1000):
    # Load the mp3 file
    audio = AudioSegment.from_mp3(mp3_file_path)

    # Split track where the silence is 1 second or more and get chunks
    chunks = split_on_silence(audio,
                              min_silence_len=min_silence_len,
                              silence_thresh=silence_thresh)

    # Combine chunks
    combined = AudioSegment.empty()
    for chunk in chunks:
        combined += chunk

    # Create a new file with silences removed
    output_file_path = "output_no_silence.mp3"
    combined.export(output_file_path, format="mp3")

    return output_file_path

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 skip-silence.py <mp3_file_path>")
        sys.exit(1)

    mp3_file_path = sys.argv[1]
    output_file_path = remove_silence(mp3_file_path)
    print(f"Silences removed. Output file saved as: {output_file_path}")
