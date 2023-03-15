function solution(rsp) {
    return [...rsp].map(a => {
        switch (+a) {
            case 2:
                return 0;
                break;
            case 5:
                return 2;
                break;
            case 0:
                return 5;
                break
            default:
                return;
        }
    }).join("");
}