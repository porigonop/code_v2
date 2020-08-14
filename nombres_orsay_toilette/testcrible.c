#include<stdio.h>
#include<math.h>

int cribble(int nb){
    double nb_d = nb;
    double nb_sqrt = sqrt(nb_d) + 1;
    char L[nb];
    for(int i = 0; i < nb; i++)
        L[i] = (i & 1);
    L[0] = 0; L[1] = 0; L[2] = 1;
    int cur = 3;
    while (cur < nb_sqrt){
        if (!L[cur])
        {
            cur += 2;
            continue;
        }
        int cur22 = cur * cur;
        for (int i = cur22; i < nb; i += cur){
            L[i] = 0;
        }
        cur += 2;
    }
    int nb_prime = 0;
    for (int i = 0; i < nb; i++){
        if (L[i])
            nb_prime++;
    }
    return nb_prime;

}

int main(){
    int nb_prime = cribble(1000000);
    printf("%d\n", nb_prime);


}

