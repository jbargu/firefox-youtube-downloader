#!/usr/bin/env python3

import sys
import json
import struct
import subprocess

# Python 3.x version
# Read a message from stdin and decode it.
def getMessage():
    rawLength = sys.stdin.buffer.read(4)
    if len(rawLength) == 0:
        sys.exit(0)
    messageLength = struct.unpack("@I", rawLength)[0]
    message = sys.stdin.buffer.read(messageLength).decode("utf-8")
    return json.loads(message)


# Encode a message for transmission,
# given its content.
def encodeMessage(messageContent):
    # https://docs.python.org/3/library/json.html#basic-usage
    # To get the most compact JSON representation, you should specify
    # (',', ':') to eliminate whitespace.
    # We want the most compact representation because the browser rejects
    # messages that exceed 1 MB.
    encodedContent = json.dumps(messageContent, separators=(",", ":")).encode("utf-8")
    encodedLength = struct.pack("@I", len(encodedContent))
    return {"length": encodedLength, "content": encodedContent}


# Send an encoded message to stdout
def sendMessage(encodedMessage):
    sys.stdout.buffer.write(encodedMessage["length"])
    sys.stdout.buffer.write(encodedMessage["content"])
    sys.stdout.buffer.flush()


while True:
    receivedMessage = getMessage()

    url = receivedMessage["url"]
    output_dir = receivedMessage["output_dir"]
    output = subprocess.run(
        [
            "yt-dlp",
            "-x",
            "--audio-format",
            "mp3",
            url,
            "-P",
            f"home:{output_dir}",
        ],
        capture_output=True,
    )
    if output.returncode == 0:
        response = {
            "code": "success",
            "message": f"Video {url} was saved to {output_dir}.",
        }
    else:
        response = {
            "code": "error",
            "message": f"Video {url} download failed. Stderr: {str(output.stderr)}",
        }

    sendMessage(encodeMessage(response))
