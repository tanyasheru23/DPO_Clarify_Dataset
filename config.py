from pathlib import Path

# Paths
DATA_DIR = Path("data")
OUTPUT_JSONL = DATA_DIR / "dataset.jsonl"
OUTPUT_HF_DIR = DATA_DIR / "dataset_hf"
PARTS_DIR = DATA_DIR / "parts"

# Create directories once
DATA_DIR.mkdir(parents=True, exist_ok=True)
OUTPUT_HF_DIR.mkdir(parents=True, exist_ok=True)
PARTS_DIR.mkdir(parents=True, exist_ok=True)

TARGET_SE_PAIRS = 600
TARGET_ELI5_PAIRS = 300
TARGET_SYNTH_PAIRS = 150

MIN_SCORE_GAP = 10
MIN_ANSWER_LENGTH = 80

OPENAI_MODEL = "gpt-4o"
