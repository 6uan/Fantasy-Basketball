console.log('Working')

// waits for the DOM to load before running the code inside
document.addEventListener('DOMContentLoaded', () => {
  const selectButtons = document.querySelectorAll('.select-button')

  selectButtons.forEach((button) => {
    button.addEventListener('click', async (e) => {
      e.preventDefault()
      const playerId = e.target.dataset.playerId
      const playerPosition = e.target.dataset.playerPosition
        .replace(/-/g, '_')
        .toLowerCase()
      const playerPrice = e.target.dataset.playerPrice

      try {
        const response = await fetch('/add-to-team', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({ playerId, playerPosition, playerPrice }),
        })

        const result = await response.json()

        if (response.ok) {
          alert(result.message)
          // Update the displayed coin balance
          const coinElement = document.querySelector('.coin-balance')
          if (coinElement) {
            coinElement.textContent = result.new_balance
          }
        } else {
          alert(result.message)
        }
      } catch (error) {
        console.error('Error:', error)
      }
    })
  })
})

// Matchday Logic

const incrementButtons = document.querySelectorAll('.increment')

incrementButtons.forEach((button) => {
  button.addEventListener('click', async (e) => {
    console.log('Increment matchday button clicked')

    try {
      const response = await fetch('/increment-matchday', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
      })

      console.log('Response status:', response.status)

      if (response.ok) {
        const data = await response.json()
        console.log('Data:', data)
        document.getElementById('matchday').innerText = `GAME: ${data.matchday}`
      } else {
        console.log('Response not OK')
        const result = await response.json()
        console.log('Response JSON:', result)
        alert(`Failed to increment matchday: ${result.message}`)
      }
    } catch (error) {
      console.error('Error in fetch request:', error)
      alert('An unexpected error occurred.')
    }
  })
})

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
