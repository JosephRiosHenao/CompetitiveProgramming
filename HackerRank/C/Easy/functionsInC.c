
//Librerias de hackerrank
//#include <iostream>
//#include <cstdio>
//using namespace std;

/*
Add `int max_of_four(int a, int b, int c, int d)` here.
*/
int max_of_four(int a,int b,int c,int d){
    int answer = a;
    answer = max(answer,b);
    answer = max(answer,c);
    answer = max(answer,d);
    return answer;
}

int main() {
    int a, b, c, d;
    scanf("%d %d %d %d", &a, &b, &c, &d);
    int ans = max_of_four(a, b, c, d);
    printf("%d", ans);
    
    return 0;
}

