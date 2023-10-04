#include "cstdio"
using namespace std;

int main(){
    int t;
    scanf("%d",&t);
    for (int i=0 ; i<t ; i++){
        int D,I;
        int k=1;
        scanf("%d%d",&D,&I);
        for (int j=0 ; j<D-1 ; j++){
            if (I%2){
                k = 2*k;
                I = (I+1)/2;
            } else{
                k = 2*k+1;
                I = I/2;
            }
        }
        printf("%d\n",k);
    }
}