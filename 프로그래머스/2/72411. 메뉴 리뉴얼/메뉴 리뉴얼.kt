import kotlin.math.*
import java.util.*

class Solution {
    val foodMap = HashMap<String, Int>()
    
    fun solution(orders: Array<String>, course: IntArray): Array<String> {
        var answer = mutableListOf<String>()
        
        for (order in orders) {
            for (len in course) {
                var sortedOrder = order.toCharArray().sorted().joinToString("")
                combination(sortedOrder, "", 0, len)
            }
        }
        
        
        for (len in course) {
            val filterd = foodMap.filter { it.key.length == len }
            val maxCount = filterd.values.maxOrNull() ?: 0
            
            if (maxCount >= 2) {
                for ((menu, count) in filterd) {
                    if (count == maxCount) {
                        answer.add(menu)
                    }
                }
            }
        
        }
        
        return answer.sorted().toTypedArray()
    }
    
    fun combination(order: String, current: String,start: Int, r: Int) {
        if (current.length == r) {
            foodMap[current] = (foodMap[current] ?: 0) + 1
            return
        }
        
        for (i in start until order.length) {
            combination(order, current+order[i], i+1, r)
        }
    }
}