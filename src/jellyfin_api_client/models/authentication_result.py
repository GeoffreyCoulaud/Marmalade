from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.session_info import SessionInfo
    from ..models.user_dto import UserDto


T = TypeVar("T", bound="AuthenticationResult")


@_attrs_define
class AuthenticationResult:
    """
    Attributes:
        user (Union[Unset, None, UserDto]): Class UserDto.
        session_info (Union[Unset, None, SessionInfo]): Class SessionInfo.
        access_token (Union[Unset, None, str]):
        server_id (Union[Unset, None, str]):
    """

    user: Union[Unset, None, "UserDto"] = UNSET
    session_info: Union[Unset, None, "SessionInfo"] = UNSET
    access_token: Union[Unset, None, str] = UNSET
    server_id: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        user: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict() if self.user else None

        session_info: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.session_info, Unset):
            session_info = self.session_info.to_dict() if self.session_info else None

        access_token = self.access_token
        server_id = self.server_id

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if user is not UNSET:
            field_dict["User"] = user
        if session_info is not UNSET:
            field_dict["SessionInfo"] = session_info
        if access_token is not UNSET:
            field_dict["AccessToken"] = access_token
        if server_id is not UNSET:
            field_dict["ServerId"] = server_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.session_info import SessionInfo
        from ..models.user_dto import UserDto

        d = src_dict.copy()
        _user = d.pop("User", UNSET)
        user: Union[Unset, None, UserDto]
        if _user is None:
            user = None
        elif isinstance(_user, Unset):
            user = UNSET
        else:
            user = UserDto.from_dict(_user)

        _session_info = d.pop("SessionInfo", UNSET)
        session_info: Union[Unset, None, SessionInfo]
        if _session_info is None:
            session_info = None
        elif isinstance(_session_info, Unset):
            session_info = UNSET
        else:
            session_info = SessionInfo.from_dict(_session_info)

        access_token = d.pop("AccessToken", UNSET)

        server_id = d.pop("ServerId", UNSET)

        authentication_result = cls(
            user=user,
            session_info=session_info,
            access_token=access_token,
            server_id=server_id,
        )

        return authentication_result
