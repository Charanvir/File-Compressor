import zipfile
import pathlib


def make_archive(filepaths, dest_dir, compression_file_name):
    # Creates a zip file
    # Methods takes the destination path and the mode, in our case being write "w"
    dest_path = pathlib.Path(dest_dir, f"{compression_file_name}.zip")
    with zipfile.ZipFile(dest_path, "w") as archive:
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            archive.write(filepath, arcname=filepath.name)


if __name__ == "__main__":
    make_archive(filepaths=["test.py", "test2.py"], dest_dir="testFolder")
