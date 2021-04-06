let args = process.argv;
//コマンドライン引数の先頭から要素を２つ削除したい
var slargs = args.slice(2);

//比較関数
var comparefunc = function (a, b) {
    return a - b  //b - aとすれば降順になる
}

//数値化して並び替え
const nums = slargs.map(Number).sort(comparefunc),
    target = Math.floor(nums.length / 2);

if (nums.length % 2 === 1) {
    console.log(nums);
    console.log(nums[target]);
}else{
    console.log(nums);
    console.log((nums[target]+nums[target-1]) / 2);
}