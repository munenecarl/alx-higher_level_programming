#!/bin/usr/bash

def print_last_digit(number):
	last_digit = (number - (10 * int(number / 10)))
	if number < 0:
		last_digit = last_digit * -1
	print(last_digit, end="")
	return last_digit
