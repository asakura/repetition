function processData(input) {
    input = input.split('\n');

    const n = parseInt(input[0]);
    const x = input[1].split(' ').map((n) => parseInt(n)).slice(0, n);
    const w = input[2].split(' ').map((n) => parseInt(n)).slice(0, n);

    const x1 = x.reduce((acc, value, index) => acc + value * w[index], 0);
    const w1 = w.reduce((acc, value) => acc + value, 0);

    console.log((x1 / w1).toFixed(1));
}

process.stdin.resume();
process.stdin.setEncoding("ascii");
_input = "";
process.stdin.on("data", function (input) {
    _input += input;
});

process.stdin.on("end", function () {
    processData(_input);
});
