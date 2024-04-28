document.addEventListener("DOMContentLoaded", function () {
    const board = document.getElementById("game-board");
    const restartBtn = document.getElementById("restart-btn");
    const endGameBtn = document.getElementById("end-game-btn");
    const cells = [];
    let currentPlayer = "X";
    let gameBoard = [
        ["", "", ""],
        ["", "", ""],
        ["", "", ""],
    ];

    // Create the game board
    for (let row = 0; row < 3; row++) {
        for (let col = 0; col < 3; col++) {
            const cell = document.createElement("div");
            cell.classList.add("cell");
            cell.dataset.row = row;
            cell.dataset.col = col;
            cell.addEventListener("click", handleCellClick);
            board.appendChild(cell);
            cells.push(cell);
        }
    }

    // Add event listeners for buttons
    restartBtn.addEventListener("click", resetGame);
    endGameBtn.addEventListener("click", endGame);

    // Handle cell click
    function handleCellClick(event) {
        const row = event.target.dataset.row;
        const col = event.target.dataset.col;

        if (gameBoard[row][col] === "") {
            gameBoard[row][col] = currentPlayer;
            event.target.textContent = currentPlayer;
            
            if (checkWin()) {
                alert(`Player ${currentPlayer} wins!`);
                resetGame();
            } else if (checkDraw()) {
                alert("It's a draw!");
                resetGame();
            } else {
                currentPlayer = currentPlayer === "X" ? "O" : "X";
            }
        }
    }

    // Check for a win
    function checkWin() {
        // Check rows and columns
        for (let i = 0; i < 3; i++) {
            if (
                gameBoard[i][0] === currentPlayer &&
                gameBoard[i][1] === currentPlayer &&
                gameBoard[i][2] === currentPlayer
            ) {
                return true; // Row win
            }
            if (
                gameBoard[0][i] === currentPlayer &&
                gameBoard[1][i] === currentPlayer &&
                gameBoard[2][i] === currentPlayer
            ) {
                return true; // Column win
            }
        }

        // Check diagonals
        if (
            gameBoard[0][0] === currentPlayer &&
            gameBoard[1][1] === currentPlayer &&
            gameBoard[2][2] === currentPlayer
        ) {
            return true; // Diagonal win
        }
        if (
            gameBoard[0][2] === currentPlayer &&
            gameBoard[1][1] === currentPlayer &&
            gameBoard[2][0] === currentPlayer
        ) {
            return true; // Diagonal win
        }

        return false;
    }

    // Check for a draw
    function checkDraw() {
        return gameBoard.every(row => row.every(cell => cell !== ""));
    }

    // Reset the game
    function resetGame() {
        gameBoard = [
            ["", "", ""],
            ["", "", ""],
            ["", "", ""],
        ];
        currentPlayer = "X";
        cells.forEach(cell => {
            cell.textContent = "";
        });
    }

    // End the game prematurely
    function endGame() {
        alert("Game ended. Thanks for playing!");
        resetGame();
    }
});
