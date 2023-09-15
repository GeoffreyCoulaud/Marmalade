from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.package_info import PackageInfo


T = TypeVar("T", bound="InstallationInfo")


@_attrs_define
class InstallationInfo:
    """Class InstallationInfo.

    Attributes:
        guid (Union[Unset, str]): Gets or sets the Id.
        name (Union[Unset, None, str]): Gets or sets the name.
        version (Union[Unset, None, str]): Gets or sets the version.
        changelog (Union[Unset, None, str]): Gets or sets the changelog for this version.
        source_url (Union[Unset, None, str]): Gets or sets the source URL.
        checksum (Union[Unset, None, str]): Gets or sets a checksum for the binary.
        package_info (Union[Unset, None, PackageInfo]): Class PackageInfo.
    """

    guid: Union[Unset, str] = UNSET
    name: Union[Unset, None, str] = UNSET
    version: Union[Unset, None, str] = UNSET
    changelog: Union[Unset, None, str] = UNSET
    source_url: Union[Unset, None, str] = UNSET
    checksum: Union[Unset, None, str] = UNSET
    package_info: Union[Unset, None, "PackageInfo"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        guid = self.guid
        name = self.name
        version = self.version
        changelog = self.changelog
        source_url = self.source_url
        checksum = self.checksum
        package_info: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.package_info, Unset):
            package_info = self.package_info.to_dict() if self.package_info else None

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if guid is not UNSET:
            field_dict["Guid"] = guid
        if name is not UNSET:
            field_dict["Name"] = name
        if version is not UNSET:
            field_dict["Version"] = version
        if changelog is not UNSET:
            field_dict["Changelog"] = changelog
        if source_url is not UNSET:
            field_dict["SourceUrl"] = source_url
        if checksum is not UNSET:
            field_dict["Checksum"] = checksum
        if package_info is not UNSET:
            field_dict["PackageInfo"] = package_info

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.package_info import PackageInfo

        d = src_dict.copy()
        guid = d.pop("Guid", UNSET)

        name = d.pop("Name", UNSET)

        version = d.pop("Version", UNSET)

        changelog = d.pop("Changelog", UNSET)

        source_url = d.pop("SourceUrl", UNSET)

        checksum = d.pop("Checksum", UNSET)

        _package_info = d.pop("PackageInfo", UNSET)
        package_info: Union[Unset, None, PackageInfo]
        if _package_info is None:
            package_info = None
        elif isinstance(_package_info, Unset):
            package_info = UNSET
        else:
            package_info = PackageInfo.from_dict(_package_info)

        installation_info = cls(
            guid=guid,
            name=name,
            version=version,
            changelog=changelog,
            source_url=source_url,
            checksum=checksum,
            package_info=package_info,
        )

        return installation_info
