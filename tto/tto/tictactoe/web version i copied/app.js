const PLAYER_TOKEN = 'X'
const COMPUTER_TOKEN = 'Y'

$(document).ready(function() {
    const grid =  [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']
    ];

    function isgameover() {
        //check horizontal
        for (var i = 0; i<3; i++) {
            if (grid[i][0] !== ' ' &&
                grid[i][0] === grid[i][1] &&
                grid[i][0] === grid[i][2] ) {

                return grid [1][0]
            }
        }

        //check vertical
        for (var j = 0; j<3; j++) {
            if (grid[0][j] !== ' ' &&
                grid[0][j] === grid[1][j] &&
                grid[0][j] === grid[2][j] ) {

                return grid [0][j]
            }
        }
        
        //check diagonal top left bottom right wtf
        if (grid[0][0] !== ' ' &&
            grid[0][0] === grid[1][1] &&
            grid[0][0] === grid[2][1] ) {

            return grid [0][0]
        }

        //check diagonal bottom left to top right
        if (grid[2][0] !== ' ' &&
            grid[2][2] === grid[1][1] &&
            grid[2][2] === grid[0][2] ) {

            return grid [2][0]
        }

        for (var i = 0; i<3; i++) {
            for (var j = 0; j<3; j++) {
                if (grid[i][j]=== ' ') {

                    return false;
                }
            }
        }

        return null;
    }

    function moveAI() {
        for (var i = 0; i<3; i++) {
            for (var j = 0; j<3; j++) {
                if (grid[i][j]=== ' ') {

                    return {
                        i: i,
                        j: j
                    };
                }
            }
        }
        return null;
    }

    $('.col').click(function() {
        $this =$(this);
        $this.html(PLAYER_TOKEN);
        const i = $this.data('i');
        const j = $this.data('j');
        grid[i][j] = PLAYER_TOKEN;
        

        let gameState = isgameover()
        if (gameState) {
            alert('game over:  ' + gameState);

        }
        else {      
            const move = moveAI()
            grid[move,i][move,j] = COMPUTER_TOKEN;
            $('.col[data-i=' + move.i + '][data-j='+ move.j + ']').html(COMPUTER_TOKEN);
        }
        gameState = isgameover()
        if (gameState) {
            alert('game over:  ' + gameState);
        }
    });
});

