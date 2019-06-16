import subprocess
import sys
import datetime
import datetime
import collections
import os
import resource

resource.setrlimit(resource.RLIMIT_NPROC, (63000, 63000))

ips = open(sys.argv[1], "r")
outfile = open("blacklisted_ips.txt", "a")

for line in ips:
    subprocess.Popen(['/home/john/blacklist.sh', '-p', line], stdout=outfile, stderr=subprocess.DEVNULL)
