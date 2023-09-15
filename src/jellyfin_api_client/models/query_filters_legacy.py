from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="QueryFiltersLegacy")


@_attrs_define
class QueryFiltersLegacy:
    """
    Attributes:
        genres (Union[Unset, None, List[str]]):
        tags (Union[Unset, None, List[str]]):
        official_ratings (Union[Unset, None, List[str]]):
        years (Union[Unset, None, List[int]]):
    """

    genres: Union[Unset, None, List[str]] = UNSET
    tags: Union[Unset, None, List[str]] = UNSET
    official_ratings: Union[Unset, None, List[str]] = UNSET
    years: Union[Unset, None, List[int]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        genres: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.genres, Unset):
            if self.genres is None:
                genres = None
            else:
                genres = self.genres

        tags: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.tags, Unset):
            if self.tags is None:
                tags = None
            else:
                tags = self.tags

        official_ratings: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.official_ratings, Unset):
            if self.official_ratings is None:
                official_ratings = None
            else:
                official_ratings = self.official_ratings

        years: Union[Unset, None, List[int]] = UNSET
        if not isinstance(self.years, Unset):
            if self.years is None:
                years = None
            else:
                years = self.years

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if genres is not UNSET:
            field_dict["Genres"] = genres
        if tags is not UNSET:
            field_dict["Tags"] = tags
        if official_ratings is not UNSET:
            field_dict["OfficialRatings"] = official_ratings
        if years is not UNSET:
            field_dict["Years"] = years

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        genres = cast(List[str], d.pop("Genres", UNSET))

        tags = cast(List[str], d.pop("Tags", UNSET))

        official_ratings = cast(List[str], d.pop("OfficialRatings", UNSET))

        years = cast(List[int], d.pop("Years", UNSET))

        query_filters_legacy = cls(
            genres=genres,
            tags=tags,
            official_ratings=official_ratings,
            years=years,
        )

        return query_filters_legacy
