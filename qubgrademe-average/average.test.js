var average = require('./average')

test('result of average function should be the average of inputs', () => {
    expect(average(10, 15, 20)).toBe(15);
  });