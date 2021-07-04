#include <iostream>

int main()
{
    // Print welcome message to terminal
    std::cout << "You are a secret agent breaking into a secure server room";
    std::cout << std::endl;
    std::cout << "You need to enter the correct code to continue...";

    // Declare the 3 number code
    const int a = 4;
    const int b = 9;
    const int c = 7;

    const int sum = a + b + c;
    const int product = a * b * c;

    // Print out to CLI
    std::cout << std::endl;
    std::cout << sum << std::endl;
    std::cout << product << std::endl;

    return 0;
}