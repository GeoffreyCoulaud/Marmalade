from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="DlnaOptions")


@_attrs_define
class DlnaOptions:
    """The DlnaOptions class contains the user definable parameters for the dlna subsystems.

    Attributes:
        enable_play_to (Union[Unset, bool]): Gets or sets a value indicating whether gets or sets a value to indicate
            the status of the dlna playTo subsystem.
        enable_server (Union[Unset, bool]): Gets or sets a value indicating whether gets or sets a value to indicate the
            status of the dlna server subsystem.
        enable_debug_log (Union[Unset, bool]): Gets or sets a value indicating whether detailed dlna server logs are
            sent to the console/log.
            If the setting "Emby.Dlna": "Debug" msut be set in logging.default.json for this property to work.
        enable_play_to_tracing (Union[Unset, bool]): Gets or sets a value indicating whether whether detailed playTo
            debug logs are sent to the console/log.
            If the setting "Emby.Dlna.PlayTo": "Debug" msut be set in logging.default.json for this property to work.
        client_discovery_interval_seconds (Union[Unset, int]): Gets or sets the ssdp client discovery interval time (in
            seconds).
            This is the time after which the server will send a ssdp search request.
        alive_message_interval_seconds (Union[Unset, int]): Gets or sets the frequency at which ssdp alive notifications
            are transmitted.
        blast_alive_message_interval_seconds (Union[Unset, int]): Gets or sets the frequency at which ssdp alive
            notifications are transmitted. MIGRATING - TO BE REMOVED ONCE WEB HAS BEEN ALTERED.
        default_user_id (Union[Unset, None, str]): Gets or sets the default user account that the dlna server uses.
        auto_create_play_to_profiles (Union[Unset, bool]): Gets or sets a value indicating whether playTo device
            profiles should be created.
        blast_alive_messages (Union[Unset, bool]): Gets or sets a value indicating whether to blast alive messages.
        send_only_matched_host (Union[Unset, bool]): gets or sets a value indicating whether to send only matched host.
    """

    enable_play_to: Union[Unset, bool] = UNSET
    enable_server: Union[Unset, bool] = UNSET
    enable_debug_log: Union[Unset, bool] = UNSET
    enable_play_to_tracing: Union[Unset, bool] = UNSET
    client_discovery_interval_seconds: Union[Unset, int] = UNSET
    alive_message_interval_seconds: Union[Unset, int] = UNSET
    blast_alive_message_interval_seconds: Union[Unset, int] = UNSET
    default_user_id: Union[Unset, None, str] = UNSET
    auto_create_play_to_profiles: Union[Unset, bool] = UNSET
    blast_alive_messages: Union[Unset, bool] = UNSET
    send_only_matched_host: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        enable_play_to = self.enable_play_to
        enable_server = self.enable_server
        enable_debug_log = self.enable_debug_log
        enable_play_to_tracing = self.enable_play_to_tracing
        client_discovery_interval_seconds = self.client_discovery_interval_seconds
        alive_message_interval_seconds = self.alive_message_interval_seconds
        blast_alive_message_interval_seconds = self.blast_alive_message_interval_seconds
        default_user_id = self.default_user_id
        auto_create_play_to_profiles = self.auto_create_play_to_profiles
        blast_alive_messages = self.blast_alive_messages
        send_only_matched_host = self.send_only_matched_host

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if enable_play_to is not UNSET:
            field_dict["EnablePlayTo"] = enable_play_to
        if enable_server is not UNSET:
            field_dict["EnableServer"] = enable_server
        if enable_debug_log is not UNSET:
            field_dict["EnableDebugLog"] = enable_debug_log
        if enable_play_to_tracing is not UNSET:
            field_dict["EnablePlayToTracing"] = enable_play_to_tracing
        if client_discovery_interval_seconds is not UNSET:
            field_dict["ClientDiscoveryIntervalSeconds"] = client_discovery_interval_seconds
        if alive_message_interval_seconds is not UNSET:
            field_dict["AliveMessageIntervalSeconds"] = alive_message_interval_seconds
        if blast_alive_message_interval_seconds is not UNSET:
            field_dict["BlastAliveMessageIntervalSeconds"] = blast_alive_message_interval_seconds
        if default_user_id is not UNSET:
            field_dict["DefaultUserId"] = default_user_id
        if auto_create_play_to_profiles is not UNSET:
            field_dict["AutoCreatePlayToProfiles"] = auto_create_play_to_profiles
        if blast_alive_messages is not UNSET:
            field_dict["BlastAliveMessages"] = blast_alive_messages
        if send_only_matched_host is not UNSET:
            field_dict["SendOnlyMatchedHost"] = send_only_matched_host

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        enable_play_to = d.pop("EnablePlayTo", UNSET)

        enable_server = d.pop("EnableServer", UNSET)

        enable_debug_log = d.pop("EnableDebugLog", UNSET)

        enable_play_to_tracing = d.pop("EnablePlayToTracing", UNSET)

        client_discovery_interval_seconds = d.pop("ClientDiscoveryIntervalSeconds", UNSET)

        alive_message_interval_seconds = d.pop("AliveMessageIntervalSeconds", UNSET)

        blast_alive_message_interval_seconds = d.pop("BlastAliveMessageIntervalSeconds", UNSET)

        default_user_id = d.pop("DefaultUserId", UNSET)

        auto_create_play_to_profiles = d.pop("AutoCreatePlayToProfiles", UNSET)

        blast_alive_messages = d.pop("BlastAliveMessages", UNSET)

        send_only_matched_host = d.pop("SendOnlyMatchedHost", UNSET)

        dlna_options = cls(
            enable_play_to=enable_play_to,
            enable_server=enable_server,
            enable_debug_log=enable_debug_log,
            enable_play_to_tracing=enable_play_to_tracing,
            client_discovery_interval_seconds=client_discovery_interval_seconds,
            alive_message_interval_seconds=alive_message_interval_seconds,
            blast_alive_message_interval_seconds=blast_alive_message_interval_seconds,
            default_user_id=default_user_id,
            auto_create_play_to_profiles=auto_create_play_to_profiles,
            blast_alive_messages=blast_alive_messages,
            send_only_matched_host=send_only_matched_host,
        )

        return dlna_options
