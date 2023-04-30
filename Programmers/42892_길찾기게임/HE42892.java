/* y는 level, x는 부모를 판별하는 데이터다.
*  출력값은 '노드의 순서'를 반환해야한다는 점에서, 입력받는 노드의 순서도 다 저장해야한다.
*  '나'보다 x값이 작으면 내 왼쪽이고, 크면 내 오른쪽이다.
*   근데 이미 해당 위치에 자식이 있는 경우, 그러면 그 자식의 자식이 될 수 있는지 보는 식으로 재귀한다.
*   전위, 후위 순회는 재귀로 구현한다.
*/

import java.util.Arrays;

class Solution {
    int[][] answer;
    int idx;
    
    class Node implements Comparable<Node>{
        int x;
        int y;
        int num;  // 내가 몇 번째인지 저장하려고
        Node left;
        Node right;
        
        public Node (int x, int y, int n, Node l, Node r) {
            this.x = x;
            this.y = y;
            this.num = n;
            this.left = l;
            this.right = r;
        }
        
        @Override
        public int compareTo(Node n) {
            // y를 큰 순서대로(내림차순) 정렬해야하기 때문에
            return n.y - this.y;
        }
    }
    
    // '나'보다 x값이 작으면 내 왼쪽이고, 크면 내 오른쪽이다.
    // 근데 이미 해당 위치에 자식이 있는 경우, 그러면 그 자식의 자식이 될 수 있는지 보는 식으로 재귀한다.
    public void makeTree(Node me, Node child) {
        if (me.x > child.x) {
            // 왼쪽인 경우
            if (me.left == null) me.left = child;
            else makeTree(me.left, child);
        } else {
            // 오른쪽인 경우
            // 나에게 이미 오른쪽 자식이 있다면, 그 자식과 비교한다.
            if (me.right == null) me.right = child;
            else makeTree(me.right, child);
        }
    }
    
    public void preOrder(Node node) {
        answer[0][idx++] = node.num;
        if (node.left != null) preOrder(node.left);
        if (node.right != null) preOrder(node.right);
    }
    
    public void postOrder(Node node) {
        if (node.left != null) postOrder(node.left);
        if (node.right != null) postOrder(node.right);
        answer[1][idx++] = node.num;
    }
    
    
    public int[][] solution(int[][] nodeinfo) {
        int cnt = nodeinfo.length;
        // 노드를 저장할 클래스 배열
        Node[] nodes = new Node[cnt];
        // y는 0까지 가능하기 때문에 0으로 초기화하면 제대로 정렬이 안된다.
        Node root = new Node(-1, -1, 0, null, null);
        
        // 루트 노드도 함께 찾는다. 루트 노드는 y값이 가장 큰!!! 노드이다.
        for (int i = 0; i < cnt; i++) {
            // 번호는 1부터 시작한다.
            // 아직 왼쪽, 오른쪽은 모른다.
            nodes[i] = new Node(nodeinfo[i][0], nodeinfo[i][1], i+1, null, null);
            if (nodes[i].y > root.y) {
                root = nodes[i];
            }
        }
        
        //nodes를 y값을 기준으로 정렬해줘야 레벨에 맞게 내려가면서 조회할 수 있다.
        Arrays.sort(nodes);
        
        
        // 트리를 만든다. 정렬을 해줬기 때문에 root를 제외한 1번째 노드부터 조회할 수 있다.
        for (int n = 1; n < cnt; n++) {
            makeTree(root, nodes[n]);
        }
        
        // 0은 전위, 1은 후위
        answer = new int[2][cnt];
        
        // 전위 순회
        idx = 0; // paramter로 넘기면 골치아파진다.
        preOrder(root);
        
        // 후위 순회
        idx = 0; // 또 초기화 해줘야됨
        postOrder(root);
        
        return answer;
    }
}