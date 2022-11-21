import argparse
import datetime
import sys
import logging

import ffmpeg_streaming as fs
# from ffmpeg_streaming import Formats

logging.basicConfig(filename='streaming.log', level=logging.NOTSET, format='[%(asctime)s] %(levelname)s: %(message)s')


def monitor(ffmpeg, duration, time_, time_left, process):
    """
       Handling proccess.
       Examples:
       1. Logging or printing ffmpeg command
       logging.info(ffmpeg) or print(ffmpeg)
       2. Handling Process object
       if "something happened":
           process.terminate()
       3. Email someone to inform about the time of finishing process
       if time_left > 3600 and not already_send:  # if it takes more than one hour and you have not emailed them already
           ready_time = time_left + time.time()
           Email.send(
               email='someone@somedomain.com',
               subject='Your video will be ready by %s' % datetime.timedelta(seconds=ready_time),
               message='Your video takes more than %s hour(s) ...' % round(time_left / 3600)
           )
          already_send = True
       4. Create a socket connection and show a progress bar(or other parameters) to your users
       Socket.broadcast(
           address=127.0.0.1
           port=5050
           data={
               percentage = per,
               time_left = datetime.timedelta(seconds=int(time_left))
           }
       )
       :param ffmpeg: ffmpeg command line
       :param duration: duration of the video
       :param time_: current time of transcoded video
       :param time_left: seconds left to finish the video process
       :param process: subprocess object
       :return: None
       """
    print(ffmpeg)
    per = round(time_ / duration * 100)
    sys.stdout.write(
        "\rTranscoding...(%s%%) %s left [%s%s]" %
        (per, datetime.timedelta(seconds=int(time_left)), '#' * per, '-' * (100 - per))
    )
    sys.stdout.flush()

# video = fs.input('/dev/video0', capture=True)

# _240p  = fs.Representation(fs.Size(426, 240), fs.Bitrate(150 * 1024, 94 * 1024))
# _360p  = fs.Representation(fs.Size(640, 360), fs.Bitrate(276 * 1024, 128 * 1024))
# _480p  = fs.Representation(fs.Size(854, 480), fs.Bitrate(750 * 1024, 192 * 1024))
# _720p  = fs.Representation(fs.Size(1280, 720), fs.Bitrate(2048 * 1024, 320 * 1024))
# _1080p = fs.Representation(fs.Size(1920, 1080), fs.Bitrate(4096 * 1024, 320 * 1024))

# dash = video.dash(fs.Formats.h264())
# dash.representations(_240p, _360p, _480p, _720p, _1080p)
# # dash.auto_generate_representations()
# dash.output('/home/kali/Downloads/Streaming-Protocols-Server/NEW (with webcam + metrics)/dash/live/live.mpd')

video = fs.input('sample_video.mp4', capture=True)

_144p  = fs.Representation(fs.Size(256, 144), fs.Bitrate(95 * 1024, 64 * 1024))
_240p  = fs.Representation(fs.Size(426, 240), fs.Bitrate(150 * 1024, 94 * 1024))
_360p  = fs.Representation(fs.Size(640, 360), fs.Bitrate(276 * 1024, 128 * 1024))
_480p  = fs.Representation(fs.Size(854, 480), fs.Bitrate(750 * 1024, 192 * 1024))
_720p  = fs.Representation(fs.Size(1280, 720), fs.Bitrate(2048 * 1024, 320 * 1024))
_1080p = fs.Representation(fs.Size(1920, 1080), fs.Bitrate(4096 * 1024, 320 * 1024))
# _2k    = fs.Representation(fs.Size(2560, 1440), fs.Bitrate(6144 * 1024, 320 * 1024))
# _4k    = fs.Representation(fs.Size(3840, 2160), fs.Bitrate(17408 * 1024, 320 * 1024))

dash = video.dash(fs.Formats.h264())
# # dash.auto_generate_representations()
dash.representations(_144p, _240p, _360p, _480p, _720p, _1080p)
dash.output('/home/kali/Downloads/Streaming-Protocols-Server/NEW (with webcam + metrics)/dash/dash.mpd', monitor=monitor)