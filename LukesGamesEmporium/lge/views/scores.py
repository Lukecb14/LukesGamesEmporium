from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from lge.models import Score, Game

@login_required
def scorePage(request):

    currentUser = request.user
    topScores = Score.objects.filter(user = currentUser).order_by('-score')[:5]
    recentScores = Score.objects.filter(user = currentUser).order_by('-date')[:5]

    arrayScores = []
    allScores = Score.objects.all()
    for score in allScores:
        arrayScores.append(score.score)

    context = {
        "arrayScores": arrayScores,    
        "topScores": topScores,    
        "recentScores": recentScores        
    }

    return render(request, 'scores.html', context)