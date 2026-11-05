import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent.parent / "skillmap.db"


def get_connection():
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    return connection


def init_db():
    with get_connection() as connection:
        connection.execute("""
            CREATE TABLE IF NOT EXISTS assessments (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                student_name TEXT NOT NULL,
                career TEXT NOT NULL,
                skills TEXT NOT NULL,
                match_percentage REAL NOT NULL,
                matched_skills TEXT NOT NULL,
                missing_skills TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)


def save_assessment(name, career, skills, result):
    with get_connection() as connection:
        connection.execute("""
            INSERT INTO assessments (
                student_name, career, skills,
                match_percentage, matched_skills,
                missing_skills
            )
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            name,
            career,
            skills,
            result["percentage"],
            ", ".join(result["matched"]),
            ", ".join(result["missing"])
        ))
