const solution = (num_list) => num_list.length >= 11
    ? num_list.reduce((s,n) => s+n, 0)
    : num_list.reduce((s,n) => s*n, num_list[0]) / num_list[0]