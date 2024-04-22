#!/usr/bin/env python

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
        if match:
            return int(match.group(1))
        raise ValueError("Failed to extract episode number from title.")

    @property
    def link_text(self):
        return f"[[動画]]({self.url})"


def fetch_and_parse_youtube_feed(channel_id):
    url = f"https://www.youtube.com/feeds/videos.xml?channel_id={channel_id}"
    with urllib.request.urlopen(url) as response:
        if response.status == 200:
            return ET.fromstring(response.read())
        raise Exception(f"Failed to fetch YouTube feed. Status: {response.status}")


def main():
    script_dir = os.path.dirname(__file__)
    schedule_files = sorted(glob.glob(os.path.join(script_dir, "../_schedule/*.md")))

    feed = fetch_and_parse_youtube_feed(YOUTUBE_CHANNEL_ID)
    for entry in feed.findall("{http://www.w3.org/2005/Atom}entry"):
        title = entry.find("{http://www.w3.org/2005/Atom}title").text
        link = entry.find("{http://www.w3.org/2005/Atom}link").attrib["href"]

        video = Video(url=link, title=title)
        schedule_file = schedule_files[video.episode_number - 1]

        with open(schedule_file, "r+", encoding="utf-8") as file:
            content = file.read()
            _, metadata, body = content.split("---\n", 2)
            if "[[動画]]" not in body:
                file.seek(0)
                file.write(f"---\n{metadata}---\n{video.link_text} {body}")


if __name__ == "__main__":
    main()
