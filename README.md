# Ex.04 Design a Website for Server Side Processing
## Date:

## AIM:
To create a web page to calculate total bill amount with GST from price and GST percentage, using server-side scripts.

## FORMULA:
Bill = P + (P * GST / 100)
<br> P --> Price (in Rupees)
<br> GST --> GST (in Percentage)
<br> Bill --> Total Bill Amount (in Rupees)

## DESIGN STEPS:

### Step 1:
Clone the repository from GitHub.

### Step 2:
Create Django Admin project.

### Step 3:
Create a New App under the Django Admin project.

### Step 4:
Create python programs for views and urls to perform server side processing.

### Step 5:
Create a HTML file to implement form based input and output.

### Step 6:
Publish the website in the given URL.

## PROGRAM:
```math.html

<!DOCTYPE html>
<html>
<head>
    <title>GST Bill Calculator</title>

    <style>

        body{
            background-color: #e37ed3;
            font-family: serif;
        }

        .container{
            width: 400px;
            background-color: white;
            padding: 30px;
            margin: 100px auto;
            border-radius: 10px;
            box-shadow: 0px 0px 10px gray;
        }

        h2{
            text-align: center;
            color: rgb(8, 230, 241);
        }

        label{
            font-size: 18px;
            font-weight: bold;
        }

        input{
            width: 95%;
            padding: 10px;
            margin-top: 10px;
            border-radius: 5px;
            border: 1px solid rgb(10, 244, 240);
        }

        .btn{
            text-align: center;
        }

        button{
            background-color: rgb(14, 195, 223);
            color: white;
            padding: 10px 20px;
            border: none;
            border-radius: 5px;
            margin-top: 20px;
            cursor: pointer;
            font-size: 16px;
        }

        button:hover{
            background-color: rgb(14, 195, 223);
        }

        h3{
            color: rgb(14, 195, 223);
            text-align: center;
            margin-top: 20px;
        }

    </style>

</head>

<body>

    <div class="container">

        <h2>GST Bill Calculator</h2>

        <form method="POST">

            {% csrf_token %}

            <label>Enter Price :</label><br>

            <input type="number" 
                   name="price" 
                   value="{{price}}" 
                   step="0.01" 
                   required>

            <br><br>

            <label>Enter GST Percentage :</label><br>

            <input type="number" 
                   name="gst" 
                   value="{{gst}}" 
                   step="0.01" 
                   required>

            <div class="btn">
                <button type="submit">Calculate</button>
            </div>

        </form>

        {% if total_bill is not None %}

            <h3>Total Bill Amount : ₹ {{ total_bill }}</h3>

        {% endif %}

    </div>

</body>
</html>
```
```
view.py

from django.shortcuts import render

def bill(request):

    context = {}
    context['price'] = 0
    context['gst'] = 0
    context['total_bill'] = 0

    if request.method == "POST":

        p = float(request.POST.get('price', '0'))
        g = float(request.POST.get('gst', '0'))

        gst_amount = (p * g) / 100
        total = p + gst_amount

        context['price'] = p
        context['gst'] = g
        context['total_bill'] = total

    return render(request, 'mathapp/math.html', context)
```
```
urls.py 

from django.contrib import admin
from django.urls import path
from mathapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.bill),
]
```

## OUTPUT - SERVER SIDE:
<img width="1678" height="1003" alt="Screenshot 2026-05-31 232003" src="https://github.com/user-attachments/assets/ecc47f3b-52f5-408b-9ec2-def4f5cb278a" />


## OUTPUT - WEBPAGE:
<img width="1538" height="903" alt="Screenshot 2026-05-31 232024" src="https://github.com/user-attachments/assets/10acaa58-2c6e-49ae-96eb-e1029600f64c" />

## RESULT:
The a web page to calculate vehicle mileage and fuel efficiency using server-side scripts is created successfully.
