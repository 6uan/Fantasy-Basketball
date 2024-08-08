console.log("Working");

// waits for the DOM to load before running the code inside
document.addEventListener("DOMContentLoaded", () => {
  console.log("DOM fully loaded and parsed");
  // Get all the select buttons (player options)
  const selectButtons = document.querySelectorAll(".select-button");
  console.log("Select buttons found:", selectButtons.length);

  // Function to add the selected class
  function selectPlayer(button) {
    console.log("Selecting player");
    button.classList.add("bg-slate-600");
  }

  selectButtons.forEach((button) => {
    button.addEventListener("click", async (e) => {
      console.log("Select button clicked");
      const playerId = e.target.dataset.playerId;
      let playerPosition = e.target.dataset.playerPosition;
      const playerPrice = e.target.dataset.playerPrice;
      // Replace hyphens with underscores in playerPosition
      playerPosition = playerPosition.replace(/-/g, "_");

      console.log(
        `Player ID: ${playerId}, Position: ${playerPosition}, Price: ${playerPrice}`
      );

      try {
        const response = await fetch("/add-to-team", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({ playerId, playerPosition, playerPrice }),
        });

        console.log("Response status:", response.status);

        if (response.ok) {
          console.log("Player added successfully");
          alert("Player added to your team!");
          selectPlayer(e.target); // Call the function to add the selected class
        } else {
          console.log("Response not OK");
          const result = await response.json();
          console.log("Response JSON:", result);
          alert(`Failed to add player to your team: ${result.message}`);
        }
      } catch (error) {
        console.error("Error in fetch request:", error);
        alert("An unexpected error occurred.");
      }
    });
  });
});

// Matchday Logic

const incrementButtons = document.querySelectorAll(".increment");

incrementButtons.forEach((button) => {
  button.addEventListener("click", async (e) => {
    console.log("Increment matchday button clicked");

    try {
      const response = await fetch("/increment-matchday", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
      });

      console.log("Response status:", response.status);

      if (response.ok) {
        const data = await response.json();
        console.log("Data:", data);
        document.getElementById(
          "matchday"
        ).innerText = `GAME: ${data.matchday}`;
      } else {
        console.log("Response not OK");
        const result = await response.json();
        console.log("Response JSON:", result);
        alert(`Failed to increment matchday: ${result.message}`);
      }
    } catch (error) {
      console.error("Error in fetch request:", error);
      alert("An unexpected error occurred.");
    }
  });
});

// document
//   .getElementById("increment-matchday-button")
//   .addEventListener("click", function () {
//     console.log("Increment matchday button clicked");
//     fetch("/increment-matchday", {
//       method: "POST",
//     })
//       .then((response) => response.json())
//       .then((data) => {
//         document.getElementById(
//           "matchday"
//         ).innerText = `GAME: ${data.matchday}`;
//       });
//   });
