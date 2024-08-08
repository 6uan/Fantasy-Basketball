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
