const { expect } = require('chai');
const calculateNumber = require('./2-calcul_chai');


describe('calculateNumber', () => {
    describe('SUM', () => {
        it('result of two positiv number 1.4 + 3.5 should return 6', () => {
            expect(calculateNumber('SUM', 1.4, 4.5)).to.equal(6)
        });

        it('result of two negativ number -1.4 + -3.5 should return -5', () => {
            expect(calculateNumber('SUM', -1.4, -4.5)).to.equal(-5)
        })
    })

    describe('SUBTRACT', () =>{
        it('result of two positiv number 4 - 2 should return 2', () => {
            expect(calculateNumber('SUBTRACT', 4, 2)).to.equal(2)
        })

        it('result of two negativ number (-3) - (-5) should return 2', () => {
            expect(calculateNumber('SUBTRACT', -3, -5)).to.equal(2)
        })
    })

    describe('DIVIDE', () => {
        it('result of two positiv number 2 / 2 should return 1', () => {
            expect(calculateNumber('DIVIDE', 2, 2)).to.equal(1)
        })

        it('result of two negativ number -4 / -2 should return 2', () => {
            expect(calculateNumber('DIVIDE', -4, -2)).to.equal(2)
        })

        it('result if b = 0 should return Error', () => {
            expect(calculateNumber('DIVIDE', 4, 0)).to.equal('Error')
        })
    })
})