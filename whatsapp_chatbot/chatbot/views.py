from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import User, Conversation
from google.cloud import dialogflow_v2 as dialogflow
import json

@api_view(['POST'])
def webhook(request):
    data = request.data
    phone = data.get('phone')
    message = data.get('message')

    if not phone or not message:
        return Response({'error': 'Missing phone or message'}, status=status.HTTP_400_BAD_REQUEST)

    user, created = User.objects.get_or_create(phone_number=phone)
    
    # Dialogflow Integration
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path('project_id', phone)
    text_input = dialogflow.TextInput(text=message, language_code='en')
    query_input = dialogflow.QueryInput(text=text_input)

    try:
        response = session_client.detect_intent(request={'session': session, 'query_input': query_input})
        reply = response.query_result.fulfillment_text
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    Conversation.objects.create(user=user, message=message, response=reply)
    
    return Response({'reply': reply}, status=status.HTTP_200_OK)