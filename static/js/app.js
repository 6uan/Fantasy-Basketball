console.log('Working')

// waits for the DOM to load before running the code inside
document.addEventListener('DOMContentLoaded', () => {
  const selectButtons = document.querySelectorAll('.select-button')

  const roundToOneDecimal = (value) => {
    return Math.round(value * 10) / 10
  }

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
          // Update the displayed coin balance and points
          const coinElement = document.querySelector('.coin-balance.coins')
          const pointsElement = document.querySelector('.coin-balance.points')

          if (coinElement) {
            coinElement.textContent = roundToOneDecimal(
              result.new_balance.coins,
            )
          }

          if (pointsElement) {
            pointsElement.textContent = roundToOneDecimal(
              result.new_balance.points,
            )
          }
        } else {
          alert(result.message)
        }
      } catch (error) {
        console.error('Error:', error)
      }
    })
  })

  document
    .getElementById('reset-matchday-button')
    .addEventListener('click', function () {
      fetch('/reset-matchday', {
        method: 'POST',
      })
        .then((response) => response.json())
        .then((data) => {
          alert(data.message)
          // Reset points on the frontend
          const pointsElement = document.querySelector('.coin-balance.points')
          if (pointsElement) {
            pointsElement.textContent = 0
          }
          document.getElementById(
            'matchday',
          ).innerText = `Matchday ${data.matchday}`
        })
        .catch((error) => console.error('Error:', error))
    })
})
