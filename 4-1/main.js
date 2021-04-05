let args = process.argv;
//コマンドライン引数の先頭から要素を２つ削除したい
args.shift()
args.shift()

//数値化して並び替え
const nums = args.map(Number).sort(),
    target = Math.floor(nums.length / 2);

if (nums.length % 2 === 1) {
    console.log(nums);
    console.log(nums[target]);
}else{
    console.log(nums);
    console.log((nums[target]+nums[target-1]) / 2);
}