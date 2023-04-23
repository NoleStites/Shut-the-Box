# Shut the Box

<img src="shut-the-box.jpg" width="200">

### Description
"Shut the Box" is a dice game (gambling often being involved) in which a player is given a box with 9 uncovered tiles and continually rolls dice and covers any tiles that add up to the sum of the dice. If you roll the dice and there is no combination of tiles that add up to the dice total, then your game is over and you sum the uncovered tiles for your score. If you successfully cover all of the tiles, then you win; you have shut the box!

### Rules
Here are the rules:
1. Rolling: you must roll two dice if the 7, 8, and 9 tiles are still uncovered. You may roll either one or two dice if the 7, 8, and 9 tiles are all covered.
2. Post-Roll: sum up the total of your dice roll and choose a combination of uncovered tiles to cover that add up to your dice total.
> Example: if a 5 is rolled, you may cover the 5 tile, both the 4 and 1 tiles, or both the 3 and 2 tiles.
3. Go back to Step 1 and repeat until either you have covered all of the tiles (in which case you have "shut the box" and won) or you can no longer cover any more tiles. If you have tiles remaining that cannot be covered, sum the values of the remaining uncovered tiles and that is your score.

---

### Setup Instructions
1. Clone the repository   
`$ git clone https://github.com/NoleStites/Shut-the-Box.git`
2. Change directories into the repo    
`$ cd Shut-the-Box` 
3. Create a Python virtual environment    
`$ python -m venv env`   
`$ source env/bin/activate`     
4. Install the required packages     
`$ pip install -r requirements.txt`     
5. Start the game    
`$ python3 app.py`   
> Note: If you get an error, you may have to use this command to get tkinter to work: `$ sudo apt-get install python3-tk`
