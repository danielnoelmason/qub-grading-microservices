module.exports = function average(...marks) {
    let totalMark = 0
    for (var i = 0; i < marks.length; i++) {
        totalMark += marks[i];
    }
    let average = totalMark / marks.length;
    return average;
}
