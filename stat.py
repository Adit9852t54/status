import psutil
import geocoder
import socket
import time

def get_battery_status():
    battery = psutil.sensors_battery()
    if battery:
        return f"Baterai: {battery.percent}% - Sisa waktu: {battery.secsleft/60} menit"
    else:
        return "Informasi baterai tidak tersedia"

def get_internet_status():
    try:
        response = geocoder.ip('me')
        return f"Alamat IP: {response.ip} - Lokasi: {response.city}, {response.country}"
    except:
        return "Tidak dapat mendapatkan informasi lokasi"

# Mendapatkan alamat IP perangkat
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

while True:
    battery_status = get_battery_status()
    internet_status = get_internet_status()

    print("\033[H\033[J")  # Clear terminal screen
    print("### Informasi Perangkat ###")
    print(f"Alamat IP Perangkat: {ip_address}")
    print(f"Status Baterai: {battery_status}")
    print(f"Status Internet: {internet_status}")

    time.sleep(5)  # Update setiap 5 detik
