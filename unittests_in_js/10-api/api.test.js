const request = require('supertest');
const app = require('./api');
const assert = require('assert');

describe('GET /available_payments', () => {
  it('should return the correct payment methods object', (done) => {
    request(app)
      .get('/available_payments')
      .expect('Content-Type', /json/)
      .expect(200)
      .end((err, res) => {
        if (err) return done(err);
        assert.deepStrictEqual(res.body, {
          payment_methods: {
            credit_cards: true,
            paypal: false,
          },
        });
        done();
      });
  });
});

describe('POST /login', () => {
  it('should return a welcome message with the userName', (done) => {
    request(app)
      .post('/login')
      .send({ userName: 'Betty' })
      .set('Content-Type', 'application/json')
      .expect(200)
      .expect('Welcome Betty', done);
  });
});

