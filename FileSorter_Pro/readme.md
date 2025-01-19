# File Organizer with Watchdog

This Python script organizes files in your `Downloads` directory by automatically moving them into categorized folders based on their file extensions. It uses the `watchdog` library to monitor the directory for changes and sorts the files into predefined folders.

## Features

- Automatically categorizes files into folders such as:
  - **Music**
  - **Videos**
  - **Images**
  - **Documents**
  - **Compressed Files**
  - **Executables**
  - **Archives**
  - **Others**
- Ensures no file is overwritten by generating unique filenames if duplicates exist.
- Efficiently processes files using `os.scandir`, which is faster than `os.listdir`.

## Requirements

- Python 3.x
- The following Python libraries:
  - `watchdog`
  - `os`
  - `shutil`
  - `logging`

Install the dependencies using pip:

```bash
pip install watchdog
```

How It Works
	1.	Monitors the specified source directory (Downloads in this case).
	2.	When a new file is detected, it determines the file’s type based on its extension.
	3.	Moves the file to its corresponding folder. If a folder does not exist, you can manually create it in the Downloads directory.

Directory Structure

By default, the script organizes files into these folders under Downloads:
	•	/Downloads/music
	•	/Downloads/Video
	•	/Downloads/image
	•	/Downloads/document
	•	/Downloads/Compressed_file
	•	/Downloads/executable
	•	/Downloads/Archive
	•	/Downloads/Other

You can modify these paths in the script according to your preferences. I liked to keep them in download folder

Supported File Types

Images
	•	Examples: .jpg, .png, .gif, .svg, .bmp, .raw, .heic, etc.

Audio
	•	Examples: .mp3, .flac, .wav, .aac, .ogg, etc.

Videos
	•	Examples: .mp4, .mkv, .avi, .mov, .webm, etc.

Documents
	•	Examples: .pdf, .docx, .xlsx, .pptx, .csv, etc.

Compressed Files
	•	Examples: .zip, .rar, .7z, .tar, etc.

Executables
	•	Examples: .exe, .bat, .sh, .py, .jar, etc.

Archives
	•	Examples: .tar, .gz, .bz2, etc.

Other
	•	Examples: .xml, .json, .html, .css, .js, etc.

Usage
	1.	Update the source_dir variable in the script to the path of the directory you want to monitor (e.g., "/Users/sajjadalsaffar/Downloads").
	2.	Specify destination directories for each file type (e.g., dest_music, dest_video, etc.).
	3.	Run the script:
 
```
python file_organizer.py
```

  4.	The script will start monitoring the specified directory and organize files automatically. You can also, make it run on OS boot via shell scripting if you had like.

Customization
	•	To add or modify file extensions, update the corresponding extension lists in the script (e.g., image_extensions, audio_extensions).
	•	To change folder destinations, update the dest_* variables with your preferred paths.

Example Output

2025-01-19 14:00:00 - Moved audio file: song.mp3
2025-01-19 14:00:10 - Moved image file: photo.jpg
2025-01-19 14:00:20 - Moved document file: report.pdf

Notes
	•	The script skips temporary files (e.g., .crdownload files).
	•	Files with unknown or unsupported extensions will remain in the Downloads folder or can be moved to the Other folder.

License

This project is licensed under the MIT License. Feel free to use and modify it for your personal needs.

Happy organizing!

