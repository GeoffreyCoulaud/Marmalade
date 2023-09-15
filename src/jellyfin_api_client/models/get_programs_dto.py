import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.image_type import ImageType
from ..models.item_fields import ItemFields
from ..models.sort_order import SortOrder
from ..types import UNSET, Unset

T = TypeVar("T", bound="GetProgramsDto")


@_attrs_define
class GetProgramsDto:
    """Get programs dto.

    Attributes:
        channel_ids (Union[Unset, List[str]]): Gets or sets the channels to return guide information for.
        user_id (Union[Unset, str]): Gets or sets optional. Filter by user id.
        min_start_date (Union[Unset, None, datetime.datetime]): Gets or sets the minimum premiere start date.
            Optional.
        has_aired (Union[Unset, None, bool]): Gets or sets filter by programs that have completed airing, or not.
            Optional.
        is_airing (Union[Unset, None, bool]): Gets or sets filter by programs that are currently airing, or not.
            Optional.
        max_start_date (Union[Unset, None, datetime.datetime]): Gets or sets the maximum premiere start date.
            Optional.
        min_end_date (Union[Unset, None, datetime.datetime]): Gets or sets the minimum premiere end date.
            Optional.
        max_end_date (Union[Unset, None, datetime.datetime]): Gets or sets the maximum premiere end date.
            Optional.
        is_movie (Union[Unset, None, bool]): Gets or sets filter for movies.
            Optional.
        is_series (Union[Unset, None, bool]): Gets or sets filter for series.
            Optional.
        is_news (Union[Unset, None, bool]): Gets or sets filter for news.
            Optional.
        is_kids (Union[Unset, None, bool]): Gets or sets filter for kids.
            Optional.
        is_sports (Union[Unset, None, bool]): Gets or sets filter for sports.
            Optional.
        start_index (Union[Unset, None, int]): Gets or sets the record index to start at. All items with a lower index
            will be dropped from the results.
            Optional.
        limit (Union[Unset, None, int]): Gets or sets the maximum number of records to return.
            Optional.
        sort_by (Union[Unset, List[str]]): Gets or sets specify one or more sort orders, comma delimited. Options: Name,
            StartDate.
            Optional.
        sort_order (Union[Unset, List[SortOrder]]): Gets or sets sort Order - Ascending,Descending.
        genres (Union[Unset, List[str]]): Gets or sets the genres to return guide information for.
        genre_ids (Union[Unset, List[str]]): Gets or sets the genre ids to return guide information for.
        enable_images (Union[Unset, None, bool]): Gets or sets include image information in output.
            Optional.
        enable_total_record_count (Union[Unset, bool]): Gets or sets a value indicating whether retrieve total record
            count.
        image_type_limit (Union[Unset, None, int]): Gets or sets the max number of images to return, per image type.
            Optional.
        enable_image_types (Union[Unset, List[ImageType]]): Gets or sets the image types to include in the output.
            Optional.
        enable_user_data (Union[Unset, None, bool]): Gets or sets include user data.
            Optional.
        series_timer_id (Union[Unset, None, str]): Gets or sets filter by series timer id.
            Optional.
        library_series_id (Union[Unset, str]): Gets or sets filter by library series id.
            Optional.
        fields (Union[Unset, List[ItemFields]]): Gets or sets specify additional fields of information to return in the
            output. This allows multiple, comma delimited. Options: Budget, Chapters, DateCreated, Genres, HomePageUrl,
            IndexOptions, MediaStreams, Overview, ParentId, Path, People, ProviderIds, PrimaryImageAspectRatio, Revenue,
            SortName, Studios, Taglines.
            Optional.
    """

    channel_ids: Union[Unset, List[str]] = UNSET
    user_id: Union[Unset, str] = UNSET
    min_start_date: Union[Unset, None, datetime.datetime] = UNSET
    has_aired: Union[Unset, None, bool] = UNSET
    is_airing: Union[Unset, None, bool] = UNSET
    max_start_date: Union[Unset, None, datetime.datetime] = UNSET
    min_end_date: Union[Unset, None, datetime.datetime] = UNSET
    max_end_date: Union[Unset, None, datetime.datetime] = UNSET
    is_movie: Union[Unset, None, bool] = UNSET
    is_series: Union[Unset, None, bool] = UNSET
    is_news: Union[Unset, None, bool] = UNSET
    is_kids: Union[Unset, None, bool] = UNSET
    is_sports: Union[Unset, None, bool] = UNSET
    start_index: Union[Unset, None, int] = UNSET
    limit: Union[Unset, None, int] = UNSET
    sort_by: Union[Unset, List[str]] = UNSET
    sort_order: Union[Unset, List[SortOrder]] = UNSET
    genres: Union[Unset, List[str]] = UNSET
    genre_ids: Union[Unset, List[str]] = UNSET
    enable_images: Union[Unset, None, bool] = UNSET
    enable_total_record_count: Union[Unset, bool] = UNSET
    image_type_limit: Union[Unset, None, int] = UNSET
    enable_image_types: Union[Unset, List[ImageType]] = UNSET
    enable_user_data: Union[Unset, None, bool] = UNSET
    series_timer_id: Union[Unset, None, str] = UNSET
    library_series_id: Union[Unset, str] = UNSET
    fields: Union[Unset, List[ItemFields]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        channel_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.channel_ids, Unset):
            channel_ids = self.channel_ids

        user_id = self.user_id
        min_start_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.min_start_date, Unset):
            min_start_date = self.min_start_date.isoformat() if self.min_start_date else None

        has_aired = self.has_aired
        is_airing = self.is_airing
        max_start_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.max_start_date, Unset):
            max_start_date = self.max_start_date.isoformat() if self.max_start_date else None

        min_end_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.min_end_date, Unset):
            min_end_date = self.min_end_date.isoformat() if self.min_end_date else None

        max_end_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.max_end_date, Unset):
            max_end_date = self.max_end_date.isoformat() if self.max_end_date else None

        is_movie = self.is_movie
        is_series = self.is_series
        is_news = self.is_news
        is_kids = self.is_kids
        is_sports = self.is_sports
        start_index = self.start_index
        limit = self.limit
        sort_by: Union[Unset, List[str]] = UNSET
        if not isinstance(self.sort_by, Unset):
            sort_by = self.sort_by

        sort_order: Union[Unset, List[str]] = UNSET
        if not isinstance(self.sort_order, Unset):
            sort_order = []
            for sort_order_item_data in self.sort_order:
                sort_order_item = sort_order_item_data.value

                sort_order.append(sort_order_item)

        genres: Union[Unset, List[str]] = UNSET
        if not isinstance(self.genres, Unset):
            genres = self.genres

        genre_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.genre_ids, Unset):
            genre_ids = self.genre_ids

        enable_images = self.enable_images
        enable_total_record_count = self.enable_total_record_count
        image_type_limit = self.image_type_limit
        enable_image_types: Union[Unset, List[str]] = UNSET
        if not isinstance(self.enable_image_types, Unset):
            enable_image_types = []
            for enable_image_types_item_data in self.enable_image_types:
                enable_image_types_item = enable_image_types_item_data.value

                enable_image_types.append(enable_image_types_item)

        enable_user_data = self.enable_user_data
        series_timer_id = self.series_timer_id
        library_series_id = self.library_series_id
        fields: Union[Unset, List[str]] = UNSET
        if not isinstance(self.fields, Unset):
            fields = []
            for fields_item_data in self.fields:
                fields_item = fields_item_data.value

                fields.append(fields_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if channel_ids is not UNSET:
            field_dict["ChannelIds"] = channel_ids
        if user_id is not UNSET:
            field_dict["UserId"] = user_id
        if min_start_date is not UNSET:
            field_dict["MinStartDate"] = min_start_date
        if has_aired is not UNSET:
            field_dict["HasAired"] = has_aired
        if is_airing is not UNSET:
            field_dict["IsAiring"] = is_airing
        if max_start_date is not UNSET:
            field_dict["MaxStartDate"] = max_start_date
        if min_end_date is not UNSET:
            field_dict["MinEndDate"] = min_end_date
        if max_end_date is not UNSET:
            field_dict["MaxEndDate"] = max_end_date
        if is_movie is not UNSET:
            field_dict["IsMovie"] = is_movie
        if is_series is not UNSET:
            field_dict["IsSeries"] = is_series
        if is_news is not UNSET:
            field_dict["IsNews"] = is_news
        if is_kids is not UNSET:
            field_dict["IsKids"] = is_kids
        if is_sports is not UNSET:
            field_dict["IsSports"] = is_sports
        if start_index is not UNSET:
            field_dict["StartIndex"] = start_index
        if limit is not UNSET:
            field_dict["Limit"] = limit
        if sort_by is not UNSET:
            field_dict["SortBy"] = sort_by
        if sort_order is not UNSET:
            field_dict["SortOrder"] = sort_order
        if genres is not UNSET:
            field_dict["Genres"] = genres
        if genre_ids is not UNSET:
            field_dict["GenreIds"] = genre_ids
        if enable_images is not UNSET:
            field_dict["EnableImages"] = enable_images
        if enable_total_record_count is not UNSET:
            field_dict["EnableTotalRecordCount"] = enable_total_record_count
        if image_type_limit is not UNSET:
            field_dict["ImageTypeLimit"] = image_type_limit
        if enable_image_types is not UNSET:
            field_dict["EnableImageTypes"] = enable_image_types
        if enable_user_data is not UNSET:
            field_dict["EnableUserData"] = enable_user_data
        if series_timer_id is not UNSET:
            field_dict["SeriesTimerId"] = series_timer_id
        if library_series_id is not UNSET:
            field_dict["LibrarySeriesId"] = library_series_id
        if fields is not UNSET:
            field_dict["Fields"] = fields

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        channel_ids = cast(List[str], d.pop("ChannelIds", UNSET))

        user_id = d.pop("UserId", UNSET)

        _min_start_date = d.pop("MinStartDate", UNSET)
        min_start_date: Union[Unset, None, datetime.datetime]
        if _min_start_date is None:
            min_start_date = None
        elif isinstance(_min_start_date, Unset):
            min_start_date = UNSET
        else:
            min_start_date = isoparse(_min_start_date)

        has_aired = d.pop("HasAired", UNSET)

        is_airing = d.pop("IsAiring", UNSET)

        _max_start_date = d.pop("MaxStartDate", UNSET)
        max_start_date: Union[Unset, None, datetime.datetime]
        if _max_start_date is None:
            max_start_date = None
        elif isinstance(_max_start_date, Unset):
            max_start_date = UNSET
        else:
            max_start_date = isoparse(_max_start_date)

        _min_end_date = d.pop("MinEndDate", UNSET)
        min_end_date: Union[Unset, None, datetime.datetime]
        if _min_end_date is None:
            min_end_date = None
        elif isinstance(_min_end_date, Unset):
            min_end_date = UNSET
        else:
            min_end_date = isoparse(_min_end_date)

        _max_end_date = d.pop("MaxEndDate", UNSET)
        max_end_date: Union[Unset, None, datetime.datetime]
        if _max_end_date is None:
            max_end_date = None
        elif isinstance(_max_end_date, Unset):
            max_end_date = UNSET
        else:
            max_end_date = isoparse(_max_end_date)

        is_movie = d.pop("IsMovie", UNSET)

        is_series = d.pop("IsSeries", UNSET)

        is_news = d.pop("IsNews", UNSET)

        is_kids = d.pop("IsKids", UNSET)

        is_sports = d.pop("IsSports", UNSET)

        start_index = d.pop("StartIndex", UNSET)

        limit = d.pop("Limit", UNSET)

        sort_by = cast(List[str], d.pop("SortBy", UNSET))

        sort_order = []
        _sort_order = d.pop("SortOrder", UNSET)
        for sort_order_item_data in _sort_order or []:
            sort_order_item = SortOrder(sort_order_item_data)

            sort_order.append(sort_order_item)

        genres = cast(List[str], d.pop("Genres", UNSET))

        genre_ids = cast(List[str], d.pop("GenreIds", UNSET))

        enable_images = d.pop("EnableImages", UNSET)

        enable_total_record_count = d.pop("EnableTotalRecordCount", UNSET)

        image_type_limit = d.pop("ImageTypeLimit", UNSET)

        enable_image_types = []
        _enable_image_types = d.pop("EnableImageTypes", UNSET)
        for enable_image_types_item_data in _enable_image_types or []:
            enable_image_types_item = ImageType(enable_image_types_item_data)

            enable_image_types.append(enable_image_types_item)

        enable_user_data = d.pop("EnableUserData", UNSET)

        series_timer_id = d.pop("SeriesTimerId", UNSET)

        library_series_id = d.pop("LibrarySeriesId", UNSET)

        fields = []
        _fields = d.pop("Fields", UNSET)
        for fields_item_data in _fields or []:
            fields_item = ItemFields(fields_item_data)

            fields.append(fields_item)

        get_programs_dto = cls(
            channel_ids=channel_ids,
            user_id=user_id,
            min_start_date=min_start_date,
            has_aired=has_aired,
            is_airing=is_airing,
            max_start_date=max_start_date,
            min_end_date=min_end_date,
            max_end_date=max_end_date,
            is_movie=is_movie,
            is_series=is_series,
            is_news=is_news,
            is_kids=is_kids,
            is_sports=is_sports,
            start_index=start_index,
            limit=limit,
            sort_by=sort_by,
            sort_order=sort_order,
            genres=genres,
            genre_ids=genre_ids,
            enable_images=enable_images,
            enable_total_record_count=enable_total_record_count,
            image_type_limit=image_type_limit,
            enable_image_types=enable_image_types,
            enable_user_data=enable_user_data,
            series_timer_id=series_timer_id,
            library_series_id=library_series_id,
            fields=fields,
        )

        return get_programs_dto
