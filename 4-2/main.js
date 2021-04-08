// 出力はすべて str
for (let i = 1; i < 51; i++) {
    if (String(i).match(/3/) || i % 3 ===0) {
        console.log('WOW');
    } else {
        console.log(String(i));
    }
}