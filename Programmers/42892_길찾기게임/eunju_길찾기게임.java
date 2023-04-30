package Programmers;

import java.util.Arrays;
import java.util.Comparator;

/**
 * 42892
 * @ 길찾기 게임
 * */
public class Eunju_42892 {

    public static class Solution {
        static int index = 0;

        public class Node{
            private Node left;
            private Node right;
            private int x, y;
            private int index;

            public Node(int x, int y,int index, Node left, Node right){
                this.x = x;
                this.y = y;
                this.left = null;
                this.right = null;
                this.index = index; //입력받은 순서대로 index 값 매겨야함
            }
        }

        /**
         * 부모가 될 노드와 x값을 비교해서 왼쪽에 붙일 지 오른쪽에 붙일 지 결정
         * 자식노드는 부모보다 y값이 더 작으니까
         * y값으로 미리 child를 정렬해서 insert
         * */
        public void insertNode(Node parent, Node child){
            // 부모보다 x값이 더 작다면 왼쪽에 추가
            if(parent.x > child.x){
                if(parent.left == null) parent.left = child;
                else insertNode(parent.left, child);    //왼쪽 자식이랑 비교 자기자리 찾아가기
            }
            //부모보다 x값이 더 크다면 오른쪽에 추가
            else{
                if(parent.right == null) parent.right = child;
                else insertNode(parent.right, child);
            }

        }

        /**
         * 전위순회
         *  root 먼저
         * */
        public static void preorder(int[][] answer, Node root){
            if(root == null) return;
            answer[0][index++] = root.index;    //root
            preorder(answer, root.left);        //left
            preorder(answer, root.right);       //right
        }

        /**
         * 후위순회
         * root 나중에
         * */
        public static void  postorder(int[][] answer, Node root){
            if(root == null) return;
            postorder(answer, root.left);       //left
            postorder(answer, root.right);      //right
            answer[1][index++] = root.index;    //root
        }

        public int[][] solution(int[][] nodeinfo) {
            //nodeinfo 트리 전위순회, 후위순회 한 순서를 리턴 예정
            int[][] answer =  new int[2][nodeinfo.length];

            // 먼저 노드 만들기 노드 번호, x, y 좌표
            // 노드를 배열로 저장
            Node[] node = new Node[nodeinfo.length];
            // 노드 생성
            for(int i=0; i<node.length; i++)
                node[i] = new Node(nodeinfo[i][0], nodeinfo[i][1], i+1,null, null);


            // 자식을 차례로 부모에 붙이게 append 할거기 때문에
            // 부모 -> 자식 순으로 정렬 ( y값이 크면 부모 작으면 자식 -> y값 기준으로 내림차순해서 저장)
            Arrays.sort(node, new Comparator<Node>() {
                // y값이 같으면(레벨이 같으면) x값이 작은 순서로 정렬(왼쪽 자식)
                @Override
                public int compare(Node o1, Node o2) {
                    if(o1.y == o2.y) return o1.x - o2.x;
                    else return o2.y - o1.y;
                }
            });

            //노드 차례로 삽입
            Node root = node[0];
            for(int i=1; i<node.length; i++)
                insertNode(root, node[i]);

            // 전위순회
            preorder(answer, root);

            // 후위순회
            index = 0;
            postorder(answer, root);

            return answer;
        }


    }

    public static void main(String args[]){

        int[][] nodeinfo={{5,3},{11,5},{13,3},{3,5},{6,1},{1,3},{8,6},{7,2},{2,2}};
        Solution solution = new Solution();
        int[][] ans = solution.solution(nodeinfo);
        for(int[] an : ans){
            for(int a : an){
                System.out.print(a+ " ");
            }
            System.out.println();
        }

    }

}
