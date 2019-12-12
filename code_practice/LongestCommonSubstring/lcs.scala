def solution(s1: String, s2: String) : Int = {
    var lcs = 0
    for (i <- 0 to s1.size){
        for (j <- 0 to s2.size){
            var pts = 0
            while (i+pts < s1.size && j+pts < s2.size && s1(i+pts) == s2(j+pts)) {
                pts += 1
            }
            if (pts > lcs) lcs=pts
        }
    }
    lcs
}

println(solution("abcde", "abcdef"))

def df_solution(s1: String, s2: String) : Int = {
    val dp = Array.ofDim[Int](s2.size, s1.size)
    for (i <- 0 to s1.size) {
        for (j <- 0 to s2.size){
            if (s1(i) == s2(j)) dp(i)(j) = dp(i-1)(j-1) + 1
        }
    }
    dp.map(_.reduce((x,y)=>x max y)).reduce((x,y)=>x max y)
}

println(solution("abcde", "abdabcdef"))