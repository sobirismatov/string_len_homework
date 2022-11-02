def main(s):
    """
    Given variable type string s. Return the character in the middle.
    If the length is even, return two characters in the middle.

    Args:
        s: str
    Returns:
        str: answer
    """
    a=0
    if len(s)%2==1:
        a=len(s)//2
        return s[a]
    else:
        return s[len(s)//2-1]+s[len(s)//2]
print(main("saom"))