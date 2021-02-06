from django.shortcuts import render
import csv

def inflation_view(request):
    template_name = 'inflation.html'

    with open('inflation_russia.csv', 'r', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=';')
        contents = {}
        for i, row in enumerate(csvreader):
            if i == 0:
                headers = [x for x in row]
            else:
                for j, value in enumerate(row):
                    if j == 0:
                        year = value
                        contents.update({year: []})
                    else:
                        if value:
                            contents[year].append(float(value))
                        else:
                            contents[year].append(value)
    context = {'headers': headers, 'contents': contents}
    print(context)

    return render(request, template_name,
                  context)
