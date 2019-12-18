"""
TODO: add os.path.expandvars to find_file
TODO: add validation, if value type is list, to deepupdate
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
        Params whose values ara the default values.
    other: dict
        Values to be updated, for example from json file.
    """
    if not isinstance(base, dict) or not isinstance(other, dict):
        raise TypeError(f"Both of base and other must be dict, but got: {type(base)} and {type(other)}.")
    for key, value in other.items():
        if isinstance(value, dict) and key in base:
            deepupdate(base[key], value)
        else:
            old_value = base.get(key)
            if old_value is None:
                raise ValueError(f"The key must not be added, but got new key: '{key}'")
            else:
                old_value_type = type(old_value)
                if isinstance(value, int) and isinstance(old_value, float):
                    value = float(value)
                if isinstance(value, old_value_type):
                    base[key] = value
                else:
                    raise ValueError(f"Value of '{key}' must be {old_value_type.__name__}, but got: {value} as {type(value).__name__}.")
