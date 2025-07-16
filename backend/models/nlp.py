def classify_message(message: str):
    message = message.lower()
    if 'water' in message:
        return {'category': 'water', 'confidence': 0.95}
    elif 'toilet' in message or 'sanitation' in message:
        return {'category': 'toilet', 'confidence': 0.93}
    elif 'clinic' in message or 'health' in message:
        return {'category': 'clinic', 'confidence': 0.92}
    else:
        return {'category': 'other', 'confidence': 0.60} 