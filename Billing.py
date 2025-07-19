// billing.js

function calculateBill(amount, gstPercent, callback) {
    const tax = (amount * gstPercent) / 100;
    const total = amount + tax;
    callback(amount, gstPercent, tax, total);
}

calculateBill(10000, 18, function(amount, gstPercent, tax, total) {
    console.log(`Without GST Amount is : ₹${amount}`);
    console.log(`Amount with GST (${gstPercent}%): ₹${total}`);
});
