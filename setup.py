#!/usr/bin/env python3

import os
import subprocess
from pathlib import Path

home_dir = Path.home()
bash_dir = home_dir / 'jacnil_settings' / 'bash'

def git_pull():
    os.system('git pull')

def bash_setup():
    print(f'Setting up .bash* files')
    for bash_file in bash_dir.iterdir():
        # Delete the old bash settings
        old_bash_file = home_dir / bash_file.name
        if old_bash_file.is_file():
            print(f'   old_bash_file.name')
            Path.unlink(home_dir / bash_file.name)

            # Load the new ones
            os.symlink(bash_file, home_dir / bash_file.name)

def conda_setup():
    print(f'Setting up conda')
    # Test if conda is initialized properly:
    os.system('conda init --reverse')

    os.system('conda init')

def refresh_setup():
    # Reload all relevant files
    print(f'. {home_dir / ".bashrc"}')
    os.system(f'. {home_dir / ".bashrc"}')

def main():
    git_pull()
    bash_setup()
    conda_setup()
    refresh_setup()

if __name__ == "__main__":
    main()
