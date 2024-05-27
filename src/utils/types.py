from __future__ import annotations

from typing import Literal, Optional, TypedDict


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


class Videos(TypedDict):
    name: str
    file_location: str
    ip: Optional[Videos_render_data]
    location: Optional[Videos_render_data]
    latlong: Optional[Videos_render_data]


class Videos_render_data(TypedDict):
    frames: Videos_render_data_frames
    position: Videos_render_data_position
    text: Videos_render_data_text


class Videos_render_data_frames(TypedDict):
    start: int
    end: int


class Videos_render_data_position(TypedDict):
    x: int
    y: int


class Videos_render_data_text(TypedDict):
    size: int
    colour: str
    location: str
    thickness: int
