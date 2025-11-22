class Solution {
    fun solution(brown: Int, yellow: Int): IntArray {

        val total = brown + yellow
        
        for (h in 3..total) {
            if (total % h == 0) {
                var w = total/h
                
                if (h > w) {
                    break
                }
                
                if ((w-2)*(h-2) == yellow) {
                    return intArrayOf(w, h)
                }
            }
        }
        return intArrayOf()
    }
}