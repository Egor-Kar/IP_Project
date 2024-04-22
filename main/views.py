from django.contrib.auth import get_user_model
from django.forms import model_to_dict
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render
import random

User = get_user_model()


# Create your views1 here.

def main(request):
    abcd = 0
    if not Previous_attempts and not Previous_attempts_1:
        abcd = 0
    else:
        abcd = 1
    return render(request, 'main/layout.html', {'abcd': abcd})


def stat_table(request):
    zxc = User.objects.all()
    nikneyms = []
    q = 0
    for i in zxc:
        nikneyms.append((i.score, i.count_play, i.username))
    nikneyms = list(sorted(nikneyms, reverse=True))
    for i in range(len(nikneyms)):
        nikneyms[i] = list(nikneyms[i])
        nikneyms[i].append(i + 1)
        print(nikneyms[i])
    print(nikneyms)
    if len(nikneyms) < 10:
        for i in range(len(nikneyms) + 1, 11):
            nikneyms.append(("-", "-", "-", i))
    return render(request, 'main/stat_table.html', {'sssr': nikneyms})


def profile(request):
    global summ_score
    top_reit = ""
    top_play = ""
    if request.user.is_authenticated:
        summ_score = []
        zxc = User.objects.all()
        answer = 0
        for i in zxc:
            cxz = i.score
            summ_score.append(int(cxz))
        summ_score = sorted(summ_score)[::-1]
        for i in range(len(summ_score)):
            if summ_score[i] == int(request.user.score):
                answer = (i / len(summ_score))
                answer *= 100
                break
        answer = round(answer, 2)
        if answer > 50:
            top_reit = "Вы не входите в топ 50% пользователей."
        elif 0.1 <= answer <= 50:
            top_reit = f"Вы входите в топ {answer}% пользователей."
        elif answer < 0.1:
            top_reit = "Поздравляем! Вы лучше чем 0.1% пользователей!"
        summ_play = []
        zxc = User.objects.all()
        answer = 0
        for i in zxc:
            cxz = i.count_play
            summ_play.append(int(cxz))
        summ_play = sorted(summ_play)[::-1]
        for i in range(len(summ_play)):
            if summ_play[i] == int(request.user.count_play):
                answer = (i / len(summ_play))
                answer *= 100
                break
        answer = round(answer, 2)
        if answer > 50:
            top_play = "Вы не входите в топ 50% пользователей."
        elif 0.1 <= answer <= 50:
            top_play = f"Вы входите в топ {answer}% пользователей."
        elif answer < 0.1:
            top_play = "Поздравляем! Вы сыграли больше игр, чем 0.1% пользователей!"
    return render(request, 'main/profile.html', {"top_reit": top_reit, 'top_play': top_play})


def rules(request):
    return render(request, 'main/rules.html')


def statistika(request):
    return render(request, 'main/statistika.html')


def game(request):
    result = 'new'
    return render(request, 'main/game.html',
                  {'result': result, 'prev': Previous_attempts, 'prev_1': Previous_attempts_1})


result = ""
flag = 0
secret_number = 0
count_hit = 0
Previous_attempts = []
Previous_attempts_1 = []
reit = 0
summ_score = 0


def game_secret(request):
    result = 'new'
    return render(request, 'main/game_secret.html',
                  {'result': result, 'prev': Previous_attempts, 'prev_1': Previous_attempts_1})


def data_form_secret(request):
    global reit
    global count_hit
    global flag
    global secret_number
    global Previous_attempts
    global Previous_attempts_1
    result = ""
    qwer = ''
    if flag == 0:
        Previous_attempts = []
        Previous_attempts_1 = []
        a = set()
        while True:
            secret_number = random.randint(1000, 9999)
            secret_number = str(secret_number)
            for i in range(len(secret_number)):
                a.add(int(secret_number[i]))
            if len(a) == 4:
                break
            else:
                a.clear()
    user_guess = int(request.POST['user_guess'])
    user_guess = str(user_guess)
    if user_guess == str(secret_number) and count_hit <= 20:
        if count_hit <= 11:
            request.user.score = request.user.score + 100 - 10 * (count_hit - 1)
            request.user.last_score = 100 - 10 * (count_hit - 1)
            result = f"Поздравляем! Вы угадали число. Ваш рейтинг увеличился на {100 - 10 * (count_hit - 1)}"
        if count_hit > 11:
            if request.user.score + 100 - 10 * (count_hit - 1) < 0:
                request.user.last_score = -request.user.score
                request.user.score = 0
                result = f"Поздравляем! Вы угадали число, но слишком поздно, поэтому ваш рейтинг упал до нуля."
            else:
                request.user.score = request.user.score + 100 - 10 * (count_hit - 1)
                result = f"Поздравляем! Вы угадали число, но слишком поздно, поэтому ваш рейтинг уменьшился на {abs(100 - 10 * (count_hit - 1))}"
                request.user.last_score = 100 - 10 * (count_hit - 1)
        request.user.save()
        request.user.count_play += 1
        request.user.last_hit = count_hit
        request.user.last_number = secret_number
        request.user.save()
        match count_hit:
            case 1:
                request.user.hit1 += 1
            case 2:
                request.user.hit2 += 1
            case 3:
                request.user.hit3 += 1
            case 4:
                request.user.hit4 += 1
            case 5:
                request.user.hit5 += 1
            case 6:
                request.user.hit6 += 1
            case 7:
                request.user.hit7 += 1
            case 8:
                request.user.hit8 += 1
            case 9:
                request.user.hit9 += 1
            case 10:
                request.user.hit10 += 1
            case 11:
                request.user.hit11 += 1
            case 12:
                request.user.hit12 += 1
            case 13:
                request.user.hit13 += 1
            case 14:
                request.user.hit14 += 1
            case 15:
                request.user.hit15 += 1
            case 16:
                request.user.hit16 += 1
            case 17:
                request.user.hit17 += 1
            case 18:
                request.user.hit18 += 1
            case 19:
                request.user.hit19 += 1
        request.user.save()
        if 100 - 10 * (count_hit - 1) < 0:
            qwer = f" К сожалению, ваш рейтинг уменьшился на {abs(100 - 10 * (count_hit - 1))} единиц."
        else:
            qwer = f" Ваш рейтинг увеличился на {100 - 10 * (count_hit - 1)} единиц. Теперь он составляет {request.user.score} единиц."
        flag = 0
        count_hit = 0
        Previous_attempts = []
        Previous_attempts_1 = []
    else:
        count_hit += 1
        cows = 0
        bulls = 0
        secret_number = str(secret_number)
        for i in range(len(user_guess)):
            if user_guess[i] == secret_number[i]:
                bulls += 1
            elif user_guess[i] in secret_number:
                cows += 1
        iuy = str(count_hit) + ". " + "Ваше число: " + str(user_guess) + ". Быков найдено " + str(
            bulls) + ", коров найдено " + str(cows) + "."
        if count_hit % 2 == 0:
            Previous_attempts.append(iuy)
        else:
            Previous_attempts_1.append(iuy)
        result = f"К сожалению, это неверное число. Количество оставшихся попыток: {20 - count_hit} {secret_number}"
        secret_number = int(secret_number)
        flag = 1
        if count_hit > 20:
            if request.user.score - 100 < 0:
                request.user.last_score = -request.user.score
                request.user.score = 0
            else:
                request.user.last_score = -100
                request.user.score -= 100
            request.user.save()
            result = "Ой! Вы использовали все попытки. Ничего, получится в следующий раз! Ваш рейтинг уменьшился на 100 единиц."
            request.user.count_play += 1
            request.user.save()
            Previous_attempts = []
            Previous_attempts_1 = []
            count_hit = 0
            request.user.hit20 += 1
    request.user.save()
    if request.user.score + 100 - 10 * (count_hit - 1) < 0:
        reit = 0
    else:
        reit = 100 - 10 * (count_hit - 1)
    if result == "Ой! Вы использовали все попытки. Ничего, получится в следующий раз! Ваш рейтинг уменьшился на 100 единиц.":
        reit = -100
    return render(request, 'main/game_secret.html',
                  {'result': result, 'prev': Previous_attempts, 'prev_1': Previous_attempts_1})


def data_form(request):
    global reit
    global count_hit
    global flag
    global secret_number
    global Previous_attempts
    global Previous_attempts_1
    result = ""
    qwer = ''
    if flag == 0:
        Previous_attempts = []
        Previous_attempts_1 = []
        a = set()
        while True:
            secret_number = random.randint(1000, 9999)
            secret_number = str(secret_number)
            for i in range(len(secret_number)):
                a.add(int(secret_number[i]))
            if len(a) == 4:
                break
            else:
                a.clear()
    user_guess = int(request.POST['user_guess'])
    user_guess = str(user_guess)
    if user_guess == str(secret_number) and count_hit <= 20:
        if count_hit <= 11:
            request.user.score = request.user.score + 100 - 10 * (count_hit - 1)
            request.user.last_score = 100 - 10 * (count_hit - 1)
            result = f"Поздравляем! Вы угадали число. Ваш рейтинг увеличился на {100 - 10 * (count_hit - 1)}"
        if count_hit > 11:
            if request.user.score + 100 - 10 * (count_hit - 1) < 0:
                request.user.last_score = -request.user.score
                request.user.score = 0
                result = f"Поздравляем! Вы угадали число, но слишком поздно, поэтому ваш рейтинг упал до нуля."
            else:
                request.user.score = request.user.score + 100 - 10 * (count_hit - 1)
                result = f"Поздравляем! Вы угадали число, но слишком поздно, поэтому ваш рейтинг уменьшился на {abs(100 - 10 * (count_hit - 1))}"
                request.user.last_score = 100 - 10 * (count_hit - 1)
        request.user.save()
        request.user.last_hit = count_hit
        request.user.last_number = secret_number
        request.user.count_play += 1
        request.user.save()
        match (count_hit):
            case 1:
                request.user.hit1 += 1
            case 2:
                request.user.hit2 += 1
            case 3:
                request.user.hit3 += 1
            case 4:
                request.user.hit4 += 1
            case 5:
                request.user.hit5 += 1
            case 6:
                request.user.hit6 += 1
            case 7:
                request.user.hit7 += 1
            case 8:
                request.user.hit8 += 1
            case 9:
                request.user.hit9 += 1
            case 10:
                request.user.hit10 += 1
            case 11:
                request.user.hit11 += 1
            case 12:
                request.user.hit12 += 1
            case 13:
                request.user.hit13 += 1
            case 14:
                request.user.hit14 += 1
            case 15:
                request.user.hit15 += 1
            case 16:
                request.user.hit16 += 1
            case 17:
                request.user.hit17 += 1
            case 18:
                request.user.hit18 += 1
            case 19:
                request.user.hit19 += 1
        request.user.save()
        if 100 - 10 * (count_hit - 1) < 0:
            qwer = f" К сожалению, ваш рейтинг уменьшился на {abs(100 - 10 * (count_hit - 1))} единиц."
        else:
            qwer = f" Ваш рейтинг увеличился на {100 - 10 * (count_hit - 1)} единиц. Теперь он составляет {request.user.score} единиц."
        flag = 0
        count_hit = 0

        Previous_attempts = []
        Previous_attempts_1 = []
    else:
        count_hit += 1
        cows = 0
        bulls = 0
        secret_number = str(secret_number)
        for i in range(len(user_guess)):
            if user_guess[i] == secret_number[i]:
                bulls += 1
            elif user_guess[i] in secret_number:
                cows += 1
        iuy = str(count_hit) + ". " + "Ваше число: " + str(user_guess) + ". Быков найдено " + str(
            bulls) + ", коров найдено " + str(cows) + "."
        if count_hit % 2 == 0:
            Previous_attempts.append(iuy)
        else:
            Previous_attempts_1.append(iuy)
        result = f"К сожалению, это неверное число. Количество оставшихся попыток: {20 - count_hit}"
        secret_number = int(secret_number)
        flag = 1
        if count_hit > 20:
            if request.user.score - 100 < 0:
                request.user.last_score = -request.user.score
                request.user.score = 0
            else:
                request.user.last_score = -100
                request.user.score -= 100
            request.user.count_play += 1
            request.user.last_hit = 20
            request.user.save()
            result = ("Ой! Вы использовали все попытки. Ничего, получится в следующий раз! Ваш рейтинг уменьшился на "
                      "100 единиц.")
            Previous_attempts = []
            Previous_attempts_1 = []
            count_hit = 0
            request.user.hit20 += 1
    request.user.save()
    if request.user.score + 100 - 10 * (count_hit - 1) < 0:
        reit = 0
    else:
        reit = 100 - 10 * (count_hit - 1)
    if result == ("Ой! Вы использовали все попытки. Ничего, получится в следующий раз! Ваш рейтинг уменьшился на 100 "
                  "единиц."):
        reit = -100
    return render(request, 'main/game.html',
                  {'result': result, 'prev': Previous_attempts, 'prev_1': Previous_attempts_1})
