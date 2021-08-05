import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import random
import qrcode
from PIL import Image, ImageDraw, ImageFont
import os


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning")
    elif hour>=12 and hour<18:
        speak("Good afternoon")
    else:
        speak("Good evening")
    speak("Hello ,, I am atlas ,,,, I hope u are feeling good ,,,,  I can able to predict disease based on symptoms ,,,and can give suitable tips for common diseases for your health ,,if you need my help please tell,,,  help me ")


def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Recognizing........")
        r.pause_threshold=1
        r.adjust_for_ambient_noise(source,duration = 1)
        audio=r.listen(source)

    try:
        print("please Wait for few minutes")
        query=r.recognize_google(audio, language='en-in')
        print("User said:",query)

    except Exception as e:
        print(e)
        speak("very sorry , can you please tell again")
        query="Nothing"
    return query

if __name__ == "__main__":
    wishme()
    while True:
        query=takecommand().lower()
        if "help me" in query:
            speak("Can you please tell me ,,, what r the symptoms you are suffering from ")
            while True:
                query=takecommand().lower()
                if 'wikipedia' in query:
                    speak('Searching Wikipedia...')
                    query = query.replace("wikipedia", "")
                    results = wikipedia.summary(query, sentences=2)
                    speak("According to Wikipedia")
                    print(results)
                    speak(results)

                elif 'fever' in query:
                    speak("You can take paracetamol or if you want to book an appoinment please say book appoinment")
                    print("CAUSES:Overexposing to sunlight,Dehydration,heart stroke,etc.,")

                elif 'headache' in query:
                    speak("you can take disprin or if you want to book an appoinment please say book appoinment")
                    print("CAUSES:Lack of sleep,stress,loud noice exposure")

                elif 'cough and cold' in query or 'cold and cough' in query:
                    speak("You can take amxicoillin or if you want to book an appoinment please say book appoinment")
                    print("CAUSES:Allergens like pollen,dust,mold or pet dander")

                elif 'skin allergies' in query:
                    speak("You can take allegra or if you want to book an appoinment please say book appoinment")
                    print("CAUSES:insect string,allergens,certain foods")

                elif 'stomach pain' in query or 'stomach ache' in query:
                    speak("You can take panadol or if you want to book an appoinment please say book appoinment")
                    print("CAUSES:stomach virus,liver or bladder issues")

                elif 'chicken pox' in query:
                    speak("You can take cool bath with added baking soda or if you want to book an appoinment please say book appoinment")
                    print("CAUSES:It is caused dueto varicella-zoster virus")

                elif 'vomiting' in query:
                    speak("You can take dolasetron or if you want to book an appoinment please say book appoinment")
                    print("CAUSES:Food poisoning,motion sickness,etc.,")

                elif 'flu' in query:
                    speak("You can take bed rest and antiviraldrug or if you want to book an appoinment please say book appoinment")
                    print("CAUSES:IS is caused due to influenza virus,")
 
                elif 'indigestion' in query:
                    speak("You can take antacids and oral medicines or if you want to book an appoinment please say book appoinment")
                    print("CAUSES:Excessive eating habits.,")

                elif 'malaria' in query:
                    speak("You can take antibiotics and consult doctor as soon as possible or if you want to book an appoinment please say book appoinment")
                    print("CAUSES:Insect bite,contaminated water")

                elif 'abdominal pain dehydration' in query:
                    speak("You are suffering from bacterial disease shigellosis bacterial dysentry For quitting say thank you or if you want to book an appoinment please say book appoinment")
                    print("CAUSITIVE AGENT: shigella sp\nSITE OF INFECTION: intestine\nMODE OF INFECTION: food and water contamination by faeces or faecal oral route")

                elif 'fever headache swollen lymph nodes' in query or 'headache swollen lymph node' in query:
                    speak("You are suffering from bacterial disease bubonic plague black death For quitting say thank you  or if you want to book an appoinment please say book appoinment")
                    print("CAUSITIVE AGENT: yersinia pestis\nSITE OF INFECTION: lymph node\nMODE OF INFECTION:Rat flea vector")

                elif 'abdominal pain' in query or ' dehydration' in query:
                    speak("You are suffering from bacterial disease shigellosis bacterial dysentry For quitting say thank you or if you want to book an appoinment please say book appoinment")
                    print("CAUSITIVE AGENT: shigella sp\nSITE OF INFECTION: intestine\nMODE OF INFECTION: ")

                elif 'fever soar throat' in query or 'hoarseness difficulty in breathing' in query:
                    speak("You are suffering from bacterial disease diphtheria For quitting say thank you or if you want to book an appoinment please say book appoinment")
                    print("CAUSITIVE AGENT: corynebacterium diphtheria\nSITE OF INFECTION: LARNX SKIN AND NASAL GENETICAL PASSAGE\nMODE OF INFECTION: DROPLET INFECTION " )

                elif 'fever difficulty in breathing'in query or 'soar throat hoarseness' in query:
                    speak("You are suffering from bacterial disease DIPHTHERIA For quitting say thank you or if you want to book an appoinment please say book appoinment")
                    print("CAUSITIVE AGENT: corynebacterium diphtheria\nSITE OF INFECTION: LARNX SKIN AND NASAL GENETICAL PASSAGE\nMODE OF INFECTION: DROPLET INFECTION " )

                elif 'severe diarrhoea' in query or 'dehydration' in query:
                    speak("You are suffering from bacterial disease cholera For quitting say thank you or if you want to book an appoinment please say book appoinment")
                    print("CAUSITIVE AGENT: vibrio cholerae\nSITE OF INFECTION: intestine\nMODE OF INFECTION: severe diarrhoea and dehydration" )

                elif 'headache diarrhoea' in query or 'fever abdominal discomfort' in query:
                    speak("You are suffering from bacterial disease typhoid For quitting say thank you or if you want to book an appoinment please say book appoinment")
                    print("CAUSITIVE AGENT: salmonella typhi\nSITE OF INFECTION: intestine\nMODE OF INFECTION: THROUGH CONTAMINATED FOOD AND WATER " )

                elif 'abdominal discomfort headache'in query or 'fever diarrhoea' in query:
                    speak("You are suffering from bacterial disease typhoid For quitting say thank you or if you want to book an appoinment please say book appoinment")
                    print("CAUSITIVE AGENT: salmonella typhi\nSITE OF INFECTION: intestine\nMODE OF INFECTION: THROUGH CONTAMINATED FOOD AND WATER ")


                elif 'thick mucopurulant nasal discharge' in query:
                    speak("You are suffering from bacterial disease tuberculosis For quitting say thank you or if you want to book an appoinment please say book appoinment")
                    print("CAUSITIVE AGENT: mycobacterium tuberculosis\nSITE OF INFECTION: lungs\nMODE OF INFECTION: DROPLET INFECTION " )

                elif 'fever brown sputum' in query or 'cough painful breathing' in query:
                    speak("You are suffering from bacterial disease pneumonia For quitting say thank you or if you want to book an appoinment please say book appoinment")
                    print("CAUSITIVE AGENT: streptococcus pneumoniae\nSITE OF INFECTION: lungs\nMODE OF INFECTION: droplet infection" )

                elif 'diarrhoea dysentery' in query or 'blood and mucus in stool' in query:
                    speak("You are suffering from protozoan disease amoebiasis For quitting say thank you or if you want to book an appoinment please say book appoinment")
                    print("CAUSITIVE AGENT: Entamoeba histolytica\nSITE OF INFECTION: Intestine\nMODE OF INFECTION: House flies" )

                elif 'sleeping sickness' in query:
                    speak("You are suffering from protozoan disease African Sleeping Sickness For quitting say thank you or if you want to book an appoinment please say book appoinment")
                    print("CAUSITIVE AGENT: Trypanosoma species\nSITE OF INFECTION:Liver,Lymph gland,Blood vessels\nMODE OF INFECTION: Tsetse flies" )

                elif 'weight loss' in query or 'enlargement of spleen and river' in query:
                    speak("You are suffering from protozoan disease kala azar Sickness For quitting say thank you or if you want to book an appoinment please say book appoinment")
                    print("CAUSITIVE AGENT: Leishmania donovani\nSITE OF INFECTION: Liver,Lymph gland,Blood vessels\nMODE OF INFECTION: sand fly" )

                elif 'acne' in query:
                    speak("You can apply aloevera and take vitamin A derivatives For quitting say thank you or if you want to book an appoinment please say book appoinment")

                elif 'thank you' in query:
                    speak("quitting..,thank you for using atlas")
                    break

                elif 'book appointment' in query:
                    speak("PLEASE FILL THE FOLLOWING DETAILS TO BOOK AN APPOINMENT")
                    image = Image.new('RGB', (1000, 900), (300, 300, 300))

                    draw = ImageDraw.Draw(image)

                    font = ImageFont.truetype('arial.ttf', size=60)

                    os.system("Title: Consultation receipt")

                    d_date = datetime.datetime.now()
                    reg_format_date = d_date.strftime("  %d-%m-%Y\t\t\t\t\t CONSULTATION RECEIPT\t\t\t\t\t  %I:%M:%S %p")
                    print(
                        '+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
                    print(reg_format_date)
                    print(
                        '+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')

                    # starting position of the message
                    (x, y) = (50, 75)
                    company = "ATLAS MULTISPECIALITY HOSPITAL"

                    color = 'rgb(0, 0, 0)' # black color
                    font = ImageFont.truetype('arial.ttf', size=45)
                    draw.text((x, y), company, fill=color, font=font)

                    # adding an RECEIPT id number. You can manually take it from user
                    (x, y) = (50,450)
                    idno = random.randint(10000000, 90000000)
                    message = str('ID: ' + str(idno))
                    color = 'rgb(0, 0, 0)'  # black color
                    font = ImageFont.truetype('arial.ttf', size=45)
                    draw.text((x, y), message, fill=color, font=font)

                    # For the Name
                    (x, y) = (50, 250)
                    name = input('Enter Your Full Name: ')

                    fname = str('Name: ' + str(name))
                    color = 'rgb(0, 0, 0)'  # black color
                    font = ImageFont.truetype('arial.ttf', size=45)
                    draw.text((x, y), fname, fill=color, font=font)

                    # For the gender
                    (x, y) = (50, 350)
                    gender = input('Enter Your Gender: ')
                    fgender = str('Gender: ' + str(gender))
                    color = 'rgb(0, 0, 0)'  # black color
                    draw.text((x, y), fgender, fill=color, font=font)

                    # For the Age
                    (x, y) = (400, 350)
                    age = int(input('Enter Your Age: '))
                    fage = str('Age: ' + str(age))
                    color = 'rgb(0, 0, 0)'  # black color
                    draw.text((x,y), fage, fill=color, font=font)


                    # For the Mob No
                    (x, y) = (50, 650)
                    No = int(input('Enter Your Mobile Number: '))

                    fNo = str('Mobile Number: ' + str(No))
                    color = 'rgb(0, 0, 0)'  # black color
                    draw.text((x, y), fNo, fill=color, font=font)

                    (x,y) = (50,750)
                    Ida = str("Appoiment Time: 7:30pm")
                    color = 'rgb(0, 0, 0)'  # black color
                    draw.text((x,y), Ida, fill=color, font=font)

                    (x,y) = (50,550)
                    Dna = str("Docter Name: Bujak")
                    color = 'rgb(0, 0, 0)'  # black color
                    draw.text((x,y), Dna, fill=color, font=font)

                    # save the edited image

                    image.save(str(name) + '.png')

                    QR = qrcode.make(str(company) +'\n' + str(name)+'\n' + str(idno) )  # this info. is added in QR code, also add other things
                    QR.save(str(idno) + '.bmp')


                    ID = Image.open(name + '.png')
                    QR = Image.open(str(idno) + '.bmp')  # 25x25
                    ID.paste(QR, (650, 350))
                    ID.save(name + '.png')

                    print(('\n\n\nYour Appoinment has been sucessfully booked.\n please collect your receipt and please say thank you for quitting'))

                
                elif 'exit' in query:
                    exit()
            break   
                            

               
              
              
              
         
            
      
      


 
              
              
              
         
            
      
      


