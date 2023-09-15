import datetime
from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.base_item_dto_query_result import BaseItemDtoQueryResult
from ...models.base_item_kind import BaseItemKind
from ...models.image_type import ImageType
from ...models.item_fields import ItemFields
from ...models.item_filter import ItemFilter
from ...models.location_type import LocationType
from ...models.series_status import SeriesStatus
from ...models.sort_order import SortOrder
from ...models.video_type import VideoType
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    user_id: Union[Unset, None, str] = UNSET,
    max_official_rating: Union[Unset, None, str] = UNSET,
    has_theme_song: Union[Unset, None, bool] = UNSET,
    has_theme_video: Union[Unset, None, bool] = UNSET,
    has_subtitles: Union[Unset, None, bool] = UNSET,
    has_special_feature: Union[Unset, None, bool] = UNSET,
    has_trailer: Union[Unset, None, bool] = UNSET,
    adjacent_to: Union[Unset, None, str] = UNSET,
    parent_index_number: Union[Unset, None, int] = UNSET,
    has_parental_rating: Union[Unset, None, bool] = UNSET,
    is_hd: Union[Unset, None, bool] = UNSET,
    is_4k: Union[Unset, None, bool] = UNSET,
    location_types: Union[Unset, None, List[LocationType]] = UNSET,
    exclude_location_types: Union[Unset, None, List[LocationType]] = UNSET,
    is_missing: Union[Unset, None, bool] = UNSET,
    is_unaired: Union[Unset, None, bool] = UNSET,
    min_community_rating: Union[Unset, None, float] = UNSET,
    min_critic_rating: Union[Unset, None, float] = UNSET,
    min_premiere_date: Union[Unset, None, datetime.datetime] = UNSET,
    min_date_last_saved: Union[Unset, None, datetime.datetime] = UNSET,
    min_date_last_saved_for_user: Union[Unset, None, datetime.datetime] = UNSET,
    max_premiere_date: Union[Unset, None, datetime.datetime] = UNSET,
    has_overview: Union[Unset, None, bool] = UNSET,
    has_imdb_id: Union[Unset, None, bool] = UNSET,
    has_tmdb_id: Union[Unset, None, bool] = UNSET,
    has_tvdb_id: Union[Unset, None, bool] = UNSET,
    is_movie: Union[Unset, None, bool] = UNSET,
    is_series: Union[Unset, None, bool] = UNSET,
    is_news: Union[Unset, None, bool] = UNSET,
    is_kids: Union[Unset, None, bool] = UNSET,
    is_sports: Union[Unset, None, bool] = UNSET,
    exclude_item_ids: Union[Unset, None, List[str]] = UNSET,
    start_index: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    recursive: Union[Unset, None, bool] = UNSET,
    search_term: Union[Unset, None, str] = UNSET,
    sort_order: Union[Unset, None, List[SortOrder]] = UNSET,
    parent_id: Union[Unset, None, str] = UNSET,
    fields: Union[Unset, None, List[ItemFields]] = UNSET,
    exclude_item_types: Union[Unset, None, List[BaseItemKind]] = UNSET,
    filters: Union[Unset, None, List[ItemFilter]] = UNSET,
    is_favorite: Union[Unset, None, bool] = UNSET,
    media_types: Union[Unset, None, List[str]] = UNSET,
    image_types: Union[Unset, None, List[ImageType]] = UNSET,
    sort_by: Union[Unset, None, List[str]] = UNSET,
    is_played: Union[Unset, None, bool] = UNSET,
    genres: Union[Unset, None, List[str]] = UNSET,
    official_ratings: Union[Unset, None, List[str]] = UNSET,
    tags: Union[Unset, None, List[str]] = UNSET,
    years: Union[Unset, None, List[int]] = UNSET,
    enable_user_data: Union[Unset, None, bool] = UNSET,
    image_type_limit: Union[Unset, None, int] = UNSET,
    enable_image_types: Union[Unset, None, List[ImageType]] = UNSET,
    person: Union[Unset, None, str] = UNSET,
    person_ids: Union[Unset, None, List[str]] = UNSET,
    person_types: Union[Unset, None, List[str]] = UNSET,
    studios: Union[Unset, None, List[str]] = UNSET,
    artists: Union[Unset, None, List[str]] = UNSET,
    exclude_artist_ids: Union[Unset, None, List[str]] = UNSET,
    artist_ids: Union[Unset, None, List[str]] = UNSET,
    album_artist_ids: Union[Unset, None, List[str]] = UNSET,
    contributing_artist_ids: Union[Unset, None, List[str]] = UNSET,
    albums: Union[Unset, None, List[str]] = UNSET,
    album_ids: Union[Unset, None, List[str]] = UNSET,
    ids: Union[Unset, None, List[str]] = UNSET,
    video_types: Union[Unset, None, List[VideoType]] = UNSET,
    min_official_rating: Union[Unset, None, str] = UNSET,
    is_locked: Union[Unset, None, bool] = UNSET,
    is_place_holder: Union[Unset, None, bool] = UNSET,
    has_official_rating: Union[Unset, None, bool] = UNSET,
    collapse_box_set_items: Union[Unset, None, bool] = UNSET,
    min_width: Union[Unset, None, int] = UNSET,
    min_height: Union[Unset, None, int] = UNSET,
    max_width: Union[Unset, None, int] = UNSET,
    max_height: Union[Unset, None, int] = UNSET,
    is_3d: Union[Unset, None, bool] = UNSET,
    series_status: Union[Unset, None, List[SeriesStatus]] = UNSET,
    name_starts_with_or_greater: Union[Unset, None, str] = UNSET,
    name_starts_with: Union[Unset, None, str] = UNSET,
    name_less_than: Union[Unset, None, str] = UNSET,
    studio_ids: Union[Unset, None, List[str]] = UNSET,
    genre_ids: Union[Unset, None, List[str]] = UNSET,
    enable_total_record_count: Union[Unset, None, bool] = True,
    enable_images: Union[Unset, None, bool] = True,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    params["userId"] = user_id

    params["maxOfficialRating"] = max_official_rating

    params["hasThemeSong"] = has_theme_song

    params["hasThemeVideo"] = has_theme_video

    params["hasSubtitles"] = has_subtitles

    params["hasSpecialFeature"] = has_special_feature

    params["hasTrailer"] = has_trailer

    params["adjacentTo"] = adjacent_to

    params["parentIndexNumber"] = parent_index_number

    params["hasParentalRating"] = has_parental_rating

    params["isHd"] = is_hd

    params["is4K"] = is_4k

    json_location_types: Union[Unset, None, List[str]] = UNSET
    if not isinstance(location_types, Unset):
        if location_types is None:
            json_location_types = None
        else:
            json_location_types = []
            for location_types_item_data in location_types:
                location_types_item = location_types_item_data.value

                json_location_types.append(location_types_item)

    params["locationTypes"] = json_location_types

    json_exclude_location_types: Union[Unset, None, List[str]] = UNSET
    if not isinstance(exclude_location_types, Unset):
        if exclude_location_types is None:
            json_exclude_location_types = None
        else:
            json_exclude_location_types = []
            for exclude_location_types_item_data in exclude_location_types:
                exclude_location_types_item = exclude_location_types_item_data.value

                json_exclude_location_types.append(exclude_location_types_item)

    params["excludeLocationTypes"] = json_exclude_location_types

    params["isMissing"] = is_missing

    params["isUnaired"] = is_unaired

    params["minCommunityRating"] = min_community_rating

    params["minCriticRating"] = min_critic_rating

    json_min_premiere_date: Union[Unset, None, str] = UNSET
    if not isinstance(min_premiere_date, Unset):
        json_min_premiere_date = min_premiere_date.isoformat() if min_premiere_date else None

    params["minPremiereDate"] = json_min_premiere_date

    json_min_date_last_saved: Union[Unset, None, str] = UNSET
    if not isinstance(min_date_last_saved, Unset):
        json_min_date_last_saved = min_date_last_saved.isoformat() if min_date_last_saved else None

    params["minDateLastSaved"] = json_min_date_last_saved

    json_min_date_last_saved_for_user: Union[Unset, None, str] = UNSET
    if not isinstance(min_date_last_saved_for_user, Unset):
        json_min_date_last_saved_for_user = (
            min_date_last_saved_for_user.isoformat() if min_date_last_saved_for_user else None
        )

    params["minDateLastSavedForUser"] = json_min_date_last_saved_for_user

    json_max_premiere_date: Union[Unset, None, str] = UNSET
    if not isinstance(max_premiere_date, Unset):
        json_max_premiere_date = max_premiere_date.isoformat() if max_premiere_date else None

    params["maxPremiereDate"] = json_max_premiere_date

    params["hasOverview"] = has_overview

    params["hasImdbId"] = has_imdb_id

    params["hasTmdbId"] = has_tmdb_id

    params["hasTvdbId"] = has_tvdb_id

    params["isMovie"] = is_movie

    params["isSeries"] = is_series

    params["isNews"] = is_news

    params["isKids"] = is_kids

    params["isSports"] = is_sports

    json_exclude_item_ids: Union[Unset, None, List[str]] = UNSET
    if not isinstance(exclude_item_ids, Unset):
        if exclude_item_ids is None:
            json_exclude_item_ids = None
        else:
            json_exclude_item_ids = exclude_item_ids

    params["excludeItemIds"] = json_exclude_item_ids

    params["startIndex"] = start_index

    params["limit"] = limit

    params["recursive"] = recursive

    params["searchTerm"] = search_term

    json_sort_order: Union[Unset, None, List[str]] = UNSET
    if not isinstance(sort_order, Unset):
        if sort_order is None:
            json_sort_order = None
        else:
            json_sort_order = []
            for sort_order_item_data in sort_order:
                sort_order_item = sort_order_item_data.value

                json_sort_order.append(sort_order_item)

    params["sortOrder"] = json_sort_order

    params["parentId"] = parent_id

    json_fields: Union[Unset, None, List[str]] = UNSET
    if not isinstance(fields, Unset):
        if fields is None:
            json_fields = None
        else:
            json_fields = []
            for fields_item_data in fields:
                fields_item = fields_item_data.value

                json_fields.append(fields_item)

    params["fields"] = json_fields

    json_exclude_item_types: Union[Unset, None, List[str]] = UNSET
    if not isinstance(exclude_item_types, Unset):
        if exclude_item_types is None:
            json_exclude_item_types = None
        else:
            json_exclude_item_types = []
            for exclude_item_types_item_data in exclude_item_types:
                exclude_item_types_item = exclude_item_types_item_data.value

                json_exclude_item_types.append(exclude_item_types_item)

    params["excludeItemTypes"] = json_exclude_item_types

    json_filters: Union[Unset, None, List[str]] = UNSET
    if not isinstance(filters, Unset):
        if filters is None:
            json_filters = None
        else:
            json_filters = []
            for filters_item_data in filters:
                filters_item = filters_item_data.value

                json_filters.append(filters_item)

    params["filters"] = json_filters

    params["isFavorite"] = is_favorite

    json_media_types: Union[Unset, None, List[str]] = UNSET
    if not isinstance(media_types, Unset):
        if media_types is None:
            json_media_types = None
        else:
            json_media_types = media_types

    params["mediaTypes"] = json_media_types

    json_image_types: Union[Unset, None, List[str]] = UNSET
    if not isinstance(image_types, Unset):
        if image_types is None:
            json_image_types = None
        else:
            json_image_types = []
            for image_types_item_data in image_types:
                image_types_item = image_types_item_data.value

                json_image_types.append(image_types_item)

    params["imageTypes"] = json_image_types

    json_sort_by: Union[Unset, None, List[str]] = UNSET
    if not isinstance(sort_by, Unset):
        if sort_by is None:
            json_sort_by = None
        else:
            json_sort_by = sort_by

    params["sortBy"] = json_sort_by

    params["isPlayed"] = is_played

    json_genres: Union[Unset, None, List[str]] = UNSET
    if not isinstance(genres, Unset):
        if genres is None:
            json_genres = None
        else:
            json_genres = genres

    params["genres"] = json_genres

    json_official_ratings: Union[Unset, None, List[str]] = UNSET
    if not isinstance(official_ratings, Unset):
        if official_ratings is None:
            json_official_ratings = None
        else:
            json_official_ratings = official_ratings

    params["officialRatings"] = json_official_ratings

    json_tags: Union[Unset, None, List[str]] = UNSET
    if not isinstance(tags, Unset):
        if tags is None:
            json_tags = None
        else:
            json_tags = tags

    params["tags"] = json_tags

    json_years: Union[Unset, None, List[int]] = UNSET
    if not isinstance(years, Unset):
        if years is None:
            json_years = None
        else:
            json_years = years

    params["years"] = json_years

    params["enableUserData"] = enable_user_data

    params["imageTypeLimit"] = image_type_limit

    json_enable_image_types: Union[Unset, None, List[str]] = UNSET
    if not isinstance(enable_image_types, Unset):
        if enable_image_types is None:
            json_enable_image_types = None
        else:
            json_enable_image_types = []
            for enable_image_types_item_data in enable_image_types:
                enable_image_types_item = enable_image_types_item_data.value

                json_enable_image_types.append(enable_image_types_item)

    params["enableImageTypes"] = json_enable_image_types

    params["person"] = person

    json_person_ids: Union[Unset, None, List[str]] = UNSET
    if not isinstance(person_ids, Unset):
        if person_ids is None:
            json_person_ids = None
        else:
            json_person_ids = person_ids

    params["personIds"] = json_person_ids

    json_person_types: Union[Unset, None, List[str]] = UNSET
    if not isinstance(person_types, Unset):
        if person_types is None:
            json_person_types = None
        else:
            json_person_types = person_types

    params["personTypes"] = json_person_types

    json_studios: Union[Unset, None, List[str]] = UNSET
    if not isinstance(studios, Unset):
        if studios is None:
            json_studios = None
        else:
            json_studios = studios

    params["studios"] = json_studios

    json_artists: Union[Unset, None, List[str]] = UNSET
    if not isinstance(artists, Unset):
        if artists is None:
            json_artists = None
        else:
            json_artists = artists

    params["artists"] = json_artists

    json_exclude_artist_ids: Union[Unset, None, List[str]] = UNSET
    if not isinstance(exclude_artist_ids, Unset):
        if exclude_artist_ids is None:
            json_exclude_artist_ids = None
        else:
            json_exclude_artist_ids = exclude_artist_ids

    params["excludeArtistIds"] = json_exclude_artist_ids

    json_artist_ids: Union[Unset, None, List[str]] = UNSET
    if not isinstance(artist_ids, Unset):
        if artist_ids is None:
            json_artist_ids = None
        else:
            json_artist_ids = artist_ids

    params["artistIds"] = json_artist_ids

    json_album_artist_ids: Union[Unset, None, List[str]] = UNSET
    if not isinstance(album_artist_ids, Unset):
        if album_artist_ids is None:
            json_album_artist_ids = None
        else:
            json_album_artist_ids = album_artist_ids

    params["albumArtistIds"] = json_album_artist_ids

    json_contributing_artist_ids: Union[Unset, None, List[str]] = UNSET
    if not isinstance(contributing_artist_ids, Unset):
        if contributing_artist_ids is None:
            json_contributing_artist_ids = None
        else:
            json_contributing_artist_ids = contributing_artist_ids

    params["contributingArtistIds"] = json_contributing_artist_ids

    json_albums: Union[Unset, None, List[str]] = UNSET
    if not isinstance(albums, Unset):
        if albums is None:
            json_albums = None
        else:
            json_albums = albums

    params["albums"] = json_albums

    json_album_ids: Union[Unset, None, List[str]] = UNSET
    if not isinstance(album_ids, Unset):
        if album_ids is None:
            json_album_ids = None
        else:
            json_album_ids = album_ids

    params["albumIds"] = json_album_ids

    json_ids: Union[Unset, None, List[str]] = UNSET
    if not isinstance(ids, Unset):
        if ids is None:
            json_ids = None
        else:
            json_ids = ids

    params["ids"] = json_ids

    json_video_types: Union[Unset, None, List[str]] = UNSET
    if not isinstance(video_types, Unset):
        if video_types is None:
            json_video_types = None
        else:
            json_video_types = []
            for video_types_item_data in video_types:
                video_types_item = video_types_item_data.value

                json_video_types.append(video_types_item)

    params["videoTypes"] = json_video_types

    params["minOfficialRating"] = min_official_rating

    params["isLocked"] = is_locked

    params["isPlaceHolder"] = is_place_holder

    params["hasOfficialRating"] = has_official_rating

    params["collapseBoxSetItems"] = collapse_box_set_items

    params["minWidth"] = min_width

    params["minHeight"] = min_height

    params["maxWidth"] = max_width

    params["maxHeight"] = max_height

    params["is3D"] = is_3d

    json_series_status: Union[Unset, None, List[str]] = UNSET
    if not isinstance(series_status, Unset):
        if series_status is None:
            json_series_status = None
        else:
            json_series_status = []
            for series_status_item_data in series_status:
                series_status_item = series_status_item_data.value

                json_series_status.append(series_status_item)

    params["seriesStatus"] = json_series_status

    params["nameStartsWithOrGreater"] = name_starts_with_or_greater

    params["nameStartsWith"] = name_starts_with

    params["nameLessThan"] = name_less_than

    json_studio_ids: Union[Unset, None, List[str]] = UNSET
    if not isinstance(studio_ids, Unset):
        if studio_ids is None:
            json_studio_ids = None
        else:
            json_studio_ids = studio_ids

    params["studioIds"] = json_studio_ids

    json_genre_ids: Union[Unset, None, List[str]] = UNSET
    if not isinstance(genre_ids, Unset):
        if genre_ids is None:
            json_genre_ids = None
        else:
            json_genre_ids = genre_ids

    params["genreIds"] = json_genre_ids

    params["enableTotalRecordCount"] = enable_total_record_count

    params["enableImages"] = enable_images

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/Trailers",
        "params": params,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, BaseItemDtoQueryResult]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = BaseItemDtoQueryResult.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = cast(Any, None)
        return response_403
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, BaseItemDtoQueryResult]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    user_id: Union[Unset, None, str] = UNSET,
    max_official_rating: Union[Unset, None, str] = UNSET,
    has_theme_song: Union[Unset, None, bool] = UNSET,
    has_theme_video: Union[Unset, None, bool] = UNSET,
    has_subtitles: Union[Unset, None, bool] = UNSET,
    has_special_feature: Union[Unset, None, bool] = UNSET,
    has_trailer: Union[Unset, None, bool] = UNSET,
    adjacent_to: Union[Unset, None, str] = UNSET,
    parent_index_number: Union[Unset, None, int] = UNSET,
    has_parental_rating: Union[Unset, None, bool] = UNSET,
    is_hd: Union[Unset, None, bool] = UNSET,
    is_4k: Union[Unset, None, bool] = UNSET,
    location_types: Union[Unset, None, List[LocationType]] = UNSET,
    exclude_location_types: Union[Unset, None, List[LocationType]] = UNSET,
    is_missing: Union[Unset, None, bool] = UNSET,
    is_unaired: Union[Unset, None, bool] = UNSET,
    min_community_rating: Union[Unset, None, float] = UNSET,
    min_critic_rating: Union[Unset, None, float] = UNSET,
    min_premiere_date: Union[Unset, None, datetime.datetime] = UNSET,
    min_date_last_saved: Union[Unset, None, datetime.datetime] = UNSET,
    min_date_last_saved_for_user: Union[Unset, None, datetime.datetime] = UNSET,
    max_premiere_date: Union[Unset, None, datetime.datetime] = UNSET,
    has_overview: Union[Unset, None, bool] = UNSET,
    has_imdb_id: Union[Unset, None, bool] = UNSET,
    has_tmdb_id: Union[Unset, None, bool] = UNSET,
    has_tvdb_id: Union[Unset, None, bool] = UNSET,
    is_movie: Union[Unset, None, bool] = UNSET,
    is_series: Union[Unset, None, bool] = UNSET,
    is_news: Union[Unset, None, bool] = UNSET,
    is_kids: Union[Unset, None, bool] = UNSET,
    is_sports: Union[Unset, None, bool] = UNSET,
    exclude_item_ids: Union[Unset, None, List[str]] = UNSET,
    start_index: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    recursive: Union[Unset, None, bool] = UNSET,
    search_term: Union[Unset, None, str] = UNSET,
    sort_order: Union[Unset, None, List[SortOrder]] = UNSET,
    parent_id: Union[Unset, None, str] = UNSET,
    fields: Union[Unset, None, List[ItemFields]] = UNSET,
    exclude_item_types: Union[Unset, None, List[BaseItemKind]] = UNSET,
    filters: Union[Unset, None, List[ItemFilter]] = UNSET,
    is_favorite: Union[Unset, None, bool] = UNSET,
    media_types: Union[Unset, None, List[str]] = UNSET,
    image_types: Union[Unset, None, List[ImageType]] = UNSET,
    sort_by: Union[Unset, None, List[str]] = UNSET,
    is_played: Union[Unset, None, bool] = UNSET,
    genres: Union[Unset, None, List[str]] = UNSET,
    official_ratings: Union[Unset, None, List[str]] = UNSET,
    tags: Union[Unset, None, List[str]] = UNSET,
    years: Union[Unset, None, List[int]] = UNSET,
    enable_user_data: Union[Unset, None, bool] = UNSET,
    image_type_limit: Union[Unset, None, int] = UNSET,
    enable_image_types: Union[Unset, None, List[ImageType]] = UNSET,
    person: Union[Unset, None, str] = UNSET,
    person_ids: Union[Unset, None, List[str]] = UNSET,
    person_types: Union[Unset, None, List[str]] = UNSET,
    studios: Union[Unset, None, List[str]] = UNSET,
    artists: Union[Unset, None, List[str]] = UNSET,
    exclude_artist_ids: Union[Unset, None, List[str]] = UNSET,
    artist_ids: Union[Unset, None, List[str]] = UNSET,
    album_artist_ids: Union[Unset, None, List[str]] = UNSET,
    contributing_artist_ids: Union[Unset, None, List[str]] = UNSET,
    albums: Union[Unset, None, List[str]] = UNSET,
    album_ids: Union[Unset, None, List[str]] = UNSET,
    ids: Union[Unset, None, List[str]] = UNSET,
    video_types: Union[Unset, None, List[VideoType]] = UNSET,
    min_official_rating: Union[Unset, None, str] = UNSET,
    is_locked: Union[Unset, None, bool] = UNSET,
    is_place_holder: Union[Unset, None, bool] = UNSET,
    has_official_rating: Union[Unset, None, bool] = UNSET,
    collapse_box_set_items: Union[Unset, None, bool] = UNSET,
    min_width: Union[Unset, None, int] = UNSET,
    min_height: Union[Unset, None, int] = UNSET,
    max_width: Union[Unset, None, int] = UNSET,
    max_height: Union[Unset, None, int] = UNSET,
    is_3d: Union[Unset, None, bool] = UNSET,
    series_status: Union[Unset, None, List[SeriesStatus]] = UNSET,
    name_starts_with_or_greater: Union[Unset, None, str] = UNSET,
    name_starts_with: Union[Unset, None, str] = UNSET,
    name_less_than: Union[Unset, None, str] = UNSET,
    studio_ids: Union[Unset, None, List[str]] = UNSET,
    genre_ids: Union[Unset, None, List[str]] = UNSET,
    enable_total_record_count: Union[Unset, None, bool] = True,
    enable_images: Union[Unset, None, bool] = True,
) -> Response[Union[Any, BaseItemDtoQueryResult]]:
    """Finds movies and trailers similar to a given trailer.

    Args:
        user_id (Union[Unset, None, str]):
        max_official_rating (Union[Unset, None, str]):
        has_theme_song (Union[Unset, None, bool]):
        has_theme_video (Union[Unset, None, bool]):
        has_subtitles (Union[Unset, None, bool]):
        has_special_feature (Union[Unset, None, bool]):
        has_trailer (Union[Unset, None, bool]):
        adjacent_to (Union[Unset, None, str]):
        parent_index_number (Union[Unset, None, int]):
        has_parental_rating (Union[Unset, None, bool]):
        is_hd (Union[Unset, None, bool]):
        is_4k (Union[Unset, None, bool]):
        location_types (Union[Unset, None, List[LocationType]]):
        exclude_location_types (Union[Unset, None, List[LocationType]]):
        is_missing (Union[Unset, None, bool]):
        is_unaired (Union[Unset, None, bool]):
        min_community_rating (Union[Unset, None, float]):
        min_critic_rating (Union[Unset, None, float]):
        min_premiere_date (Union[Unset, None, datetime.datetime]):
        min_date_last_saved (Union[Unset, None, datetime.datetime]):
        min_date_last_saved_for_user (Union[Unset, None, datetime.datetime]):
        max_premiere_date (Union[Unset, None, datetime.datetime]):
        has_overview (Union[Unset, None, bool]):
        has_imdb_id (Union[Unset, None, bool]):
        has_tmdb_id (Union[Unset, None, bool]):
        has_tvdb_id (Union[Unset, None, bool]):
        is_movie (Union[Unset, None, bool]):
        is_series (Union[Unset, None, bool]):
        is_news (Union[Unset, None, bool]):
        is_kids (Union[Unset, None, bool]):
        is_sports (Union[Unset, None, bool]):
        exclude_item_ids (Union[Unset, None, List[str]]):
        start_index (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):
        recursive (Union[Unset, None, bool]):
        search_term (Union[Unset, None, str]):
        sort_order (Union[Unset, None, List[SortOrder]]):
        parent_id (Union[Unset, None, str]):
        fields (Union[Unset, None, List[ItemFields]]):
        exclude_item_types (Union[Unset, None, List[BaseItemKind]]):
        filters (Union[Unset, None, List[ItemFilter]]):
        is_favorite (Union[Unset, None, bool]):
        media_types (Union[Unset, None, List[str]]):
        image_types (Union[Unset, None, List[ImageType]]):
        sort_by (Union[Unset, None, List[str]]):
        is_played (Union[Unset, None, bool]):
        genres (Union[Unset, None, List[str]]):
        official_ratings (Union[Unset, None, List[str]]):
        tags (Union[Unset, None, List[str]]):
        years (Union[Unset, None, List[int]]):
        enable_user_data (Union[Unset, None, bool]):
        image_type_limit (Union[Unset, None, int]):
        enable_image_types (Union[Unset, None, List[ImageType]]):
        person (Union[Unset, None, str]):
        person_ids (Union[Unset, None, List[str]]):
        person_types (Union[Unset, None, List[str]]):
        studios (Union[Unset, None, List[str]]):
        artists (Union[Unset, None, List[str]]):
        exclude_artist_ids (Union[Unset, None, List[str]]):
        artist_ids (Union[Unset, None, List[str]]):
        album_artist_ids (Union[Unset, None, List[str]]):
        contributing_artist_ids (Union[Unset, None, List[str]]):
        albums (Union[Unset, None, List[str]]):
        album_ids (Union[Unset, None, List[str]]):
        ids (Union[Unset, None, List[str]]):
        video_types (Union[Unset, None, List[VideoType]]):
        min_official_rating (Union[Unset, None, str]):
        is_locked (Union[Unset, None, bool]):
        is_place_holder (Union[Unset, None, bool]):
        has_official_rating (Union[Unset, None, bool]):
        collapse_box_set_items (Union[Unset, None, bool]):
        min_width (Union[Unset, None, int]):
        min_height (Union[Unset, None, int]):
        max_width (Union[Unset, None, int]):
        max_height (Union[Unset, None, int]):
        is_3d (Union[Unset, None, bool]):
        series_status (Union[Unset, None, List[SeriesStatus]]):
        name_starts_with_or_greater (Union[Unset, None, str]):
        name_starts_with (Union[Unset, None, str]):
        name_less_than (Union[Unset, None, str]):
        studio_ids (Union[Unset, None, List[str]]):
        genre_ids (Union[Unset, None, List[str]]):
        enable_total_record_count (Union[Unset, None, bool]):  Default: True.
        enable_images (Union[Unset, None, bool]):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, BaseItemDtoQueryResult]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        max_official_rating=max_official_rating,
        has_theme_song=has_theme_song,
        has_theme_video=has_theme_video,
        has_subtitles=has_subtitles,
        has_special_feature=has_special_feature,
        has_trailer=has_trailer,
        adjacent_to=adjacent_to,
        parent_index_number=parent_index_number,
        has_parental_rating=has_parental_rating,
        is_hd=is_hd,
        is_4k=is_4k,
        location_types=location_types,
        exclude_location_types=exclude_location_types,
        is_missing=is_missing,
        is_unaired=is_unaired,
        min_community_rating=min_community_rating,
        min_critic_rating=min_critic_rating,
        min_premiere_date=min_premiere_date,
        min_date_last_saved=min_date_last_saved,
        min_date_last_saved_for_user=min_date_last_saved_for_user,
        max_premiere_date=max_premiere_date,
        has_overview=has_overview,
        has_imdb_id=has_imdb_id,
        has_tmdb_id=has_tmdb_id,
        has_tvdb_id=has_tvdb_id,
        is_movie=is_movie,
        is_series=is_series,
        is_news=is_news,
        is_kids=is_kids,
        is_sports=is_sports,
        exclude_item_ids=exclude_item_ids,
        start_index=start_index,
        limit=limit,
        recursive=recursive,
        search_term=search_term,
        sort_order=sort_order,
        parent_id=parent_id,
        fields=fields,
        exclude_item_types=exclude_item_types,
        filters=filters,
        is_favorite=is_favorite,
        media_types=media_types,
        image_types=image_types,
        sort_by=sort_by,
        is_played=is_played,
        genres=genres,
        official_ratings=official_ratings,
        tags=tags,
        years=years,
        enable_user_data=enable_user_data,
        image_type_limit=image_type_limit,
        enable_image_types=enable_image_types,
        person=person,
        person_ids=person_ids,
        person_types=person_types,
        studios=studios,
        artists=artists,
        exclude_artist_ids=exclude_artist_ids,
        artist_ids=artist_ids,
        album_artist_ids=album_artist_ids,
        contributing_artist_ids=contributing_artist_ids,
        albums=albums,
        album_ids=album_ids,
        ids=ids,
        video_types=video_types,
        min_official_rating=min_official_rating,
        is_locked=is_locked,
        is_place_holder=is_place_holder,
        has_official_rating=has_official_rating,
        collapse_box_set_items=collapse_box_set_items,
        min_width=min_width,
        min_height=min_height,
        max_width=max_width,
        max_height=max_height,
        is_3d=is_3d,
        series_status=series_status,
        name_starts_with_or_greater=name_starts_with_or_greater,
        name_starts_with=name_starts_with,
        name_less_than=name_less_than,
        studio_ids=studio_ids,
        genre_ids=genre_ids,
        enable_total_record_count=enable_total_record_count,
        enable_images=enable_images,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    user_id: Union[Unset, None, str] = UNSET,
    max_official_rating: Union[Unset, None, str] = UNSET,
    has_theme_song: Union[Unset, None, bool] = UNSET,
    has_theme_video: Union[Unset, None, bool] = UNSET,
    has_subtitles: Union[Unset, None, bool] = UNSET,
    has_special_feature: Union[Unset, None, bool] = UNSET,
    has_trailer: Union[Unset, None, bool] = UNSET,
    adjacent_to: Union[Unset, None, str] = UNSET,
    parent_index_number: Union[Unset, None, int] = UNSET,
    has_parental_rating: Union[Unset, None, bool] = UNSET,
    is_hd: Union[Unset, None, bool] = UNSET,
    is_4k: Union[Unset, None, bool] = UNSET,
    location_types: Union[Unset, None, List[LocationType]] = UNSET,
    exclude_location_types: Union[Unset, None, List[LocationType]] = UNSET,
    is_missing: Union[Unset, None, bool] = UNSET,
    is_unaired: Union[Unset, None, bool] = UNSET,
    min_community_rating: Union[Unset, None, float] = UNSET,
    min_critic_rating: Union[Unset, None, float] = UNSET,
    min_premiere_date: Union[Unset, None, datetime.datetime] = UNSET,
    min_date_last_saved: Union[Unset, None, datetime.datetime] = UNSET,
    min_date_last_saved_for_user: Union[Unset, None, datetime.datetime] = UNSET,
    max_premiere_date: Union[Unset, None, datetime.datetime] = UNSET,
    has_overview: Union[Unset, None, bool] = UNSET,
    has_imdb_id: Union[Unset, None, bool] = UNSET,
    has_tmdb_id: Union[Unset, None, bool] = UNSET,
    has_tvdb_id: Union[Unset, None, bool] = UNSET,
    is_movie: Union[Unset, None, bool] = UNSET,
    is_series: Union[Unset, None, bool] = UNSET,
    is_news: Union[Unset, None, bool] = UNSET,
    is_kids: Union[Unset, None, bool] = UNSET,
    is_sports: Union[Unset, None, bool] = UNSET,
    exclude_item_ids: Union[Unset, None, List[str]] = UNSET,
    start_index: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    recursive: Union[Unset, None, bool] = UNSET,
    search_term: Union[Unset, None, str] = UNSET,
    sort_order: Union[Unset, None, List[SortOrder]] = UNSET,
    parent_id: Union[Unset, None, str] = UNSET,
    fields: Union[Unset, None, List[ItemFields]] = UNSET,
    exclude_item_types: Union[Unset, None, List[BaseItemKind]] = UNSET,
    filters: Union[Unset, None, List[ItemFilter]] = UNSET,
    is_favorite: Union[Unset, None, bool] = UNSET,
    media_types: Union[Unset, None, List[str]] = UNSET,
    image_types: Union[Unset, None, List[ImageType]] = UNSET,
    sort_by: Union[Unset, None, List[str]] = UNSET,
    is_played: Union[Unset, None, bool] = UNSET,
    genres: Union[Unset, None, List[str]] = UNSET,
    official_ratings: Union[Unset, None, List[str]] = UNSET,
    tags: Union[Unset, None, List[str]] = UNSET,
    years: Union[Unset, None, List[int]] = UNSET,
    enable_user_data: Union[Unset, None, bool] = UNSET,
    image_type_limit: Union[Unset, None, int] = UNSET,
    enable_image_types: Union[Unset, None, List[ImageType]] = UNSET,
    person: Union[Unset, None, str] = UNSET,
    person_ids: Union[Unset, None, List[str]] = UNSET,
    person_types: Union[Unset, None, List[str]] = UNSET,
    studios: Union[Unset, None, List[str]] = UNSET,
    artists: Union[Unset, None, List[str]] = UNSET,
    exclude_artist_ids: Union[Unset, None, List[str]] = UNSET,
    artist_ids: Union[Unset, None, List[str]] = UNSET,
    album_artist_ids: Union[Unset, None, List[str]] = UNSET,
    contributing_artist_ids: Union[Unset, None, List[str]] = UNSET,
    albums: Union[Unset, None, List[str]] = UNSET,
    album_ids: Union[Unset, None, List[str]] = UNSET,
    ids: Union[Unset, None, List[str]] = UNSET,
    video_types: Union[Unset, None, List[VideoType]] = UNSET,
    min_official_rating: Union[Unset, None, str] = UNSET,
    is_locked: Union[Unset, None, bool] = UNSET,
    is_place_holder: Union[Unset, None, bool] = UNSET,
    has_official_rating: Union[Unset, None, bool] = UNSET,
    collapse_box_set_items: Union[Unset, None, bool] = UNSET,
    min_width: Union[Unset, None, int] = UNSET,
    min_height: Union[Unset, None, int] = UNSET,
    max_width: Union[Unset, None, int] = UNSET,
    max_height: Union[Unset, None, int] = UNSET,
    is_3d: Union[Unset, None, bool] = UNSET,
    series_status: Union[Unset, None, List[SeriesStatus]] = UNSET,
    name_starts_with_or_greater: Union[Unset, None, str] = UNSET,
    name_starts_with: Union[Unset, None, str] = UNSET,
    name_less_than: Union[Unset, None, str] = UNSET,
    studio_ids: Union[Unset, None, List[str]] = UNSET,
    genre_ids: Union[Unset, None, List[str]] = UNSET,
    enable_total_record_count: Union[Unset, None, bool] = True,
    enable_images: Union[Unset, None, bool] = True,
) -> Optional[Union[Any, BaseItemDtoQueryResult]]:
    """Finds movies and trailers similar to a given trailer.

    Args:
        user_id (Union[Unset, None, str]):
        max_official_rating (Union[Unset, None, str]):
        has_theme_song (Union[Unset, None, bool]):
        has_theme_video (Union[Unset, None, bool]):
        has_subtitles (Union[Unset, None, bool]):
        has_special_feature (Union[Unset, None, bool]):
        has_trailer (Union[Unset, None, bool]):
        adjacent_to (Union[Unset, None, str]):
        parent_index_number (Union[Unset, None, int]):
        has_parental_rating (Union[Unset, None, bool]):
        is_hd (Union[Unset, None, bool]):
        is_4k (Union[Unset, None, bool]):
        location_types (Union[Unset, None, List[LocationType]]):
        exclude_location_types (Union[Unset, None, List[LocationType]]):
        is_missing (Union[Unset, None, bool]):
        is_unaired (Union[Unset, None, bool]):
        min_community_rating (Union[Unset, None, float]):
        min_critic_rating (Union[Unset, None, float]):
        min_premiere_date (Union[Unset, None, datetime.datetime]):
        min_date_last_saved (Union[Unset, None, datetime.datetime]):
        min_date_last_saved_for_user (Union[Unset, None, datetime.datetime]):
        max_premiere_date (Union[Unset, None, datetime.datetime]):
        has_overview (Union[Unset, None, bool]):
        has_imdb_id (Union[Unset, None, bool]):
        has_tmdb_id (Union[Unset, None, bool]):
        has_tvdb_id (Union[Unset, None, bool]):
        is_movie (Union[Unset, None, bool]):
        is_series (Union[Unset, None, bool]):
        is_news (Union[Unset, None, bool]):
        is_kids (Union[Unset, None, bool]):
        is_sports (Union[Unset, None, bool]):
        exclude_item_ids (Union[Unset, None, List[str]]):
        start_index (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):
        recursive (Union[Unset, None, bool]):
        search_term (Union[Unset, None, str]):
        sort_order (Union[Unset, None, List[SortOrder]]):
        parent_id (Union[Unset, None, str]):
        fields (Union[Unset, None, List[ItemFields]]):
        exclude_item_types (Union[Unset, None, List[BaseItemKind]]):
        filters (Union[Unset, None, List[ItemFilter]]):
        is_favorite (Union[Unset, None, bool]):
        media_types (Union[Unset, None, List[str]]):
        image_types (Union[Unset, None, List[ImageType]]):
        sort_by (Union[Unset, None, List[str]]):
        is_played (Union[Unset, None, bool]):
        genres (Union[Unset, None, List[str]]):
        official_ratings (Union[Unset, None, List[str]]):
        tags (Union[Unset, None, List[str]]):
        years (Union[Unset, None, List[int]]):
        enable_user_data (Union[Unset, None, bool]):
        image_type_limit (Union[Unset, None, int]):
        enable_image_types (Union[Unset, None, List[ImageType]]):
        person (Union[Unset, None, str]):
        person_ids (Union[Unset, None, List[str]]):
        person_types (Union[Unset, None, List[str]]):
        studios (Union[Unset, None, List[str]]):
        artists (Union[Unset, None, List[str]]):
        exclude_artist_ids (Union[Unset, None, List[str]]):
        artist_ids (Union[Unset, None, List[str]]):
        album_artist_ids (Union[Unset, None, List[str]]):
        contributing_artist_ids (Union[Unset, None, List[str]]):
        albums (Union[Unset, None, List[str]]):
        album_ids (Union[Unset, None, List[str]]):
        ids (Union[Unset, None, List[str]]):
        video_types (Union[Unset, None, List[VideoType]]):
        min_official_rating (Union[Unset, None, str]):
        is_locked (Union[Unset, None, bool]):
        is_place_holder (Union[Unset, None, bool]):
        has_official_rating (Union[Unset, None, bool]):
        collapse_box_set_items (Union[Unset, None, bool]):
        min_width (Union[Unset, None, int]):
        min_height (Union[Unset, None, int]):
        max_width (Union[Unset, None, int]):
        max_height (Union[Unset, None, int]):
        is_3d (Union[Unset, None, bool]):
        series_status (Union[Unset, None, List[SeriesStatus]]):
        name_starts_with_or_greater (Union[Unset, None, str]):
        name_starts_with (Union[Unset, None, str]):
        name_less_than (Union[Unset, None, str]):
        studio_ids (Union[Unset, None, List[str]]):
        genre_ids (Union[Unset, None, List[str]]):
        enable_total_record_count (Union[Unset, None, bool]):  Default: True.
        enable_images (Union[Unset, None, bool]):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, BaseItemDtoQueryResult]
    """

    return sync_detailed(
        client=client,
        user_id=user_id,
        max_official_rating=max_official_rating,
        has_theme_song=has_theme_song,
        has_theme_video=has_theme_video,
        has_subtitles=has_subtitles,
        has_special_feature=has_special_feature,
        has_trailer=has_trailer,
        adjacent_to=adjacent_to,
        parent_index_number=parent_index_number,
        has_parental_rating=has_parental_rating,
        is_hd=is_hd,
        is_4k=is_4k,
        location_types=location_types,
        exclude_location_types=exclude_location_types,
        is_missing=is_missing,
        is_unaired=is_unaired,
        min_community_rating=min_community_rating,
        min_critic_rating=min_critic_rating,
        min_premiere_date=min_premiere_date,
        min_date_last_saved=min_date_last_saved,
        min_date_last_saved_for_user=min_date_last_saved_for_user,
        max_premiere_date=max_premiere_date,
        has_overview=has_overview,
        has_imdb_id=has_imdb_id,
        has_tmdb_id=has_tmdb_id,
        has_tvdb_id=has_tvdb_id,
        is_movie=is_movie,
        is_series=is_series,
        is_news=is_news,
        is_kids=is_kids,
        is_sports=is_sports,
        exclude_item_ids=exclude_item_ids,
        start_index=start_index,
        limit=limit,
        recursive=recursive,
        search_term=search_term,
        sort_order=sort_order,
        parent_id=parent_id,
        fields=fields,
        exclude_item_types=exclude_item_types,
        filters=filters,
        is_favorite=is_favorite,
        media_types=media_types,
        image_types=image_types,
        sort_by=sort_by,
        is_played=is_played,
        genres=genres,
        official_ratings=official_ratings,
        tags=tags,
        years=years,
        enable_user_data=enable_user_data,
        image_type_limit=image_type_limit,
        enable_image_types=enable_image_types,
        person=person,
        person_ids=person_ids,
        person_types=person_types,
        studios=studios,
        artists=artists,
        exclude_artist_ids=exclude_artist_ids,
        artist_ids=artist_ids,
        album_artist_ids=album_artist_ids,
        contributing_artist_ids=contributing_artist_ids,
        albums=albums,
        album_ids=album_ids,
        ids=ids,
        video_types=video_types,
        min_official_rating=min_official_rating,
        is_locked=is_locked,
        is_place_holder=is_place_holder,
        has_official_rating=has_official_rating,
        collapse_box_set_items=collapse_box_set_items,
        min_width=min_width,
        min_height=min_height,
        max_width=max_width,
        max_height=max_height,
        is_3d=is_3d,
        series_status=series_status,
        name_starts_with_or_greater=name_starts_with_or_greater,
        name_starts_with=name_starts_with,
        name_less_than=name_less_than,
        studio_ids=studio_ids,
        genre_ids=genre_ids,
        enable_total_record_count=enable_total_record_count,
        enable_images=enable_images,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    user_id: Union[Unset, None, str] = UNSET,
    max_official_rating: Union[Unset, None, str] = UNSET,
    has_theme_song: Union[Unset, None, bool] = UNSET,
    has_theme_video: Union[Unset, None, bool] = UNSET,
    has_subtitles: Union[Unset, None, bool] = UNSET,
    has_special_feature: Union[Unset, None, bool] = UNSET,
    has_trailer: Union[Unset, None, bool] = UNSET,
    adjacent_to: Union[Unset, None, str] = UNSET,
    parent_index_number: Union[Unset, None, int] = UNSET,
    has_parental_rating: Union[Unset, None, bool] = UNSET,
    is_hd: Union[Unset, None, bool] = UNSET,
    is_4k: Union[Unset, None, bool] = UNSET,
    location_types: Union[Unset, None, List[LocationType]] = UNSET,
    exclude_location_types: Union[Unset, None, List[LocationType]] = UNSET,
    is_missing: Union[Unset, None, bool] = UNSET,
    is_unaired: Union[Unset, None, bool] = UNSET,
    min_community_rating: Union[Unset, None, float] = UNSET,
    min_critic_rating: Union[Unset, None, float] = UNSET,
    min_premiere_date: Union[Unset, None, datetime.datetime] = UNSET,
    min_date_last_saved: Union[Unset, None, datetime.datetime] = UNSET,
    min_date_last_saved_for_user: Union[Unset, None, datetime.datetime] = UNSET,
    max_premiere_date: Union[Unset, None, datetime.datetime] = UNSET,
    has_overview: Union[Unset, None, bool] = UNSET,
    has_imdb_id: Union[Unset, None, bool] = UNSET,
    has_tmdb_id: Union[Unset, None, bool] = UNSET,
    has_tvdb_id: Union[Unset, None, bool] = UNSET,
    is_movie: Union[Unset, None, bool] = UNSET,
    is_series: Union[Unset, None, bool] = UNSET,
    is_news: Union[Unset, None, bool] = UNSET,
    is_kids: Union[Unset, None, bool] = UNSET,
    is_sports: Union[Unset, None, bool] = UNSET,
    exclude_item_ids: Union[Unset, None, List[str]] = UNSET,
    start_index: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    recursive: Union[Unset, None, bool] = UNSET,
    search_term: Union[Unset, None, str] = UNSET,
    sort_order: Union[Unset, None, List[SortOrder]] = UNSET,
    parent_id: Union[Unset, None, str] = UNSET,
    fields: Union[Unset, None, List[ItemFields]] = UNSET,
    exclude_item_types: Union[Unset, None, List[BaseItemKind]] = UNSET,
    filters: Union[Unset, None, List[ItemFilter]] = UNSET,
    is_favorite: Union[Unset, None, bool] = UNSET,
    media_types: Union[Unset, None, List[str]] = UNSET,
    image_types: Union[Unset, None, List[ImageType]] = UNSET,
    sort_by: Union[Unset, None, List[str]] = UNSET,
    is_played: Union[Unset, None, bool] = UNSET,
    genres: Union[Unset, None, List[str]] = UNSET,
    official_ratings: Union[Unset, None, List[str]] = UNSET,
    tags: Union[Unset, None, List[str]] = UNSET,
    years: Union[Unset, None, List[int]] = UNSET,
    enable_user_data: Union[Unset, None, bool] = UNSET,
    image_type_limit: Union[Unset, None, int] = UNSET,
    enable_image_types: Union[Unset, None, List[ImageType]] = UNSET,
    person: Union[Unset, None, str] = UNSET,
    person_ids: Union[Unset, None, List[str]] = UNSET,
    person_types: Union[Unset, None, List[str]] = UNSET,
    studios: Union[Unset, None, List[str]] = UNSET,
    artists: Union[Unset, None, List[str]] = UNSET,
    exclude_artist_ids: Union[Unset, None, List[str]] = UNSET,
    artist_ids: Union[Unset, None, List[str]] = UNSET,
    album_artist_ids: Union[Unset, None, List[str]] = UNSET,
    contributing_artist_ids: Union[Unset, None, List[str]] = UNSET,
    albums: Union[Unset, None, List[str]] = UNSET,
    album_ids: Union[Unset, None, List[str]] = UNSET,
    ids: Union[Unset, None, List[str]] = UNSET,
    video_types: Union[Unset, None, List[VideoType]] = UNSET,
    min_official_rating: Union[Unset, None, str] = UNSET,
    is_locked: Union[Unset, None, bool] = UNSET,
    is_place_holder: Union[Unset, None, bool] = UNSET,
    has_official_rating: Union[Unset, None, bool] = UNSET,
    collapse_box_set_items: Union[Unset, None, bool] = UNSET,
    min_width: Union[Unset, None, int] = UNSET,
    min_height: Union[Unset, None, int] = UNSET,
    max_width: Union[Unset, None, int] = UNSET,
    max_height: Union[Unset, None, int] = UNSET,
    is_3d: Union[Unset, None, bool] = UNSET,
    series_status: Union[Unset, None, List[SeriesStatus]] = UNSET,
    name_starts_with_or_greater: Union[Unset, None, str] = UNSET,
    name_starts_with: Union[Unset, None, str] = UNSET,
    name_less_than: Union[Unset, None, str] = UNSET,
    studio_ids: Union[Unset, None, List[str]] = UNSET,
    genre_ids: Union[Unset, None, List[str]] = UNSET,
    enable_total_record_count: Union[Unset, None, bool] = True,
    enable_images: Union[Unset, None, bool] = True,
) -> Response[Union[Any, BaseItemDtoQueryResult]]:
    """Finds movies and trailers similar to a given trailer.

    Args:
        user_id (Union[Unset, None, str]):
        max_official_rating (Union[Unset, None, str]):
        has_theme_song (Union[Unset, None, bool]):
        has_theme_video (Union[Unset, None, bool]):
        has_subtitles (Union[Unset, None, bool]):
        has_special_feature (Union[Unset, None, bool]):
        has_trailer (Union[Unset, None, bool]):
        adjacent_to (Union[Unset, None, str]):
        parent_index_number (Union[Unset, None, int]):
        has_parental_rating (Union[Unset, None, bool]):
        is_hd (Union[Unset, None, bool]):
        is_4k (Union[Unset, None, bool]):
        location_types (Union[Unset, None, List[LocationType]]):
        exclude_location_types (Union[Unset, None, List[LocationType]]):
        is_missing (Union[Unset, None, bool]):
        is_unaired (Union[Unset, None, bool]):
        min_community_rating (Union[Unset, None, float]):
        min_critic_rating (Union[Unset, None, float]):
        min_premiere_date (Union[Unset, None, datetime.datetime]):
        min_date_last_saved (Union[Unset, None, datetime.datetime]):
        min_date_last_saved_for_user (Union[Unset, None, datetime.datetime]):
        max_premiere_date (Union[Unset, None, datetime.datetime]):
        has_overview (Union[Unset, None, bool]):
        has_imdb_id (Union[Unset, None, bool]):
        has_tmdb_id (Union[Unset, None, bool]):
        has_tvdb_id (Union[Unset, None, bool]):
        is_movie (Union[Unset, None, bool]):
        is_series (Union[Unset, None, bool]):
        is_news (Union[Unset, None, bool]):
        is_kids (Union[Unset, None, bool]):
        is_sports (Union[Unset, None, bool]):
        exclude_item_ids (Union[Unset, None, List[str]]):
        start_index (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):
        recursive (Union[Unset, None, bool]):
        search_term (Union[Unset, None, str]):
        sort_order (Union[Unset, None, List[SortOrder]]):
        parent_id (Union[Unset, None, str]):
        fields (Union[Unset, None, List[ItemFields]]):
        exclude_item_types (Union[Unset, None, List[BaseItemKind]]):
        filters (Union[Unset, None, List[ItemFilter]]):
        is_favorite (Union[Unset, None, bool]):
        media_types (Union[Unset, None, List[str]]):
        image_types (Union[Unset, None, List[ImageType]]):
        sort_by (Union[Unset, None, List[str]]):
        is_played (Union[Unset, None, bool]):
        genres (Union[Unset, None, List[str]]):
        official_ratings (Union[Unset, None, List[str]]):
        tags (Union[Unset, None, List[str]]):
        years (Union[Unset, None, List[int]]):
        enable_user_data (Union[Unset, None, bool]):
        image_type_limit (Union[Unset, None, int]):
        enable_image_types (Union[Unset, None, List[ImageType]]):
        person (Union[Unset, None, str]):
        person_ids (Union[Unset, None, List[str]]):
        person_types (Union[Unset, None, List[str]]):
        studios (Union[Unset, None, List[str]]):
        artists (Union[Unset, None, List[str]]):
        exclude_artist_ids (Union[Unset, None, List[str]]):
        artist_ids (Union[Unset, None, List[str]]):
        album_artist_ids (Union[Unset, None, List[str]]):
        contributing_artist_ids (Union[Unset, None, List[str]]):
        albums (Union[Unset, None, List[str]]):
        album_ids (Union[Unset, None, List[str]]):
        ids (Union[Unset, None, List[str]]):
        video_types (Union[Unset, None, List[VideoType]]):
        min_official_rating (Union[Unset, None, str]):
        is_locked (Union[Unset, None, bool]):
        is_place_holder (Union[Unset, None, bool]):
        has_official_rating (Union[Unset, None, bool]):
        collapse_box_set_items (Union[Unset, None, bool]):
        min_width (Union[Unset, None, int]):
        min_height (Union[Unset, None, int]):
        max_width (Union[Unset, None, int]):
        max_height (Union[Unset, None, int]):
        is_3d (Union[Unset, None, bool]):
        series_status (Union[Unset, None, List[SeriesStatus]]):
        name_starts_with_or_greater (Union[Unset, None, str]):
        name_starts_with (Union[Unset, None, str]):
        name_less_than (Union[Unset, None, str]):
        studio_ids (Union[Unset, None, List[str]]):
        genre_ids (Union[Unset, None, List[str]]):
        enable_total_record_count (Union[Unset, None, bool]):  Default: True.
        enable_images (Union[Unset, None, bool]):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, BaseItemDtoQueryResult]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        max_official_rating=max_official_rating,
        has_theme_song=has_theme_song,
        has_theme_video=has_theme_video,
        has_subtitles=has_subtitles,
        has_special_feature=has_special_feature,
        has_trailer=has_trailer,
        adjacent_to=adjacent_to,
        parent_index_number=parent_index_number,
        has_parental_rating=has_parental_rating,
        is_hd=is_hd,
        is_4k=is_4k,
        location_types=location_types,
        exclude_location_types=exclude_location_types,
        is_missing=is_missing,
        is_unaired=is_unaired,
        min_community_rating=min_community_rating,
        min_critic_rating=min_critic_rating,
        min_premiere_date=min_premiere_date,
        min_date_last_saved=min_date_last_saved,
        min_date_last_saved_for_user=min_date_last_saved_for_user,
        max_premiere_date=max_premiere_date,
        has_overview=has_overview,
        has_imdb_id=has_imdb_id,
        has_tmdb_id=has_tmdb_id,
        has_tvdb_id=has_tvdb_id,
        is_movie=is_movie,
        is_series=is_series,
        is_news=is_news,
        is_kids=is_kids,
        is_sports=is_sports,
        exclude_item_ids=exclude_item_ids,
        start_index=start_index,
        limit=limit,
        recursive=recursive,
        search_term=search_term,
        sort_order=sort_order,
        parent_id=parent_id,
        fields=fields,
        exclude_item_types=exclude_item_types,
        filters=filters,
        is_favorite=is_favorite,
        media_types=media_types,
        image_types=image_types,
        sort_by=sort_by,
        is_played=is_played,
        genres=genres,
        official_ratings=official_ratings,
        tags=tags,
        years=years,
        enable_user_data=enable_user_data,
        image_type_limit=image_type_limit,
        enable_image_types=enable_image_types,
        person=person,
        person_ids=person_ids,
        person_types=person_types,
        studios=studios,
        artists=artists,
        exclude_artist_ids=exclude_artist_ids,
        artist_ids=artist_ids,
        album_artist_ids=album_artist_ids,
        contributing_artist_ids=contributing_artist_ids,
        albums=albums,
        album_ids=album_ids,
        ids=ids,
        video_types=video_types,
        min_official_rating=min_official_rating,
        is_locked=is_locked,
        is_place_holder=is_place_holder,
        has_official_rating=has_official_rating,
        collapse_box_set_items=collapse_box_set_items,
        min_width=min_width,
        min_height=min_height,
        max_width=max_width,
        max_height=max_height,
        is_3d=is_3d,
        series_status=series_status,
        name_starts_with_or_greater=name_starts_with_or_greater,
        name_starts_with=name_starts_with,
        name_less_than=name_less_than,
        studio_ids=studio_ids,
        genre_ids=genre_ids,
        enable_total_record_count=enable_total_record_count,
        enable_images=enable_images,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    user_id: Union[Unset, None, str] = UNSET,
    max_official_rating: Union[Unset, None, str] = UNSET,
    has_theme_song: Union[Unset, None, bool] = UNSET,
    has_theme_video: Union[Unset, None, bool] = UNSET,
    has_subtitles: Union[Unset, None, bool] = UNSET,
    has_special_feature: Union[Unset, None, bool] = UNSET,
    has_trailer: Union[Unset, None, bool] = UNSET,
    adjacent_to: Union[Unset, None, str] = UNSET,
    parent_index_number: Union[Unset, None, int] = UNSET,
    has_parental_rating: Union[Unset, None, bool] = UNSET,
    is_hd: Union[Unset, None, bool] = UNSET,
    is_4k: Union[Unset, None, bool] = UNSET,
    location_types: Union[Unset, None, List[LocationType]] = UNSET,
    exclude_location_types: Union[Unset, None, List[LocationType]] = UNSET,
    is_missing: Union[Unset, None, bool] = UNSET,
    is_unaired: Union[Unset, None, bool] = UNSET,
    min_community_rating: Union[Unset, None, float] = UNSET,
    min_critic_rating: Union[Unset, None, float] = UNSET,
    min_premiere_date: Union[Unset, None, datetime.datetime] = UNSET,
    min_date_last_saved: Union[Unset, None, datetime.datetime] = UNSET,
    min_date_last_saved_for_user: Union[Unset, None, datetime.datetime] = UNSET,
    max_premiere_date: Union[Unset, None, datetime.datetime] = UNSET,
    has_overview: Union[Unset, None, bool] = UNSET,
    has_imdb_id: Union[Unset, None, bool] = UNSET,
    has_tmdb_id: Union[Unset, None, bool] = UNSET,
    has_tvdb_id: Union[Unset, None, bool] = UNSET,
    is_movie: Union[Unset, None, bool] = UNSET,
    is_series: Union[Unset, None, bool] = UNSET,
    is_news: Union[Unset, None, bool] = UNSET,
    is_kids: Union[Unset, None, bool] = UNSET,
    is_sports: Union[Unset, None, bool] = UNSET,
    exclude_item_ids: Union[Unset, None, List[str]] = UNSET,
    start_index: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    recursive: Union[Unset, None, bool] = UNSET,
    search_term: Union[Unset, None, str] = UNSET,
    sort_order: Union[Unset, None, List[SortOrder]] = UNSET,
    parent_id: Union[Unset, None, str] = UNSET,
    fields: Union[Unset, None, List[ItemFields]] = UNSET,
    exclude_item_types: Union[Unset, None, List[BaseItemKind]] = UNSET,
    filters: Union[Unset, None, List[ItemFilter]] = UNSET,
    is_favorite: Union[Unset, None, bool] = UNSET,
    media_types: Union[Unset, None, List[str]] = UNSET,
    image_types: Union[Unset, None, List[ImageType]] = UNSET,
    sort_by: Union[Unset, None, List[str]] = UNSET,
    is_played: Union[Unset, None, bool] = UNSET,
    genres: Union[Unset, None, List[str]] = UNSET,
    official_ratings: Union[Unset, None, List[str]] = UNSET,
    tags: Union[Unset, None, List[str]] = UNSET,
    years: Union[Unset, None, List[int]] = UNSET,
    enable_user_data: Union[Unset, None, bool] = UNSET,
    image_type_limit: Union[Unset, None, int] = UNSET,
    enable_image_types: Union[Unset, None, List[ImageType]] = UNSET,
    person: Union[Unset, None, str] = UNSET,
    person_ids: Union[Unset, None, List[str]] = UNSET,
    person_types: Union[Unset, None, List[str]] = UNSET,
    studios: Union[Unset, None, List[str]] = UNSET,
    artists: Union[Unset, None, List[str]] = UNSET,
    exclude_artist_ids: Union[Unset, None, List[str]] = UNSET,
    artist_ids: Union[Unset, None, List[str]] = UNSET,
    album_artist_ids: Union[Unset, None, List[str]] = UNSET,
    contributing_artist_ids: Union[Unset, None, List[str]] = UNSET,
    albums: Union[Unset, None, List[str]] = UNSET,
    album_ids: Union[Unset, None, List[str]] = UNSET,
    ids: Union[Unset, None, List[str]] = UNSET,
    video_types: Union[Unset, None, List[VideoType]] = UNSET,
    min_official_rating: Union[Unset, None, str] = UNSET,
    is_locked: Union[Unset, None, bool] = UNSET,
    is_place_holder: Union[Unset, None, bool] = UNSET,
    has_official_rating: Union[Unset, None, bool] = UNSET,
    collapse_box_set_items: Union[Unset, None, bool] = UNSET,
    min_width: Union[Unset, None, int] = UNSET,
    min_height: Union[Unset, None, int] = UNSET,
    max_width: Union[Unset, None, int] = UNSET,
    max_height: Union[Unset, None, int] = UNSET,
    is_3d: Union[Unset, None, bool] = UNSET,
    series_status: Union[Unset, None, List[SeriesStatus]] = UNSET,
    name_starts_with_or_greater: Union[Unset, None, str] = UNSET,
    name_starts_with: Union[Unset, None, str] = UNSET,
    name_less_than: Union[Unset, None, str] = UNSET,
    studio_ids: Union[Unset, None, List[str]] = UNSET,
    genre_ids: Union[Unset, None, List[str]] = UNSET,
    enable_total_record_count: Union[Unset, None, bool] = True,
    enable_images: Union[Unset, None, bool] = True,
) -> Optional[Union[Any, BaseItemDtoQueryResult]]:
    """Finds movies and trailers similar to a given trailer.

    Args:
        user_id (Union[Unset, None, str]):
        max_official_rating (Union[Unset, None, str]):
        has_theme_song (Union[Unset, None, bool]):
        has_theme_video (Union[Unset, None, bool]):
        has_subtitles (Union[Unset, None, bool]):
        has_special_feature (Union[Unset, None, bool]):
        has_trailer (Union[Unset, None, bool]):
        adjacent_to (Union[Unset, None, str]):
        parent_index_number (Union[Unset, None, int]):
        has_parental_rating (Union[Unset, None, bool]):
        is_hd (Union[Unset, None, bool]):
        is_4k (Union[Unset, None, bool]):
        location_types (Union[Unset, None, List[LocationType]]):
        exclude_location_types (Union[Unset, None, List[LocationType]]):
        is_missing (Union[Unset, None, bool]):
        is_unaired (Union[Unset, None, bool]):
        min_community_rating (Union[Unset, None, float]):
        min_critic_rating (Union[Unset, None, float]):
        min_premiere_date (Union[Unset, None, datetime.datetime]):
        min_date_last_saved (Union[Unset, None, datetime.datetime]):
        min_date_last_saved_for_user (Union[Unset, None, datetime.datetime]):
        max_premiere_date (Union[Unset, None, datetime.datetime]):
        has_overview (Union[Unset, None, bool]):
        has_imdb_id (Union[Unset, None, bool]):
        has_tmdb_id (Union[Unset, None, bool]):
        has_tvdb_id (Union[Unset, None, bool]):
        is_movie (Union[Unset, None, bool]):
        is_series (Union[Unset, None, bool]):
        is_news (Union[Unset, None, bool]):
        is_kids (Union[Unset, None, bool]):
        is_sports (Union[Unset, None, bool]):
        exclude_item_ids (Union[Unset, None, List[str]]):
        start_index (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):
        recursive (Union[Unset, None, bool]):
        search_term (Union[Unset, None, str]):
        sort_order (Union[Unset, None, List[SortOrder]]):
        parent_id (Union[Unset, None, str]):
        fields (Union[Unset, None, List[ItemFields]]):
        exclude_item_types (Union[Unset, None, List[BaseItemKind]]):
        filters (Union[Unset, None, List[ItemFilter]]):
        is_favorite (Union[Unset, None, bool]):
        media_types (Union[Unset, None, List[str]]):
        image_types (Union[Unset, None, List[ImageType]]):
        sort_by (Union[Unset, None, List[str]]):
        is_played (Union[Unset, None, bool]):
        genres (Union[Unset, None, List[str]]):
        official_ratings (Union[Unset, None, List[str]]):
        tags (Union[Unset, None, List[str]]):
        years (Union[Unset, None, List[int]]):
        enable_user_data (Union[Unset, None, bool]):
        image_type_limit (Union[Unset, None, int]):
        enable_image_types (Union[Unset, None, List[ImageType]]):
        person (Union[Unset, None, str]):
        person_ids (Union[Unset, None, List[str]]):
        person_types (Union[Unset, None, List[str]]):
        studios (Union[Unset, None, List[str]]):
        artists (Union[Unset, None, List[str]]):
        exclude_artist_ids (Union[Unset, None, List[str]]):
        artist_ids (Union[Unset, None, List[str]]):
        album_artist_ids (Union[Unset, None, List[str]]):
        contributing_artist_ids (Union[Unset, None, List[str]]):
        albums (Union[Unset, None, List[str]]):
        album_ids (Union[Unset, None, List[str]]):
        ids (Union[Unset, None, List[str]]):
        video_types (Union[Unset, None, List[VideoType]]):
        min_official_rating (Union[Unset, None, str]):
        is_locked (Union[Unset, None, bool]):
        is_place_holder (Union[Unset, None, bool]):
        has_official_rating (Union[Unset, None, bool]):
        collapse_box_set_items (Union[Unset, None, bool]):
        min_width (Union[Unset, None, int]):
        min_height (Union[Unset, None, int]):
        max_width (Union[Unset, None, int]):
        max_height (Union[Unset, None, int]):
        is_3d (Union[Unset, None, bool]):
        series_status (Union[Unset, None, List[SeriesStatus]]):
        name_starts_with_or_greater (Union[Unset, None, str]):
        name_starts_with (Union[Unset, None, str]):
        name_less_than (Union[Unset, None, str]):
        studio_ids (Union[Unset, None, List[str]]):
        genre_ids (Union[Unset, None, List[str]]):
        enable_total_record_count (Union[Unset, None, bool]):  Default: True.
        enable_images (Union[Unset, None, bool]):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, BaseItemDtoQueryResult]
    """

    return (
        await asyncio_detailed(
            client=client,
            user_id=user_id,
            max_official_rating=max_official_rating,
            has_theme_song=has_theme_song,
            has_theme_video=has_theme_video,
            has_subtitles=has_subtitles,
            has_special_feature=has_special_feature,
            has_trailer=has_trailer,
            adjacent_to=adjacent_to,
            parent_index_number=parent_index_number,
            has_parental_rating=has_parental_rating,
            is_hd=is_hd,
            is_4k=is_4k,
            location_types=location_types,
            exclude_location_types=exclude_location_types,
            is_missing=is_missing,
            is_unaired=is_unaired,
            min_community_rating=min_community_rating,
            min_critic_rating=min_critic_rating,
            min_premiere_date=min_premiere_date,
            min_date_last_saved=min_date_last_saved,
            min_date_last_saved_for_user=min_date_last_saved_for_user,
            max_premiere_date=max_premiere_date,
            has_overview=has_overview,
            has_imdb_id=has_imdb_id,
            has_tmdb_id=has_tmdb_id,
            has_tvdb_id=has_tvdb_id,
            is_movie=is_movie,
            is_series=is_series,
            is_news=is_news,
            is_kids=is_kids,
            is_sports=is_sports,
            exclude_item_ids=exclude_item_ids,
            start_index=start_index,
            limit=limit,
            recursive=recursive,
            search_term=search_term,
            sort_order=sort_order,
            parent_id=parent_id,
            fields=fields,
            exclude_item_types=exclude_item_types,
            filters=filters,
            is_favorite=is_favorite,
            media_types=media_types,
            image_types=image_types,
            sort_by=sort_by,
            is_played=is_played,
            genres=genres,
            official_ratings=official_ratings,
            tags=tags,
            years=years,
            enable_user_data=enable_user_data,
            image_type_limit=image_type_limit,
            enable_image_types=enable_image_types,
            person=person,
            person_ids=person_ids,
            person_types=person_types,
            studios=studios,
            artists=artists,
            exclude_artist_ids=exclude_artist_ids,
            artist_ids=artist_ids,
            album_artist_ids=album_artist_ids,
            contributing_artist_ids=contributing_artist_ids,
            albums=albums,
            album_ids=album_ids,
            ids=ids,
            video_types=video_types,
            min_official_rating=min_official_rating,
            is_locked=is_locked,
            is_place_holder=is_place_holder,
            has_official_rating=has_official_rating,
            collapse_box_set_items=collapse_box_set_items,
            min_width=min_width,
            min_height=min_height,
            max_width=max_width,
            max_height=max_height,
            is_3d=is_3d,
            series_status=series_status,
            name_starts_with_or_greater=name_starts_with_or_greater,
            name_starts_with=name_starts_with,
            name_less_than=name_less_than,
            studio_ids=studio_ids,
            genre_ids=genre_ids,
            enable_total_record_count=enable_total_record_count,
            enable_images=enable_images,
        )
    ).parsed
