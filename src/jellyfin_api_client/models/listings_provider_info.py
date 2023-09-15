from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.name_value_pair import NameValuePair


T = TypeVar("T", bound="ListingsProviderInfo")


@_attrs_define
class ListingsProviderInfo:
    """
    Attributes:
        id (Union[Unset, None, str]):
        type (Union[Unset, None, str]):
        username (Union[Unset, None, str]):
        password (Union[Unset, None, str]):
        listings_id (Union[Unset, None, str]):
        zip_code (Union[Unset, None, str]):
        country (Union[Unset, None, str]):
        path (Union[Unset, None, str]):
        enabled_tuners (Union[Unset, None, List[str]]):
        enable_all_tuners (Union[Unset, bool]):
        news_categories (Union[Unset, None, List[str]]):
        sports_categories (Union[Unset, None, List[str]]):
        kids_categories (Union[Unset, None, List[str]]):
        movie_categories (Union[Unset, None, List[str]]):
        channel_mappings (Union[Unset, None, List['NameValuePair']]):
        movie_prefix (Union[Unset, None, str]):
        preferred_language (Union[Unset, None, str]):
        user_agent (Union[Unset, None, str]):
    """

    id: Union[Unset, None, str] = UNSET
    type: Union[Unset, None, str] = UNSET
    username: Union[Unset, None, str] = UNSET
    password: Union[Unset, None, str] = UNSET
    listings_id: Union[Unset, None, str] = UNSET
    zip_code: Union[Unset, None, str] = UNSET
    country: Union[Unset, None, str] = UNSET
    path: Union[Unset, None, str] = UNSET
    enabled_tuners: Union[Unset, None, List[str]] = UNSET
    enable_all_tuners: Union[Unset, bool] = UNSET
    news_categories: Union[Unset, None, List[str]] = UNSET
    sports_categories: Union[Unset, None, List[str]] = UNSET
    kids_categories: Union[Unset, None, List[str]] = UNSET
    movie_categories: Union[Unset, None, List[str]] = UNSET
    channel_mappings: Union[Unset, None, List["NameValuePair"]] = UNSET
    movie_prefix: Union[Unset, None, str] = UNSET
    preferred_language: Union[Unset, None, str] = UNSET
    user_agent: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        type = self.type
        username = self.username
        password = self.password
        listings_id = self.listings_id
        zip_code = self.zip_code
        country = self.country
        path = self.path
        enabled_tuners: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.enabled_tuners, Unset):
            if self.enabled_tuners is None:
                enabled_tuners = None
            else:
                enabled_tuners = self.enabled_tuners

        enable_all_tuners = self.enable_all_tuners
        news_categories: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.news_categories, Unset):
            if self.news_categories is None:
                news_categories = None
            else:
                news_categories = self.news_categories

        sports_categories: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.sports_categories, Unset):
            if self.sports_categories is None:
                sports_categories = None
            else:
                sports_categories = self.sports_categories

        kids_categories: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.kids_categories, Unset):
            if self.kids_categories is None:
                kids_categories = None
            else:
                kids_categories = self.kids_categories

        movie_categories: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.movie_categories, Unset):
            if self.movie_categories is None:
                movie_categories = None
            else:
                movie_categories = self.movie_categories

        channel_mappings: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.channel_mappings, Unset):
            if self.channel_mappings is None:
                channel_mappings = None
            else:
                channel_mappings = []
                for channel_mappings_item_data in self.channel_mappings:
                    channel_mappings_item = channel_mappings_item_data.to_dict()

                    channel_mappings.append(channel_mappings_item)

        movie_prefix = self.movie_prefix
        preferred_language = self.preferred_language
        user_agent = self.user_agent

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["Id"] = id
        if type is not UNSET:
            field_dict["Type"] = type
        if username is not UNSET:
            field_dict["Username"] = username
        if password is not UNSET:
            field_dict["Password"] = password
        if listings_id is not UNSET:
            field_dict["ListingsId"] = listings_id
        if zip_code is not UNSET:
            field_dict["ZipCode"] = zip_code
        if country is not UNSET:
            field_dict["Country"] = country
        if path is not UNSET:
            field_dict["Path"] = path
        if enabled_tuners is not UNSET:
            field_dict["EnabledTuners"] = enabled_tuners
        if enable_all_tuners is not UNSET:
            field_dict["EnableAllTuners"] = enable_all_tuners
        if news_categories is not UNSET:
            field_dict["NewsCategories"] = news_categories
        if sports_categories is not UNSET:
            field_dict["SportsCategories"] = sports_categories
        if kids_categories is not UNSET:
            field_dict["KidsCategories"] = kids_categories
        if movie_categories is not UNSET:
            field_dict["MovieCategories"] = movie_categories
        if channel_mappings is not UNSET:
            field_dict["ChannelMappings"] = channel_mappings
        if movie_prefix is not UNSET:
            field_dict["MoviePrefix"] = movie_prefix
        if preferred_language is not UNSET:
            field_dict["PreferredLanguage"] = preferred_language
        if user_agent is not UNSET:
            field_dict["UserAgent"] = user_agent

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.name_value_pair import NameValuePair

        d = src_dict.copy()
        id = d.pop("Id", UNSET)

        type = d.pop("Type", UNSET)

        username = d.pop("Username", UNSET)

        password = d.pop("Password", UNSET)

        listings_id = d.pop("ListingsId", UNSET)

        zip_code = d.pop("ZipCode", UNSET)

        country = d.pop("Country", UNSET)

        path = d.pop("Path", UNSET)

        enabled_tuners = cast(List[str], d.pop("EnabledTuners", UNSET))

        enable_all_tuners = d.pop("EnableAllTuners", UNSET)

        news_categories = cast(List[str], d.pop("NewsCategories", UNSET))

        sports_categories = cast(List[str], d.pop("SportsCategories", UNSET))

        kids_categories = cast(List[str], d.pop("KidsCategories", UNSET))

        movie_categories = cast(List[str], d.pop("MovieCategories", UNSET))

        channel_mappings = []
        _channel_mappings = d.pop("ChannelMappings", UNSET)
        for channel_mappings_item_data in _channel_mappings or []:
            channel_mappings_item = NameValuePair.from_dict(channel_mappings_item_data)

            channel_mappings.append(channel_mappings_item)

        movie_prefix = d.pop("MoviePrefix", UNSET)

        preferred_language = d.pop("PreferredLanguage", UNSET)

        user_agent = d.pop("UserAgent", UNSET)

        listings_provider_info = cls(
            id=id,
            type=type,
            username=username,
            password=password,
            listings_id=listings_id,
            zip_code=zip_code,
            country=country,
            path=path,
            enabled_tuners=enabled_tuners,
            enable_all_tuners=enable_all_tuners,
            news_categories=news_categories,
            sports_categories=sports_categories,
            kids_categories=kids_categories,
            movie_categories=movie_categories,
            channel_mappings=channel_mappings,
            movie_prefix=movie_prefix,
            preferred_language=preferred_language,
            user_agent=user_agent,
        )

        return listings_provider_info
