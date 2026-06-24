# 🛰️ ISS Tracker

A Python application that tracks the **International Space Station (ISS)** in real time and displays its current position on an interactive world map. Also includes a companion script to fetch live data on the astronauts currently aboard the ISS.

---

## Features

- **Live ISS Tracking** — Fetches the ISS's current latitude and longitude from the Open Notify API and displays it on a world map using Python's `turtle` graphics library.
- **Your Location on the Map** — Plots your own location as a red dot so you can visually compare it to where the ISS is right now.
- **Astronaut Data** — A separate script retrieves the names and spacecraft of every person currently in space.

---

## Screenshots

> The map window displays a world map with the ISS icon positioned at its live coordinates, alongside a red dot marking your location.

---

## Project Structure

```
ISS-Tracker/
├── main.py             # Main ISS tracker — fetches live position and renders the map
├── Astronaut_data.py   # Fetches and prints current astronauts in space
├── iss.gif             # ISS icon used as the turtle sprite on the map
└── map.gif             # World map background image
```

---

## How It Works

### `main.py`
1. Calls the [Open Notify ISS Now API](http://api.open-notify.org/iss-now.json) to get the ISS's current latitude and longitude.
2. Opens a 720×360 `turtle` window set to world coordinates (matching longitude/latitude).
3. Renders a world map as the background and places an ISS icon at the live position.
4. Marks **your location** with a red dot based on coordinates you set in the script.

### `Astronaut_data.py`
1. Calls the [Open Notify Astros API](http://api.open-notify.org/astros.json).
2. Prints the total number of people currently in space along with each astronaut's name and their spacecraft.

---

## Getting Started

### Prerequisites

- Python 3.x
- No external libraries required — the project uses only Python's standard library (`json`, `urllib`, `turtle`, `time`).

### Installation

```bash
git clone https://github.com/Pranav-Katarru07/ISS-Tracker.git
cd ISS-Tracker
```

### Configuration

Open `main.py` and update the coordinates at the bottom of the file to match your location:

```python
# Example: Abu Dhabi, UAE
user_lat = 24.4539
user_lon = 54.3773
```

You can find your coordinates using [Google Maps](https://maps.google.com) or any geocoding tool.

### Running the Tracker

```bash
python3 main.py
```

A window will open showing the world map with the ISS's current position and your location marked in red.

### Running the Astronaut Data Script

```bash
python3 Astronaut_data.py
```

This will print something like:

```
People in space:  7
Astronaut: Jasmin Moghbeli
craft: ISS
Astronaut: Andreas Mogensen
craft: ISS
...
```

---

## API Reference

| API | Endpoint | Description |
|-----|----------|-------------|
| Open Notify | `http://api.open-notify.org/iss-now.json` | Current ISS position |
| Open Notify | `http://api.open-notify.org/astros.json` | People currently in space |

> **Note:** The ISS pass prediction endpoint (`iss-pass.json`) from Open Notify is currently offline. The pass prediction feature is commented out in `main.py` pending a replacement API.

---

## Known Limitations

- The ISS pass prediction feature (showing *when* the ISS will be visible from your location) is currently disabled because the Open Notify pass prediction API has been shut down. A future update may integrate an alternative API.
- The map is a static snapshot — the ISS position shown is accurate at the time the script is run, not continuously updated in real time.

---

## Author

**Pranav Katarru** — [@Pranav-Katarru07](https://github.com/Pranav-Katarru07)

---

## License

This project is open source. Feel free to fork, modify, and build upon it!
