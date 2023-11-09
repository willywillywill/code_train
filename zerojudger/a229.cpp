#include <stdio.h>
int n, num;
char arr[30];
void dfs(int now, int left, int right) {
    if(left>n || right>left)return; /*左括弧或右括弧數量大於n，或是左括弧數量小於右括弧，皆為不合法的排列，可以直接返回*/
    if(now==num) {
        arr[num]='\0'; /*!在結尾補/0再輸出字串，比以for迴圈輸出字元陣列快*/
        printf("%s\n", arr);
        return;
    }
    arr[now]='('; /*選取左括弧*/
    dfs(now+1, left+1, right); /*將左括弧數量加一後進入下一項的討論*/
    arr[now]=')'; /*選取右括弧*/
    dfs(now+1, left, right+1); /*將右括弧數量加一後進入下一項的討論*/
}
int main() {
    while(scanf("%d", &n)!=EOF) {
        num=2*n; /*!在這裡先把num算出來，每筆測資只需算一次，比每次遞迴時都將條件設為2*n快*/
        dfs(0, 0, 0);
    }
    return 0;
}