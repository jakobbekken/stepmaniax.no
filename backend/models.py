from db import get_conn

def get_rand_chart():
    conn = get_conn()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM charts ORDER BY RANDOM() LIMIT 1;")
    chart = cursor.fetchone()

    cursor.close()
    conn.close()

    return chart

def get_charts(chart_ids):
    conn = get_conn()
    cursor = conn.cursor()

    placeholders = ", ".join(["%s"] * len(chart_ids))

    cursor.execute(f"""
        SELECT
            charts.id,
            charts.difficulty,
            charts.difficulty_display,
            songs.title,
            songs.artist,
            songs.genre,
            songs.bpm,
            songs.cover_path
        FROM charts
        JOIN songs ON charts.song_id = songs.id
        WHERE charts.id IN ({placeholders})
        ORDER BY charts.difficulty;
    """, chart_ids)

    charts = [{
        "chart_id": row[0],
        "difficulty": row[1],
        "difficulty_display": row[2],
        "title": row[3],
        "artist": row[4],
        "genre": row[5],
        "bpm": row[6],
        "cover_path": row[7]
    } for row in cursor.fetchall()]

    cursor.close()
    conn.close()

    return charts

    

def get_charts_between(a, b):
    conn = get_conn()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id
        FROM charts
        WHERE
            NOT (difficulty_display = 'full' OR difficulty_display = 'full+' OR difficulty_display = 'dual' OR difficulty_display = 'dual+')
            AND difficulty BETWEEN %s AND %s
        ORDER BY RANDOM();
    """, (a, b))

    chart_ids = [row[0] for row in cursor.fetchall()]

    cursor.close()
    conn.close()

    return chart_ids
