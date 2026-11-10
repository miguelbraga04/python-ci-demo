# python-ci-demo
# 1. Luo virtuaaliympäristö
python3 -m venv .venv

# 2. Aktivoi virtuaaliympäristö
source .venv/bin/activate

# 3. Päivitä pip
python -m pip install --upgrade pip

# 4. Asenna riippuvuudet
pip install -e ".[dev]"

# 5. Suorita testit
pytest -v

# 6. Suorita linttaus
ruff check .
