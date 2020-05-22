#!/usr/bin/env python3

import os
import subprocess
from pathlib import Path

home_dir = Path.home()

def bash_setup():
    bash_dir = home_dir / 'jacnil_settings' / 'bash'
    for bash_file in bash_dir.iterdir():
        # Delete the old bash settings
        old_bash_file = home_dir / bash_file.name
        if old_bash_file.is_file():
            print(old_bash_file)
            Path.unlink(home_dir / bash_file.name)

            os.symlink(bash_file, home_dir / bash_file.name)

def main():
    bash_setup()

if __name__ == "__main__":
    main()
