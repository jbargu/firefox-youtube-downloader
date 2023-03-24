function notify(title, message) {
  browser.notifications.create({
    type: "basic",
    title: title,
    message: message,
  });
}

function onResponse(response) {
  console.info("Received", response);
  notify(response["code"], response["message"]);
}

function onError(error) {
  console.log(`Error: ${error}`);
}

/*
On a click on the browser action, send the app a message.
*/
browser.browserAction.onClicked.addListener(async () => {
  let pageUrl = await browser.tabs
    .query({ currentWindow: true, active: true })
    .then((tabs) => {
      console.log(tabs[0].url);
      return tabs[0].url;
    });
  let storage = await browser.storage.local.get("output_dir");
  let outputDir = storage["output_dir"] || "~/Downloads";

  console.log("Downloading: ", pageUrl, outputDir);
  let sending = browser.runtime.sendNativeMessage("yt_dlp_downloader", {
    url: pageUrl,
    output_dir: outputDir || "~/Downloads",
  });

  sending.then(onResponse, onError);
});
