Some say paying taxes makes Finns happy, so let's see if the secret of happiness lies in one of the taxes set out in Finnish tax code.

According to the Finnish Tax Administration, a gift is a transfer of property to another person against no compensation or payment. If the total value of the gifts you receive from the same donor in the course of 3 years is €5,000 or more, you must pay gift tax.

When the gift is received from a close relative or a family member, the amount of tax to be paid is determined by the following table, which is also available on this website:

Value of gift	Tax at the lower limit	Tax rate for the exceeding part (%)
5 000 — 25 000	100	8
25 000 — 55 000	1 700	10
55 000 — 200 000	4 700	12
200 000 — 1 000 000	22 100	15
1 000 000 —	142 100	17
So, for a gift of 6 000 euros the recipient pays a tax of 180 euros (100 + (6 000 - 5 000) * 0.08). Similarly, for a gift of 75 000 euros the recipient pays a tax of 7 100 euros (4 700 + (75 000 - 55 000) * 0.12).

Please write a program which calculates the correct amount of tax for a gift from a close relative. Have a look at the examples below to see what is expected. Notice the lack of thousands separators in the input values - you may assume there will be no spaces or other thousands separators in the numbers in the input, as we haven't yet covered dealing with these.

Sample output
Value of gift: 3500
No tax!

Sample output
Value of gift: 5000
Amount of tax: 100.0 euros

Sample output
Value of gift: 27500
Amount of tax: 1950.0 euros












To solve this problem, we need to calculate the gift tax based on the value of the gift received from a close relative or family member according to the Finnish tax code. The tax is calculated using a tiered system where different portions of the gift value are taxed at different rates.

Approach
Check for Tax Applicability: If the gift value is less than €5,000, no tax is due.

Determine the Tax Bracket: For gifts valued at €5,000 or more, we need to find the appropriate tax bracket in the given table. Each bracket has a lower limit, a fixed tax amount for amounts up to the lower limit, and a marginal tax rate for the amount exceeding the lower limit.

Calculate the Tax: Using the identified bracket, compute the tax by adding the fixed tax for the bracket to the product of the marginal rate and the amount exceeding the bracket's lower limit.
    












    python
value = int(input("Value of gift: "))

if value < 5000:
    print("No tax!")
else:
    if 5000 <= value < 25000:
        tax = 100 + (value - 5000) * 0.08
    elif 25000 <= value < 55000:
        tax = 1700 + (value - 25000) * 0.10
    elif 55000 <= value < 200000:
        tax = 4700 + (value - 55000) * 0.12
    elif 200000 <= value < 1000000:
        tax = 22100 + (value - 200000) * 0.15
    else:
        tax = 142100 + (value - 1000000) * 0.17
    print(f"Amount of tax: {tax:.1f} euros")
Explanation
Input Handling: The program reads the gift value as an integer input.

Tax Check: If the gift value is below €5,000, it prints "No tax!" and exits.

Bracket Determination: The program checks which tax bracket the gift value falls into:

€5,000 to €25,000: The tax is €100 plus 8% of the amount exceeding €5,000.

€25,000 to €55,000: The tax is €1,700 plus 10% of the amount exceeding €25,000.

€55,000 to €200,000: The tax is €4,700 plus 12% of the amount exceeding €55,000.

€200,000 to €1,000,000: The tax is €22,100 plus 15% of the amount exceeding €200,000.

Above €1,000,000: The tax is €142,100 plus 17% of the amount exceeding €1,000,000.

Tax Calculation: Based on the identified bracket, the program calculates the tax by applying the fixed tax for the bracket and the marginal rate on the excess amount. The result is printed with one decimal place.

This approach efficiently handles the tiered tax calculation by systematically checking each bracket and applying the corresponding tax rules, ensuring accurate and clear output.