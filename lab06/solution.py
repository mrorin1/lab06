UNITS = ["Б", "КБ", "МБ", "ГБ", "ТБ"]


def count_by_extension(paths):
    counts = {}
    for path in paths:
        name = path.split("/")[-1].lstrip(".")
        ext = name.rsplit(".", 1)[1].lower() if "." in name else ""
        counts[ext] = counts.get(ext, 0) + 1
    return counts


def deepest_path(paths):
    return min(paths, key=lambda path: (-path.count("/"), path), default="")


def human_size(n_bytes):
    if n_bytes < 1024:
        return f"{n_bytes} Б"
    size, unit = n_bytes, 0
    while size >= 1024 and unit < len(UNITS) - 1:
        size, unit = size / 1024, unit + 1
    return f"{size:.1f} {UNITS[unit]}"