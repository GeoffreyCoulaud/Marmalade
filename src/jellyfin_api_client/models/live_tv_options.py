from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.listings_provider_info import ListingsProviderInfo
    from ..models.tuner_host_info import TunerHostInfo


T = TypeVar("T", bound="LiveTvOptions")


@_attrs_define
class LiveTvOptions:
    """
    Attributes:
        guide_days (Union[Unset, None, int]):
        recording_path (Union[Unset, None, str]):
        movie_recording_path (Union[Unset, None, str]):
        series_recording_path (Union[Unset, None, str]):
        enable_recording_subfolders (Union[Unset, bool]):
        enable_original_audio_with_encoded_recordings (Union[Unset, bool]):
        tuner_hosts (Union[Unset, None, List['TunerHostInfo']]):
        listing_providers (Union[Unset, None, List['ListingsProviderInfo']]):
        pre_padding_seconds (Union[Unset, int]):
        post_padding_seconds (Union[Unset, int]):
        media_locations_created (Union[Unset, None, List[str]]):
        recording_post_processor (Union[Unset, None, str]):
        recording_post_processor_arguments (Union[Unset, None, str]):
    """

    guide_days: Union[Unset, None, int] = UNSET
    recording_path: Union[Unset, None, str] = UNSET
    movie_recording_path: Union[Unset, None, str] = UNSET
    series_recording_path: Union[Unset, None, str] = UNSET
    enable_recording_subfolders: Union[Unset, bool] = UNSET
    enable_original_audio_with_encoded_recordings: Union[Unset, bool] = UNSET
    tuner_hosts: Union[Unset, None, List["TunerHostInfo"]] = UNSET
    listing_providers: Union[Unset, None, List["ListingsProviderInfo"]] = UNSET
    pre_padding_seconds: Union[Unset, int] = UNSET
    post_padding_seconds: Union[Unset, int] = UNSET
    media_locations_created: Union[Unset, None, List[str]] = UNSET
    recording_post_processor: Union[Unset, None, str] = UNSET
    recording_post_processor_arguments: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        guide_days = self.guide_days
        recording_path = self.recording_path
        movie_recording_path = self.movie_recording_path
        series_recording_path = self.series_recording_path
        enable_recording_subfolders = self.enable_recording_subfolders
        enable_original_audio_with_encoded_recordings = self.enable_original_audio_with_encoded_recordings
        tuner_hosts: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.tuner_hosts, Unset):
            if self.tuner_hosts is None:
                tuner_hosts = None
            else:
                tuner_hosts = []
                for tuner_hosts_item_data in self.tuner_hosts:
                    tuner_hosts_item = tuner_hosts_item_data.to_dict()

                    tuner_hosts.append(tuner_hosts_item)

        listing_providers: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.listing_providers, Unset):
            if self.listing_providers is None:
                listing_providers = None
            else:
                listing_providers = []
                for listing_providers_item_data in self.listing_providers:
                    listing_providers_item = listing_providers_item_data.to_dict()

                    listing_providers.append(listing_providers_item)

        pre_padding_seconds = self.pre_padding_seconds
        post_padding_seconds = self.post_padding_seconds
        media_locations_created: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.media_locations_created, Unset):
            if self.media_locations_created is None:
                media_locations_created = None
            else:
                media_locations_created = self.media_locations_created

        recording_post_processor = self.recording_post_processor
        recording_post_processor_arguments = self.recording_post_processor_arguments

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if guide_days is not UNSET:
            field_dict["GuideDays"] = guide_days
        if recording_path is not UNSET:
            field_dict["RecordingPath"] = recording_path
        if movie_recording_path is not UNSET:
            field_dict["MovieRecordingPath"] = movie_recording_path
        if series_recording_path is not UNSET:
            field_dict["SeriesRecordingPath"] = series_recording_path
        if enable_recording_subfolders is not UNSET:
            field_dict["EnableRecordingSubfolders"] = enable_recording_subfolders
        if enable_original_audio_with_encoded_recordings is not UNSET:
            field_dict["EnableOriginalAudioWithEncodedRecordings"] = enable_original_audio_with_encoded_recordings
        if tuner_hosts is not UNSET:
            field_dict["TunerHosts"] = tuner_hosts
        if listing_providers is not UNSET:
            field_dict["ListingProviders"] = listing_providers
        if pre_padding_seconds is not UNSET:
            field_dict["PrePaddingSeconds"] = pre_padding_seconds
        if post_padding_seconds is not UNSET:
            field_dict["PostPaddingSeconds"] = post_padding_seconds
        if media_locations_created is not UNSET:
            field_dict["MediaLocationsCreated"] = media_locations_created
        if recording_post_processor is not UNSET:
            field_dict["RecordingPostProcessor"] = recording_post_processor
        if recording_post_processor_arguments is not UNSET:
            field_dict["RecordingPostProcessorArguments"] = recording_post_processor_arguments

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.listings_provider_info import ListingsProviderInfo
        from ..models.tuner_host_info import TunerHostInfo

        d = src_dict.copy()
        guide_days = d.pop("GuideDays", UNSET)

        recording_path = d.pop("RecordingPath", UNSET)

        movie_recording_path = d.pop("MovieRecordingPath", UNSET)

        series_recording_path = d.pop("SeriesRecordingPath", UNSET)

        enable_recording_subfolders = d.pop("EnableRecordingSubfolders", UNSET)

        enable_original_audio_with_encoded_recordings = d.pop("EnableOriginalAudioWithEncodedRecordings", UNSET)

        tuner_hosts = []
        _tuner_hosts = d.pop("TunerHosts", UNSET)
        for tuner_hosts_item_data in _tuner_hosts or []:
            tuner_hosts_item = TunerHostInfo.from_dict(tuner_hosts_item_data)

            tuner_hosts.append(tuner_hosts_item)

        listing_providers = []
        _listing_providers = d.pop("ListingProviders", UNSET)
        for listing_providers_item_data in _listing_providers or []:
            listing_providers_item = ListingsProviderInfo.from_dict(listing_providers_item_data)

            listing_providers.append(listing_providers_item)

        pre_padding_seconds = d.pop("PrePaddingSeconds", UNSET)

        post_padding_seconds = d.pop("PostPaddingSeconds", UNSET)

        media_locations_created = cast(List[str], d.pop("MediaLocationsCreated", UNSET))

        recording_post_processor = d.pop("RecordingPostProcessor", UNSET)

        recording_post_processor_arguments = d.pop("RecordingPostProcessorArguments", UNSET)

        live_tv_options = cls(
            guide_days=guide_days,
            recording_path=recording_path,
            movie_recording_path=movie_recording_path,
            series_recording_path=series_recording_path,
            enable_recording_subfolders=enable_recording_subfolders,
            enable_original_audio_with_encoded_recordings=enable_original_audio_with_encoded_recordings,
            tuner_hosts=tuner_hosts,
            listing_providers=listing_providers,
            pre_padding_seconds=pre_padding_seconds,
            post_padding_seconds=post_padding_seconds,
            media_locations_created=media_locations_created,
            recording_post_processor=recording_post_processor,
            recording_post_processor_arguments=recording_post_processor_arguments,
        )

        return live_tv_options
