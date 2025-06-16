from pathlib import Path

from gi.repository import GLib

from src.database.homemade.repositories.EverythingRepository import EverythingRepository

app_data_dir = Path(GLib.get_user_data_dir()) / "marmalade"
app_cache_dir = Path(GLib.get_user_cache_dir()) / "marmalade"
app_config_dir = Path(GLib.get_user_config_dir()) / "marmalade"

# TODO remove the common repository, and use the repositories directly
repository: EverythingRepository = None  # type: ignore
