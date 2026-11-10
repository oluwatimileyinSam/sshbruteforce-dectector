threshold = 3
counts = {}

with open("sample.log") as f:
    for line in f:
        if "Failed password" in line:
            ip = line.split("from ")[1].split()[0]
            if ip in counts:
                counts[ip] += 1
            else:
                counts[ip] = 1

for ip, total in counts.items():
    if total >= threshold:
        print("ALERT", ip, "| failed logins:", total)
    else:
        print(ip, "| failed logins:", total)