const request = require('supertest');
const app = require('./api');
const { expect } = require('chai');

describe('Index page', () => {
  it('GET / should return correct message and status code 200', (done) => {
    request(app)
      .get('/')
      .expect(200)
      .end((err, res) => {
        expect(res.text).to.equal('Welcome to the payment system');
        done(err);
      });
  });
});

describe('Cart page', () => {
  it('GET /cart/123 should return correct message and status 200', (done) => {
    request(app)
      .get('/cart/123')
      .expect(200)
      .end((err, res) => {
        expect(res.text).to.equal('Payment methods for cart 123');
        done(err);
      });
  });

  it('GET /cart/abc should return 404 for invalid id', (done) => {
    request(app)
      .get('/cart/abc')
      .expect(404, done);
  });
});

