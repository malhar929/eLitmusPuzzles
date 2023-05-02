# eLitmusPuzzles

Admin Id : malhar 

Admin Pass : malhar


****Puzzle1****

**Logic**
The goal of the game is to move the shuffled tiles one at a time by dragging and dropping them into the blank tiles until the original image is restored. 

**ALgorithm**
This code is an HTML file with embedded CSS and JavaScript. It creates an image puzzle game with a 5x5 grid. The game board is divided into two parts: "pieces" and "board." The "pieces" section contains a grid of images that make up the puzzle pieces, and the "board" section is where the user can drag and drop the puzzle pieces to complete the puzzle.
The CSS code is used to style the HTML elements, including the navbar, the puzzle pieces, and the game board. It sets the background color, font, and alignment.
The JavaScript code is used to initialize the game, including setting the number of rows and columns, creating the puzzle pieces, and setting up the drag and drop functionality for the puzzle pieces. It also tracks the number of turns taken to complete the puzzle.
The code includes event listeners for drag and drop functionality, and keeps track of the number of turns taken to complete the puzzle. Additionally, the code includes some CSS styles to format the layout and appearance of the game.


****Puzzle2****

**Logic**

The above code is an HTML and CSS code for an 8 puzzle game. The logic of the game is not explicitly defined in the code, but rather it is implemented using JavaScript, which is not included in the code snippet provided.
The HTML code defines the structure of the web page, including the title, header, body, and footer. The CSS code defines the visual style and layout of the elements on the page, including the navbar, body, puzzle tiles, and modal.
The JavaScript code, which is not included in the snippet, would implement the game logic, including the generation of the puzzle tiles, shuffling of the tiles, movement of the tiles, and checking if the puzzle is solved. The setUp() function that is called in the onload event of the body element is likely the starting point for initializing the game and setting up the event listeners for handling user input.

**Algorithm**
The given code is an HTML document that creates a web page for the 8 puzzle game. It starts with setting the document type and language to HTML and defining the metadata, including the viewport and character set. It also defines some CSS styles, such as font family, colors, and layout for various page elements like the navbar and the game board.
The body of the page contains the HTML elements that create the navbar, the game board, and a modal window that appears when the game is won. The game board consists of a 3x3 grid with nine tiles, where eight of them contain a number from 1 to 8, and one of them is empty. The user can move the tiles around by clicking on them to try to get the numbers in order. When the numbers are in order, the modal window appears with a congratulatory message.
The body of the HTML document has an onload event that triggers a JavaScript function called setUp() when the page is loaded. However, the code for this function is not included in the HTML document.


****Puzzle3****

**Logic**
The above code is an HTML document that defines the structure and appearance of a "Numbers Puzzle" game webpage. The HTML file includes a head section that contains the metadata about the webpage, such as the character encoding, viewport settings, and the webpage title. The head section also includes a link to an external stylesheet that defines the webpage's styles.
The body section of the HTML document contains the visible content of the webpage. It consists of a navbar section that includes a logo and navigation links, a body section that contains the main content of the webpage, and a footer section that includes a message and some buttons.
The body section contains a game section that includes a grid of buttons representing numbers from 1 to 16. The goal of the game is to arrange the buttons in ascending order by clicking on them, thus solving the puzzle. The buttons are styled using CSS to give them a specific appearance, and JavaScript code is used to handle the logic of the game, such as shuffling the buttons and detecting when the puzzle has been solved.

**Algorithm**
1) Initialize a variable number to 20.
2) Check if the number is greater than 0.
3) If the number is greater than 0, then check if it is an even number.
4) If the number is even, then print the number.
5) Subtract 1 from the number.
6) Repeat steps 2-5 until the number becomes less than or equal to 0.
The algorithm essentially starts with a number and checks if it is greater than 0. If it is, it checks if it is an even number and prints it if it is. Then it subtracts 1 from the number and repeats the process until the number becomes less than or equal to 0. This algorithm will print all even numbers from 20 down to 2.
