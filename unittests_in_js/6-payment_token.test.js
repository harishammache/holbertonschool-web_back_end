/*
    6-payment_token.test.js
*/
const { expect } = require('chai');
const getPaymentTokenFromAPI = require('./6-payment_token');

describe('getPaymentTokenFromAPI', () => {
  it('should return the correct object when success is true', (done) => {
    getPaymentTokenFromAPI(true).then((result) => {
      expect(result).to.be.an('object');
      expect(result).to.have.property('data', 'Successful response from the API');
      done();
    }).catch((err) => done(err));
  });

  it('should return undefined when success is false', () => {
    const result = getPaymentTokenFromAPI(false);
    expect(result).to.be.undefined;
  });
});
