#!/usr/bin/env python3
import tomllib
from pathlib import Path

root = Path(__file__).parent.parent


def assert_icon(path: Path):
    assert path.is_file(), f"{path}: operator icon files must be a file"
    assert path.suffix == ".png", f"{path}: operator icon files must be .PNG"
    data = path.read_bytes()
    assert len(data) >= 33, f"{path}: operator icon files must be at least 33 bytes"
    assert data.startswith(b"\x89PNG\r\n\x1a\n"), f"{path}: operator icon files must start with PNG signature"
    width = int.from_bytes(data[16:20], "big")
    height = int.from_bytes(data[20:24], "big")
    assert 256 <= width <= 1024, f"{path}: operator icon files must be between 256 and 1024 pixels"
    assert 256 <= height <= 1024, f"{path}: operator icon files must be between 256 and 1024 pixels"
    assert width == height, f"{path}: operator icon files must be square"


def assert_catalog(catalog_path: Path):
    try:
        data = tomllib.loads(catalog_path.read_text())
    except Exception as error:
        raise RuntimeError(f"{catalog_path}: invalid TOML: {error}") from error

    assert "operators" in data, f"{catalog_path}: catalog missing operators"
    for operator in data.get("operators", []):
        entries = [operator, *operator.get("gids", [])]
        for entry in entries:
            icon = entry.get("icon")
            icon_scope = entry.get("icon_scope")
            assert bool(icon) == bool(icon_scope), f"{catalog_path}: icon and icon_scope must be set together"
            if not icon:
                continue
            target = root / "icons" / icon_scope / f"{icon}.png"
            assert target.is_file(), f"{catalog_path}: missing referenced icon {target}"


def main():
    icon_files = list[Path](root.rglob("icons/**/*.png"))
    catalog_files = list[Path](root.rglob("catalog/**/*.toml"))
    assert any(icon_files), "icons/: no PNG icon files found"
    assert any(catalog_files), "catalog/: no catalog files found"
    for icon_path in icon_files:
        assert_icon(icon_path)
    for catalog_path in catalog_files:
        assert_catalog(catalog_path)
    print(f"Validated {len(icon_files)} PNG icons and {len(catalog_files)} catalog files.")


if __name__ == "__main__":
    main()
