const assert = require('assert');
const calculateNumber = require('./0-calcul');

describe('calculateNumber', () => {

  it('should return 4 when a = 1 and b = 3', () => {
    assert.strictEqual(calculateNumber(1, 3), 4);
  });

  it('should add two negativ number return -5 when a = -1 and b = -4', () => {
    assert.strictEqual(calculateNumber(-1, -4), -5);
  })

  it('should round 1.4 and 4.5 correctly to sum = 5', () => {
    assert.strictEqual(calculateNumber(1.4, 4.5), 5);
  });

  it('should round 1.5 and 3.7 correctly to sum = 6', () => {
    assert.strictEqual(calculateNumber(1.5, 3.7), 6);
  });

  it('should round negative numbers correctly (-1.4 and -3.6)', () => {
    assert.strictEqual(calculateNumber(-1.4, -3.6), -5);
  });

  it('should round 0.5 correctly (0.5 + 0.5)', () => {
    assert.strictEqual(calculateNumber(0.5, 0.5), 2);
  });

});
