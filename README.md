# [lol.uwu.gal](https://lol.uwu.gal)
 A funny ip-geolocation website that incorporates memes into web security awareness.

# PRs and extra memes are welcome!
 Feel free to create a pull-request improving the code (or expanding on it!)

 If you'd like to submit a new meme please make sure you read the below!
 1. Upload the font to `static/fonts/` as a `.ttf` (or use an existing one).
 2. Upload the video to `static/videos/` as a `.mp4`.
 3. Add the video settings to `src/config/ip_memes.json` with the appropriate information!
 4. Create a pull request with your changes!

## Project requirements
 1. Python3.12
 2. Packages listed in `requirements.txt`

## Setup guide
 1. `python3.12 -m venv venv`
 2. `source venv/bin/activate`
 3. `pip install -r requirements.txt`
 4. `cd src`
 5. `uvicorn router:app` OR `gunicorn -c gunicorn_conf.py`

## Quicklinks
 - [lol.uwu.gal](https://lol.uwu.gal) - A live version of this repro.
 - [git.uwu.gal/lol.uwu.gal](https://git.uwu.gal/lol.uwu.gal) - A quicklink to this repro

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=Isabe1le/lol.uwu.gal&type=Date)](https://star-history.com/#Isabe1le/lol.uwu.gal&Date)