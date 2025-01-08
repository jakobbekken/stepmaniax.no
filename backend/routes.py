from flask import Flask, jsonify, request
from models import get_charts_between, get_charts
import random
import os

def init_routes(app):
    @app.route("/charts_info", methods=["POST"])
    def chart_info():
        if request.is_json:
            data = request.get_json()
        else:
            return jsonify({
                "success": False,
                "error": "Request must be JSON formatted."
            })

        chart_ids = data.get("chart_ids")
        charts = get_charts(chart_ids)

        for chart in charts:
            chart["cover_path"] = f"https://data.stepmaniax.com/{chart['cover_path']}cover@256x256.jpg"

        return jsonify(charts)
        

    @app.route("/draft/generate_link", methods=["POST"])
    def gen_link():

        if request.is_json:
            data = request.get_json()
        else:
            return jsonify({
                "success": False,
                "error": "Request must be JSON formatted."
            })

        p1 = data.get("p1")
        p2 = data.get("p2")
        difficulty_from = data.get("difficulty_from")
        difficulty_to = data.get("difficulty_to")
        
        
        charts = get_charts_between(difficulty_from, difficulty_to)
        if len(charts) < 5:
            return jsonify({
                "success": False,
                "error": f"Not enough charts in range {difficulty_from} to {difficulty_to}."
            })

        random_charts = random.sample(charts, 5)

        chart_ids = [chart for chart in random_charts]
        base_url = os.getenv("FRONTEND_URL")
        query_params = f"p1={p1}&p2={p2}&chart_ids={','.join(map(str, chart_ids))}"

        link = f"{base_url}/draft?{query_params}"
        
        return jsonify({
            "success": True,
            "link": link
        })
