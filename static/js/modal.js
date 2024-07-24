document.addEventListener("DOMContentLoaded", function () {
  var modal = document.getElementById("loginModal");
  var span = document.getElementsByClassName("close")[0];

  function showModal() {
    modal.style.display = "block";
  }

  function hideModal() {
    modal.style.display = "none";
  }

  span.onclick = function () {
    hideModal();
  };

  window.onclick = function (event) {
    if (event.target == modal) {
      hideModal();
    }
  };

  document.getElementById("loginButton").addEventListener("click", showModal);
});
