# Firefox extension for downloading Youtube using `yt-dlp`
A very simple Firefox extension to download audio of the current Youtube URL by clicking onto the extension icon. It requires `yt-dlp` to be available on the path. The output folder can be changed in the preferences. Based of the [native messaging example](https://github.com/mdn/webextensions-examples/tree/main/native-messaging).

The WebExtension, which can be found under "add-on", connects to the native application and listens to messages from it. It then sends a message to the native application when the user clicks on the WebExtension's browser action. 

The native application, which can be found under "app", listens for messages from the WebExtension. The native application is written in Python.

## Setup ##

To get this working, there's a little setup to do. The signed `.xpi` file can be downloaded from [the release page](https://github.com/jbargu/firefox-youtube-downloader/releases/tag/v1.0.0).

### Mac OS/Linux setup ###

1. Install [yt-dlp](https://github.com/yt-dlp/yt-dlp).
2. Check that the [file permissions](https://en.wikipedia.org/wiki/File_system_permissions) for `yt_dlp_downloader.py` include the `execute` permission.
3. Edit the "path" property of `yt_dlp_downloader.json` to point to the location of `yt_dlp_downloader.py` on your computer.
4. copy `yt_dlp_downloader.json` to the correct location on your computer. See [App manifest location ](https://developer.mozilla.org/en-US/Add-ons/WebExtensions/Native_manifests#Manifest_location) to find the correct location for your OS. I use a symbolic linking:

    ```bash
    ln -s <path>/firefox-youtube-downloader/app/yt_dlp_downloader.json ~/.mozilla/native-messaging-hosts/yt_dlp_downloader.json
    ```

## Debugging

Then just install the add-on as usual, by visiting about:debugging, clicking "Load Temporary Add-on", and selecting the add-on's "manifest.json".

Now, open the extension's console using the "Inspect" button - this is where you'll see communication between the browser and native app. 

You should see a new browser action icon in the toolbar. Click it. If you are on a Youtube video, the video will be downloaded.


## Developing

Run:

```
npm run start
```

or use the above method for debugging if you don't like to install `npm` packages.
