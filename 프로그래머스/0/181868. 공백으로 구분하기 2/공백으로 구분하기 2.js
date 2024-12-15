const solution = (my_string) => {
    const spliting = my_string.split(" ");
    const filtering = spliting.filter(str => str);
    return filtering;
};