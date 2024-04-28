const obstacleSpeed = 5;
let score = 0;
let isJumping = false;
const gameContainer = document.getElementById('game-container');
const scoreElement = document.getElementById('score');

// Function to create obstacles
function createObstacle() {
    const obstacle = document.createElement('div');
    obstacle.classList.add('obstacle');
    gameContainer.appendChild(obstacle);

    // Set initial position
    obstacle.style.left = `${Math.random() * (gameContainer.clientWidth - 50)}px`;

    // Move the obstacle
    let obstaclePosition = 0;

    function moveObstacle() {
        obstaclePosition += obstacleSpeed;
        obstacle.style.bottom = `${obstaclePosition}px`;

        // Check for collision with the spaceship
        if (
            obstaclePosition > 0 &&
            obstaclePosition < 50 &&
            spaceship.offsetLeft < obstacle.offsetLeft + 50 &&
            spaceship.offsetLeft + 50 > obstacle.offsetLeft
        ) {
            endGame(); // Collision detected, end the game
        }

        // Remove obstacle when it goes out of the screen
        if (obstaclePosition > gameContainer.clientHeight) {
            obstacle.remove();
            score += 10; // Increase score when obstacle is avoided
        } else {
            requestAnimationFrame(moveObstacle);
        }
    }

    moveObstacle();
}

// Function to create collectibles
function createCollectible() {
    // Similar to createObstacle, implement as needed
}

// Function to create upgrades
function createUpgrade() {
    // Similar to createObstacle, implement as needed
}

function gameLoop() {
    // Move the spaceship based on user input
    document.addEventListener('keydown', (event) => {
        if (event.code === 'Space' && !isJumping) {
            jump();
        }
    });

    function jump() {
        isJumping = true;
        spaceship.classList.add('jump');

        setTimeout(() => {
            spaceship.classList.remove('jump');
            isJumping = false;
        }, 800);
    }

    // Create obstacles periodically
    if (Math.random() < 0.02) {
        createObstacle();
    }

    // Update the score
    scoreElement.innerText = `Score: ${score}`;

    // Continue the game loop
    requestAnimationFrame(gameLoop);
}

// Function to end the game
function endGame() {
    alert(`Game Over! Your score is ${score}.`);
    resetGame();
}

function resetGame() {
    // Reset variables, clear game container, etc.
    score = 0;
    // Additional reset steps...

    // Restart the game loop
    gameLoop();
}

gameLoop();
