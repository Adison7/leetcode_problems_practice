def isNumber(s):
    def is_decimal(s):
        # optional sign
        if s and s[0] in '+-':
            s = s[1:]
        if not s:
            return False
        
        if '.' in s:
            left, _, right = s.partition('.')
            if not left.isdigit() and not right.isdigit():
                return False
            if (left and not left.isdigit()) or (right and not right.isdigit()):
                return False
            return True
        else:
            return s.isdigit()
    
    def is_integer(s):
        if s and s[0] in '+-':
            s = s[1:]
        return s.isdigit()  # isdigit() is False for empty string
    
    s = s.strip()
    if not s:
        return False
    
    if 'e' in s or 'E' in s:
        parts = s.replace('E', 'e').split('e')
        if len(parts) != 2:
            return False
        mantissa, exponent = parts
        return is_decimal(mantissa) and is_integer(exponent)
    else:
        return is_decimal(s)