#include <cs50.h>
#include <stdio.h>

void print_row(int spaces, int bricks);

int main(void)
{
    // Prompt the user for the pyramid's height
    int n;
    do
    {
        n = get_int("Height: ");
    }
    while (n < 1);

    // Print a pyramid of that height
    for (int i = 0; i < n; i++)
    {
        print_row(n - i - 1, i + 1);
    }
}

void print_row(int spaces, int bricks)
{
    for (int k = 0; k < spaces; k++)
    {
        printf(" ");
    }

    // Print bricks
    for (int k = 0; k < bricks; k++)
    {
        printf("#");
    }
    // Print gap
    printf("  ");

    // print right pyramid
    for (int k = 0; k < bricks; k++)
    {
        printf("#");
    }

    printf("\n");
}
