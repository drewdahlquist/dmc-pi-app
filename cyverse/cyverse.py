from dotenv import dotenv_values

import subprocess

config = dotenv_values(".env")  # take environment variables from .env.


def main():
    """
    irods sync from LOCAL_DIR to REMOTE_DIR
    -r, recursively
    -v, verbose
    """
    process = subprocess.run(
        ['irsync', '-r', '-v', config["LOCAL_DIR"], config["REMOTE_DIR"]])


if __name__ == '__main__':
    main()
