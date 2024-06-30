from flask import Blueprint, request, jsonify, Response
import requests
import time
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import urllib
import sqlite3

import json

from api.db import get_db
from api.db import make_example

# TourAPI Key
api_key = "J%2FMF%2FFZu79F5m8IclqQvnPX3FEnkqzmgeDwH38xvKaB49HL3PrZ91d5TE0qApitoEBHy%2F5wfhDKhDXJlYVOlQA%3D%3D"

place_bp = Blueprint('place', __name__, url_prefix='/place')

@place_bp.route('/listup', methods=['GET'])
def place_listup():
    mapX = request.args.get('mapX', type=float)
    mapY = request.args.get('mapY', type=float)

    # 입력값이 없으면 에러 메시지 반환
    if mapX is None or mapY is None:
        return jsonify({"error": "mapX and mapY are required"}), 400

    service = "locationBasedList1"
    url = f"http://apis.data.go.kr/B551011/KorService1/{service}?serviceKey={api_key}&numOfRows=10&pageNo=1&MobileOS=ETC&MobileApp=TestApp&_type=json"
    params = { "mapX":mapX, "mapY":mapY, "radius":30000 }
    res = requests.get(url,params=params)
    data = res.json()['response']['body']['items']['item']
    df = pd.DataFrame(data).head()
    result = df.to_json(orient='records', force_ascii=False)

    return jsonify({"result": result})

@place_bp.route('/getAddress', methods=['GET'])
def place_getAddress():
    make_example()
    pid = request.args.get('pid')
    if pid is None:
        return jsonify({"error": "pid is required"}), 400

    conn = get_db('placeDB.db')
    place = conn.execute('SELECT pAddrs FROM place WHERE pid = ?', (pid,)).fetchone()
    conn.close()

    if place is None:
        return jsonify({"error": "Place not found"}), 404

    response = Response(json.dumps({"pAddrs": place[0]}, ensure_ascii=False), content_type="application/json; charset=utf-8")
    return response


@place_bp.route('/detail', methods=['GET'])
def place_detail():
    pid = request.args.get('pid')
    if pid is None:
        return jsonify({"error": "pid is required"}), 400

    conn = get_db('placeDB.db')
    place = conn.execute('SELECT * FROM place WHERE pid = ?', (pid,)).fetchall()
    conn.close()

    if place is None:
        return jsonify({"error": "Place not found"}), 404
    
    place_dict = {
            "place_id": place[0][0],
            "name": place[0][1],
            "description": place[0][2],
            "location": place[0][3],
            "pAddrs": place[0][4]
        }
    
    print(place_dict)
    return jsonify(place_dict)