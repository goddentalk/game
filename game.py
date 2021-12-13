import random

dl=int(input('Введите длину норы:')) #Длина норы
hp=int(input('Введите здоровье:')) #Здоровье
rep=int(input('Введите репутацию:')) #Уважение
p=int(input('Введите вес:')) #Вес

def indificators(long,health,reputation,weight): #Вывод показателей
    print('Длина норы=',dl)
    print('Ваше здоровье=',hp)
    print('Репутация=',rep)
    print('Вес=',p)
    indent()
    input()

def indent(): #отступ
    print('', end='\n')

print('Добро пожаловать в Королевство!')

vs=random.randint(0,1) #Время суток
phrase=random.randint(0,1)

if vs==0:
    indent()
    if phrase==0:
        print('В холодном поту вы просыпаетесь у себя в яме. Вам снился кошмар. Снаружи уже темнеет, делать нечего. Вы решаете поспать до утра.')
    else:
        print('Вы просыпаетесь у себя в яме. Вам снился загадочный сон... Снаружи уже темнеет, делать нечего. Вы решаете поспать до утра.')
    indent()
else:
    indent()
    if phrase==0:
        print('В холодном поту вы просыпаетесь у себя в яме. Вам снился кошмар. Снаружи уже темнеет, делать нечего. Вы решаете поспать до утра.')
    else:
        print('Вы просыпаетесь у себя в яме. Вам снился загадочный сон... Снаружи уже темнеет, делать нечего. Вы решаете поспать до утра.')
    indent()

while dl>0 and hp>0 and p>0:
    if rep>=100:
        print('Вы сидите в таверне, попиваете медовуху со своими друзьями. Вы стали узнаваемыми во всех уголках Королевства. Вы счастливы.')
        indent()
        print('Игра пройдена.')
        break
    if vs==0:
        print('Наступает ночь. Вы спите.')
        indent()
        dl-=2
        print('Вам снится прекрасный сон.')
        indent()
        hp+=20
        rep-=2
        p-=5
        vs+=1
        indificators(dl,hp,p,rep)
        indent()
        print('Наступает утро. Вы чувствуете, что выспались.')
        indent()

    if vs==1:
        act=int(input('Выберите занятие (0-копать нору,1-поесть травки, 2-пойти подраться, 3-спать весь день):'))
        indent()
        if act==0:
            rezhim=int(input('Вы копаете яму. Стоит ли тратить на это свои силы? (0-нет, 1-да):'))
            indent()
            if rezhim==1:
                if hp<=30:
                    print('ВЫ слишком устали для интенсивной работы.')
                    indent()
                    if hp<=10:
                        print('Да ты валишься с ног! Вам следует отдохнуть.')
                        indent()
                    else:
                        print('Вы летаете в облаках. Вы лениво выполняете свою работу.')
                        indent()
                        dl+=2
                        hp-=10
                    indificators(dl,hp,p,rep)
                    indent()
                else:
                    print('ОГО! Да вы полны сил! Вы начинаете работать в полную силу.')
                    indent()
                    dl+=5
                    hp-=30
                indificators(dl,hp,p,rep)
                indent()
            else:
                if hp<=10:
                    print('Да ты валишься с ног! Вам следует отдохнуть.')
                    indent()
                else:
                    print('Вы летаете в облаках. Вы лениво выполняете свою работу.')
                    indent()
                    dl+=2
                    hp-=10
                indificators(dl,hp,p,rep)
                indent()

        elif act==1: 
            food=int(input('Ваш живот урчит. Вы решаете перекусить травкой. Какой травкой вы утолите свой голод?(0-жухлой, 1-зелёной):'))
            indent()
            if food==0:
                print('Вы решили не радовать себя роскошной едой.')
                indent()
                hp+=10
                p+=15
                indificators(dl,hp,p,rep)
                indent()

            else:
                print('Вы решили порадовать себя роскошной едой.')
                indent()
                if rep<30:
                    print('На вашем пути встаёт бык,видимо,охранник золотой поляны. Он смотрит на вас с презрением и с силой выгоняет вас с этого места. Вы остались без еды. Станьте более уважаемым, чтобы вас приняли здесь, как своего.')
                    indent()
                    hp-=30
                    indificators(dl,hp,p,rep)
                    indent()
                else:
                    print('На вашем пути встаёт бык,видимо,охранник золотой поляны. Он смотрит на вас с уважением и с радостью пропускает вас.')
                    indent()
                    hp+=30
                    p+=30
                indificators(dl,hp,p,rep)
                indent()

        elif act==2:
            boss=int(input('Вы пришли на арену. На доске вы видите трёх участников (0-кролик(самый слабый), 1-волк(средний по силе), 2-змей(босс)):'))
            if boss==0:
                rand_p = random.randint(20, 50)
                kof = p / (p + rand_p)
                rand = random.uniform(0.1, 1.0)
                if rand<=kof:
                    if p-rand_p >= 15: 
                        rep += 5
                    if p - rand_p < 15: 
                        rep += 15   
                    if p == rand_p: 
                        rep += 10
                    indent()
                    print('Победа за тобой! Доктор залатал все твои раны.')
                    if hp<100:
                        s=100-hp
                        hp+=s
                    indificators(dl,hp,p,rep)
                    indent()
                if rand>kof:
                    if p-rand_p >= 15: 
                        rep-=15
                        hp-=15
                    if p-rand_p < 15: 
                        rep-=5 
                        hp-=5
                    if p == rand_p: 
                        rep-=10
                        hp-=10
                    indent()
                    print('Ты проиграл')
                    indificators(dl,hp,p,rep)
                    indent()
            elif boss==1:
                rand_p = random.randint(50, 70)
                kof = p / (p + rand_p)
                rand = random.uniform(0.1, 1.0)
                if rand<=kof:
                    if p-rand_p >= 30: 
                        rep += 10
                    if p - rand_p < 30: 
                        rep += 20   
                    if p == rand_p: 
                        rep += 15
                    indent()
                    print('Победа за тобой! Доктор залатал все твои раны.')
                    if hp<100:
                        s=100-hp
                        hp+=s
                    indificators(dl,hp,p,rep)
                    indent()
                if rand>kof:
                    if p-rand_p >= 30: 
                        rep-=20
                        hp-=20
                    if p-rand_p < 30: 
                        rep-=10 
                        hp-=10
                    if p == rand_p: 
                        rep-=15
                        hp-=15
                    indent()
                    print('Ты проиграл')
                    indificators(dl,hp,p,rep)
                    indent()
            elif boss==2:
                rand_p = random.randint(70, 100)
                kof = p / (p + rand_p)
                rand = random.uniform(0.1, 1.0)
                if rand<=kof:
                    if p-rand_p >= 45: 
                        rep += 20
                    if p - rand_p < 45: 
                        rep += 30  
                    if p == rand_p: 
                        rep += 25
                    indent()
                    print('Победа за тобой! Доктор залатал все твои раны.')
                    if hp<100:
                        s=100-hp
                        hp+=s
                    indificators(dl,hp,p,rep)
                    indent()
                if rand>kof:
                    if p-rand_p >= 45: 
                        rep-=30
                        hp-=30
                    if p-rand_p < 45: 
                        rep-=20
                        hp-=20
                    if p == rand_p: 
                        rep-=25
                        hp-=25
                    indent()
                    print('Ты проиграл')
                    indificators(dl,hp,p,rep)
                    indent()

        else:
            print('Вы решаете прилечь на кровать и, закрыв глаза, вы тоните в сновидениях.')
            indent()
            hp+=40
            rep-=4
            p-=10
            print('Вам снится прекрасный сон, в котором вас уважает всё Королевство.')
            indent()
            indificators(dl,hp,p,rep)
            indent()
        vs-=1
indent()
print('Сложив своё оружие, ты лег в поле. Закрыва глаза, ты уснул вечным сном.')
indent()
print('Ты проиграл.')
            







                
                




            




