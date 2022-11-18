import ffmpeg_streaming as fs

video = fs.input('/dev/video0', capture=True)

_240p  = fs.Representation(fs.Size(426, 240), fs.Bitrate(150 * 1024, 94 * 1024))
_360p  = fs.Representation(fs.Size(640, 360), fs.Bitrate(276 * 1024, 128 * 1024))
_480p  = fs.Representation(fs.Size(854, 480), fs.Bitrate(750 * 1024, 192 * 1024))
_720p  = fs.Representation(fs.Size(1280, 720), fs.Bitrate(2048 * 1024, 320 * 1024))
_1080p = fs.Representation(fs.Size(1920, 1080), fs.Bitrate(4096 * 1024, 320 * 1024))

dash = video.dash(fs.Formats.h264())
dash.representations(_240p, _360p, _480p, _720p, _1080p)
# dash.auto_generate_representations()
dash.output('/home/kali/Downloads/Streaming/mix/dash/live/live.mpd')

# video = fs.input('sample_video.mp4', capture=True)

# _144p  = fs.Representation(fs.Size(256, 144), fs.Bitrate(95 * 1024, 64 * 1024))
# _240p  = fs.Representation(fs.Size(426, 240), fs.Bitrate(150 * 1024, 94 * 1024))
# _360p  = fs.Representation(fs.Size(640, 360), fs.Bitrate(276 * 1024, 128 * 1024))
# _480p  = fs.Representation(fs.Size(854, 480), fs.Bitrate(750 * 1024, 192 * 1024))
# _720p  = fs.Representation(fs.Size(1280, 720), fs.Bitrate(2048 * 1024, 320 * 1024))
# _1080p = fs.Representation(fs.Size(1920, 1080), fs.Bitrate(4096 * 1024, 320 * 1024))
# _2k    = fs.Representation(fs.Size(2560, 1440), fs.Bitrate(6144 * 1024, 320 * 1024))
# _4k    = fs.Representation(fs.Size(3840, 2160), fs.Bitrate(17408 * 1024, 320 * 1024))

# dash = video.dash(fs.Formats.h264())
# # dash.auto_generate_representations()
# dash.representations(_144p, _240p, _360p, _480p, _720p, _1080p, _2k, _4k)
# dash.output('/home/kali/Downloads/Streaming/mix/dash/dash.mpd')