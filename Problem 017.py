otn = len("onetwothreefourfivesixseveneightnine")                                   #one to nine
udtth = otn * 9                                                                     #units digit twenty through one hundred
ttn = len("teneleventwelvethirteenfourteenfifteensixteenseventeeneighteennineteen") #ten through nineteen
twentytoninety = len("twentythirtyfortyfiftysixtyseventyeightyninety")              #twenty to ninety
hundred_and = len("hundredand")                                                     #length of connecting words
thousand = len("onethousand")
hundreds_place = (otn + (9 * hundred_and)) * 100 - 27
tens_and_ones = 10 * (udtth + (10 * twentytoninety) + ttn)
total = hundreds_place + tens_and_ones + thousand
print total

