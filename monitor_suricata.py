import json
import os

def monitor_suricata_alerts(alert_file):
    with open(alert_file, 'r') as file:
        for line in file:
            alert = json.loads(line)
            process_alert(alert)

def process_alert(alert):
    print(f"Alert: {alert['alert']['signature']}")
    # Add more processing logic here

if __name__ == "__main__":
    alert_file = "/var/log/suricata/fast.log"
    monitor_suricata_alerts(alert_file)
