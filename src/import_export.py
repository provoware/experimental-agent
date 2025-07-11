import tarfile
from pathlib import Path


def export_archive(src_dir: str, archive_path: str) -> None:
    """Packt einen Ordner in ein .tar.gz-Archiv."""
    src = Path(src_dir)
    with tarfile.open(archive_path, "w:gz") as tar:
        tar.add(src, arcname=src.name)


def import_archive(archive_path: str, target_dir: str) -> None:
    """Entpackt ein .tar.gz-Archiv fehlerfrei."""
    with tarfile.open(archive_path, "r:gz") as tar:
        tar.extractall(path=target_dir)

