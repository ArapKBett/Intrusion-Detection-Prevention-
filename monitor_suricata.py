import json
import os
import smtplib
from email.mime.text import MIMEText
from datetime import datetime

def monitor_suricata_alerts(alert_file):
    with open(alert_file, 'r') as file:
        for line in file:
            alert = json.loads(line)
            process_alert(alert)

def process_alert(alert):
    signature = alert['alert']['signature']
    src_ip = alert['src_ip']
    dest_ip = alert['dest_ip']
    timestamp = alert['timestamp']
    
    # Log the alert to a file
    log_alert(signature, src_ip, dest_ip, timestamp)
    
    # Send an email notification
    send_email_notification(signature, src_ip, dest_ip, timestamp)
    
    # Take automated action based on alert type
    if "malware" in signature.lower():
        block_ip(src_ip)

    print(f"Alert: {signature} from {src_ip} to {dest_ip} at {timestamp}")

def log_alert(signature, src_ip, dest_ip, timestamp):
    log_entry = f"{timestamp} - Alert: {signature} from {src_ip} to {dest_ip}\n"
    with open("alerts.log", "a") as log_file:
        log_file.write(log_entry)

def send_email_notification(signature, src_ip, dest_ip, timestamp):
    msg = MIMEText(f"Alert: {signature}\nSource IP: {src_ip}\nDestination IP: {dest_ip}\nTimestamp: {timestamp}")
    msg['Subject'] = 'Suricata Alert Notification'
    msg['From'] = 'your_email@example.com'
    msg['To'] = 'admin@example.com'

    try:
        with smtplib.SMTP('smtp.example.com', 587) as server:
            server.starttls()
            server.login('your_email@example.com', 'your_password')
            server.sendmail('your_email@example.com', 'admin@example.com', msg.as_string())
        print("Email notification sent.")
    except Exception as e:
        print(f"Failed to send email notification: {e}")

def block_ip(ip):
    os.system(f"sudo iptables -A INPUT -s {ip} -j DROP")
    print(f"Blocked IP: {ip}")

if __name__ == "__main__":
    alert_file = "/var/log/suricata/fast.log"
    monitor_suricata_alerts(alert_file)
