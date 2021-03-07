def main ():
    print("=====DOUBLE OR NOTHING=====")
    import random
    play = input(("apakah kamu sudah siap? (ya/tidak): "))
    play = play.lower ()
    point = 1
    while play == "ya":
        random1 = random.randint(1,2)
        if random1 == 2:
            point = point * 2
        elif random1 == 1:
            print("ZONKKKKK!")
            break
        play = input("apakah anda ingin lanjut? (ya/tidak): ")
        play = play.lower ()
    if play == "tidak":
        print("Point anda = ", point)
    restart = (input("ulangi? (ya/tidak): "))
    restart = restart.lower ()
    if restart == "ya":
        main()
    else:
        exit()
print (main())

