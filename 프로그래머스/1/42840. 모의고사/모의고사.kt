class Solution {
    fun solution(answers: IntArray): IntArray {
        var p1 = intArrayOf(1, 2, 3, 4,5)
        var p2 = intArrayOf(2,1,2,3,2,4,2,5)
        var p3 = intArrayOf(3,3,1,1,2,2,4,4,5,5)
        
        // 점수 저장
        var score = IntArray(3)
        
        for (i in answers.indices) {
            if (answers[i] == p1[i % p1.size]) {
                score[0]++
            }
            if (answers[i] == p2[i % p2.size]) {
                score[1]++
            }
            if (answers[i] == p3[i % p3.size]) {
                score[2]++
            }
        }
        
        val maxScore = score.maxOrNull() ?: 0
        
        val answer = mutableListOf<Int>()
        for (i in score.indices) {
            if (score[i] == maxScore) {
                answer.add(i+1)
            }
            
        }
        
        
        return answer.toIntArray()
    }
}