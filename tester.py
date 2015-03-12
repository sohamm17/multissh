#!/usr/bin/python2

"""
	This file is used to run experiments
"""	

"""
This file is part of multissh.

multissh is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

multissh is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with multissh.  If not, see <http://www.gnu.org/licenses/>.
"""


import time
import subprocess
import shlex

RUNS = 10

results = open("rsync_3_workers.out", "a")

command = "rsync -a blaine1@cold06:/dev/shm/1g.blob /dev/shm/1g.blob"
command = 'rsync -a rsh="/home/blaine1/assignment2/launcher.py" blaine1@cold06:/dev/shm/1g.blob /dev/shm/1g.blob'
args = shlex.split(command)

cleanup = "rm -f /dev/shm/1g.blob"
cleanup_args = shlex.split(cleanup)

for i in range(RUNS):

	start = time.time()

	subprocess.call(args)

	end = time.time()

	results.write(str(end-start) + "\n")

	subprocess.call(cleanup_args)


