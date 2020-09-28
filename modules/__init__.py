from pathlib import Path


# Create directory if not exist
file = Path('data', 'data.json')
file.parent.mkdir(exist_ok=True)
