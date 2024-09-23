import matplotlib.pyplot as plt
from numpy import *
import math
import requests

#Define functions

def display_menu():
    print("""
        ====================================
                WELCOME TO CALCULATOR
        ====================================
                     _______
                    |  ___  |
                    | |   | |
                    | |___| |
                    |_______|
        """)

#input from simple calculations
def get_numbers():
    number1 = float(input("Please enter your first number: "))
    number2 = float(input("Please enter your second number: "))
    return number1, number2

#math functions
def addition(no1, no2):
    print(no1+no2)

def subtraction(no1, no2):
    print(f"result: {no1-no2}")

def multiplication(no1, no2):
    print(no1*no2)

def division(no1, no2):
    try:
        if number2 != "0":
            print(number1 / number2)
    except ZeroDivisionError:
        print("ERROR - You can´t divide by 0")

def modulo(no1, no2):
    print(no1 % no2)


#graphical functions
def quadratic_display():
    x = linspace(-10,10)
    print("Quadratic function formula: f(x) = ax^2 + bx + c " )
    a = float(input("Please enter your number for a : "))
    b = float(input("Please enter your number for b : "))
    c = float(input("Please enter your number for c : "))

    y = a*x**2 + b*x + c

    plt.plot(x,y)
    plt.title("Quadratic function")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.show()

def linear_display():
    x = linspace(-10,10)
    print("linear function formula: f(x) = m*x +b")
    m = float(input("Please enter your number for m: "))
    b = float(input("Please enter your number for b: "))

    y = m * x + b

    plt.plot(x,y)
    plt.title("Linearic function")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.show()

def sinus_display():
    t = arange(0,10,0.1)
    amp = sin(t)
    plt.plot(t, amp)
    plt.show()

def cosinus_display():
    t = arange(0,10,0.1)
    amp = cos(t)
    plt.plot(t, amp)
    plt.show()

def circular_display():
    radius = float(input("Please enter your radius: "))
    t = arange(0, 2*pi, .01 )
    x = radius * sin(t)
    y = radius * cos(t)
    plt.plot(x, y)
    plt.xlabel(" X - Achsis ")
    plt.ylabel(" Y - Achsis ")
    plt.show()

#api connection
url = "http://api.exchangeratesapi.io/v1/latest?access_key=77a46e703c138f40123ac19771f856e6"

#Currency exchange calculator with real-life information (API)
def currency_exchange():
    print("""
    Notice: Only enter the abbreviation of currencys -> USD, EUR, GBP...
    """)
    from_currency = input("From Country: ")
    to_currency = input("To Country: ")
    amount = int(input("Please enter your amount: "))
    response = requests.get(url)
    rate = response.json()["rates"][from_currency]
    amount_in_EUR = amount/rate
    amount = amount_in_EUR*(response.json()["rates"][to_currency])
    amount = round(amount, 2)
    print(amount)
    again = input("Try again?: (Y)(N)").lower()
    if again == "y":
        currency_exchange()

#ETF calculator
def etf_saving():
    start_budget = float(input("Please enter your starting budget: "))
    rate = float(input("Now enter your interest rate: "))
    years = int(input("How long you want to calculate? : "))
    end_budget = start_budget

    i = 0
    while i < years:
        end_budget += round((end_budget * (rate/100)),2)
        i += 1
    print(f"Your Start-Budget: {start_budget}€\n{rate/100}%\n{years} years\nYour End-Budget: {end_budget}€\n")
