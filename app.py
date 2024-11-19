from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/alerts')
def alerts():
    with open('/var/log/suricata/fast.log', 'r') as file:
        alerts = file.readlines()
    return render_template('alerts.html', alerts=alerts)

@app.route('/block_ip', methods=['POST'])
def block_ip():
    ip = request.form['ip']
    subprocess.run(['sudo', 'iptables', '-A', 'INPUT', '-s', ip, '-j', 'DROP'])
    return 'IP Blocked'

if __name__ == '__main__':
    app.run(debug=True)
  
