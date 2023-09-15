from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="BrandingOptions")


@_attrs_define
class BrandingOptions:
    """The branding options.

    Attributes:
        login_disclaimer (Union[Unset, None, str]): Gets or sets the login disclaimer.
        custom_css (Union[Unset, None, str]): Gets or sets the custom CSS.
        splashscreen_enabled (Union[Unset, bool]): Gets or sets a value indicating whether to enable the splashscreen.
    """

    login_disclaimer: Union[Unset, None, str] = UNSET
    custom_css: Union[Unset, None, str] = UNSET
    splashscreen_enabled: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        login_disclaimer = self.login_disclaimer
        custom_css = self.custom_css
        splashscreen_enabled = self.splashscreen_enabled

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if login_disclaimer is not UNSET:
            field_dict["LoginDisclaimer"] = login_disclaimer
        if custom_css is not UNSET:
            field_dict["CustomCss"] = custom_css
        if splashscreen_enabled is not UNSET:
            field_dict["SplashscreenEnabled"] = splashscreen_enabled

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        login_disclaimer = d.pop("LoginDisclaimer", UNSET)

        custom_css = d.pop("CustomCss", UNSET)

        splashscreen_enabled = d.pop("SplashscreenEnabled", UNSET)

        branding_options = cls(
            login_disclaimer=login_disclaimer,
            custom_css=custom_css,
            splashscreen_enabled=splashscreen_enabled,
        )

        return branding_options
