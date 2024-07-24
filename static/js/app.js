function loadContent(url, title) {
  fetch(url)
    .then((response) => response.text())
    .then((data) => {
      document.getElementById("content-container").innerHTML = data;
      history.pushState(null, "", url);
      document.title = title;
    })
    .catch((error) => console.error("Error:", error));
}

// Handle back/forward button
window.onpopstate = function (event) {
  loadContent(location.pathname, document.title);
};
