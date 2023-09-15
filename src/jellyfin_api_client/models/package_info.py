from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.version_info import VersionInfo


T = TypeVar("T", bound="PackageInfo")


@_attrs_define
class PackageInfo:
    """Class PackageInfo.

    Attributes:
        name (Union[Unset, str]): Gets or sets the name.
        description (Union[Unset, str]): Gets or sets a long description of the plugin containing features or helpful
            explanations.
        overview (Union[Unset, str]): Gets or sets a short overview of what the plugin does.
        owner (Union[Unset, str]): Gets or sets the owner.
        category (Union[Unset, str]): Gets or sets the category.
        guid (Union[Unset, str]): Gets or sets the guid of the assembly associated with this plugin.
            This is used to identify the proper item for automatic updates.
        versions (Union[Unset, List['VersionInfo']]): Gets or sets the versions.
        image_url (Union[Unset, None, str]): Gets or sets the image url for the package.
    """

    name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    overview: Union[Unset, str] = UNSET
    owner: Union[Unset, str] = UNSET
    category: Union[Unset, str] = UNSET
    guid: Union[Unset, str] = UNSET
    versions: Union[Unset, List["VersionInfo"]] = UNSET
    image_url: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        description = self.description
        overview = self.overview
        owner = self.owner
        category = self.category
        guid = self.guid
        versions: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.versions, Unset):
            versions = []
            for versions_item_data in self.versions:
                versions_item = versions_item_data.to_dict()

                versions.append(versions_item)

        image_url = self.image_url

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if overview is not UNSET:
            field_dict["overview"] = overview
        if owner is not UNSET:
            field_dict["owner"] = owner
        if category is not UNSET:
            field_dict["category"] = category
        if guid is not UNSET:
            field_dict["guid"] = guid
        if versions is not UNSET:
            field_dict["versions"] = versions
        if image_url is not UNSET:
            field_dict["imageUrl"] = image_url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.version_info import VersionInfo

        d = src_dict.copy()
        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        overview = d.pop("overview", UNSET)

        owner = d.pop("owner", UNSET)

        category = d.pop("category", UNSET)

        guid = d.pop("guid", UNSET)

        versions = []
        _versions = d.pop("versions", UNSET)
        for versions_item_data in _versions or []:
            versions_item = VersionInfo.from_dict(versions_item_data)

            versions.append(versions_item)

        image_url = d.pop("imageUrl", UNSET)

        package_info = cls(
            name=name,
            description=description,
            overview=overview,
            owner=owner,
            category=category,
            guid=guid,
            versions=versions,
            image_url=image_url,
        )

        return package_info
