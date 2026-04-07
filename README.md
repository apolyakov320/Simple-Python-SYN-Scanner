# Python SYN Scanner & Banner Grabber 🔍🛡️

A lightweight network reconnaissance tool built with **Python** and **Scapy**. This script performs stealthy half-open (SYN) scans and attempts to identify services by capturing their banners.

## 🚀 Features
* **SYN Scanning:** Uses raw packets to identify open ports without completing the full TCP handshake (stealthier than a standard connect scan).
* **Banner Grabbing:** Automatically attempts to pull service information (like SSH version or web server type) once an open port is found.
* **Automatic Reset:** Sends `RST` packets to properly close half-open connections and stay "quiet" on the network.

## 📋 Prerequisites
Since this tool crafts raw network packets, it requires **root/sudo** privileges to run on Linux.

* **Python 3.x**
* **Scapy** library

## 🛠 Installation
    Clone the repository:

    git clone https://github.com/apolyakov320/Simple-Python-SYN-Scanner.git
    cd Simple-Python-SYN-Scanner

    python3 -m venv .venv
    source .venv/bin/activate

    pip install -r requirements.txt