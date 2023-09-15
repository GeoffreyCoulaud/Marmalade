from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..models.architecture import Architecture
from ..models.f_fmpeg_location import FFmpegLocation
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.installation_info import InstallationInfo


T = TypeVar("T", bound="SystemInfo")


@_attrs_define
class SystemInfo:
    """Class SystemInfo.

    Attributes:
        local_address (Union[Unset, None, str]): Gets or sets the local address.
        server_name (Union[Unset, None, str]): Gets or sets the name of the server.
        version (Union[Unset, None, str]): Gets or sets the server version.
        product_name (Union[Unset, None, str]): Gets or sets the product name. This is the AssemblyProduct name.
        operating_system (Union[Unset, None, str]): Gets or sets the operating system.
        id (Union[Unset, None, str]): Gets or sets the id.
        startup_wizard_completed (Union[Unset, None, bool]): Gets or sets a value indicating whether the startup wizard
            is completed.
        operating_system_display_name (Union[Unset, None, str]): Gets or sets the display name of the operating system.
        package_name (Union[Unset, None, str]): Gets or sets the package name.
        has_pending_restart (Union[Unset, bool]): Gets or sets a value indicating whether this instance has pending
            restart.
        is_shutting_down (Union[Unset, bool]):
        supports_library_monitor (Union[Unset, bool]): Gets or sets a value indicating whether [supports library
            monitor].
        web_socket_port_number (Union[Unset, int]): Gets or sets the web socket port number.
        completed_installations (Union[Unset, None, List['InstallationInfo']]): Gets or sets the completed
            installations.
        can_self_restart (Union[Unset, bool]): Gets or sets a value indicating whether this instance can self restart.
        can_launch_web_browser (Union[Unset, bool]):
        program_data_path (Union[Unset, None, str]): Gets or sets the program data path.
        web_path (Union[Unset, None, str]): Gets or sets the web UI resources path.
        items_by_name_path (Union[Unset, None, str]): Gets or sets the items by name path.
        cache_path (Union[Unset, None, str]): Gets or sets the cache path.
        log_path (Union[Unset, None, str]): Gets or sets the log path.
        internal_metadata_path (Union[Unset, None, str]): Gets or sets the internal metadata path.
        transcoding_temp_path (Union[Unset, None, str]): Gets or sets the transcode path.
        has_update_available (Union[Unset, bool]): Gets or sets a value indicating whether this instance has update
            available.
        encoder_location (Union[Unset, FFmpegLocation]): Enum describing the location of the FFmpeg tool.
        system_architecture (Union[Unset, Architecture]):
    """

    local_address: Union[Unset, None, str] = UNSET
    server_name: Union[Unset, None, str] = UNSET
    version: Union[Unset, None, str] = UNSET
    product_name: Union[Unset, None, str] = UNSET
    operating_system: Union[Unset, None, str] = UNSET
    id: Union[Unset, None, str] = UNSET
    startup_wizard_completed: Union[Unset, None, bool] = UNSET
    operating_system_display_name: Union[Unset, None, str] = UNSET
    package_name: Union[Unset, None, str] = UNSET
    has_pending_restart: Union[Unset, bool] = UNSET
    is_shutting_down: Union[Unset, bool] = UNSET
    supports_library_monitor: Union[Unset, bool] = UNSET
    web_socket_port_number: Union[Unset, int] = UNSET
    completed_installations: Union[Unset, None, List["InstallationInfo"]] = UNSET
    can_self_restart: Union[Unset, bool] = UNSET
    can_launch_web_browser: Union[Unset, bool] = UNSET
    program_data_path: Union[Unset, None, str] = UNSET
    web_path: Union[Unset, None, str] = UNSET
    items_by_name_path: Union[Unset, None, str] = UNSET
    cache_path: Union[Unset, None, str] = UNSET
    log_path: Union[Unset, None, str] = UNSET
    internal_metadata_path: Union[Unset, None, str] = UNSET
    transcoding_temp_path: Union[Unset, None, str] = UNSET
    has_update_available: Union[Unset, bool] = UNSET
    encoder_location: Union[Unset, FFmpegLocation] = UNSET
    system_architecture: Union[Unset, Architecture] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        local_address = self.local_address
        server_name = self.server_name
        version = self.version
        product_name = self.product_name
        operating_system = self.operating_system
        id = self.id
        startup_wizard_completed = self.startup_wizard_completed
        operating_system_display_name = self.operating_system_display_name
        package_name = self.package_name
        has_pending_restart = self.has_pending_restart
        is_shutting_down = self.is_shutting_down
        supports_library_monitor = self.supports_library_monitor
        web_socket_port_number = self.web_socket_port_number
        completed_installations: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.completed_installations, Unset):
            if self.completed_installations is None:
                completed_installations = None
            else:
                completed_installations = []
                for completed_installations_item_data in self.completed_installations:
                    completed_installations_item = completed_installations_item_data.to_dict()

                    completed_installations.append(completed_installations_item)

        can_self_restart = self.can_self_restart
        can_launch_web_browser = self.can_launch_web_browser
        program_data_path = self.program_data_path
        web_path = self.web_path
        items_by_name_path = self.items_by_name_path
        cache_path = self.cache_path
        log_path = self.log_path
        internal_metadata_path = self.internal_metadata_path
        transcoding_temp_path = self.transcoding_temp_path
        has_update_available = self.has_update_available
        encoder_location: Union[Unset, str] = UNSET
        if not isinstance(self.encoder_location, Unset):
            encoder_location = self.encoder_location.value

        system_architecture: Union[Unset, str] = UNSET
        if not isinstance(self.system_architecture, Unset):
            system_architecture = self.system_architecture.value

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if local_address is not UNSET:
            field_dict["LocalAddress"] = local_address
        if server_name is not UNSET:
            field_dict["ServerName"] = server_name
        if version is not UNSET:
            field_dict["Version"] = version
        if product_name is not UNSET:
            field_dict["ProductName"] = product_name
        if operating_system is not UNSET:
            field_dict["OperatingSystem"] = operating_system
        if id is not UNSET:
            field_dict["Id"] = id
        if startup_wizard_completed is not UNSET:
            field_dict["StartupWizardCompleted"] = startup_wizard_completed
        if operating_system_display_name is not UNSET:
            field_dict["OperatingSystemDisplayName"] = operating_system_display_name
        if package_name is not UNSET:
            field_dict["PackageName"] = package_name
        if has_pending_restart is not UNSET:
            field_dict["HasPendingRestart"] = has_pending_restart
        if is_shutting_down is not UNSET:
            field_dict["IsShuttingDown"] = is_shutting_down
        if supports_library_monitor is not UNSET:
            field_dict["SupportsLibraryMonitor"] = supports_library_monitor
        if web_socket_port_number is not UNSET:
            field_dict["WebSocketPortNumber"] = web_socket_port_number
        if completed_installations is not UNSET:
            field_dict["CompletedInstallations"] = completed_installations
        if can_self_restart is not UNSET:
            field_dict["CanSelfRestart"] = can_self_restart
        if can_launch_web_browser is not UNSET:
            field_dict["CanLaunchWebBrowser"] = can_launch_web_browser
        if program_data_path is not UNSET:
            field_dict["ProgramDataPath"] = program_data_path
        if web_path is not UNSET:
            field_dict["WebPath"] = web_path
        if items_by_name_path is not UNSET:
            field_dict["ItemsByNamePath"] = items_by_name_path
        if cache_path is not UNSET:
            field_dict["CachePath"] = cache_path
        if log_path is not UNSET:
            field_dict["LogPath"] = log_path
        if internal_metadata_path is not UNSET:
            field_dict["InternalMetadataPath"] = internal_metadata_path
        if transcoding_temp_path is not UNSET:
            field_dict["TranscodingTempPath"] = transcoding_temp_path
        if has_update_available is not UNSET:
            field_dict["HasUpdateAvailable"] = has_update_available
        if encoder_location is not UNSET:
            field_dict["EncoderLocation"] = encoder_location
        if system_architecture is not UNSET:
            field_dict["SystemArchitecture"] = system_architecture

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.installation_info import InstallationInfo

        d = src_dict.copy()
        local_address = d.pop("LocalAddress", UNSET)

        server_name = d.pop("ServerName", UNSET)

        version = d.pop("Version", UNSET)

        product_name = d.pop("ProductName", UNSET)

        operating_system = d.pop("OperatingSystem", UNSET)

        id = d.pop("Id", UNSET)

        startup_wizard_completed = d.pop("StartupWizardCompleted", UNSET)

        operating_system_display_name = d.pop("OperatingSystemDisplayName", UNSET)

        package_name = d.pop("PackageName", UNSET)

        has_pending_restart = d.pop("HasPendingRestart", UNSET)

        is_shutting_down = d.pop("IsShuttingDown", UNSET)

        supports_library_monitor = d.pop("SupportsLibraryMonitor", UNSET)

        web_socket_port_number = d.pop("WebSocketPortNumber", UNSET)

        completed_installations = []
        _completed_installations = d.pop("CompletedInstallations", UNSET)
        for completed_installations_item_data in _completed_installations or []:
            completed_installations_item = InstallationInfo.from_dict(completed_installations_item_data)

            completed_installations.append(completed_installations_item)

        can_self_restart = d.pop("CanSelfRestart", UNSET)

        can_launch_web_browser = d.pop("CanLaunchWebBrowser", UNSET)

        program_data_path = d.pop("ProgramDataPath", UNSET)

        web_path = d.pop("WebPath", UNSET)

        items_by_name_path = d.pop("ItemsByNamePath", UNSET)

        cache_path = d.pop("CachePath", UNSET)

        log_path = d.pop("LogPath", UNSET)

        internal_metadata_path = d.pop("InternalMetadataPath", UNSET)

        transcoding_temp_path = d.pop("TranscodingTempPath", UNSET)

        has_update_available = d.pop("HasUpdateAvailable", UNSET)

        _encoder_location = d.pop("EncoderLocation", UNSET)
        encoder_location: Union[Unset, FFmpegLocation]
        if isinstance(_encoder_location, Unset):
            encoder_location = UNSET
        else:
            encoder_location = FFmpegLocation(_encoder_location)

        _system_architecture = d.pop("SystemArchitecture", UNSET)
        system_architecture: Union[Unset, Architecture]
        if isinstance(_system_architecture, Unset):
            system_architecture = UNSET
        else:
            system_architecture = Architecture(_system_architecture)

        system_info = cls(
            local_address=local_address,
            server_name=server_name,
            version=version,
            product_name=product_name,
            operating_system=operating_system,
            id=id,
            startup_wizard_completed=startup_wizard_completed,
            operating_system_display_name=operating_system_display_name,
            package_name=package_name,
            has_pending_restart=has_pending_restart,
            is_shutting_down=is_shutting_down,
            supports_library_monitor=supports_library_monitor,
            web_socket_port_number=web_socket_port_number,
            completed_installations=completed_installations,
            can_self_restart=can_self_restart,
            can_launch_web_browser=can_launch_web_browser,
            program_data_path=program_data_path,
            web_path=web_path,
            items_by_name_path=items_by_name_path,
            cache_path=cache_path,
            log_path=log_path,
            internal_metadata_path=internal_metadata_path,
            transcoding_temp_path=transcoding_temp_path,
            has_update_available=has_update_available,
            encoder_location=encoder_location,
            system_architecture=system_architecture,
        )

        return system_info
