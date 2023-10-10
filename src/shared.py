from pathlib import Path
from gi.repository import GLib, Adw

from src.database.api import DataHandler

app_data_dir = Path(GLib.get_user_data_dir()) / "marmalade"
app_cache_dir = Path(GLib.get_user_cache_dir()) / "marmalade"
app_config_dir = Path(GLib.get_user_config_dir()) / "marmalade"
window: Adw.ApplicationWindow = None
settings: DataHandler = None