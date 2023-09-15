import datetime
from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="RemoteSubtitleInfo")


@_attrs_define
class RemoteSubtitleInfo:
    """
    Attributes:
        three_letter_iso_language_name (Union[Unset, None, str]):
        id (Union[Unset, None, str]):
        provider_name (Union[Unset, None, str]):
        name (Union[Unset, None, str]):
        format_ (Union[Unset, None, str]):
        author (Union[Unset, None, str]):
        comment (Union[Unset, None, str]):
        date_created (Union[Unset, None, datetime.datetime]):
        community_rating (Union[Unset, None, float]):
        download_count (Union[Unset, None, int]):
        is_hash_match (Union[Unset, None, bool]):
    """

    three_letter_iso_language_name: Union[Unset, None, str] = UNSET
    id: Union[Unset, None, str] = UNSET
    provider_name: Union[Unset, None, str] = UNSET
    name: Union[Unset, None, str] = UNSET
    format_: Union[Unset, None, str] = UNSET
    author: Union[Unset, None, str] = UNSET
    comment: Union[Unset, None, str] = UNSET
    date_created: Union[Unset, None, datetime.datetime] = UNSET
    community_rating: Union[Unset, None, float] = UNSET
    download_count: Union[Unset, None, int] = UNSET
    is_hash_match: Union[Unset, None, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        three_letter_iso_language_name = self.three_letter_iso_language_name
        id = self.id
        provider_name = self.provider_name
        name = self.name
        format_ = self.format_
        author = self.author
        comment = self.comment
        date_created: Union[Unset, None, str] = UNSET
        if not isinstance(self.date_created, Unset):
            date_created = self.date_created.isoformat() if self.date_created else None

        community_rating = self.community_rating
        download_count = self.download_count
        is_hash_match = self.is_hash_match

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if three_letter_iso_language_name is not UNSET:
            field_dict["ThreeLetterISOLanguageName"] = three_letter_iso_language_name
        if id is not UNSET:
            field_dict["Id"] = id
        if provider_name is not UNSET:
            field_dict["ProviderName"] = provider_name
        if name is not UNSET:
            field_dict["Name"] = name
        if format_ is not UNSET:
            field_dict["Format"] = format_
        if author is not UNSET:
            field_dict["Author"] = author
        if comment is not UNSET:
            field_dict["Comment"] = comment
        if date_created is not UNSET:
            field_dict["DateCreated"] = date_created
        if community_rating is not UNSET:
            field_dict["CommunityRating"] = community_rating
        if download_count is not UNSET:
            field_dict["DownloadCount"] = download_count
        if is_hash_match is not UNSET:
            field_dict["IsHashMatch"] = is_hash_match

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        three_letter_iso_language_name = d.pop("ThreeLetterISOLanguageName", UNSET)

        id = d.pop("Id", UNSET)

        provider_name = d.pop("ProviderName", UNSET)

        name = d.pop("Name", UNSET)

        format_ = d.pop("Format", UNSET)

        author = d.pop("Author", UNSET)

        comment = d.pop("Comment", UNSET)

        _date_created = d.pop("DateCreated", UNSET)
        date_created: Union[Unset, None, datetime.datetime]
        if _date_created is None:
            date_created = None
        elif isinstance(_date_created, Unset):
            date_created = UNSET
        else:
            date_created = isoparse(_date_created)

        community_rating = d.pop("CommunityRating", UNSET)

        download_count = d.pop("DownloadCount", UNSET)

        is_hash_match = d.pop("IsHashMatch", UNSET)

        remote_subtitle_info = cls(
            three_letter_iso_language_name=three_letter_iso_language_name,
            id=id,
            provider_name=provider_name,
            name=name,
            format_=format_,
            author=author,
            comment=comment,
            date_created=date_created,
            community_rating=community_rating,
            download_count=download_count,
            is_hash_match=is_hash_match,
        )

        return remote_subtitle_info
