const assert = require('assert');
const calculateNumber = require('./1-calcul');

describe('calculateNumber', () => {
    describe('SUM', () => {
        it('result of two positiv number 1.4 + 3.5 should return 6', () => {
            assert.strictEqual(calculateNumber('SUM', 1.4, 4.5), 6)
        });

        it('result of two negativ number -1.4 + -3.5 should return -6', () => {
            assert.strictEqual(calculateNumber('SUM', -1.4, -4.5), -6)
        })
    })

    describe('SUBSTRACT', () =>{
        it('result of two positiv number 4 - 2 should return 2', () => {
            assert.strictEqual(calculateNumber('SUBSTRACT', 4, 2), 2)
        })

        it('result of two negativ number (-3) - (-5) should return 2', () => {
            assert.strictEqual(calculateNumber('SUBSTRACT', -3, -5), 2)
        })
    })

    describe('DIVIDE', () => {
        it('result of two positiv number 2 / 2 should return 1', () => {
            assert.strictEqual(calculateNumber('DIVIDE', 2, 2), 1)
        })

        it('result of two negativ number -4 / -2 should return 2', () => {
            assert.strictEqual(calculateNumber('DIVIDE', -4, -2), 2)
        })

        it('result if b = 0 should return Error', () => {
            assert.strictEqual(calculateNumber('DIVIDE', 4, 0), 'ERROR')
        })
    })
})