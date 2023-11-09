import socket
import time
from typing import Optional

from hishel import CacheTransport
from httpx import HTTPTransport
from jellyfin_api_client.client import Client


def make_device_id() -> str:
    """Generate a device id for use with Jellyfin authentication"""
    max_len = 255  # Imposed by the database (quite reasonable)
    timestamp = str(time.time_ns())
    separator = "-"
    max_hostname_len = max_len - len(timestamp) - len(separator)
    hostname = socket.gethostname()[: max_hostname_len - 1]
    device_id = f"{hostname}{separator}{timestamp}"
    return device_id


class JellyfinClient(Client):
    """
    Subclass of the Jellyfin API Client client.

    - Supports proper creation of the Jellyfin/Emby authorization header
    - Supports generating a device_id on the fly
    - The client can be authenticated or not, with the same constructor
    """

    _version: str = "1.9.1"
    _client_name: str = "Marmalade"
    _device_id: str = "-"
    _device: str
    _token: str

    def __init__(
        self,
        *args,
        device_id: Optional[str] = None,
        token: Optional[str] = None,
        **kwargs,
    ):
        # Initialize the client, with caching support
        httpx_args = {
            "transport": CacheTransport(transport=HTTPTransport()),
        }
        super().__init__(*args, **kwargs, httpx_args=httpx_args)
        # Set the client headers
        self._device = socket.gethostname()
        self._token = token
        if device_id:
            self._device_id = device_id
        self._init_emby_header()

    def _init_emby_header(self) -> None:
        """
        Update or create the mandatory X-Emby-Authorization header

        Note: you can only have a single access token per device id
        (see https://github.com/home-assistant/core/issues/70124#issuecomment-1278033166)
        """
        parameters = {
            "Client": self._client_name,
            "Version": self._version,
            "Device": self._device,
            "DeviceId": self._device_id,
        }
        if self._token is not None:
            parameters["Token"] = self._token
        parts = [f'{key}="{value}"' for key, value in parameters.items()]
        header_value = f"MediaBrowser {', '.join(parts)}"
        self._headers["X-Emby-Authorization"] = header_value

    def __str__(self) -> str:
        return '"%s" Jellyfin Client v%s for %s (%s) on %s' % (
            self._client_name,
            self._version,
            self._device,
            self._device_id,
            self._base_url,
        )
