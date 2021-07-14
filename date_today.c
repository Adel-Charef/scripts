#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#define n 12

int main()
{
    int j, m, a, nbj_m;

    printf("Donnez la date d'aujourd'hui: \n");

    printf("\t mois: ");
    scanf("%d", &m);
    while(m <= 0 || m > 12)
    {
    printf("Le mois doit etre compris entre 1 et 12 \n");
    printf("\t mois: ");
    scanf("%d", &m);
    }

    printf("\t jour: ");

    if(m == 2)
    {
        scanf("%d", &j);
        while((j <= 0) || (j > 29))
        {
            printf("erreur! le mois de fevrier compte 28 ou 29 ! ");
            printf("\t jour: ");
            scanf("%d", &j);
        }
    }
    else
    {
    scanf("%d", &j);
    while((j <= 0) || (j > 31))
    {
    printf("Le jour doit etre compris entre 0 et 31 \n");
    printf("\t jour: ");
    scanf("%d", &j);
    }
    } // *******************

    printf("\t annee: ");
    scanf("%d", &a);
    while((a <= 0) || (a > 5000))
    {
    printf("L'annee doit etre comprise entre 1900 et 2999 \n");
    printf("\t annee: ");
    scanf("%d", &a);
    }
    printf("Donnez le nombre de jours du mois saisi: ");
    if(m == 2)
    {
    printf("Entrer 28 ou 29: ");
    scanf("%d", &nbj_m);
    while((nbj_m != 28) && (nbj_m != 29))
    {
        printf("Entrer 28 ou 29: ");
        scanf("%d", &nbj_m);
    }
    }
    else
    {
    printf("Entrer 30 ou 31: ");
    scanf("%d", &nbj_m);
    while((nbj_m != 30) && (nbj_m != 31))
    {
        printf("Entrer 30 ou 31: ");
        scanf("%d", &nbj_m);
    }
    }
    printf("\n");
    if(j < nbj_m)
    {
    j++; // ou j = j + 1
    printf("%d/%d/%d est la date de demain \n", j, m, a);
    }
    else // j >= nbj_m
    {
    if(m < 12)
    {
    m++;
    j = 1;
    printf("%d/%d/%d est la date de demain \n", j, m, a);
    }
    else // m >= 12
    {
    a++;
    m = 1;
    j = 1;
    printf("%d/%d/%d est la date de demain \n", j, m, a);
    }
    }


    return 0;
}
