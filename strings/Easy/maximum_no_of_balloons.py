def maxNumberOfBalloons(self, text):
    counter_balloons = [0, 0, 0, 0, 0]
    balloon = "balon"
    for c in text:
        try:
            index = balloon.index(c)
            counter_balloons[index] += 1
        except:
            continue
    counter_balloons[2] //= 2
    counter_balloons[3] //= 2
    return min(counter_balloons)
