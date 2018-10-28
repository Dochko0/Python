import math

dohod = float(input())
uspeh = float(input())
salary = float(input())

if uspeh <= 4.50:
    print('You cannot get a scholarship!')
elif 4.50 < uspeh < 5.50:
    if dohod > salary:
        print('You cannot get a scholarship!')
    else:
        print(f'You get a Social scholarship {math.floor(0.35*salary)} BGN')
elif uspeh >= 5.50:
    if dohod < salary:
        excelent1 = math.floor(uspeh * 25)
        excelent2 = math.floor(0.35 * salary)

        max_Scholarship = max(excelent1, excelent2)

        if excelent1 == max_Scholarship:
            print(f'You get a scholarship for excellent results {math.floor(max_Scholarship)} BGN')
        elif excelent2 == max_Scholarship:
            print(f'You get a Social scholarship {math.floor(max_Scholarship)} BGN')
    else:
        excelent3 = math.floor(uspeh * 25)
        print(f'You get a scholarship for excellent results {math.floor(excelent3)} BGN')
