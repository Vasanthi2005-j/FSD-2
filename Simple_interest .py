// simpleInterest.js

function interest(p, t, r, callback) {
    const si = (p * t * r) / 100;
    callback(p, t, r, si);
}

interest(10000, 2, 2, function(p, t, r, si) {
    console.log(`Simple Interest is : ₹${si}`);
});
