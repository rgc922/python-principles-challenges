def validate(Str_val):

    if not "def" in Str_val:
        return "missing def"
    
    if not ":" in Str_val:
        return "missing :"

    if not ("(" in Str_val and ")" in Str_val):
        return "missing paren"
    
    temp = '('
    temp2 = ')'
    if  temp + temp2 in Str_val:
        return "missing param"
    
    if not "    " in Str_val:
        return "missing indent"

    if not "validate" in Str_val:
        return "wrong name"
    
    if not "return" in Str_val:
        return "missing return"
    
    

    return True

print('def validate(Str_val):\n\n if not "def" in Str_val:\n')
