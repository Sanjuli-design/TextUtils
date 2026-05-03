from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    
    return render(request,'index.html')
    # return HttpResponse("home")
def analyze(request):
        djtext=request.POST.get('text','default')
        removepunc=request.POST.get('removepunc','off')
        fullcaps=request.POST.get('fullcaps','off')
        newlineremove=request.POST.get('newlineremove','off')
        extraspaceremover=request.POST.get('extraspaceremover','off')
        charcount=request.POST.get('charcount','off')
        analyzed=djtext
        purpose=[]
        if removepunc=="on":
            
            punctuations='''!()-[]{};:"\,<>./?@#$%^&_*~'''
            temp=""
            for char in analyzed:
                if char not in punctuations:
                    temp+=char
            analyzed=temp        
            purpose.append("removed punctuations")
            # params={'purpose':'removepunc','analyzed_text':analyzed}
            # return render(request,'analyze.html',params)
        if(fullcaps=="on"):
            
            analyzed=analyzed.upper()
            purpose.append("conveted to uppercase")
            # params={'purpose':'uppercase','analyzed_text':analyzed}
            # return render(request,'analyze.html',params)     
        if(newlineremove=="on"):
             
             analyzed=analyzed.replace("\r"," ").replace("\n"," ")
             purpose.append("remove new line")
            #  params={'purpose':'newlineremover','analyzed_text':analyzed}
            #  return render(request,'analyze.html',params)     
        if(extraspaceremover=="on"):
             temp=""
             for index,char in enumerate(analyzed):
                  if index<len(analyzed)-1 and analyzed[index]== " " and analyzed[index+1]==" ":
                       continue
                  
                  temp+=char
             analyzed=temp      
             purpose.append("remove extra space")
            #  params={'purpose':'remove extra space','analyzed_text':analyzed}
            #  return render(request,'analyze.html',params)
        if(charcount=="on"):
             count=len(analyzed)
             purpose.append(f"character count={count}")
            #  params={'purpose':'count character','analyzed_text':count}
            #  return render(request,'analyze.html',params)                           

        if not purpose:
             return render(request,'analyze.html',{'purpose':'no operation selected','analyzed_text':djtext})
        return render(request,'analyze.html',{'purpose':", ".join(purpose),'analyzed_text':analyzed})
# def removepunc(request):
#     djtext=request.GET.get('text','default')
#     print(djtext)
#     return HttpResponse("remove punc")
# def capitalisefirst(request):
#     return HttpResponse("capitalise first")
# def newlineremove(request):
#     return HttpResponse("REMOVE LINE")
# def charcount(request):
#     return HttpResponse('''count characater <a href="http://127.0.0.1:8000/">back</a>''')
# def spaceremove(request):
#     return HttpResponse("remove apace")
