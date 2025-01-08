import psycopg2
from psycopg2 import sql
from flask import current_app
import os
import requests
import json

def get_conn():
    conn = psycopg2.connect(
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
    )

    return conn

def create_tables():
    conn = get_conn()
    cursor = conn.cursor()

    try:

        # Charts

        # DROP TABLE IF EXISTS charts;
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS charts (
                id INTEGER PRIMARY KEY,
                difficulty INTEGER,
                difficulty_display VARCHAR,
                song_id INTEGER,
                FOREIGN KEY (song_id) REFERENCES songs (id)
            );
        """)
        conn.commit()
        
        cursor.execute("""
            SELECT COUNT(*) FROM charts;
        """)

        charts_row_count = cursor.fetchone()[0]

        if charts_row_count:
            print("Table 'charts' already existed!")
        else:
            base_url = "https://api.smx.573.no/charts"
            charts = []
            take = 100
            skip = 0

            while True:
                query = {
                    "q": json.dumps({
                        "_take": take,
                        "_skip": skip
                    })
                }
                response = requests.get(base_url, params=query)

                if response.status_code == 200:
                    data = response.json()
                    if not data:
                        break

                    selected_data = [(chart["id"], chart["difficulty"], chart["difficulty_display"], chart["song_id"]) for chart in data]
                    charts.extend(selected_data)
                    skip += take

                    if len(data) < take:
                        break

            insert_query = """
                INSERT INTO charts (id, difficulty, difficulty_display, song_id)
                VALUES (%s, %s, %s, %s)
            """

            try:
                cursor.executemany(insert_query, charts)
                conn.commit()
                print(f"{len(charts)} charts inserted successfully!")
            except Exception as e:
                conn.rollback()
                print(f"Error inserting charts: {e}")

            print("Table 'charts' created successfully!")


        # Songs
        
        # DROP TABLE IF EXISTS songs CASCADE;
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS songs (
                id INTEGER PRIMARY KEY,
                artist VARCHAR,
                title VARCHAR,
                genre VARCHAR,
                bpm VARCHAR,
                cover_path VARCHAR
            );
        """)
        conn.commit()

        cursor.execute("""
            SELECT COUNT(*) FROM songs;
        """)

        songs_row_count = cursor.fetchone()[0]

        if songs_row_count:
            print("Table 'songs' already existed!")
        else:
            base_url = "https://api.smx.573.no/songs"
            songs = []
            take = 100
            skip = 0

            while True:
                query = {
                    "q": json.dumps({
                        "_take": take,
                        "_skip": skip
                    })
                }
                response = requests.get(base_url, params=query)

                if response.status_code == 200:
                    data = response.json()
                    if not data:
                        break

                    selected_data = [(song["id"], song["artist"], song["title"], song["genre"], song["cover_path"], song["bpm"]) for song in data]
                    songs.extend(selected_data)
                    skip += take

                    if len(data) < take:
                        break

            insert_query = """
                INSERT INTO songs (id, artist, title, genre, cover_path, bpm)
                VALUES (%s, %s, %s, %s, %s, %s)
            """

            try:
                cursor.executemany(insert_query, songs)
                conn.commit()
                print(f"{len(songs)} songs inserted successfully!")
            except Exception as e:
                conn.rollback()
                print(f"Error inserting songs: {e}")

            print("Table 'songs' created successfully!")


            
    except Exception as e:
        conn.rollback()
        print(f"Error creating 'songs' table: {e}")

    finally:
        cursor.close()
        conn.close()
