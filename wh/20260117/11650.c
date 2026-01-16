#include <stdio.h>
int main(){
    int n=0;
    int a[100][100];
    int x=0;
    int y=0;
    int q=0;
    scanf("%d",&n);
    for(int i=0;i<n;i++){
        scanf("%d %d",&x,&y);
        a[i][0]=x;
        a[i][1]=y;
    }
    for(int i=0;i<n-1;i++){
        for(int j=0;j<n-1;j++){
            if(a[i][0]>a[i+1][0]){
                q=a[i][0];
                a[i][0]=a[i+1][0];
                a[i+1][0]=q;

                q=a[i][1];
                a[i][1]=a[i+1][1];
                a[i+1][1]=q;
            }
            else if(a[i][0]==a[i+1][0]){
                    if(a[i][1]>a[i+1][1]){
                    q=a[i][0];
                    a[i][0]=a[i+1][0];
                    a[i+1][0]=q;

                    q=a[i][1];
                    a[i][1]=a[i+1][1];
                    a[i+1][1]=q;
                }
            }
        }
    }
    for(int i=0;i<n;i++){
        printf("%d %d\n", a[i][0],a[i][1]);
    }

}
