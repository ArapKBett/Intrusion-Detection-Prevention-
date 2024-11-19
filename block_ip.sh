#!/bin/bash

ALERT_FILE="/var/log/suricata/fast.log"
BLOCKED_IPS="/var/log/suricata/blocked_ips.txt"

tail -F $ALERT_FILE | while read line; do
    IP=$(echo $line | grep -oE '([0-9]{1,3}\.){3}[0-9]{1,3}')
    if ! grep -q $IP $BLOCKED_IPS; then
        echo "Blocking IP: $IP"
        sudo iptables -A INPUT -s $IP -j DROP
        echo $IP >> $BLOCKED_IPS
    fi
done
