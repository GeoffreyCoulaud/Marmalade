from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..models.image_type import ImageType
from ..models.rating_type import RatingType
from ..types import UNSET, Unset

T = TypeVar("T", bound="RemoteImageInfo")


@_attrs_define
class RemoteImageInfo:
    """Class RemoteImageInfo.

    Attributes:
        provider_name (Union[Unset, None, str]): Gets or sets the name of the provider.
        url (Union[Unset, None, str]): Gets or sets the URL.
        thumbnail_url (Union[Unset, None, str]): Gets or sets a url used for previewing a smaller version.
        height (Union[Unset, None, int]): Gets or sets the height.
        width (Union[Unset, None, int]): Gets or sets the width.
        community_rating (Union[Unset, None, float]): Gets or sets the community rating.
        vote_count (Union[Unset, None, int]): Gets or sets the vote count.
        language (Union[Unset, None, str]): Gets or sets the language.
        type (Union[Unset, ImageType]): Enum ImageType.
        rating_type (Union[Unset, RatingType]):
    """

    provider_name: Union[Unset, None, str] = UNSET
    url: Union[Unset, None, str] = UNSET
    thumbnail_url: Union[Unset, None, str] = UNSET
    height: Union[Unset, None, int] = UNSET
    width: Union[Unset, None, int] = UNSET
    community_rating: Union[Unset, None, float] = UNSET
    vote_count: Union[Unset, None, int] = UNSET
    language: Union[Unset, None, str] = UNSET
    type: Union[Unset, ImageType] = UNSET
    rating_type: Union[Unset, RatingType] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        provider_name = self.provider_name
        url = self.url
        thumbnail_url = self.thumbnail_url
        height = self.height
        width = self.width
        community_rating = self.community_rating
        vote_count = self.vote_count
        language = self.language
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        rating_type: Union[Unset, str] = UNSET
        if not isinstance(self.rating_type, Unset):
            rating_type = self.rating_type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if provider_name is not UNSET:
            field_dict["ProviderName"] = provider_name
        if url is not UNSET:
            field_dict["Url"] = url
        if thumbnail_url is not UNSET:
            field_dict["ThumbnailUrl"] = thumbnail_url
        if height is not UNSET:
            field_dict["Height"] = height
        if width is not UNSET:
            field_dict["Width"] = width
        if community_rating is not UNSET:
            field_dict["CommunityRating"] = community_rating
        if vote_count is not UNSET:
            field_dict["VoteCount"] = vote_count
        if language is not UNSET:
            field_dict["Language"] = language
        if type is not UNSET:
            field_dict["Type"] = type
        if rating_type is not UNSET:
            field_dict["RatingType"] = rating_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        provider_name = d.pop("ProviderName", UNSET)

        url = d.pop("Url", UNSET)

        thumbnail_url = d.pop("ThumbnailUrl", UNSET)

        height = d.pop("Height", UNSET)

        width = d.pop("Width", UNSET)

        community_rating = d.pop("CommunityRating", UNSET)

        vote_count = d.pop("VoteCount", UNSET)

        language = d.pop("Language", UNSET)

        _type = d.pop("Type", UNSET)
        type: Union[Unset, ImageType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = ImageType(_type)

        _rating_type = d.pop("RatingType", UNSET)
        rating_type: Union[Unset, RatingType]
        if isinstance(_rating_type, Unset):
            rating_type = UNSET
        else:
            rating_type = RatingType(_rating_type)

        remote_image_info = cls(
            provider_name=provider_name,
            url=url,
            thumbnail_url=thumbnail_url,
            height=height,
            width=width,
            community_rating=community_rating,
            vote_count=vote_count,
            language=language,
            type=type,
            rating_type=rating_type,
        )

        return remote_image_info
