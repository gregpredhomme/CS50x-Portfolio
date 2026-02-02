#include <ctype.h>
#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>


bool only_digits(string s);
char rotate(char c, int n);

int main(int argc, string argv[])
{
    // Make sure program was run with just one command-line argument
    if (argc != 2)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }

    // Make sure every character in argv[1] is a digit
    if (!only_digits(argv[1]))
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }

    // Convert argv[1] from a `string` to an `int`
    int k = atoi(argv[1]);

    // Prompt user for plaintext
    string plaintext = get_string("plaintext: ");
    printf("ciphertext: ");

    // For each character in the plaintext:
    for (int i = 0, n = strlen(plaintext); i < n; i++)
    {
        printf("%c", rotate(plaintext[i], k));
    }
    printf("\n");
    return 0;
        // Rotate the character if it's a letter
}

bool only_digits(string s)
{
    // loop
    for (int i = 0, n = strlen(s); i < n; i++)
    {
        if (!isdigit(s[i]))
        {
            return false;
        }
    }
    return true;
}

char rotate(char c, int n)
{
    if (isupper(c))
    {
        return ((c - 'A' + n) % 26) + 'A';
    }
    else if (islower(c))
    {
        return ((c - 'a' + n) % 26) + 'a';
    }
    else
    {
        return c;
    }
}
