#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <stdlib.h>
#include <string.h>

char rotate(char c, int n);

int main(int argc, string argv[])
{
    bool only_digits = true;

    for (int i = 0; i < strlen(argv[1]); i++)
    {
        if (argv[1][i] <= '0' || argv[1][i] >= '9')
        {
            only_digits = false;
        }
    }

    if (only_digits == false || argc != 2)
    {
        printf("Usage: %s key\n", argv[0]);
        return 1;
    }

    string plain_text = get_string("plaintext:  ");
    int n = atoi(argv[1]);

    printf("ciphertext:  ");

    for (int i = 0; i < strlen(plain_text); i++)
    {
        printf("%c", rotate(plain_text[i], n));
    }
    printf("\n");
    return 0;
}





char rotate(char c, int n)
{
    int key = n % 26;
    if (c >= 'a' && c <= 'z')
    {
        int diferencia = c - 'a' + key;
        if (diferencia >= 26)
        {
            return 'a' + (diferencia - 26);
        }
        return c + key;
    }

    else if (c >= 'A' && c <= 'Z')
    {
        int diferencia = c - 'A' + key;
        if (diferencia >= 26)
        {
            return 'A' + (diferencia - 26);
        }
        return c + key;
    }

    else
    {
        return c;
    }
}
