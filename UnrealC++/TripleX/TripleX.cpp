#include <iostream>

int main()
{
    // Print welcome message to terminal
    std::cout << "You are a secret agent breaking into a secure server room";
    std::cout << std::endl;
    std::cout << "You need to enter the correct code to continue...";

    // Declare the 3 number code
    const int CodeA = 4;
    const int CodeB = 9;
    const int CodeC = 7;

    const int CodeSum = CodeA + CodeB + CodeC;
    const int CodeProduct = CodeA * CodeB * CodeC;

    // Print out to CLI
    std::cout << std::endl;
    std::cout << std::endl;
    std::cout << "+ There are 3 numbers in the code" << std::endl;
    std::cout << "+ The codes add-up to: " << CodeSum << std::endl;
    std::cout << "+ The codes multiply to give: " << CodeProduct << std::endl;

    int GuessA, GuessB, GuessC;
    std::cin >> GuessA;
    std::cin >> GuessB;
    std::cin >> GuessC;

    const int GuessSum = GuessA + GuessB + GuessC;
    const int GuessProduct = GuessA * GuessB * GuessC;

    if(GuessSum == CodeSum && GuessProduct == CodeProduct)
    {
        std::cout << "You win!";
    }
    else
    {
        std::cout << "You died";
    }

    return 0;
}