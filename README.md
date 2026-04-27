# 💰 Cash - Greedy Coin Change (Python)

![Python](https://img.shields.io/badge/Language-Python-blue.svg)
![CS50x](https://img.shields.io/badge/CS50x-Week%206-orange.svg)
![Algorithm](https://img.shields.io/badge/Algorithm-Greedy-brightgreen.svg)

A clean and simple Python program that calculates the **minimum number of coins** needed to make change for a given amount in dollars.

## ✨ Overview

This program asks the user how much change is owed (in dollars) and then outputs the fewest number of quarters (0.25), dimes (0.10), nickels (0.05), and pennies (0.01) required to make that exact amount using the **greedy algorithm**.

## 🎯 Features

- ✅ Accepts input in dollars (e.g., `9.75`, `0.41`, `1.00`)
- ✅ Robust input validation (re-prompts for negative or invalid input)
- ✅ Uses the greedy algorithm (optimal for standard US coins)
- ✅ Counts quarters, dimes, nickels, and pennies
- ✅ Clean, readable, and well-commented code
- ✅ Simple and user-friendly output

## 🚀 Quick Start

```bash
# Clone the repository
git clone https://github.com/yourusername/cash.git
cd cash

# Run the program
python cash.py
Example Input:
textChange owed: 9.75
Output:
text6
(Explanation: 4 quarters + 2 dimes = 6 coins)
📊 More Examples






























AmountMinimum CoinsBreakdown0.4141Q + 1D + 1N + 1P9.7564Q + 2D1.0044Q0.000No coins
🧠 What I Learned

Implementing the greedy algorithm in Python
Handling floating-point input safely
Converting dollars to cents to avoid precision issues
Input validation with loops
Writing clean and readable Python code

🛠️ Built With

Python 3
