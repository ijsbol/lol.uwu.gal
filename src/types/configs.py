from __future__ import annotations

from typing import TypedDict


class IPMemes(TypedDict):
    file_location: str
    frames: IPMemes_frames
    position: IPMemes_position
    font: IPMemes_font


class IPMemes_frames(TypedDict):
    start: int
    end: int


class IPMemes_position(TypedDict):
    x: int
    y: int


class IPMemes_font(TypedDict):
    size: int
    location: str
