// we can see the javascript, that there is an unescape function, so we can just repeat to find the password
let hardcoded_string = "%63%70%61%73%62%69%65%6e%64%75%72%70%61%73%73%77%6f%72%64"
let response = unescape(hardcoded_string)

console.log('response is : ' + response)