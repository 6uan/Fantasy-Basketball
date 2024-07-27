// Toggle between signup and login forms
document.getElementById("signupTab").addEventListener("click", function () {
  document.getElementById("signupForm").classList.remove("hidden");
  document.getElementById("loginForm").classList.add("hidden");
  document.getElementById("signupTab").classList.add("border-b-2");
  document.getElementById("loginTab").classList.remove("border-b-2");
});

document.getElementById("loginTab").addEventListener("click", function () {
  document.getElementById("loginForm").classList.remove("hidden");
  document.getElementById("signupForm").classList.add("hidden");
  document.getElementById("loginTab").classList.add("border-b-2");
  document.getElementById("signupTab").classList.remove("border-b-2");
});

// Toggle login modal visibility
document.getElementById("loginButton").addEventListener("click", function () {
  document.getElementById("loginModal").classList.remove("hidden");
});

// Close modal when clicking on the close button
document.querySelectorAll(".close").forEach(function (element) {
  element.addEventListener("click", function () {
    document.getElementById("loginModal").classList.add("hidden");
  });
});

// Close modal when clicking outside of the modal
window.addEventListener("click", function (event) {
  if (event.target == document.getElementById("loginModal")) {
    document.getElementById("loginModal").classList.add("hidden");
  }
});
