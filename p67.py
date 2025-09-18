def triangle_rep(s):
    """
    Convert a comma-separated string of numbers into a triangular list of lists.
    
    Each row of the triangle has increasing length (1, 2, 3, ...), and
    the numbers are converted from strings to integers.
    
    Parameters
    ----------
    s : str
        A string of numbers separated by commas.
    
    Returns
    -------
    list of list of int
        A nested list representation of the triangle.
    """
    s = s.split(',')
    s = [k for k in s if k != ',']
    g = []

    begin = 0 
    increment = 1
    while begin < len(s):
        end = begin + increment
        g.append(s[begin:end])
        begin = end 
        increment += 1
    
    for i,k in enumerate(g):
        g[i] = [int(j) for j in g[i]]
    
    return g


def max_path_sum(s):
    """
    Compute the maximum path sum through a number triangle using dynamic programming.
    
    The triangle is represented by a comma-separated string, which is first
    converted into a triangular list of lists by `triangle_rep`. The algorithm
    collapses the triangle bottom-up, summing each element with the maximum of 
    its two children, until a single maximum sum remains at the top.
    
    Parameters
    ----------
    s : str
        A string of numbers separated by commas, representing the triangle.
    
    Returns
    -------
    int
        The maximum path sum from top to bottom of the triangle.
    """
    g = triangle_rep(s)
    i=len(g)-1
    v=g[i]
    while i > 0:
        v = [g[i-1][j] + max(v[j], v[j+1]) for j in range(len(g[i-1]))]
        i -= 1
    return v