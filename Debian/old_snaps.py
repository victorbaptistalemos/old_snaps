"""
Module to delete all old snaps installed.
This script requires su privileges.
"""


def snapshots(arg: str = '', index: int = 1) -> list:
    """
    Returns a list with the name of all snaps installed or the number(s) of its revision(s).
    :param arg: str,
    :param index: int
    :return: list
    """
    from subprocess import getoutput
    grep_arg: str = 'latest/stable' if index == 1 else arg
    flag: str = '' if index == 1 else '--all'
    return getoutput(f"snap list {arg} {flag} | grep '{grep_arg}' | awk " + "'{print$" + str(index) + "}'").split('\n')


def old_snapshots() -> None:
    """
    Deletes all old
     snaps installed.
    :return: None
    """
    from os import system
    system('snap refresh')
    snaps = snapshots()
    for s in snaps:
        snap = snapshots(s, 3)
        if len(snap) > 1:
            snap.pop(-1)
            for revision in snap:
                print(f'the snap {s} revision {revision} will be deleted!')
                system(f'snap remove {s} --revision {revision}')
        else:
            print(f'snap {s} has only one snap installed!')
    print()


if __name__ == '__main__':
    old_snapshots()
