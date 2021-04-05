const arga = process.argv[2];
const argb = process.argv[3];

function reverse_a_number(arg){
    //文字のまま受け取り 分割 反転 結合 します
    return arg.split('').reverse().join('');
}

const testResult = reverse_a_number(arga);

const result = Number(reverse_a_number(arga)) 
                + Number(reverse_a_number(argb));


console.log(typeof testResult)
console.log(testResult)

console.log(typeof result)
console.log(result)