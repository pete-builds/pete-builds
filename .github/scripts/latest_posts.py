"""Rewrite the Writing section of README.md with the latest Stack posts.

Stack posts have no headline; the RSS <title> is the tag list. The first
paragraph of each post is written to stand on its own, so it is the label.
Fails loudly (non-zero exit) rather than blanking the section when the feed
is empty or the README markers are missing.
"""

import html
import re
import sys
import urllib.request
import xml.etree.ElementTree as ET
from email.utils import parsedate_to_datetime

FEED = "https://stack.brooksnewmedia.com/rss.xml"
README = "README.md"
START = "<!-- STACK-POSTS:START -->"
END = "<!-- STACK-POSTS:END -->"
COUNT = 5
SOFT_LEN = 120
MAX_LEN = 160


def label(description: str) -> str:
    text = html.unescape(re.sub(r"<[^>]+>", "", description or "")).strip()
    first = text.split("\n", 1)[0].strip()
    # Whole sentences up to SOFT_LEN; only cut mid-sentence if the first
    # sentence alone runs past MAX_LEN.
    out = ""
    for sentence in re.split(r"(?<=[.!?])\s+", first):
        if out and len(out) + 1 + len(sentence) > SOFT_LEN:
            break
        out = f"{out} {sentence}".strip()
    if len(out) > MAX_LEN:
        out = out[:MAX_LEN].rsplit(" ", 1)[0].rstrip(",.;:") + "..."
    return out.replace("[", "(").replace("]", ")")


def render(feed_xml: str) -> str:
    items = ET.fromstring(feed_xml).iter("item")
    lines = []
    for item in items:
        link = (item.findtext("link") or "").strip()
        text = label(item.findtext("description") or "")
        if not link or not text:
            continue
        date = parsedate_to_datetime(item.findtext("pubDate")).strftime("%b %-d, %Y")
        lines.append(f"- [{text}]({link}) <sub>{date}</sub>")
        if len(lines) == COUNT:
            break
    if not lines:
        sys.exit("feed returned no usable posts; leaving README untouched")
    return "\n".join(lines)


def main() -> None:
    with urllib.request.urlopen(FEED, timeout=30) as resp:
        posts = render(resp.read().decode("utf-8"))
    with open(README, encoding="utf-8") as fh:
        readme = fh.read()
    if readme.count(START) != 1 or readme.count(END) != 1:
        sys.exit(f"expected exactly one {START} and {END} in {README}")
    head, rest = readme.split(START)
    _, tail = rest.split(END)
    new = f"{head}{START}\n{posts}\n{END}{tail}"
    if new != readme:
        with open(README, "w", encoding="utf-8") as fh:
            fh.write(new)


if __name__ == "__main__":
    main()
