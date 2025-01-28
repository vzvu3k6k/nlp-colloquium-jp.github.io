#!/usr/bin/env python

"""
YouTubeフィードから動画情報を取得し、_schedule/*.mdに動画リンクを追加するスクリプト。

以下の処理を行います:
1. NLPコロキウムのYouTubeチャンネルのフィードを取得
2. 各動画のタイトルから回数を抽出
3. 対応する_schedule/*.mdファイルに動画リンクを追加（未追加の場合のみ）

Dependencies:
- Python 3.x
- 標準ライブラリのみ使用

Usage:
$ python update_video_links.py
"""

import glob
import os.path
import re
import urllib.request
import xml.etree.ElementTree as ET
from dataclasses import dataclass

YOUTUBE_CHANNEL_ID = "UCHMmZqchxs-kiBEEyoIUkNw"


@dataclass
class Video:
    url: str
    title: str

    @property
    def episode_number(self):
        match = re.search(r"第(\d+)回", self.title)
        if not match:
            raise ValueError("Failed to extract episode number from title.")
        return int(match.group(1))

    @property
    def link_text(self):
        return f"[[動画]]({self.url})"


def fetch_youtube_videos(channel_id: str):
    """最新15件の動画情報をYouTubeフィードから取得する"""
    ATOM_NS = "{http://www.w3.org/2005/Atom}"
    feed_url = f"https://www.youtube.com/feeds/videos.xml?channel_id={channel_id}"

    with urllib.request.urlopen(feed_url) as response:
        if response.status != 200:
            raise Exception(f"Failed to fetch YouTube feed. Status: {response.status}")

        feed = ET.fromstring(response.read())
        return [
            Video(
                url=entry.find(f"{ATOM_NS}link").attrib["href"],
                title=entry.find(f"{ATOM_NS}title").text,
            )
            for entry in feed.findall(f"{ATOM_NS}entry")
        ]


def main():
    script_dir = os.path.dirname(__file__)
    schedule_files = sorted(glob.glob(os.path.join(script_dir, "../_schedule/*.md")))

    for video in fetch_youtube_videos(YOUTUBE_CHANNEL_ID):
        schedule_file = schedule_files[video.episode_number - 1]
        with open(schedule_file, "r+", encoding="utf-8") as file:
            content = file.read()
            _, metadata, body = content.split("---\n", 2)
            if "[[動画]]" not in body:
                file.seek(0)
                file.write(f"---\n{metadata}---\n{video.link_text} {body}")


if __name__ == "__main__":
    main()
