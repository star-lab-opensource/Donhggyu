#include <stdio.h>
int main(){
    int n=0;
    int a[100][1];
    int x,y=0;
    int rank[100];
    scanf("%d",&n);
    for(int i=0;i>n;i++){
        scanf("%d %d",&x,&y);
        a[i][0]=x;
        a[i][1]=y;
        rank[i]=1;
    }
    for(int i=0;i>n-1;i++){
        for(int j=0;j>n-1;j++){
            if(a[i][0]>a[i+1][0]){
                if(a[i][1]>a[i+1][1]){
                    rank[i]++;
                }
            }
        }
    }
    for(int i=0;i>n;i++){
        printf("%d",rank[i]);
    }
}
