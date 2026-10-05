import os

def ls_r(path="."):
    print(f"{path}:")
    entries = sorted(os.listdir(path))
    print("  ".join(entries))
    print("==========================================")
    for e in entries:
        full = os.path.join(path, e)
        #if is a folder and if is not a shortcut
        if os.path.isdir(full) and not os.path.islink(full): 
            ls_r(full)

ls_r(".")