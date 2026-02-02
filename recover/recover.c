#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

int main(int argc, char *argv[])
{
    // Accept a single command-line argument
    if (argc != 2)
    {
        printf("Usage: ./recover FILE\n");
        return 1;
    }

    // Open the memory card
    FILE *card = fopen(argv[1], "r");
    if (card == NULL)
    {
        printf("Could not open file %s.\n", argv[1]);
        return 1;
    }

    // Create a buffer for a block of data
    uint8_t buffer[512];
    FILE *output_file = NULL;
    char filename[8];
    int image_count = 0;

    // While there's still data left to read from the memory card
    while (fread(buffer, 1, 512, card) == 512)
    {
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {
            if (output_file != NULL)
            {
                fclose(output_file);
            }
            sprintf(filename, "%03i.jpg", image_count);

            output_file = fopen(filename, "w");
            image_count++;
        }
        if (output_file != NULL)
        {
            fwrite(buffer, 1, 512, output_file);
        }
    }
    if (output_file != NULL)
    {
        fclose(output_file);
    }
    fclose(card);

    return 0;
}
