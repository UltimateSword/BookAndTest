def anagram_group(l : Array[String]): List[Array[String]] = {
    l.groupBy(_.toCharArray().map((_,1)).groupBy(_._1).map(t=>(t._1, t._2.size))).map(_._2).toList
}

anagram_group(Array("ate","eta","eat","nat","tan","abc")).foreach(t=>println(t.toList))