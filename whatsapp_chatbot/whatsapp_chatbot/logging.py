import logging

logger = logging.getLogger(__name__)

@csrf_exempt
def webhook(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            phone = data.get('phone')
            message = data.get('message')
            logger.info(f"Received message from {phone}: {message}")
            # Rest of the code...
        except Exception as e:
            logger.error(f"Error processing webhook: {e}")
            return JsonResponse({'error': 'Internal Server Error'}, status=500)
    # Rest of the code...