from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..models.general_command_type import GeneralCommandType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.device_profile import DeviceProfile


T = TypeVar("T", bound="ClientCapabilities")


@_attrs_define
class ClientCapabilities:
    """
    Attributes:
        playable_media_types (Union[Unset, None, List[str]]):
        supported_commands (Union[Unset, None, List[GeneralCommandType]]):
        supports_media_control (Union[Unset, bool]):
        supports_content_uploading (Union[Unset, bool]):
        message_callback_url (Union[Unset, None, str]):
        supports_persistent_identifier (Union[Unset, bool]):
        supports_sync (Union[Unset, bool]):
        device_profile (Union[Unset, None, DeviceProfile]): A MediaBrowser.Model.Dlna.DeviceProfile represents a set of
            metadata which determines which content a certain device is able to play.
            <br />
            Specifically, it defines the supported <see
            cref="P:MediaBrowser.Model.Dlna.DeviceProfile.ContainerProfiles">containers</see> and
            <see cref="P:MediaBrowser.Model.Dlna.DeviceProfile.CodecProfiles">codecs</see> (video and/or audio, including
            codec profiles and levels)
            the device is able to direct play (without transcoding or remuxing),
            as well as which <see cref="P:MediaBrowser.Model.Dlna.DeviceProfile.TranscodingProfiles">containers/codecs to
            transcode to</see> in case it isn't.
        app_store_url (Union[Unset, None, str]):
        icon_url (Union[Unset, None, str]):
    """

    playable_media_types: Union[Unset, None, List[str]] = UNSET
    supported_commands: Union[Unset, None, List[GeneralCommandType]] = UNSET
    supports_media_control: Union[Unset, bool] = UNSET
    supports_content_uploading: Union[Unset, bool] = UNSET
    message_callback_url: Union[Unset, None, str] = UNSET
    supports_persistent_identifier: Union[Unset, bool] = UNSET
    supports_sync: Union[Unset, bool] = UNSET
    device_profile: Union[Unset, None, "DeviceProfile"] = UNSET
    app_store_url: Union[Unset, None, str] = UNSET
    icon_url: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        playable_media_types: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.playable_media_types, Unset):
            if self.playable_media_types is None:
                playable_media_types = None
            else:
                playable_media_types = self.playable_media_types

        supported_commands: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.supported_commands, Unset):
            if self.supported_commands is None:
                supported_commands = None
            else:
                supported_commands = []
                for supported_commands_item_data in self.supported_commands:
                    supported_commands_item = supported_commands_item_data.value

                    supported_commands.append(supported_commands_item)

        supports_media_control = self.supports_media_control
        supports_content_uploading = self.supports_content_uploading
        message_callback_url = self.message_callback_url
        supports_persistent_identifier = self.supports_persistent_identifier
        supports_sync = self.supports_sync
        device_profile: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.device_profile, Unset):
            device_profile = self.device_profile.to_dict() if self.device_profile else None

        app_store_url = self.app_store_url
        icon_url = self.icon_url

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if playable_media_types is not UNSET:
            field_dict["PlayableMediaTypes"] = playable_media_types
        if supported_commands is not UNSET:
            field_dict["SupportedCommands"] = supported_commands
        if supports_media_control is not UNSET:
            field_dict["SupportsMediaControl"] = supports_media_control
        if supports_content_uploading is not UNSET:
            field_dict["SupportsContentUploading"] = supports_content_uploading
        if message_callback_url is not UNSET:
            field_dict["MessageCallbackUrl"] = message_callback_url
        if supports_persistent_identifier is not UNSET:
            field_dict["SupportsPersistentIdentifier"] = supports_persistent_identifier
        if supports_sync is not UNSET:
            field_dict["SupportsSync"] = supports_sync
        if device_profile is not UNSET:
            field_dict["DeviceProfile"] = device_profile
        if app_store_url is not UNSET:
            field_dict["AppStoreUrl"] = app_store_url
        if icon_url is not UNSET:
            field_dict["IconUrl"] = icon_url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.device_profile import DeviceProfile

        d = src_dict.copy()
        playable_media_types = cast(List[str], d.pop("PlayableMediaTypes", UNSET))

        supported_commands = []
        _supported_commands = d.pop("SupportedCommands", UNSET)
        for supported_commands_item_data in _supported_commands or []:
            supported_commands_item = GeneralCommandType(supported_commands_item_data)

            supported_commands.append(supported_commands_item)

        supports_media_control = d.pop("SupportsMediaControl", UNSET)

        supports_content_uploading = d.pop("SupportsContentUploading", UNSET)

        message_callback_url = d.pop("MessageCallbackUrl", UNSET)

        supports_persistent_identifier = d.pop("SupportsPersistentIdentifier", UNSET)

        supports_sync = d.pop("SupportsSync", UNSET)

        _device_profile = d.pop("DeviceProfile", UNSET)
        device_profile: Union[Unset, None, DeviceProfile]
        if _device_profile is None:
            device_profile = None
        elif isinstance(_device_profile, Unset):
            device_profile = UNSET
        else:
            device_profile = DeviceProfile.from_dict(_device_profile)

        app_store_url = d.pop("AppStoreUrl", UNSET)

        icon_url = d.pop("IconUrl", UNSET)

        client_capabilities = cls(
            playable_media_types=playable_media_types,
            supported_commands=supported_commands,
            supports_media_control=supports_media_control,
            supports_content_uploading=supports_content_uploading,
            message_callback_url=message_callback_url,
            supports_persistent_identifier=supports_persistent_identifier,
            supports_sync=supports_sync,
            device_profile=device_profile,
            app_store_url=app_store_url,
            icon_url=icon_url,
        )

        return client_capabilities
