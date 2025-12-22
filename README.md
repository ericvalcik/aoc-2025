# Advent of Code 2025

Python solutions for Advent of Code 2025.

## Setup

1. Create a virtual environment:

   ```bash
   python3 -m venv venv
   ```

2. Activate the virtual environment:

   ```bash
   # On macOS/Linux:
   source venv/bin/activate

   # On Windows:
   venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Structure

- `day01/`, `day02/`, etc. - Solutions for each day
- `utils.py` - Common utility functions for reading input, parsing, etc.
- `template.py` - Template file for starting new problems

## Usage

Each day's directory should contain:

- `solution.py` - Your solution code
- `input.txt` - Your puzzle input
- `test_input.txt` - Test input (optional)

Run a solution:

```bash
python day01/solution.py
```

## Notes

- Remember to add your session cookie to download inputs automatically (if using a script)
- Keep your `.env` file (if used) out of version control
