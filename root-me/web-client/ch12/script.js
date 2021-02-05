
// we just need to run several evals and unescape to retreive the password

let hardcoded_string = "unescape%28%22String.fromCharCode%2528104%252C68%252C117%252C102%252C106%252C100%252C107%252C105%252C49%252C53%252C54%2529%22%29"

let tmp_1 = unescape(hardcoded_string)
let tmp_2 = eval(tmp_1)
let answer = eval(tmp_2)
console.log('result is : ', answer)