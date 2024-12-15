from KochCurve import *

if __name__ == "__main__":
    notFool = True
    while (notFool):
        print("Enter a length between 0.25 and 0.5 (included):")
        l = float(input())
        print("Enter a number of iteration (0 to whatever integer):")
        n = int(input())
        print("Search in your documents for the files Koch-curve.png and Koch-snowflake.png")
        KC = KochCurve(l, n)
        KC.plotCurve()
        KC.plotSnowFlake()

        print("Wanna make better life decisions? Enter y for yes.")
        choice = input()
        if choice == "y":
            print("You've made the right choice...")
            print("-------------------------------------------------------------")
        else:
            print("If you think you're gonna get out of this easily... Just kidding... Bye lah!")
            notFool = False