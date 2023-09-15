from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="VersionInfo")


@_attrs_define
class VersionInfo:
    """Defines the MediaBrowser.Model.Updates.VersionInfo class.

    Attributes:
        version (Union[Unset, str]): Gets or sets the version.
        version_number (Union[Unset, str]): Gets the version as a System.Version.
        changelog (Union[Unset, None, str]): Gets or sets the changelog for this version.
        target_abi (Union[Unset, None, str]): Gets or sets the ABI that this version was built against.
        source_url (Union[Unset, None, str]): Gets or sets the source URL.
        checksum (Union[Unset, None, str]): Gets or sets a checksum for the binary.
        timestamp (Union[Unset, None, str]): Gets or sets a timestamp of when the binary was built.
        repository_name (Union[Unset, str]): Gets or sets the repository name.
        repository_url (Union[Unset, str]): Gets or sets the repository url.
    """

    version: Union[Unset, str] = UNSET
    version_number: Union[Unset, str] = UNSET
    changelog: Union[Unset, None, str] = UNSET
    target_abi: Union[Unset, None, str] = UNSET
    source_url: Union[Unset, None, str] = UNSET
    checksum: Union[Unset, None, str] = UNSET
    timestamp: Union[Unset, None, str] = UNSET
    repository_name: Union[Unset, str] = UNSET
    repository_url: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        version = self.version
        version_number = self.version_number
        changelog = self.changelog
        target_abi = self.target_abi
        source_url = self.source_url
        checksum = self.checksum
        timestamp = self.timestamp
        repository_name = self.repository_name
        repository_url = self.repository_url

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if version is not UNSET:
            field_dict["version"] = version
        if version_number is not UNSET:
            field_dict["VersionNumber"] = version_number
        if changelog is not UNSET:
            field_dict["changelog"] = changelog
        if target_abi is not UNSET:
            field_dict["targetAbi"] = target_abi
        if source_url is not UNSET:
            field_dict["sourceUrl"] = source_url
        if checksum is not UNSET:
            field_dict["checksum"] = checksum
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp
        if repository_name is not UNSET:
            field_dict["repositoryName"] = repository_name
        if repository_url is not UNSET:
            field_dict["repositoryUrl"] = repository_url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        version = d.pop("version", UNSET)

        version_number = d.pop("VersionNumber", UNSET)

        changelog = d.pop("changelog", UNSET)

        target_abi = d.pop("targetAbi", UNSET)

        source_url = d.pop("sourceUrl", UNSET)

        checksum = d.pop("checksum", UNSET)

        timestamp = d.pop("timestamp", UNSET)

        repository_name = d.pop("repositoryName", UNSET)

        repository_url = d.pop("repositoryUrl", UNSET)

        version_info = cls(
            version=version,
            version_number=version_number,
            changelog=changelog,
            target_abi=target_abi,
            source_url=source_url,
            checksum=checksum,
            timestamp=timestamp,
            repository_name=repository_name,
            repository_url=repository_url,
        )

        return version_info
