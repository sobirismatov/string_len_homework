def main(a):
    """
    A string type variable is given. Return True if its length is even. Return False if its length is odd.
    Args:
        a: string
    Returns:
        True or False
    """
    s=0
    if len(a)%2==0:
        s="True"
    else:
        s="False"

    return s
