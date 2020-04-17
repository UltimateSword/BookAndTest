def is_match(s: string, p: string): Boolean = {
    if (p == ""){
        return s == ""
    }
    first = (s == "") && (set(p(0), '.').contains(s(0)))
    if (p.size > 1 && p(1) == '*'){
        return is_match(s.drop(1), p) or is_match(s, p.drop(2))  // [aa a*], [ab c*ab]
    }
    else {
        return first and is_match(s.drop(1), p.drop(1))
    }
}