"""
main.py — Entry point for SpotifyLocalPrep.

Run this file to start the application:
    python main.py
"""

import sys
from pathlib import Path

# Make sure the project root is on the import path.
# This is needed when running with: python main.py from the project root.
sys.path.insert(0, str(Path(__file__).parent))

from app.utils.logger import setup_logging
from app.gui.main_window import MainWindow


def main():
    """Set up logging and launch the GUI."""
    # Log file lives next to main.py
    log_file = Path(__file__).parent / "spotify_local_prep.log"
    setup_logging(log_file=log_file)

    app = MainWindow()
    app.mainloop()


if __name__ == "__main__":
    main()
