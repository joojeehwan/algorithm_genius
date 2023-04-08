#include <string>
#include <vector>

using namespace std;

int solution(vector<vector<int>> board, vector<vector<int>> skill) {
    int answer = 0;


    
    return answer;
}

int main(){

    vector<vector<int>> board = {
                                {5,5,5,5,5},
                                {5,5,5,5,5},
                                {5,5,5,5,5},
                                {5,5,5,5,5}
                                };

                                //type 1 : 1(적), 2(아군)
                                //좌표1, 좌표2
                                //dgree
    vector<vector<int>> skill = {
                                {1,0,0,3,4,4},
                                {1,2,0,2,3,2},
                                {2,1,0,3,1,2},
                                {1,0,1,3,3,1}
                                };


    solution(board,skill);

    return 0;
}