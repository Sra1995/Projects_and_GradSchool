from os import scandir, rename
from os.path import splitext, exists, join  
from shutil import move
from time import sleep

import logging

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

source_dir = "/Users/sajjadalsaffar/Downloads"

# name of folders to move files to
dest_music = '/Users/sajjadalsaffar/Downloads/music'
dest_video = '/Users/sajjadalsaffar/Downloads/Video'
dest_image = '/Users/sajjadalsaffar/Downloads/image'
dest_documents = '/Users/sajjadalsaffar/Downloads/document'
dest_Compressed_file = '/Users/sajjadalsaffar/Downloads/Compressed_file'
dest_executable = '/Users/sajjadalsaffar/Downloads/executable'
dest_archive = '/Users/sajjadalsaffar/Downloads/Archive'
dest_other = '/Users/sajjadalsaffar/Downloads/Other'

# file extensions that runs on macOS - list from ChatGPT
# Image extensions
image_extensions = [".jpg", ".jpeg", ".jpe", ".jif", ".jfif", ".jfi", ".png", ".gif", ".webp", ".tiff", ".tif", ".psd", ".raw", ".arw", ".cr2", ".nrw",
                    ".k25", ".bmp", ".dib", ".heif", ".heic", ".ind", ".indd", ".indt", ".jp2", ".j2k", ".jpf", ".jpx", ".jpm", ".mj2", ".svg", ".svgz", ".ai", ".eps", ".ico"]

# Audio extensions
audio_extensions = [".m4a", ".flac", ".mp3", ".wav", ".wma", ".aac", ".ogg", ".mid", ".midi", ".ac3"]

# Video extensions
video_extensions = [".webm", ".mpg", ".mp2", ".mpeg", ".mpe", ".mpv", ".mp4", ".mp4v",
                     ".m4v", ".avi", ".wmv", ".mov", ".qt", ".flv", ".swf", ".avchd", ".mkv", ".flv", ".asf", ".rm", ".rmvb", ".m2ts", ".mts", ".vob"]

# Document extensions
document_extensions = [".doc", ".docx", ".odt", ".pdf", ".xls", ".xlsx", ".ppt", ".pptx", ".txt", ".rtf", ".csv"]

# Compressed file extensions
compressed_extensions = [".zip", ".rar", ".7z", ".tar", ".gz", ".bz2", ".xz"]

# Executable and script extensions
executable_extensions = [".app", ".exe", ".com", ".bat", ".sh", ".py", ".pl", ".rb", ".jar"]

# Archive extensions
archive_extensions = [".tar", ".gz", ".bz2", ".xz", ".zip", ".rar", ".7z"]

# Other extensions (add more if needed)
other_extensions = [".xml", ".json", ".html", ".css", ".js", ".php", ".asp", ".sql", ".java", ".cpp", ".h", ".hpp"]



def make_unique(dest,name):
    filename, extenstion = splitext(name)
    counter = 1
    # if the file exists, adds number at the end of the filename
    while exists(f"{dest}/{name}"):
        name = f"{filename}({str(counter)}){extenstion}"
        counter += 1

    return name

def move_file(dest, entry, name):
    try:
        if exists(f"{dest}/{name}"):
            uniquie_name = make_unique(dest, name)
            oldName = join(dest, name)
            newName = join(dest, uniquie_name)
            rename(oldName, newName)
        move(entry, dest)
    except FileNotFoundError:
        logging.warning(f"File not found at source location: {name}")


class MoverHandler(FileSystemEventHandler):
    def on_modified(self, event):
        with scandir(source_dir) as entries:
            for entry in entries:
                # Check if the entry is a directory and if it should be skipped
                if entry.is_dir() and entry.name in ["image", "music", "Video", "document", "Compressed_file", "executable", "Archive", "Other"]:
                    continue  # Skip checking this directory

                # Check if the entry is a temporary download file (ends with .crdownload)
                if entry.name.endswith(".crdownload"):
                    continue  # Skip temporary download files

                name = entry.name
                processed = False  # Initialize a flag

                if not processed:
                    processed = self.check_audio_files(entry, name)
                if not processed:
                    processed = self.check_video_files(entry, name)
                if not processed:
                    processed = self.check_image_files(entry, name)
                if not processed:
                    processed = self.check_document_files(entry, name)
                if not processed:
                    processed = self.check_compressed_files(entry, name)
                if not processed:
                    processed = self.check_executable_files(entry, name)
                if not processed:
                    processed = self.check_archive_files(entry, name)
                if not processed:
                    processed = self.check_other_files(entry, name)  # Process in the last function


                

    def check_audio_files(self, entry, name):
        for audio_extension in audio_extensions:
            if name.endswith(audio_extension) or name.endswith(audio_extension.upper()):
                move_file(dest_music, entry, name)
                logging.info(f"Moved audio file: {name}")
                return True  # File is processed
        return False

    
    def check_audio_files(self, entry, name):
        for audio_extension in audio_extensions:
            if name.endswith(audio_extension) or name.endswith(audio_extension.upper()):
                move_file(dest_music, entry, name)
                logging.info(f"Moved audio file: {name}")
                return True  # File is processed
        return False

    def check_video_files(self, entry, name):
        for video_extension in video_extensions:
            if name.endswith(video_extension) or name.endswith(video_extension.upper()):
                move_file(dest_video, entry, name)
                logging.info(f"Moved video file: {name}")
                return True
        return False

    def check_image_files(self, entry, name):
        for image_extension in image_extensions:
            if name.endswith(image_extension) or name.endswith(image_extension.upper()):
                move_file(dest_image, entry, name)
                logging.info(f"Moved image file: {name}")
                return True
        return False

    def check_document_files(self, entry, name):
        for documents_extension in document_extensions:
            if name.endswith(documents_extension) or name.endswith(documents_extension.upper()):
                move_file(dest_documents, entry, name)
                logging.info(f"Moved document file: {name}")
                return True
        return False

    def check_compressed_files(self, entry, name):
        for compressed_extension in compressed_extensions:
            if name.endswith(compressed_extension) or name.endswith(compressed_extension.upper()):
                move_file(dest_Compressed_file, entry, name)
                logging.info(f"Moved compressed file: {name}")
                return True
        return False

    def check_executable_files(self, entry, name):
        for executable_extension in executable_extensions:
            if name.endswith(executable_extension) or name.endswith(executable_extension.upper()):
                move_file(dest_executable, entry, name)
                logging.info(f"Moved executable file: {name}")
                return True
        return False

    def check_archive_files(self, entry, name):
        for archive_extension in archive_extensions:
            if name.endswith(archive_extension) or name.endswith(archive_extension.upper()):
                move_file(dest_archive, entry, name)
                logging.info(f"Moved archive file: {name}")
                return True
        return False


    def check_other_files(self, entry, name):
        if name.startswith('.') or name == '.localized':
            return False  # Skip system files

        is_in_extension_lists = False
        for extension_list in [audio_extensions, video_extensions, image_extensions, document_extensions, compressed_extensions, executable_extensions, archive_extensions]:
            for extension in extension_list:
                if name.endswith(extension) or name.endswith(extension.upper()):
                    is_in_extension_lists = True
                    break

        if not is_in_extension_lists:
            logging.info(f"File extension not in any list, leaving in download folder: {name}")
            print(name)
            return False  # File not processed

        for other_extension in other_extensions:
            if name.endswith(other_extension) or name.endswith(other_extension.upper()):
                move_file(source_dir, entry, name)  # Move to the source directory, as you requested
                logging.info(f"Moved other file: {name}")
                return True  # File processed

        return False

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = source_dir
    event_handler = MoverHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            sleep(10)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()