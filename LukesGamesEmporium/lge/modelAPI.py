from lge.models import Score
import re

def addScore(raw_score_data, game, user):
    
    match = re.search(r'#\d+\s(\d{1,3}(?:,\d{3})*)', raw_score_data)
    if match:
        score = match.group(1).replace(',', '')
        score = int(score)
    else:
        raise ValueError("Invalid score format. Score not added.")

    newScore = Score.objects.create(rawData=raw_score_data, game=game, user=user, score=score)

    return newScore