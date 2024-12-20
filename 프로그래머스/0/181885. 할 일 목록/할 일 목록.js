function solution(todo_list, finished) {
    const converted =  todo_list.map((todo, idx) =>
         finished[idx] ? null : todo
    )
    return converted.filter((todo) => !!todo);
}