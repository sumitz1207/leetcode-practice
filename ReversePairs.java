public class Solution {
    public int rev(int[] n) {
        return merge(n, 0, n.length-1);
    }
    private int merge(int[] n, int s, int e){
        if(s>=e) return 0; 
        int m = s + (e-s)/2; 
        int cnt = merge(n, s, m) + merge(n, m+1, e); 
        for(int i = s, j = m+1; i<=m; i++){
            while(j<=e && n[i]/2.0 > n[j]) j++; 
            cnt += j-(m+1); 
        }
        Arrays.sort(n, s, e+1); 
        return cnt; 
    }
}
