/*
 * 류호석님 영상 보고 작성
 * https://www.youtube.com/watch?v=PIov0Fv_IvE
 * */
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.HashSet;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class SolutionHE {
	static int N;
	
	// 쉬고있는 채점기 중 가장 낮은 번호를 빠르게 찾기 위한 PQ
	static PriorityQueue<Integer> freeCal = new PriorityQueue<>();
	// 채점기 번호를 idx로 하여, (domain, 채점 시작시간)을 저장함
	static Mark[] calInfo;
	
	// 채점 대기 큐
	// key = 도메인, value = PQ
	// 각 도메인 별로, 우선순위를 저장해둔다. 5만개의 모든 채점 task를 확인하지 않고, 300개 안에 끝낼 수 있다.
	static HashMap<String, PriorityQueue<Wait>> domainPQ = new HashMap<>();
	// 대기열에 있는 url 저장
	static HashSet<String> waitUrl = new HashSet<>();
	// 대기열 사이즈 저장
	static int waitSize = 0;
	
	// 도메인별 채점 시도 불가 시간
	// key = domain, value = (int) start + gap*3
	static HashMap<String, Integer> domainLock = new HashMap<>();
	
	
	static class Wait implements Comparable<Wait>{
		int priority;
		int insertTime;
		String number;
		
		public Wait(int p, int i,  String n) {
			this.priority = p;
			this.insertTime = i;
			this.number = n;
		}
		
		@Override
		public int compareTo(Wait w) {
			if (this.priority != w.priority) return this.priority - w.priority;
			return this.insertTime - w.insertTime;
		}
	}
	
	
	static class Mark{
		String domain;
		int startTime;
		
		public Mark(String d, int s) {
			this.domain = d;
			this.startTime = s;
		}
	}
	
	static String[] parseUrl(String u) {
		String[] urlSet = u.split("/");
		return urlSet;
	}
	
	static void insertPQ(int t, int p, String u) {
		if (waitUrl.contains(u)) return;
		// 대기열 추가
		waitSize++;
		waitUrl.add(u);

		// 첫 도메인에 대해 우선순위큐 생성하고 Task 추가
		String[] url = parseUrl(u);

		PriorityQueue<Wait> q = domainPQ.getOrDefault(url[0], new PriorityQueue<Wait>());
		q.add(new Wait(p, t, url[1]));
//		 기존에 값이 있었다면 필요없지만, 기존에 domain이 없었던 경우에는 put을 해줘야함.
		domainPQ.put(url[0], q);
	}
	
	
	static void init(int cnt, String u) {
		N = cnt;
		// 채점기 생성
		calInfo = new Mark[N+1];
		
		// 쉬는 채점기 추가
		for(int i = 1; i <= N; i++) {
			freeCal.add(i);
		}
		
		insertPQ(0, 1, u);
	}
	
	// O(300 + logQ + logN )
	static void mark(int t) {
		// 쉬고있는 채점기가 필요하다.
		if(freeCal.isEmpty()) return;
		
		// 1. 채점할 Task 찾아오기
		// 1-1. 이번에 사용할 PQ를 생성한다.
		Wait mTask = new Wait (Integer.MAX_VALUE, Integer.MAX_VALUE, "");
		String mDomain = "";
		
		// 1-2. 대기열에 있는 도메인을 돌며 각 도메인별 가장 우선순위가 높은 Task를 찾아온다.
		for(String domain : domainPQ.keySet()) {
			// 비어있다면 넘어감
			if (domainPQ.get(domain).isEmpty()) continue;
			// 현재 채점을 진행중인 도메인이라면 불가능하다. -> 이건 어떻게 구현??
			// => 채점 시간을 INF로 설정해버린다. 
			// 해당 도메인에서 가장 최근에 채점된 task의 start + gap*3보다 작으면 불가능하다.
			if (domainLock.containsKey(domain) && t < domainLock.get(domain)) continue;
			// 비교하기
			Wait nTask = domainPQ.get(domain).peek();
			if ((nTask.priority < mTask.priority) || (nTask.priority == mTask.priority && nTask.insertTime < mTask.insertTime)) {
				mTask = nTask;
				mDomain = domain;
			}
		}
		
		// 채점을 할 task를 골랐다면
		if (!mDomain.equals("")) {
			
			// 2-2. 사용할 채점기를 고른다. O(logN)
			calInfo[freeCal.poll()] = new Mark(mDomain, t);
			
			// 3-1. 채점한 Task의 Url을 대기 목록에서 지운다. O(logQ)
			domainPQ.get(mDomain).poll();
			// 3-2. 대기열 목록에서 url 지움
			waitUrl.remove(mDomain+"/"+mTask.number);
			// 3-3. 채점중임을 표기하기 위해 domainLock에 매우 큰값 걸어버림
			// 그래도 채점 종료하면 값이 바뀌니깐!
			domainLock.put(mDomain, Integer.MAX_VALUE);
			// 3-4. waitSize 하나 줄인다.
			waitSize--;
		}
	}
	
	static void finish(int t, int Jid) {
		if(calInfo[Jid] == null) return;
		// 쉬는 채점기
		freeCal.add(Jid);
		// 해당 채점기의 task 정보 가져오기
		Mark fin = calInfo[Jid];
		calInfo[Jid] = null;
		// 락 걸기
		domainLock.put(fin.domain, fin.startTime + (t-fin.startTime)*3);
	}
	

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		int Q = Integer.parseInt(br.readLine());
		
		// O(Q * (300 + logQ + logN))
		for(int i = 0; i < Q; i++) {
			st = new StringTokenizer(br.readLine());
			switch (st.nextToken()) {
			case "100":
				init(Integer.parseInt(st.nextToken()), st.nextToken());
				break;
			case "200":
				// O(logQ)
				insertPQ(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()), st.nextToken());
				break;
			case "300":
				// O(300 + logQ + logN)
				mark(Integer.parseInt(st.nextToken()));
				break;
			case "400":
				// O(logN)
				finish(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()));
				break;
			case "500":
				System.out.println(waitSize);
				break;
			}
		}
	}

}
