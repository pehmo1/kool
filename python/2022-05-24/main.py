import os
import datetime
import requests

def main():
    # mälu
    total_memory, used_memory, free_memory = map(
        int, os.popen('free -t -m').readlines()[-1].split()[1:])
    print(f"Vaba mälu on {free_memory}M ja kokku on {total_memory}M")

    # kettaruum
    free_disk, total_disk, pcent_disk = map(str, os.popen(
        'df -BM -t ext4 --output=avail,size,pcent --total').readlines()[-1].split())
    print(f"Vaba salvestusruumi on {free_disk} ja kokku on {total_disk}")

    # % checks
    warn_at = 20
    mem_warn = used_memory / free_memory * 100 > warn_at
    disk_warn = int(pcent_disk[:-1]) > warn_at
    if mem_warn:
        print(f"Mälu kasutus kõrgem kui {warn_at}%")
    if disk_warn:
        print(f"Ketta kasutus kõrgem kui {warn_at}%")

    # log
    with open("log.txt", "a") as f:
        f.writelines([f"{datetime.datetime.now()}:",
                      f"Vaba mälu {free_memory}M, vaba ketas {free_disk}"])
        if mem_warn: f.write(f"\nMälu kasutus kõrgem kui {warn_at}%")
        if disk_warn: f.write(f"\nKetta kasutus kõrgem kui {warn_at}%")
        f.write(f"\n{requests.get('https://wttr.in/tallinn?0AnT').content}")

if __name__ == "__main__":
    main()
