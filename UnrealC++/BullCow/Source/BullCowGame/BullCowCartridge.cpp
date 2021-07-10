// Fill out your copyright notice in the Description page of Project Settings.
#include "BullCowCartridge.h"

void UBullCowCartridge::BeginPlay() // When the game begins
{
    Super::BeginPlay();

    SetupGame();
}

void UBullCowCartridge::OnInput(const FString& Input) // When the player hits enter
{
    ClearScreen();
    /* // if game is over ClearScreen() and SetupGame()
    // else Check the player guess */

    if (Input == HiddenWord)
    {
        PrintLine(TEXT("Huzzah! You got it!"));
        // bGameOver = true;
    }
    else
    {
        if (Input.Len() != HiddenWord.Len()) 
        {
            PrintLine(TEXT("The Hidden Word is %i characters long, try again!"), HiddenWord.Len());
        }
        PrintLine(TEXT("Not Quite"));

        // bGameOver = false;
    }
    // Check if Isogram
    // Remove a life

    // Check if lives > 0
    // If true PlayAgain
    // If false GameOver
    // Prompt to PlayAgain
}

void UBullCowCartridge::SetupGame()
{
    HiddenWord = TEXT("cakes");
    Lives = 4;
    bGameOver = false;
    
    PrintLine(TEXT("The Hidden Word is: %s."), *HiddenWord);
    
    // Welcome the Player
    PrintLine(TEXT("Welcome to the Bull Cow Game!"));
    PrintLine(TEXT("Guess the %i letter word!"), HiddenWord.Len());
    PrintLine(TEXT("Type in your guess and press Enter to continue..."));

    // Prompt for a guess
}

void UBullCowCartridge::EndGame()
{
    bGameOver = true;
    PrintLine(TEXT("Press enter to continue."));
}