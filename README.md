# CS361-Portfolio-Project
Clear instructions for how to programmatically REQUEST data from the microservice you implemented. Include an example call.
Clear instructions for how to programmatically RECEIVE data from the microservice you implemented.
UML sequence diagram showing how requesting and receiving data works. Make it detailed enough that your partner (and your grader) will understand.

To request the number of days until a specific date, have in the microservice_communication.txt the line "deadline: DDMMYYYY" where DD is the day MM is the month and YYYY is the year. An example is 17032025 as March 17, 2025. 

The output is in the microservice_communication.txt in the format "days_left: NUMBER" where NUMBER is the days calculated to be in between today's date and the deadline date. An example when given March 17, 2025, as the deadline date and July 31, 2023, as today's date is "days_left: 595".

When the program is called, and the txt file reads an input that is not in the input or output formats of "deadline: DDMMYYYY" and "days_left: NUMBER" it will fail.

![UML](https://github.com/HaileyRichter/CS361-Portfolio-Project/assets/74836020/cf01275d-2c1b-4a00-a054-196b55a7224f)
