#include <iostream>
#include <ctime>

// Game introduction
void PrintIntroduction(int Difficulty)
{
    // Print welcome message to terminal
    std::cout << "\n\nYou are a secret agent breaking into a level " << Difficulty;
    std::cout << " secure server room...\nEnter the correct code to continue...\n\n";
}

// Main game loop
bool PlayGame(int Difficulty)
{
    PrintIntroduction(Difficulty);

    // Declare the 3 number code
    const int CodeA = rand() % Difficulty + Difficulty;
    const int CodeB = rand() % Difficulty + Difficulty;
    const int CodeC = rand() % Difficulty + Difficulty;

    const int CodeSum = CodeA + CodeB + CodeC;
    const int CodeProduct = CodeA * CodeB * CodeC;

    // Print out to CLI
    std::cout << "+ There are 3 numbers in the code";
    std::cout << "\n+ The codes add-up to: " << CodeSum;
    std::cout << "\n+ The codes multiply to give: " << CodeProduct << std::endl;

    // Store player guess
    int GuessA, GuessB, GuessC;
    std::cin >> GuessA >> GuessB >> GuessC;

    int GuessSum = GuessA + GuessB + GuessC;
    int GuessProduct = GuessA * GuessB * GuessC;

    // Check if player's guess is correct
    if(GuessSum == CodeSum && GuessProduct == CodeProduct)
    {
        std::cout << "\nYou win!";
        return true;
    }
    else
    {
        std::cout << "\nYou died!";
        return false;
    }
}

int main()
{
    srand(time(NULL)); // Create random sequence based on the time of day

    int LevelDifficulty = 1;
    const int MaxLevel = 10;

    while(LevelDifficulty <= MaxLevel) // Loop until all levels are completed
    {
        bool bLevelComplete = PlayGame(LevelDifficulty);
        std::cin.clear(); // Clears any errors
        std::cin.ignore(); // Discards the buffer

        if(bLevelComplete)
        {
            ++LevelDifficulty;
        }
    }
    return 0;
}