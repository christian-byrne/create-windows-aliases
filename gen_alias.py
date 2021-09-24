"""
Script to create Windows aliases

Author:
    Christian P. Byrne


"""

import os


def main():
    path = input("Enter Path to a Directory:\n")
    alias = input("Enter Alias:\n")

    if "n" in input("Is the alias for a folder? [Y/N]\n").lower():
        command = f'START "{path}"'
    else:
        command = f'%SystemRoot%\explorer.exe "{path}"'

    bat_filename = f"{alias}.bat"
    bat = open(bat_filename, "w")
    bat.write(command)
    bat.close()

    os.rename(bat_filename, "C:\\Users\\" +
              os.getlogin() + "\\" + bat_filename)


if __name__ == "__main__":
    main()
