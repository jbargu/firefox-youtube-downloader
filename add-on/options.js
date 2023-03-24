const DEFAULT_DIR = "~/Downloads";

function saveOptions(e) {
  browser.storage.local.set({
    output_dir: document.querySelector("#output-directory").value,
  });
  e.preventDefault();
}

function restoreOptions() {
  let storageItem = browser.storage.local.get();
  storageItem.then(
    (res) => {
      document.querySelector("#output-directory").value =
        res.output_dir || DEFAULT_DIR;
    },
    (err) => {
      console.error(err);
    }
  );
}

document.addEventListener("DOMContentLoaded", restoreOptions);
document.querySelector("form").addEventListener("submit", saveOptions);
