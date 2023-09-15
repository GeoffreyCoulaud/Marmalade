from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="MediaAttachment")


@_attrs_define
class MediaAttachment:
    """Class MediaAttachment.

    Attributes:
        codec (Union[Unset, None, str]): Gets or sets the codec.
        codec_tag (Union[Unset, None, str]): Gets or sets the codec tag.
        comment (Union[Unset, None, str]): Gets or sets the comment.
        index (Union[Unset, int]): Gets or sets the index.
        file_name (Union[Unset, None, str]): Gets or sets the filename.
        mime_type (Union[Unset, None, str]): Gets or sets the MIME type.
        delivery_url (Union[Unset, None, str]): Gets or sets the delivery URL.
    """

    codec: Union[Unset, None, str] = UNSET
    codec_tag: Union[Unset, None, str] = UNSET
    comment: Union[Unset, None, str] = UNSET
    index: Union[Unset, int] = UNSET
    file_name: Union[Unset, None, str] = UNSET
    mime_type: Union[Unset, None, str] = UNSET
    delivery_url: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        codec = self.codec
        codec_tag = self.codec_tag
        comment = self.comment
        index = self.index
        file_name = self.file_name
        mime_type = self.mime_type
        delivery_url = self.delivery_url

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if codec is not UNSET:
            field_dict["Codec"] = codec
        if codec_tag is not UNSET:
            field_dict["CodecTag"] = codec_tag
        if comment is not UNSET:
            field_dict["Comment"] = comment
        if index is not UNSET:
            field_dict["Index"] = index
        if file_name is not UNSET:
            field_dict["FileName"] = file_name
        if mime_type is not UNSET:
            field_dict["MimeType"] = mime_type
        if delivery_url is not UNSET:
            field_dict["DeliveryUrl"] = delivery_url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        codec = d.pop("Codec", UNSET)

        codec_tag = d.pop("CodecTag", UNSET)

        comment = d.pop("Comment", UNSET)

        index = d.pop("Index", UNSET)

        file_name = d.pop("FileName", UNSET)

        mime_type = d.pop("MimeType", UNSET)

        delivery_url = d.pop("DeliveryUrl", UNSET)

        media_attachment = cls(
            codec=codec,
            codec_tag=codec_tag,
            comment=comment,
            index=index,
            file_name=file_name,
            mime_type=mime_type,
            delivery_url=delivery_url,
        )

        return media_attachment
