import shutil
from pathlib import Path


def organize_jpg_files(source_folder):
    source = Path(source_folder).expanduser()

    if not source.exists():
        print("Error: The source folder does not exist.")
        return
    if not source.is_dir():
        print("Error: The provided path is not a folder.")
        return

    destination = source / "JPG_Images"
    destination.mkdir(exist_ok=True)

    image_files = [
        path for path in source.iterdir()
        if path.is_file() and path.suffix.lower() in {".jpg", ".jpeg"}
    ]

    if not image_files:
        print("No JPG/JPEG files found in the source folder.")
        return

    moved_count = 0
    skipped_count = 0

    for image_path in image_files:
        target = destination / image_path.name

        # Avoid overwriting an existing file by choosing a new name.
        if target.exists():
            stem = image_path.stem
            suffix = image_path.suffix
            counter = 1
            while target.exists():
                target = destination / f"{stem}_{counter}{suffix}"
                counter += 1

        try:
            shutil.move(str(image_path), str(target))
            print(f"Moved: {image_path.name} -> {target.name}")
            moved_count += 1
        except OSError as error:
            print(f"Could not move {image_path.name}: {error}")
            skipped_count += 1

    print("\n=== Automation Summary ===")
    print(f"Files moved: {moved_count}")
    print(f"Files not moved: {skipped_count}")
    print(f"Destination folder: {destination}")


def main():
    print("=== CodeAlpha JPG File Organizer ===")
    print("This script moves JPG/JPEG files from a chosen folder into a JPG_Images subfolder.")
    folder = input("Enter the full path of the folder to organize: ").strip().strip('"')

    confirmation = input(
        "This will move files from that folder. Continue? (yes/no): "
    ).strip().lower()

    if confirmation in {"yes", "y"}:
        organize_jpg_files(folder)
    else:
        print("Cancelled. No files were moved.")


if __name__ == "__main__":
    main()
