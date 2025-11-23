import java.util.ArrayDeque

class Solution {
    lateinit var visited: BooleanArray
    lateinit var computers: Array<IntArray>
    var N = 0
    
    fun solution(n: Int, computer: Array<IntArray>): Int {
        var answer = 0
        visited = BooleanArray(n)
        computers = computer
        N = n
        
    
        for (i in 0..(N-1)) {
            if (!visited[i]) {
                bfs(i)
                answer++
            }
        }
        
        return answer
    }
    
    fun bfs(start: Int) {
        val q = ArrayDeque<Int>()
        q.add(start)
        visited[start] = true
        
        while(q.isNotEmpty()) {
            var current = q.removeFirst()
            
            for (next in 0 until N) {
                if (computers[current][next] == 1 && !visited[next]) {
                    visited[next] = true
                    q.add(next)
                }
            }
        }
    }
    
    
    
}