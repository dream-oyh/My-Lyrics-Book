import os
import re


def extract_lyrics(lrc_content):
    # Remove timestamps in [xx:xx.xxx] format
    lyrics_without_timestamps = re.sub(r"\[\d{2}:\d{2}\.\d{3}\]", "", lrc_content)

    # Remove timestamps in xx:xx:xx,xxx format and arrows
    lyrics_without_timestamps = re.sub(
        r"\d{2}:\d{2}:\d{2},\d{3}\s*-->\s*|\d{2}:\d{2}:\d{2},\d{3}",
        "",
        lyrics_without_timestamps,
    )

    # Remove line numbers at start of lines
    lyrics_without_numbers = re.sub(
        r"^\d+\s*$|^\d+\s+", "", lyrics_without_timestamps, flags=re.MULTILINE
    )

    # Get only the lyrics lines (non-empty lines after cleaning)
    lyrics_lines = [
        line.strip() for line in lyrics_without_numbers.split("\n") if line.strip()
    ]

    return "\n".join(lyrics_lines)


def process_lrc_files(input_dir):
    # Create output directory if it doesn't exist
    output_dir = "lyrics_txt"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Process each LRC file in the input directory
    for filename in os.listdir(input_dir):
        if filename.endswith(".lrc"):
            # Read LRC file
            with open(os.path.join(input_dir, filename), "r", encoding="utf-8") as f:
                lrc_content = f.read()

            # Extract lyrics
            lyrics = extract_lyrics(lrc_content)

            # Create output filename
            output_filename = os.path.splitext(filename)[0] + ".txt"

            # Write lyrics to txt file
            with open(
                os.path.join(output_dir, output_filename), "w", encoding="utf-8"
            ) as f:
                f.write(lyrics)


if __name__ == "__main__":
    input_dir = "the great impersonator_lrc"
    process_lrc_files(input_dir)
