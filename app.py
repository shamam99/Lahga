from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

import webbrowser

# Dictionary mapping colloquial words to classical words
word_mappings = {
 "يويق": ["اللهجة النجدية", "ينظر بخلسة"],
"القابله": ["اللهجة النجدية","غداً"],
"يدرعم": ["اللهجة الحجازية", "يأتي بسرعه"],
"احتري": ["اللهجة النجدية","انتظر"],
"القايله": ["اللهجة النجدية","الظهر"],
"ازهل": ["اللهجةالنجدية","اعتمد"],
"اصنك": ["اللهجة النجدية","اصفقك"],
"تعقب": ["اللهجة النجدية","خسئت"],
"تهقى": ["اللهجة النجدية","تعتقد"],
"ارعصه": ["اللهجة الحجازية","اضغطه"],
"ميد": ["اللهجة الجنوبية","اليه"],
"مايقه": ["اللهجة الشمالية","تتكبر"],
"الطمك": ["اللهجة الحجازية","اضربك"],
"داويه": ["اللهجة الشرقاوية","ماذا بك"],
"كسحه": ["اللهجة الجنوبية","فشله"],
"مير": ["اللهجة النجدية","لكن"],
"يلفح": ["اللهجة الحازية","يتحرك بقوة"],
"امصع": ["اللهجة الحجازية","اشد"],
"ازهملي": ["اللهجة الحجازية","نادي لي"],
"زمبيل": ["اللهجة الحجازية","كيس"],
"صمرقع": ["اللهجة الحجازية","جنان"],
"اترينو": ["اللهجة الحجازية","عشان كذا"],
"افتر": ["اللهجة الحجازية","اهدأ"],
"محزق": ["اللهجة الحجازية","ضيق"],
"دحلسه": ["اللهجة الحجازية","اقناع"],
"كرته": ["اللهجة الحجازية","فستان"],
"عازه": ["اللهجة الحجازية","حاجة"],
"تبحر": ["اللهجة الشمالية","تنظر بقوة"],
"هبولي": ["اللهجة الجنوبية","اعطني"],
"قر": ["اللهجة الجنوبية","اهدأ"],
"تقطب": ["اللهجة الجنوبية","تمسك و احذر"],
"يذل": ["اللهجة الجنوبية","يخاف"],
"بقعاء": ["اللهجة الجنوبية"," اسم جنية"],
"اشقومك": ["اللهجة الجنوبية","ماذا بك"],
"أدمي": ["اللهجة الجنوبية","تعالي"],
"تقمبر": ["اللهجة الجنوبية","اجلس"],
"هنيه": ["اللهجة الجنوبية","اعطني"],
"صمة": ["اللهجة الجنوبة","مقدمه الرأس"],
"دنقر": ["اللهجة الجنوبية","مؤخرة الرأس"],
"صابر": ["اللهجة الجنوبية","نهاية الشعر الواصل الى الاذن"],
"لجع": ["اللهجة الجنوبية","الفك السفلي"],
"الكلحة": ["اللهجة الجنوبية","الفم"],
"حنتول": ["اللهجة الجنوبة","الطفل الرضيع"],
"ملكد": ["اللهجة الجنوبية","شيء يهرس به"],
"مروط": ["اللهجة الجنوبية","البلعوم"],
"ديم": ["اللهجة الجنوبية","جلد"],
"مغشر": ["اللهجة الجنوبة","فريد"],
"ما حالشه": ["اللهجة الجنوبية","كيف الحال"],
"ازم": ["اللهجة الجنوبية","امسك"],
"أمرط": ["اللهجة الجنوبية","ابلع"],
"تقمبري": ["الهجة الجنوبة","اجلسي"],
"لهلم": ["اللهجة الجنوبية","الى هنا"],
"زله": ["اللهجة الجنوبية","ادخل"],
"يتشبح": ["اللهجة الجنوبية","ينظر"],
"بانكه": ["اللهجة الجنوبية","مروحه في السقف"],
"وش خانته": ["اللهجة الجنوبية","ما فائدته"],
"اتسحج": ["اللهجة الشمالية","امشط شعري"],
"جدوع": ["اللهجة الشرقاوية","فطور"],
"نصيفات": ["اللهجة الشرقاوية","توأم"],
"افلح": ["اللهجة الجنوبية","اذهب"],
"غدوة": ["الهجة الشرقاوية","الضحى"],
"هويه": ["اللهجة الشمالية","لماذا"],
"اركد": ["اللهجة الحجازية","اهدأ"],
"اركدي": ["اللهجة الحجازية","اهدأي"],
"ابطيت": ["اللهجة النجدية","تأخرت"],
"ميدي": ["اللهجة الجنوبية","لي"],
"اسرح": ["اللهجة الجنوبية","اذهب للعمل"],
"أربا": ["اللهجة الجنوبية","انظر"],
"جيفا الله بجا": ["اللهجة الجنوبية","كيف حالك"],
"يقدا ويل": ["اللهجة الجنوبية","اين انت"],
"زغفه": ["اللهجة الجنوبية","الزاوية"],
"رقد": ["اللهجة الجنوبية","نام"],
"جزي": ["اللهجة الجنوبية","نشط"],
"ساذابي": ["اللهجة الجنوبية","انما اقصد"],
"بنا": ["اللهجة الجنوبية","انا"],
"عستيمك": ["اللهجة الجنوبية","جلدك"],
"خالس": ["اللهجة الجنوبية","سأسلخ"],
"مهبا": ["اللهجة الجنوبية","لماذا"],
"يلايع": ["اللهجة الجنوبية","يتمشى دون هدف"],
"هوجا": ["اللهجة الجنوبية","خذ"],
"الكابة": ["اللهجة الجنوبية","الباب"],
"دبع": ["اللهجة الجنوبية","حلق"],
"يفشي": ["الهجة الجنوبية","حلو وجميل"],
"تكوكحه": ["اللهجة الجنوبية","حمله على ظهره"],
"ينجع": ["اللهجة الجنوبة","ينتقل من بيت الى آخر"],
"يعكش": ["اللهجة الجنوبية","يجري"],
"اسطى": ["اللهجة الجنوبية","ااقبل منك"],
"جثم": ["اللهججة الجنوبية","نام قليلا"],
"تجثوع": ["اللهجة الجنوبية","ينام ويستيقظ"],
"هايشن": ["اللهجة الجنوبية","ذاهب"],
"نبز": ["اللهجة الجنوبية","قفز"],
"دبايه": ["اللهجة الجنوبية","بنت"],
"هيجه": ["الهجة الجنوبية","شجرة"],
"اشتحر": ["اللهجة الجنوبية","انشق"],
"سبحن": ["اللهجة الجنوبية","كسل"],
"خنذور": ["اللهجة الجنوبية","حجره"],
"لذع": ["اللهجة الجنوبية","غضب"],
"استكا": ["اللهجة الجنوبية","دق"],
"تعرقستا": ["اللهجة الجنوبية","تعرقل"],
"اللهج": [" اللهجة الجنوبية","الشباك"],
"سامطن": ["اللهجة الجنوبية","بارد"],
    # Add more mappings here as needed
}

# Function to find the classical word for a colloquial word
def find_classical_word(colloquial_word):
    return word_mappings.get(colloquial_word.lower(), "No classical word found")

# Function to search siwar for a word
def search_on_siwar(word):
    search_query = f"https://siwar.ksaa.gov.sa/api/alriyadh/search?query=%D8%B4%D9%85%D9%85"
    query = {word}
    headers = {
    'accept': 'application/json',
    'apikey': '94c0e4b1-ed24-4664-a63a-94ea18c30135'
}
    webbrowser.open(search_query)

# Taking input from the user
colloquial_input = input("Enter a colloquial word: ")

# Finding and displaying the classical counterpart
classical_word = find_classical_word(colloquial_input)

if classical_word == "No classical word found":
    print(f"No classical word found for '{colloquial_input}'")
    print("Searching on siwar...")
    search_on_siwar(colloquial_input)
else:
    print(f"هذه الكلمة  '{colloquial_input}' ترادف '{classical_word}'")

@app.route('C:\Users\shama\Downloads\lujain\website')
def index():
    return ('index.html')
# New endpoint for translation
@app.route('/api/translate', methods=['GET'])
def translate():
    colloquial_word = request.args.get('colloquial')

    if colloquial_word:
        classical_word = find_classical_word(colloquial_word)
        return jsonify({'classical_word': classical_word})
    else:
        return jsonify({'error': 'Colloquial word not provided'}), 400

if __name__ == '__main__':
    app.run(debug=True)
