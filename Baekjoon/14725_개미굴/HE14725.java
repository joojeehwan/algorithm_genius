import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.TreeMap;

public class HE14725 {
	
	static class Tree {
		TreeMap<String, Tree> child = new TreeMap<>();
	}
	
	
	static void print(Tree tree, String depth) {
		Object[] children = tree.child.keySet().toArray();
//		System.out.println(Arrays.toString(children));
		for(Object child : children) {
			Tree cur = tree.child.get(child);
			System.out.println(depth + child);
			print(cur, depth+"--");
		}
	}
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		StringTokenizer st;
		
		Tree root = new Tree();
		
		for(int l = 0; l < N; l++) {
			st = new StringTokenizer(br.readLine());
			int K = Integer.parseInt(st.nextToken());
			Tree cur = root;
			for(int m = 0; m < K; m++) {
				String name = st.nextToken();
				if (!cur.child.containsKey(name)) {
					cur.child.put(name, new Tree());
				}
				cur = cur.child.get(name);
			}
		}
		
		print(root, "");
	}

}
