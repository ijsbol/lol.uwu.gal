from __future__ import annotations

from typing import Literal, TypedDict


class IPAPI_IPInformation_fail(TypedDict):
    status: Literal["fail"]
    message: Literal["private range", "reserved range", "invalid query"]


class IPAPI_IPInformation_success(TypedDict):
    status: Literal["success"]
    country: str
    region: str
    regionName: str
    city: str
    zip: str
    lat: float
    lon: float


class IPInformation(TypedDict):
    country: str
    region: str
    regionName: str
    city: str
    zip: str
    lat: str
    long: str


class IPMemes(TypedDict):
    name: str
    file_location: str
    frames: IPMemes_frames
    position: IPMemes_position
    text: IPMemes_text


class IPMemes_frames(TypedDict):
    start: int
    end: int


class IPMemes_position(TypedDict):
    x: int
    y: int


class IPMemes_text(TypedDict):
    size: int
    colour: str
    location: str
    thickness: int
