import os
import sys
import glob
from pydub import AudioSegment

# Check if the correct number of arguments is provided
if len(sys.argv) != 3:
    print("Usage: python mp3_to_wav.py mp3_folder_path wav_folder_path")
    sys.exit(1)

# Get the input and output folders from the command line arguments
mp3_folder_path = sys.argv[1]
wav_folder_path = sys.argv[2]

# Create the output folder if it does not exist
if not os.path.exists(wav_folder_path):
    os.makedirs(wav_folder_path)

# Loop through all MP3 files in the input folder
for mp3_file_path in glob.glob(os.path.join(mp3_folder_path, "*.mp3")):
    # Load the MP3 file using pydub
    audio_segment = AudioSegment.from_file(mp3_file_path, format="mp3")

    # Construct the output file path by replacing the extension
    wav_file_path = os.path.join(
        wav_folder_path, os.path.splitext(os.path.basename(mp3_file_path))[0] + ".wav"
    )

    # Export the audio segment as a WAV file
    audio_segment.export(wav_file_path, format="wav")

print("All MP3 files in {} have been converted to WAV format and saved in {}".format(mp3_folder_path, wav_folder_path))
