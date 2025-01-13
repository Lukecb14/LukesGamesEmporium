from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from lge.models import Game
from lge.modelAPI import addScore

@login_required
def uploadPage(request):


    if request.method == 'POST':
        game_id = request.POST.get('game_title')
        raw_score_data = request.POST.get('scores')
        user = request.user
        try:
            game = Game.objects.get(id=game_id)
        
            try:
                addScore(raw_score_data, game, user)
            except ValueError as e:
                print(e)
                
        except Game.DoesNotExist:
            print("Game not found")
        
        
    context = {
        "games": Game.objects.all()
    }
        
    return render(request, 'upload.html', context)