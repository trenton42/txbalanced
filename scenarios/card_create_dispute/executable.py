import balanced

balanced.configure('ak-test-1o9QKwUCrwstHWO5sGxICtIJdQXFTjnrV')

card = balanced.Card(
  cvv='123',
  expiration_month='12',
  number='6500000000000002',
  expiration_year='3000'
).save()