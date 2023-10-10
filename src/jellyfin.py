import socket
from typing import Optional

from jellyfin_api_client.client import Client


class JellyfinClient(Client):
    """
    Subclass of the Jellyfin API Client client.

    - Supports proper creation of the Jellyfin/Emby authorization header
    - The client can be authenticated or not, with the same constructor
    """

    def __init__(
        self,
        *args,
        device_id: str = "-",
        token: Optional[str] = None,
        **kwargs,
    ):
        headers = {}
        headers.update(
            self.__make_emby_header(
                client="Marmalade",
                version="1.9.1",
                device=socket.gethostname(),
                device_id=device_id,
                token=token,
            )
        )
        super().__init__(*args, **kwargs, headers=headers)

    def __make_emby_header(
        self,
        client: str,
        version: str,
        device: str,
        device_id: str,
        token: Optional[str] = None,
    ) -> dict[str, str]:
        """
        Make the mandatory X-Emby-Authorization header

        Note: you can only have a single access token per device id
        (see https://github.com/home-assistant/core/issues/70124#issuecomment-1278033166)
        """
        parameters = {
            "Client": client,
            "Version": version,
            "Device": device,
            "DeviceId": device_id,
        }
        if token is not None:
            parameters["Token"] = token
        parts = [f'{key}="{value}"' for key, value in parameters.items()]
        header_value = f"MediaBrowser {', '.join(parts)}"
        return {"X-Emby-Authorization": header_value}
