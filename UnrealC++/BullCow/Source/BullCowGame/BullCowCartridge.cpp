// Fill out your copyright notice in the Description page of Project Settings.
#include "BullCowCartridge.h"

void UBullCowCartridge::BeginPlay() // When the game starts
{
    Super::BeginPlay();
    PrintLine(TEXT("Welcome to the Bull Cow Game!"));
    PrintLine(TEXT("Guess the 4 letter word!")); // Magic Number Remove!
    PrintLine(TEXT("Press Enter to continue..."));
    HiddenWord = TEXT("cake");
}

void UBullCowCartridge::OnInput(const FString& Input) // When the player hits enter
{
    ClearScreen();
    PrintLine(Input);

    if (Input == HiddenWord)
    {
        PrintLine(TEXT("Huzzah! You got it!"));
    }
    else
    {
        PrintLine(TEXT("Not Quite")); 
    }
}