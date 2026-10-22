UNITS = ["Б", "КБ", "МБ", "ГБ", "ТБ"]


def count_by_extension(paths): 
    counts = {}
    for path in paths:
        name = path.split("/")[-1]
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


paths = ["docs/report.PDF", "notes.txt", "docs/img/logo.png", "Makefile"]

print(count_by_extension(paths))   # {"pdf": 1, "txt": 1, "png": 1, "": 1}
print(deepest_path(paths))         # "docs/img/logo.png"

print(human_size(900))             # "900 Б"
print(human_size(1536))            # "1.5 КБ"
print(human_size(5 * 1024 * 1024)) # "5.0 МБ"