def solution(s1 : String, s2 : String) : Boolean = {
    s1.toCharArray().map((_,1)).groupBy(_._1).map(t=>(t._1, t._2.size)) == s2.toCharArray().map((_,1)).groupBy(_._1).map(t=>(t._1, t._2.size))
}

println(solution("abcd", "adcb"))

def solution2(s1 : String, s2 : String) : Boolean ={
    if (s1.size != s2.size){
        return false
    }
    val letter_count = new Array[Int](256)
    for (i <- 0.until(s1.size)){
        letter_count(s1(i).toInt) += 1
        letter_count(s2(i).toInt) -= 1
    }
    for (i <- letter_count){
        if (i != 0){
            return false
        }
    }
    true
}

println(solution2("abcd", "addcb"))

// 子集
def solution3(s1 : String, s2 : String) : Boolean ={
    if (s1.size < s2.size){
        return false
    }
    val letter_count = new Array[Int](256)
    for (i <- 0.until(s1.size)){
        letter_count(s1(i).toInt) += 1
        if (i < s2.size){
            letter_count(s2(i).toInt) -= 1
        }
    }
    for (i <- letter_count){
        if (i == -1){
            return false
        }
    }
    true
}

println(solution3("abdecd", "addcb"))
