#!/usr/local/bin/python3

#
# takes as input channelurls separated by newlines
# links to all video from the channel in the last 24h
#
# Usage:
#
#     cat subscriptions.txt | ./filter24h.py | youtube-dl -a -
#
# where subscriptions.txt is a list of channelurls
# youtube-dl: https://github.com/ytdl-org/youtube-dl
#

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import re
import sys
import time

options = Options()
options.headless = True
driver = webdriver.Chrome(options=options)

for line in sys.stdin:
    channel_url = line.strip()
    # print("checking channel:", channel_url)
    driver.get("%s/videos" % channel_url)

    video_xpath = "//*[@id=\"items\"]/ytd-grid-video-renderer[1]"
    try:
        videos = driver.find_elements_by_xpath(video_xpath)
    except:
        raise Exception("Failed to find videos in", channel_url)

    for video in videos:
        video_url = video. \
            find_element_by_xpath("//*[@id=\"thumbnail\"]"). \
            get_attribute("href")
        # print("checking video:", video_url)

        date_xpath = "//*[@id=\"metadata-line\"]/span[2]"
        try:
            date = video.find_element_by_xpath(date_xpath)
        except:
            raise Exception("Failed to find date in", video_url)

        # if the date_string contains the word "second(s)" "minute(s)" or "hour(s)",
        # it means the video is less than 24 hours old
        date_string = date.get_attribute("innerText")  # example: 3 weeks ago | 21 hours ago
        within24h = bool(re.search("(second|minute|hour)", date_string))
        if not within24h:
            # print("not within24h:", date_str)
            break

        print(video_url)

driver.close()
