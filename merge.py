import requests

URLS = [
    "https://raw.githubusercontent.com/Cepreu54/Hyh/refs/heads/main/working/clean.txt",
    "https://raw.githubusercontent.com/Cepreu54/Hyh/refs/heads/main/working/clean1.txt",
    "https://raw.githubusercontent.com/Cepreu54/Hyh/refs/heads/main/working/clean2.txt",
    "https://raw.githubusercontent.com/Cepreu54/Hyh/refs/heads/main/working/clean3.txt",
    "https://raw.githubusercontent.com/Cepreu54/Hyh/refs/heads/main/working/clean4.txt",
    "https://raw.githubusercontent.com/Cepreu54/Hyh/refs/heads/main/working/clean5.txt",
    "https://raw.githubusercontent.com/Cepreu54/Hyh/refs/heads/main/working/clean6.txt",
    "https://raw.githubusercontent.com/Cepreu54/Hyh/refs/heads/main/working/clean7.txt",
    "https://raw.githubusercontent.com/Cepreu54/Hyh/refs/heads/main/working/clean8.txt",
    "https://raw.githubusercontent.com/Cepreu54/Hyh/refs/heads/main/working/clean9.txt",
    "https://raw.githubusercontent.com/Cepreu54/Hyh/refs/heads/main/working/clean10.txt",
    "https://raw.githubusercontent.com/Cepreu54/Hyh/refs/heads/main/working/clean11.txt",
    "https://raw.githubusercontent.com/Cepreu54/Hyh/refs/heads/main/working/vless-clean.txt",
    "https://raw.githubusercontent.com/Cepreu54/Hyh/refs/heads/main/working/vless-clean-2.txt",
    "https://raw.githubusercontent.com/Cepreu54/Hyh/refs/heads/main/working/vless-clean-3.txt"
]

all_configs = set()

for url in URLS:
    try:
        r = requests.get(url, timeout=15)

        for line in r.text.splitlines():
            line = line.strip()

            if line.startswith(("vmess://", "vless://", "trojan://", "ss://")):
                all_configs.add(line)

    except:
        pass

with open("merged.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(sorted(all_configs)))
