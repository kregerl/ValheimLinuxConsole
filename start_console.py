#!/usr/bin/env python3
import subprocess
import time

def get_pids(name):
    pgrep = ['pgrep', '-f', name]
    try:
        pids = subprocess.check_output(pgrep)
        pids_list = pids.decode('UTF-8').split('\n')
        return pids_list
    except:
        return []

if __name__ == '__main__':
    time.sleep(2)
    terminal = 'gnome-terminal'
    valheim = 'valheim.x86_64'
    pids_list = get_pids(valheim)
    if pids_list:
        subprocess.run([terminal, '-e', 'tail -f /proc/{pid}/fd/1'.format(pid = pids_list[1])])
        while pids_list:
            pids_list = get_pids(valheim)
            time.sleep(2)
    gnome_pids = get_pids(terminal)
    if gnome_pids:
        subprocess.run(['kill', gnome_pids[0]])
    exit(0)
