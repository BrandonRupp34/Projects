#include <stdio.h>
#include <stdlib.h>
#include <conio.h>
#include <stdbool.h>
// Programmer: Brandon Rupp


/*
Requirements
The game *must* compile and run.  No credit will be given to a project that fails this step.
The game will be played in a field measuring 25 vertical spaces by 80 horizontal spaces - or larger.
The player will start the game with three lives (snakes).
There will be a method for the player to view their current score and number of lives left.
The score will not be reset between lives, but will accumulate during the entire game
The snake will start in the middle of the screen - initial direction East (right).
The snake will change direction when an arrow key is pressed.
The snake will initially consist of 3 segments.
The snake will grow 1 segment for each object collected, to a maximum of 15 segments.
There will be 5 objects on the screen at all times; point values need not be the same for all objects.
Objects will be placed randomly.  As objects are collected, new objects will be randomly placed.
After every 10 objects consumed, the player will earn an additional life.
After every 10 objects consumed, the speed of the snake will increase by ten per cent (10%).
*/

int i = 0;
int j = 0;
int k = 0;
int n = 0;
int lives = 3;
int score = 0;
const int borderWidth = 80;
const int borderHeight = 25;
int watermelonScore = 5;
int appleScore = 10;
int mangoScore = 15;
int orangeScore = 25;
int pearScore = 50;
int snakeHeadX;
int snakeHeadY;
int snakeBodyX[80];
int snakeBodyY[25];
int snakeBodyLength = 2;
int snakeTailX;
int snakeTailY;
int temp1X, temp2X;
int temp1Y, temp2Y;
int mangoX, mangoY;
int appleX, appleY;
int orangeX, orangeY;
int watermelonX, watermelonY;
int pearX, pearY;
int fruitCollected;
int oldgetchar;
double snakeSpeed;
char mango = 'M';
char apple = 'A';
char orange = 'G';
char watermelon = 'W';
char pear = 'P';
char snakeHead = '0';
char snakeBody = 'o';
char snakeTail = 'q';
int userInput;
int snakeDirection;
bool printed;

void initialize(void) {
	// starts the snake in the middle of the screen
	snakeHeadX = 40;
	snakeHeadY = 12;
	// sets all the fruit to a random location in the game
	mangoX = (rand() % (borderWidth - 3)) + 1;
	mangoY = (rand() % (borderHeight - 3)) + 1;
	appleX = (rand() % (borderWidth - 3)) + 1;
	appleY = (rand() % (borderHeight - 3)) + 1;
	orangeX = (rand() % (borderWidth - 3)) + 1;
	orangeY = (rand() % (borderHeight - 3)) + 1;
	watermelonX = (rand() % (borderWidth - 3)) + 1;
	watermelonY = (rand() % (borderHeight - 3)) + 1;
	pearX = (rand() % (borderWidth - 3)) + 1;
	pearY = (rand() % (borderHeight - 3)) + 1;
	snakeSpeed = 10000000.0;
}
void draw(void) {
	system("cls");
	printf("Lives: %d   Fruit Key: W = 5 Points   A = 10 Points\n", lives);
	printf("Score: %d   M = 15 Points   G = 25 Points   P = 50 Points\n", score);
	for (i = 0; i < borderHeight; i++) {
		for (j = 0; j < borderWidth; j++) {
			if (j == snakeHeadX && i == snakeHeadY) {
				printf("%c", snakeHead);
			}
			else if (j == mangoX && i == mangoY) {
				printf("%c", mango);
			}
			else if (j == appleX && i == appleY) {
				printf("%c", apple);
			}
			else if (j == orangeX && i == orangeY) {
				printf("%c", orange);
			}
			else if (j == watermelonX && i == watermelonY) {
				printf("%c", watermelon);
			}
			else if (j == pearX && i == pearY) {
				printf("%c", pear);
			}
			else if (i == 0 || i == borderHeight - 1) {
				printf("*");
			}
			else if (j == 0 || j == borderWidth - 1) {
				printf("*");
			}
			else {
				printed = false;
				for (k = 0; k < snakeBodyLength; k++) {
					if (snakeBodyX[k] == j && snakeBodyY[k] == i && (k == snakeBodyLength - 1)) {
						printf("%c", snakeTail);
						printed = true;
					}
					else if (snakeBodyX[k] == j && snakeBodyY[k] == i) {
						printf("%c", snakeBody);
						printed = true;
					}
				}
				if (!printed) {
					printf(" ");
				}
			}
		}
		printf("\n");
	}
	bodyMechanics();
}
	
void bodyMechanics(void){
	
	temp1X = snakeBodyX[0];
	temp1Y = snakeBodyY[0];
	snakeBodyX[0] = snakeHeadX;
	snakeBodyY[0] = snakeHeadY;
	for (int i = 1; i < snakeBodyLength; i++) {
		temp2X = snakeBodyX[i];
		temp2Y = snakeBodyY[i];
		snakeBodyX[i] = temp1X;
		snakeBodyY[i] = temp1Y;
		temp1X = temp2X;
		temp1Y = temp2Y;
	}
}

void move(void) {
	for (i = 0; i < snakeSpeed; ++i) { //controls the snake speed
	}
	if (!_kbhit()) {
		snakeHeadX++;
	}
	if (_kbhit()) {
		userInput = _getch();
		if (userInput == 0 || userInput == 224) { // getch returns 2 numbers for arrow keys, first 0 or 224, then the number for the specific arrow key
			switch (_getch()) {

			case 72:
				while (!_kbhit()) {
					for (i = 0; i < snakeSpeed; ++i) {
					}
					snakeHeadY--;
					draw();
					food();
					checkPosition();
					gameover();
				}
				break;

			case 80:
				while (!_kbhit()) {
					for (i = 0; i < snakeSpeed; ++i) {
					}
					snakeHeadY++;
					draw();
					food();
					checkPosition();
					gameover();
				}
				break;

			case 75:
				while (!_kbhit()) {
					for (i = 0; i < snakeSpeed; ++i) {
					}
					snakeHeadX--;
					draw();
					food();
					checkPosition();
					gameover();
				}
				break;

			case 77:
				while (!_kbhit()) {
					for (i = 0; i < snakeSpeed; ++i) {
					}
					snakeHeadX++;
					draw();
					food();
					checkPosition();
					gameover();
				}
				break;
			}
		}
	}
} 

void checkPosition(void) {
		if ((snakeHeadX <= 0 || snakeHeadX >= borderWidth - 1 || snakeHeadY <= 0 || snakeHeadY >= borderHeight - 1)) { // resets the snake and takes away a life if the snake goes outside the border or goes in itself
			lives--;
			snakeHeadX = 40;
			snakeHeadY = 12;
			snakeBodyLength = 4;
		}
		for (i = 4; i < snakeBodyLength; ++i) {
			if ((snakeBodyX[i] == snakeHeadX) && (snakeBodyY[i] == snakeHeadY)) {
				lives--;
				snakeHeadX = 40;
				snakeHeadY = 12;
				snakeBodyLength = 4;
			}
		}
}

void food(void) {
	if ((snakeHeadX == mangoX) && (snakeHeadY == mangoY)) {
		score = score + mangoScore;
		mangoX = (rand() % (borderWidth - 3)) + 1;
		mangoY = (rand() % (borderHeight - 3)) + 1;
		fruitCollected++;
		if (snakeBodyLength < 15) {
			snakeBodyLength++;
		}
		Tenfruits();
	}
	else if ((snakeHeadX == watermelonX) && (snakeHeadY == watermelonY)) {
		score = score + watermelonScore;
		watermelonX = (rand() % (borderWidth - 3)) + 1;
		watermelonY = (rand() % (borderHeight - 3)) + 1;
		fruitCollected++;
		if (snakeBodyLength < 15) {
			snakeBodyLength++;
		}
		Tenfruits();
	}
	else if ((snakeHeadX == appleX) && (snakeHeadY == appleY)) {
		score = score + appleScore;
		appleX = (rand() % (borderWidth - 3)) + 1;
		appleY = (rand() % (borderHeight - 3)) + 1;
		fruitCollected++;
		if (snakeBodyLength < 15) {
			snakeBodyLength++;
		}
		Tenfruits();
	}
	else if ((snakeHeadX == orangeX) && (snakeHeadY == orangeY)) {
		score = score + orangeScore;
		orangeX = (rand() % (borderWidth - 3)) + 1;
		orangeY = (rand() % (borderHeight - 3)) + 1;
		fruitCollected++;
		if (snakeBodyLength < 15) {
			snakeBodyLength++;
		}
		Tenfruits();
	}
	else if ((snakeHeadX == pearX) && (snakeHeadY == pearY)) {
		score = score + pearScore;
		pearX = (rand() % (borderWidth - 3)) + 1;
		pearY = (rand() % (borderHeight - 3)) + 1;
		fruitCollected++;
		if (snakeBodyLength < 15) {
			snakeBodyLength++;
		}
		Tenfruits();
	}
}

void Tenfruits(void) {
	if ((fruitCollected % 10) == 0) {
		lives++;
		snakeSpeed = snakeSpeed * 0.9;
	}
}

void gameover(void) {
	if (lives == 0) {
		system("cls");
		printf("Game over\nYour score was %d", score);
		getchar();
	}
	return 0;
}

void main(void) {
		
	initialize();
	
	while (lives != 0) {
		draw();
		
		move();

	}
	gameover();

}
