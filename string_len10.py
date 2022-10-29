def main(s):
    """
    A string of length three is given. Check that it is a palindrome.
    Return True if the palindrome is False otherwise

    Args:
        s: str
    Returns:
        bool: answer
    """
    a= 0
    if len(s)//10==len(s)%2:
        s="True"
    else:
        s="False"
    return s