const prompt = require('prompt-sync')({sigint: true});

function get_change(m) {
    var return_list;
    return_list = [];
    while ((m !== 0)) {
        if ((m >= 10)) {
            return_list.push(10);
            m -= 10;
        } else {
            if ((m >= 5)) {
                return_list.push(5);
                m -= 5;
            } else {
                if ((m >= 1)) {
                    return_list.push(1);
                    m -= 1;
                }
            }
        }
    }
    return return_list.length;
}
const x = prompt()
console.log(get_change(x))