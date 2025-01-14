from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from lge.models import Game
from lge.modelAPI import addScore

@login_required
def uploadPage(request):
    submissionMessage = ""
    errorMessage = ""

    if request.method == 'POST':
        game_id = request.POST.get('game_title')
        raw_score_data = request.POST.get('scores')
        user = request.user
        try:
            game = Game.objects.get(id=game_id)
        
            try:
                newScore = addScore(raw_score_data, game, user)
                if newScore:
                    submissionMessage = "Score added successfully"
            except ValueError as e:
                errorMessage = str(e)
                
        except ValueError:
            errorMessage = "Game not selected, please choose a game"
        
        
    context = {
        "games": Game.objects.all(),
        "submissionMessage": submissionMessage,
        "errorMessage": errorMessage
    }
        
    return render(request, 'upload.html', context)