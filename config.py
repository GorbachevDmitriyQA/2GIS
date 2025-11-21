from dotenv import load_dotenv
import os
"""Подгружаем переменные из env"""
load_dotenv()

TEST_URL = os.environ.get("TEST_URL")