#include <bits/stdc++.h>

using namespace std;

#define INF 0xffffff

int solution(int alp, int cop, vector<vector<int>> problems) {
    int maxAlp = 0;
    int maxCop = 0;

    for(int i=0; i<problems.size(); i++){
        maxAlp = max(maxAlp,problems[i][0]);
        maxCop = max(maxCop,problems[i][1]);
    }
    alp = min(alp,maxAlp);
    cop = min(cop,maxCop);

    //dp[a][c] = k 는 알고력 a와 코딩력 b를 얻는데 걸리는 시간
    int dp[maxAlp+1][maxCop+1]; 
    fill(&dp[0][0], &dp[maxAlp][maxCop+1], INF);
    dp[alp][cop] = 0;

    for(int i=alp; i<maxAlp+1; i++){
        for(int j=cop; j<maxCop+1; j++){
            if(i+1<=maxAlp)
                dp[i+1][j] = min(dp[i+1][j], dp[i][j]+1);                
            if(j+1<=maxCop)
                dp[i][j+1] =  min(dp[i][j+1], dp[i][j]+1);           

            for(int idx=0; idx<problems.size(); idx++){
                if(i >= problems[idx][0] && j >=problems[idx][1]){

                    int nextAlp = min(maxAlp, i+problems[idx][2]);
                    int nextCop = min(maxCop, j+problems[idx][3]);
                    
                    //min(문제 중 가장 큰 알고력, 현재의 알고력, 코딩력 + 문제를 풀면 얻는 알고력,코딩력)
                    dp[nextAlp][nextCop] = min(dp[nextAlp][nextCop], dp[i][j]+problems[idx][4]);
                }
            }
        }
    }

    return dp[maxAlp][maxCop];
}

int main(){

    int alp;
    int cop;
    vector<vector<int>> problems;

    cout << solution(alp, cop, problems);

    return 0;
}