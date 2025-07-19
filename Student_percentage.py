// student_percentage.js

function percentage(a, b, c, d, e, callback) {
    const total_obtained = a + b + c + d + e;
    const percent = (total_obtained / 500) * 100;
    callback(percent);
}

percentage(92, 98, 89, 90, 100, function(percent) {
    if (percent >= 90) {
        console.log("A Grade");
    } else if (percent < 90 && percent >= 80) {
        console.log("B Grade");
    } else if (percent < 80 && percent >= 70) {
        console.log("C Grade");
    } else {
        console.log("D Grade");
    }
});
