from django.http import HttpResponse
from django.shortcuts import render
from django.template import TemplateDoesNotExist
from django.views import View
from django.shortcuts import render, redirect
from django.template.loader import get_template
from django.views import View
from .models import TravelPlan
from .models import Post
from xhtml2pdf import pisa
from reportlab.pdfgen import canvas
from io import BytesIO
import openai
import requests
import json
from django.urls import reverse

# Initialize the OpenAI API client with your API key
openai.api_key = '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'

def home(request):
    return render(request, 'planner/home.html')

def explo(request):
    return render(request, 'cbe/explore.html')

def hcbe(request):
    return render(request, 'cbe/hotels.html')

def h1cbe(request):
    return render(request, 'cbe/hotel1.html')

def h2cbe(request):
    return render(request, 'cbe/hotel2.html')

def h3cbe(request):
    return render(request, 'cbe/hotel3.html')

def rcbe(request):
    return render(request, 'cbe/rest.html')

def hicbe(request):
    return render(request, 'cbe/hid.html')

def result1(request):
    return render(request, 'cbe/result1.html')

def explo2(request):
    return render(request, 'Chennai/chennai.html')

def chtl(request):
    return render(request, 'Chennai/chhotel.html')

def chtl1(request):
    return render(request, 'Chennai/chhotel1.html')

def chtl2(request):
    return render(request, 'Chennai/chhotel2.html')

def chtl3(request):
    return render(request, 'Chennai/chhotel3.html')

def cfamous(request):
    return render(request, 'Cbe/famous.html')

def chennai(request):
    return render(request, 'Cbe/chat.html')

def crs(request):
    return render(request, 'Chennai/crest.html')

def result2(request):
    return render(request, 'Chennai/result2.html')

def chd(request):
    return render(request, 'Chennai/chid.html')

def cfa(request):
    return render(request, 'Chennai/cfam.html')

def ch1(request):
    return render(request, 'Chennai/chat1.html')

def about(request):
    team_members = [
        {   
            'name': 'Muhammad Saqib',
            'role': 'Full-Stack Developer',
            'info': 'Saqib is an experienced full-stack web developer who studied at Curtin University. With a strong foundation in computer science, he has developed expertise in various programming languages, frameworks, and libraries such as JavaScript, Python, React, and Node.js. Saqib is a dedicated learner who actively participates in coding competitions, hackathons, and industry events to stay updated with the latest trends and advancements. His ability to seamlessly transition between frontend and backend development, coupled with his problem-solving skills, enables him to tackle complex challenges and deliver high-quality solutions. Saqibs passion for continuous learning, combined with his excellent communication and collaboration skills, makes him a valuable asset to any team or project.',
            'image': 'Saqib1.jpeg',
            'linkedin': 'https://www.linkedin.com/in/muhammad-saqib-doullah-092107201/',
            'instagram': 'https://www.instagram.com/saqqii_9613/',
            'email': 'https://github.com/SaqibDoullah'
        },
        {
            'name': 'Fateh Amjad',
            'role': 'Back-end Developer',
            'info': 'Fateh is an exceptional back-end developer with a strong focus on creating robust and scalable systems. His extensive knowledge and expertise in programming languages and frameworks allow him to design and implement high-quality solutions that meet the demanding needs of modern applications. Currently pursuing a degree in Computer Science at Curtin University Dubai, Fateh is equipped with a deep understanding of computer science principles, which he seamlessly combines with his practical skills. With a keen eye for efficient database architecture, optimized APIs, and secure authentication mechanisms, Fateh consistently delivers top-notch results. His proficiency in cloud technologies enables him to leverage the power of platforms like AWS or Azure, ensuring the scalability of his solutions. Collaborative by nature, Fateh excels in working alongside diverse teams and effectively communicates his ideas to achieve project objectives. Always eager to stay ahead of the curve, Fateh actively seeks out the latest industry trends and emerging technologies, making him a valuable asset in creating innovative and future-proof systems.',
            'image': 'fateh1.jpeg',
            'linkedin': 'https://www.linkedin.com/in/fatehamjad/',
            'instagram': 'https://www.instagram.com/fatehamjxd/',
            'email': 'https://github.com/fatehamjad'
        },
        {
            'name': 'Ali Omar',
            'role': 'UX/UI Designer',
            'info': 'Ali is an exceptionally talented designer with a relentless dedication to crafting intuitive and visually captivating user experiences. Currently enrolled in studies at Curtin University Dubai, Ali combines his educational background with a natural flair for creativity to produce remarkable design solutions. His keen eye for aesthetics, attention to detail, and deep understanding of user psychology enable him to create interfaces that seamlessly blend functionality and visual appeal. Alis studies at Curtin University Dubai provide him with a solid theoretical foundation in design principles and a platform to experiment with emerging technologies. He constantly pushes the boundaries of innovation, leveraging his passion for learning and keeping up with the latest design trends to deliver cutting-edge solutions. With a collaborative mindset and excellent communication skills, Ali excels in working closely with cross-functional teams to transform ideas into captivating user experiences. His passion for design and commitment to excellence make him a valuable asset in creating immersive and user-centric interfaces that leave a lasting impression.',
            'image': 'Ali1.jpeg',
            'linkedin': 'https://www.linkedin.com/in/ali-omar-mustafa-0a49681b8/',
            'instagram': 'https://www.instagram.com/pxxiy/',
            'email': 'https://github.com/ali220066'
        },
        {
            'name': 'Ahmed Faisal',
            'role': 'Front-end Developer',
            'info': 'Ahmed is a standout front-end developer known for his outstanding skills in creating responsive and interactive interfaces. With a deep passion for design aesthetics and a strong focus on user experience, Ahmed consistently delivers visually stunning and engaging applications. Currently pursuing his studies at Curtin University Dubai, Ahmed combines his theoretical knowledge with practical expertise to produce cutting-edge solutions. He possesses a strong willingness to work collaboratively and learn from others, making him an asset in any team setting. Ahmeds attention to detail and commitment to staying up-to-date with the latest industry trends enable him to create modern and innovative user interfaces. His proficiency in front-end technologies such as HTML, CSS, and JavaScript allows him to develop seamless and intuitive user experiences. With his natural talent for problem-solving and dedication to continuous improvement, Ahmed is poised to make a significant impact in the world of front-end development.',
            'image': 'Ahmed.jpg',
            'linkedin': 'https://www.linkedin.com/in/ahmed-faisal-717604228/',
            'instagram': 'https://www.instagram.com/ahmedfaisalz/',
            'email': 'https://github.com/ahmedfaisalz'
        }
    ]
    context = {
        'title': 'About',
        'team_members': team_members
    }    
    return render(request, 'planner/about.html', context)
def travel_plan(request):
    if request.method == "POST":
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        destination = request.POST.get('destination')
        age = request.POST.get('age')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        budget = request.POST.get('budget')
        places = request.POST.getlist('places[]')
        places_str = ", ".join(places)
        no_of_visitors = request.POST.get('no_of_visitors')
        booked_before = True if request.POST.get('booked_before') == 'yes' else False
        find = request.POST.get('find')

        if destination == 'Coimbatore':
            return redirect(reverse('explo1'))  # Redirect to Dubai page
        elif destination == 'Chennai':
            return redirect(reverse('explo2'))  # Redirect to Abu Dhabi page
        else:
            # Redirect to a default page if destination not found
            return redirect(reverse('explo1'))  # Replace 'default_page' with your default page name

    return render(request, 'planner/create_travel_plan.html')

def itinerary(request):
    # Retrieve all travel plan objects from the database
    travel_plans = TravelPlan.objects.all()

    # Print the user data to the terminal
    #for travel_plan in travel_plans:
    #    print(
    #        travel_plan.firstname,
    #        travel_plan.lastname,
    #        travel_plan.destination,
    #        travel_plan.age,
    #        travel_plan.contact_number,
    #        travel_plan.start_date,
    #        travel_plan.end_date,
    #        travel_plan.budget,
    #        travel_plan.places,
    #        travel_plan.booked_before,
    #        travel_plan.find
    #    )

    try:
        # Retrieve the latest travel plan from the database
        latest_travel_plan = TravelPlan.objects.latest('id')
        generated_itinerary = latest_travel_plan.generated_itinerary
    except TravelPlan.DoesNotExist:
        latest_travel_plan = None
        generated_itinerary = ""  # Set a default value when there's no latest_travel_plan

    # Pass the generated itinerary to the context dictionary
    context = {'generated_itinerary': generated_itinerary}

    return render(request, 'planner/itinerary.html', context)

def save_pdf(request):
    # Retrieve the generated itinerary
    latest_travel_plan = TravelPlan.objects.latest('id')
    generated_itinerary = latest_travel_plan.generated_itinerary

    # Create a PDF file using ReportLab
    pdf_buffer = BytesIO()
    p = canvas.Canvas(pdf_buffer)

    # Set font and size for the title
    p.setFont("Helvetica-Bold", 14)
    p.drawString(100, 750, "Travel Itinerary")

    # Set font and size for the content
    p.setFont("Helvetica", 12)
    text_lines = generated_itinerary.split("\n")
    y = 700
    for line in text_lines:
        p.drawString(100, y, line)
        y -= 20

    # Save the PDF content
    p.showPage()
    p.save()

    # Reset the buffer and set the response headers for PDF file download
    pdf_buffer.seek(0)
    response = HttpResponse(pdf_buffer, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="travel_itinerary.pdf"'

    return response
class SavePDFView(View):
    def get(self, request):
        # Retrieve the generated itinerary
        latest_travel_plan = TravelPlan.objects.latest('id')
        generated_itinerary = latest_travel_plan.generated_itinerary

        # Create a PDF file
        pdf_buffer = BytesIO()
        p = canvas.Canvas(pdf_buffer)

        # Set font and size for the title
        p.setFont("Helvetica-Bold", 14)
        p.drawString(100, 750, "Travel Itinerary")

        # Set font and size for the content
        p.setFont("Helvetica", 12)
        text_lines = generated_itinerary.split("\n")
        y = 700
        for line in text_lines:
            p.drawString(100, y, line)
            y -= 20

        # Save the PDF content
        p.showPage()
        p.save()

        # Reset the buffer and set the response headers for PDF file download
        pdf_buffer.seek(0)
        response = HttpResponse(pdf_buffer, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="travel_itinerary.pdf"'

        return response
    
    