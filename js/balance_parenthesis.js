let map = {
    '(':')',
    '[':']',
    '{':'}'
}

let paranthesis_matching = function(test_string){
    stack = []
    for(let i=0;i<test_string.length;i++){
        if(test_string[i] == "{" || test_string[i] == "[" || test_string[i] == "("){
            stack.push(test_string[i])
        }
        else if (test_string[i] == "}" || test_string[i] == "]" || test_string[i] == ")")
        {
            let last = stack.pop()
            if(test_string[i] !== map[last]){
                return false
            }
        }
    
    }

    if (stack.length !==0)
    {
        return false
    }

    return true
}



string1 = "{{}}"
string2 = "{{{"
string3 = "{(})"
string4 = "{{}{}}"
string5 = "{2+3(2+})"
string6 = "{2+3(2+)}"


console.log(paranthesis_matching(string1))
console.log(paranthesis_matching(string2))
console.log(paranthesis_matching(string3))
console.log(paranthesis_matching(string4))
console.log(paranthesis_matching(string5))
console.log(paranthesis_matching(string6))

