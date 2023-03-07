#include <bits/stdc++.h>

using namespace std;

int N, K;

struct Node{
    //오름차순 자동 정렬
    map<string, Node> child;
};

// 2 B A
// 4 A B C D
// 2 A C
void insert(Node &node, vector<string> v, int index){
    //vector의 값을 node로 다 추가하면 끝
    if(index == v.size()) return;

    //vector에서 가져온 string이 트리에 없을 때만
    //다음 노드로 추가a
    if(node.child.count(v[index]) == 0)
        node.child[v[index]] = Node();
    
    insert(node.child[v[index]], v, index+1);
}

void print(Node &node, int depth=0){
    for(auto node : node.child){

        for(int i=0; i<depth; i++) cout << "--";
        cout <<node.first<<"\n";

        //다음 노드 출력
        print(node.second, depth+1);
    }
}

int main(){
    Node root;
    cin >> N;
    
    for(int i=0; i<N; i++){
        int K; cin >> K;

        vector<string> v(K);
        for(int j=0; j<K; j++)  cin >> v[j];

        //이 벡터를 root노드부터 추가
        insert(root, v, 0);
    }

    print(root);

    return 0;
}