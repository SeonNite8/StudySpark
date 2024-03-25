from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
import stripe

stripe.api_key = settings.STRIPE_TEST_SECRET_KEY

def process_payment(request):
    if request.method == 'POST':
        # Handle POST request (payment processing logic)
        card_number = request.POST.get('card_number')
        expiry = request.POST.get('expiry')
        cvv = request.POST.get('cvv')

        try:
            # Create a charge (this will not actually charge the card)
            charge = stripe.Charge.create(
                amount=1000,  # Amount in cents
                currency='usd',
                source='tok_visa',  # Use a test token
                description='Example Charge'
            )
            return HttpResponse('Payment successful')
        except stripe.error.StripeError as e:
            return HttpResponse('Payment failed: {}'.format(e))
    else:
        # Handle GET request (render the payment form)
        return render(request, 'payment_form.html')
