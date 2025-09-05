// 3-payment.test.js
const sinon = require('sinon');
const { expect } = require('chai');
const Utils = require('./utils');
const sendPaymentRequestToApi = require('./3-payment');

describe('sendPaymentRequestToApi', () => {
  it('should call Utils.calculateNumber with SUM and the correct arguments', () => {
    const spy = sinon.spy(Utils, 'calculateNumber');

    const total = sendPaymentRequestToApi(100, 20);

    expect(spy.calledOnce).to.be.true;

    expect(spy.calledWith('SUM', 100, 20)).to.be.true;

    expect(total).to.equal(Utils.calculateNumber('SUM', 100, 20));

    spy.restore();
  });
});