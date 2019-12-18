"""
TODO: add os.path.expandvars to find_file
"""
from pathlib import Path


def find_file(filename, path_dirs=None):
    """Find a file by looking through a sequence of paths.

    Parameters
    ----------
    filename: str or Path
        The filename to look for.
    path_dirs: str, None or list of str
        The list of paths to look for the file in. If None, the filename
        need to be absolute or be in the cwd. If a string, the string is
        put into a sequence and the searched.

    Raises
    ------
    FileNotFoundError:
        If all elements of path_dirs are invalid.
    """
    filename = Path(filename)
    if filename.is_absolute() and filename.is_file():
        return filename

    if path_dirs is None:
        path_dirs = (Path(''), )
    elif isinstance(path_dirs, str):
        path_dirs = (Path(path_dirs), )

    for path in path_dirs:
        path = Path(path)
        if str(path) == '.':
            path = Path.cwd()
        testname = path / filename
        try:
            testname.touch()
        except FileNotFoundError:
            pass
        if testname.parent.exists():
            return Path.resolve(testname)

    raise FileNotFoundError(f"File '{filename}' can not be made in any of the search paths: {[str(path) for path in path_dirs]}")


def deepupdate(base, other):
    """Update dict even if some key doesn't exist.

    Parameters
    ----------
    base: dict
    other: dict
    """
    if not isinstance(base, dict) or not isinstance(other, dict):
        raise TypeError(f"both of base and other must be dict, but got: {type(base)} and {type(other)}")
    for k, v in other.items():
        if isinstance(v, dict) and k in base:
            deepupdate(base[k], v)
        else:
            base[k] = v
