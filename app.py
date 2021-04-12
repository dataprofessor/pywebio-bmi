# A simple script to calculate BMI
import pywebio
from pywebio.input import input, FLOAT
from pywebio.output import put_text, put_html, put_markdown, put_table

def bmi():
    height = input("Input your height(cm)：", type=FLOAT)
    weight = input("Input your weight(kg)：", type=FLOAT)

    BMI = weight / (height / 100) ** 2

    top_status = [(16, 'Severely underweight'), (18.5, 'Underweight'),
                  (25, 'Normal'), (30, 'Overweight'),
                  (35, 'Moderately obese'), (float('inf'), 'Severely obese')]

    for top, status in top_status:
        if BMI <= top:
            put_markdown('# **Results**')
            put_text('Your BMI: %.1f. Category: %s' % (BMI, status))
            put_html('<br><br>')
            put_markdown('Your BMI: `%.1f`. Category: `%s`' % (BMI, status))
            put_html('<hr>')
            put_table([
                ['Your BMI', 'Category'],
                [BMI, status],
            ])

            break

if __name__ == '__main__':
    pywebio.start_server(bmi, port=55)
