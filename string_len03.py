def main(a,b):
    """
    String type variables a and b are given. Return True if the length is equal. If not equal, return False.
    Args:
        a: string
        b: string
    Returns:
        True or False
    """
    s=0
    if len(a)==len(b):
        s="True"
    else:
        s="False"
    return s
