/* 
    5-payment.test.js
*/
const sinon = require('sinon');
const { expect } = require('chai');
const sendPaymentRequestToApi = require('./5-payment');

describe('sendPaymentRequestToApi with hooks', () => {
  let consoleSpy;

  beforeEach(() => {
    consoleSpy = sinon.spy(console, 'log');
  });


  afterEach(() => {
    consoleSpy.restore();
  });

  it('should log "The total is: 120" when called with 100, 20', () => {
    const total = sendPaymentRequestToApi(100, 20);

    expect(consoleSpy.calledOnce).to.be.true;
    expect(consoleSpy.calledWith('The total is: 120')).to.be.true;

    expect(total).to.equal(120);
  });

  it('should log "The total is: 20" when called with 10, 10', () => {
    const total = sendPaymentRequestToApi(10, 10);

    expect(consoleSpy.calledOnce).to.be.true;
    expect(consoleSpy.calledWith('The total is: 20')).to.be.true;
    expect(total).to.equal(20);
  });
});