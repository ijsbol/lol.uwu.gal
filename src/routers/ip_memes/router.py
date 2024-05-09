from typing import Union, cast

from aiohttp import ClientResponseError, ClientSession, ContentTypeError
import cv2
from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import StreamingResponse

from utils.config import ENABLED_MEMES
from utils.types import IPAPI_IPInformation_fail, IPAPI_IPInformation_success, IPInformation, IPMemes


router = APIRouter()


async def get_ip_information(ip: str) -> IPInformation:
    async with ClientSession(
        base_url="http://ip-api.com"
    ) as session:
        async with session.get(
            url=f"/json/{ip}",
            params={
                "fields": ','.join([
                    "status", "message", "country",
                    "region", "regionName", "city",
                    "zip", "lat", "lon",
                ]),
            },
        ) as resp:
            api_data: IPAPI_IPInformation_fail | IPAPI_IPInformation_success
            try:
                resp.raise_for_status()
                api_data = cast(
                    Union[IPAPI_IPInformation_fail, IPAPI_IPInformation_success],
                    await resp.json()
                )
            except ClientResponseError or ContentTypeError:
                api_data = {"status": "fail", "message": "invalid query"}

    processed_data: IPInformation
    if api_data["status"] == "fail":
        processed_data = {
            "city": "Unknown",
            "country": "Unknown",
            "lat": "0.0",
            "long": "0.0",
            "region": "Unknown",
            "regionName": "Unknown",
            "zip": "Unknown"
        }
    else:
        processed_data = {
            "city": api_data["city"],
            "country": api_data["country"],
            "lat": str(api_data["lat"]),
            "long": str(api_data["lon"]),
            "region": api_data["region"],
            "regionName": api_data["regionName"],
            "zip": api_data["zip"],
        }

    return processed_data


@router.get("/{meme}")
async def ip_meme_gen(
    request: Request,
    meme: str,
) -> StreamingResponse:
    """ Successful purchase page """

    if meme not in ENABLED_MEMES.keys():
        raise HTTPException(404)

    assert request.client is not None

    meme_config = ENABLED_MEMES[meme]
    cloudflare_protected = True if request.headers.get('cf-connecting-ip', None) is not None else False
    ip: str
    if cloudflare_protected:
        ip = request.headers['x-real-ip']
        ip_info: IPInformation = IPInformation(
            country=request.headers['cf-ipcountry'],
            region=request.headers['cf-region'],
            regionName=request.headers['cf-region'],
            city=request.headers['cf-ipcity'],
            zip=request.headers['cf-postal-code'],
            lat=request.headers['cf-iplatitude'],
            long=request.headers['cf-iplongitude'],
        )
    else:
        ip = request.client.host
        ip_info = await get_ip_information(ip)

    video_path = meme_config["file_location"]
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = meme_config["text"]["size"]
    font_color = meme_config["text"]["colour"]
    position = (meme_config["position"]["x"], meme_config["position"]["y"])
    thickness = meme_config["text"]["thickness"]
    text = (
        f"{ip}"
        + f"\n{ip_info['city']}, {ip_info['region']}"
        + f"\n{ip_info['lat']}, {ip_info['long']}"
    )

    def generate_frames():
        cap = cv2.VideoCapture(video_path)
        text_start_frame = meme_config["frames"]["start"]
        text_end_frame = meme_config["frames"]["end"]
        total_frame_count: int = cast(int, cap.read().count)
        current_frame = 0

        while cap.isOpened() or current_frame < total_frame_count:
            ret, frame = cap.read()
            if not ret:
                break

            # Overlay text on the frame
            if (
                current_frame > text_start_frame
                and current_frame < text_end_frame
            ):
                lines = text.split('\n')
                y = 0
                for line in lines:
                    cv2.putText(frame, line, (position[0], position[1]+y), font, font_scale, font_color, thickness, cv2.LINE_AA)
                    y += meme_config["text"]["size"] * 30

            # Convert the frame to JPEG format
            _, buffer = cv2.imencode('.jpg', frame)
            frame_bytes = buffer.tobytes()

            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')
            current_frame += 1

        cap.release()

    return StreamingResponse(
        generate_frames(),
        media_type="multipart/x-mixed-replace; boundary=frame",
    )
