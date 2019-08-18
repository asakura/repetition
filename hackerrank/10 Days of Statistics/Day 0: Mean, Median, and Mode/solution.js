function processData(input) {
    input = input.split('\n');

    const n = parseInt(input[0]);
    const x = input[1].split(' ').map((n) => parseInt(n)).slice(0, n);

    x.sort((a, b) => a - b);

    const mean = x.reduce((acc, value) => value + acc, 0) / n;
    const middle = ~~(n / 2);
    const median = n % 2 !== 0 ? x[middle] : (x[middle - 1] + x[middle]) / 2;

    let freq = x.reduce((acc, value) => {
        acc[value] = (acc[value] || 0) + 1;

        return acc;
    }, {});

    freq = Object.keys(freq).map((key) => [key, freq[key]]);

    const mode = freq.sort((a, b) => {
        if (a[1] == b[1]) {
            return a[0] - b[0];
        }

        return b[1] - a[1];
    })[0][0];

    console.log(mean);
    console.log(median);
    console.log(mode);
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
