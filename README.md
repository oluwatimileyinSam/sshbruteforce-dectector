SSH Brute Force Detector

A small Python script that reads an SSH login log and finds IP addresses with many failed logins. It counts the failures for each IP and marks the ones that go over a limit.

How it works

The script reads sample.log line by line. When a line contains "Failed password", it pulls out the IP address and adds one to that IP's count. At the end it prints every IP with its number of failed logins. Any IP with 5 or more gets ALERT in front.

The limit is the threshold variable at the top of detector.py. Change that number to make the rule stricter or looser.
