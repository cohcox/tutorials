#include <iostream>

void PrintIntroduction()
{
    // Print welcome message to terminal
    std::cout << "\n\nYou are a secret agent breaking into a secure server room\n";
    std::cout << "You need to enter the correct code to continue...\n\n";
}

bool PlayGame()
{
    PrintIntroduction();

    // Declare the 3 number code
    const int CodeA = 4;
    const int CodeB = 9;
    const int CodeC = 7;

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
    while(true)
    {
        bool bLevelComplete = PlayGame();
        std::cin.clear(); // Clears any errors
        std::cin.ignore(); // Discards the buffer
    }
    return 0;
}