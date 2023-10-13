<h1>Sticman</h1>

<h2>The Problem<h2/>
<p>I want to program a Hangman game. The Player has to guess a Word. But he has to guess the word before the Hangman is going to die. with every wrong letter the gallow grows until a stick man is going to hang and the Player loses. In this game the gallow is replaced by 10 Lives. with every wrong answer the Player loses a Live. If you guess the word before losing all lives you win. if not you lose.</p>




<h2>My Solution</h2>
<p>At the Start of the program it displays the Menu. In the Menu you can choose between the 2 main functions of the program . With the first option you can start the game. With the second option you can add words to the lists form that the program chooses random words for the game. The menu has a 3. Option to End the Program. 
The Menu will be called in a while loop until the User chooses to end the program.</p>
<h3>The Algorithm</h3>
<p>1. Choose random Word<br />
2. Loop while the player didn’t win and has lives leftover.<br />
	A. Ask player to guess a letter<br />
	B. If letter is correct add it to the solution<br />
	C. If not decrease lives by one<br />
	D. Check if Player won and set it to true if he won.<br />
3. After the loop: Print if the player won or lost.</p>
<h3>The Game</h3>
<p>If you type 1 at the start of the Program you will take the Menus Option “START Game'' the program will now call the function game(). This function has a while loop that runs until the Player wins or loses the game. 

Before the While loop starts the Program closes a random word from the wordlist.txt file. With the function selectWord()

Every repetition of the While loop The program will print the current amount of Letters that are guests right and it will show the remaining Lives. After this it asked the Player to enter a Letter. Now the player can guess one letter of the Word. If the Letter is wrong the lives are decreased if the letter is correct the solution will be updated. If the Player didn’t win and Hase lives left the loop will start again. If the loop stops it will be displayed if the Player won or lost.</p>
<h3>Add Words</h3>
If you type 2 at the Menu the program will ask the User for a new word to add to the list. With the Word it starts the function addWord(word). The function adds the Word to the List in the wordlist.txt file. It opens the File and writes the new word at the end of the File.


