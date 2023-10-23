#include <stdio.h>
#include <stdlib.h>
#include <time.h>
int game(int n)
{
    srand(time(NULL));
    return rand() % n;
}

int main()
{
    int k, l;
    printf("Hello World\n");
    printf("Welcome Player enter your name\n");
    printf("For computer\n 0-Scissors\n1-rock\n2-paper\n");
    char str[40];
    scanf("%s", str);
    printf("You entered %s as your name", str);
    for (int i = 1; i < 4; i++)
    {
        printf("\nEnter what you choose\n");
        int z;
        scanf("%d", &z);
        printf("You entered %d as option", z);
        int x = game(3);
        printf("\ncomputer chooses %d", x);
        if (x == z)
        {
            printf("\nNobody wins match %d", i);
        }
        if ((x == 0 && z == 2) || (x == 1 && z == 0) || (x == 2 && z == 1))
        {
            printf("\nComputer wins match %d", i);
            k++;
        }
        if ((x == 0 && z == 1) || (x == 1 && z == 2) || (x == 2 && z == 0))
        {
            printf("\n%s wins match %d", str, i);
            l++;
        }
        if (x != 0 && x != 1 && x != 2)
        {
            printf("\nEnter a valid Number");
        }
    }
    printf("\nThe end scores of conputer-%s are %d-%d", str,k,l);
    if (k > l)
    {
        printf("\nComputer wins");
    }
    else if (l > k)
    {
        printf("\ncongratulations you won");
    }

    return 0;
}
