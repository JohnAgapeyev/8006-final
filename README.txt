Along with the final report, and project waiver, I have submitted 2 scripts that were used in my analysis.
blacklist.sh is a script that checks an IP address against 117 blacklists to determine if the IP has a history of malicious or unwanted activity.
run_ips.py utilizes blacklist.sh to independently check each IP in a file in a seperate process, to speed up the process fo bulk DNS queriers.

blacklist.sh was downloaded from https://github.com/IntellexApps/blcheck under the name blcheck.
I wrote run_ips myself.

I used these tools in the analysis of the data, but they did not make it into the report since I figured stating x% of several thousand IP addresses that connected
was neither useful nor relevant to the analysis and its conclusions.
