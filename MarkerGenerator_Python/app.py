from flask import Flask, jsonify, request
import random

app = Flask(__name__)

@app.route('/')
def generate_geojson():
    iterations = int(request.args.get('iterations', default=10))  # Get 'iterations' query parameter, default to 10 if not provided
    features = []
    for _ in range(iterations):  # Generate 10 random points
        lon = random.uniform(-180, 180)
        lat = random.uniform(-90, 90)
        point = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [lon, lat]
            },
            "properties": {
                "name": "Random Point"
            }
        }
        features.append(point)

    geojson = {
        "type": "FeatureCollection",
        "features": features
    }

    return jsonify(geojson)

if __name__ == '__main__':
    app.run(debug=True)
