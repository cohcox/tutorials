#include <iostream>

int main()
{
    std::cout << "You are a secret agent breaking into a secure server room";
    std::cout << std::endl;
    std::cout << "You need to enter the correct code to continue...";

    const int a = 4;
    const int b = 9;
    const int c = 7;

    const int sum = a + b + c;
    const int product = a * b * c;

    std::cout << std::endl;
    std::cout << sum << std::endl;
    std::cout << product << std::endl;

    return 0;
}