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

    return render(request, 'mathsever/math.html', context)