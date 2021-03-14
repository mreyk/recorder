# Recorder

This application records a video stream from a USB Camera plug into a Raspberry Pi Model 3B using Raspbian OS.

## Requirements

- Python 3
- Supervisor

## Installation

Git clone this repository:

```
git clone git@github.com:mreyk/recorder.git /opt/recorder
```

Install supervisor config file and reread information:

```
cp /opt/recorder/config/recorder.config /etc/supervisor/config.d/.
supervisorctl reread
supervisorctl update
```

Install logrotate configuration:

```
cp /opt/recorder/config/recorder /etc/logrotate.d/recorder
logrotate /etc/logrotate.d/recorder
```

## FFMPEG

Useful FFMPEG commands:

- Record only video until the user stops the running command:

```
ffmpeg -f v4l2 -r 25 -s 640x480 -i /dev/video0 /opt/recorder/output/recorder_TIMESTAMP.avi
```

- Record only video for 60 seconds:

```
ffmpeg -f v4l2 -r 25 -s 1280x720 -i /dev/video0 -t 60 /opt/recorder/output/recorder_TIMESTAMP.avi
```

- Record only video for 1 hour:

```
ffmpeg -f v4l2 -r 25 -s 640x480 -i /dev/video0 -t 3600 /opt/recorder/output/recorder_TIMESTAMP.avi
```

- Record audio and video for 15 seconds:

```
ffmpeg -ar 44100 -ac 1 -f alsa -i hw:1 -f v4l2 -c:v h264 -r 30 -s 1920x1080 -itsoffset 0.5 -i /dev/video0 -t 15 -copyinkf -codec:v copy -codec:a aac -ab 128k -g 10 /opt/recorder/output/recorder_TIMESTAMP.mp4
ffmpeg -n -ar 44100 -ac 1 -f alsa -i hw:1 -f v4l2 -r 25 -s 640x480 -itsoffset 0.5 -i /dev/video0 -t 15 -copyinkf -codec:v copy -codec:a aac -ab 128k /opt/recorder/output/recorder_TIMESTAMP.avi
```

- Record audio and video for 60 seconds:

```
ffmpeg -ar 44100 -ac 1 -f alsa -i hw:1 -f v4l2 -r 30 -s 640x480 -i /dev/video0 -t 60 -codec:v copy -copyinkf -codec:a aac -ab 128k -g 10 /opt/recorder/output/recorder_TIMESTAMP.avi
```
