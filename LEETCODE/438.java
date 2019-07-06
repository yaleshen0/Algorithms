class Solution {
    // :type s: str e.x: "cbaebabacd"
    // :type p: str e.x: "abc"
    // :rtype: List[int]
    public List<Integer> findAnagrams(String s, String p) {
		if (s.length() == 0 || p.length() == 0 || p.length() > s.length())
			return new ArrayList<>();
		List<Integer> res = new ArrayList<>();
		char[] arr = p.toCharArray();
		int[] dp = new int[26];
		int flag = 0, j;
		for (char c : arr) {
			j = c - 'a';
			dp[j]++;
			if (dp[j] == 1)
				flag++;
		}
		arr = s.toCharArray();
		for (int i = 0; i < p.length(); i++) {
			j = arr[i] - 'a';
			dp[j]--;
			if (dp[j] == 0)
				flag--;
			else if (dp[j] == -1)
				flag++;
		}
		if (flag == 0)
			res.add(0);
		for (int i = p.length(); i < s.length(); i++) {
			j = arr[i] - 'a';
			dp[j]--;
			if (dp[j] == 0)
				flag--;
			else if (dp[j] == -1)
				flag++;
			j = arr[i - p.length()] - 'a';
			dp[j]++;
			if (dp[j] == 0)
				flag--;
			else if (dp[j] == 1)
				flag++;
			if (flag == 0)
				res.add(i - p.length() + 1);
		}
		return res;
    }
}