Installation
 For Debian-based systems:

`sudo apt-get update
sudo apt-get install suricata`

Configuration
Edit the Suricata configuration file (`/etc/suricata/suricata.yaml`) to set up your network interfaces and rules.

Email Settings: Replace '`your_email@example.com'`, '`your_password'`, and '`smtp.example.com`' with your actual email credentials and SMTP server details.
Alert File Path: Ensure the `monitor_suricata.py` path matches the location of your Suricata alert log.

Running the System
`Start Suricata:
sudo suricata -c /etc/suricata/suricata.yaml -i eth0`

Run the Python monitoring script:
`python3 monitor_suricata.py`

Start the Flask web application:
`python3 app.py`
