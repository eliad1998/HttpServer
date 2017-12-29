# -*- coding: utf-8 -*-

def createArticles():
    article1 = {
      'link': 'http://www.ynet.co.il/articles/0,7340,L-4713571,00.html',
      'img': 'https://images1.ynet.co.il/PicServer4/2014/08/05/5506384/52203970100690640360no.jpg',
      'title': 'החוש הדומיננטי שיעזור לכם בלימודים',
      'content': 'החוש הדומיננטי שיעזור לכם בלימודים. אילו טיפים של שימוש בחושים יעזרו לכם?',
    }

    article2 = {
      'link': 'http://www.ynet.co.il/articles/0,7340,L-4713571,00.html',
      'img': 'https://images1.ynet.co.il/PicServer5/2017/11/23/8172884/817287001000100980704no.jpg',
      'title': '"כ"ט בנובמבר: "שמחה שנמשכה ימים ולילות,הייתה אופוריה"',
      'content': 'ב-1947 הם היו ילדים או צעירים בתחילת דרכם, אבל את היום הגורלי ב-29 בנובמבר הם לא\
                  שוכחים עד היום. "כולם היו צמודים לרדיו. אני זוכרת את התפרצות השמחה, ריקודים\
                  והתחבקויות".',
    }

    article3 = {
      'link': 'https://www.calcalist.co.il/world/articles/0,7340,L-3726321,00.html',
      'img': 'https://images1.calcalist.co.il/PicServer3/2017/11/30/775736/2_l.jpg',
      'title': 'רוצים נייר טואלט? הזדהו: כך משפרים הסינים￼ את מצב השירותים הציבוריים',
      'content': 'שבוע קרא נשיא סין שי ג‘ינפינג להמשיך את מהפכת השירותים הציבוריים עליה הכריז ב-2015.ֿֿ\
                    עד כה שופצו ונבנו 68 אלף מתקנים',
    }

    article4 = {
      'link': 'http://www.nrg.co.il/online/13/ART2/902/962.html',
      'img': 'http://www.nrg.co.il/images/archive/465x349/1/646/416.jpg',
      'title': 'מחקו לכם הודעה בווטסאפ? עדיין תוכלו לקרוא אותה',
      'content': 'אפליקציה בשם Noti cation History מאפשרת למשתמשי  '
                  'אנדרואיד לקרוא את הנתונים הזמניים הנשמרים ביומן הפעילות של הסמארטפון, כולל הודעות מחוקות.'
    }

    article5 = {
      'link': 'http://www.nrg.co.il/online/55/ART2/904/542.html',
      'img': 'http://www.nrg.co.il/images/archive/465x349/1/795/429.jpg',
      'title': 'גם בחורף: זה בדיוק הזמן לקפוץ לאילת',
      'content': 'העיר הדרומית נעימה לנופש גם בחודשי החורף. '
                  'כעת מוצעים מחירים אטרקטיביים במיוחד בחבילות שכוללות מגוון אטרקציות, לינה וטיסות'
    }

    article6 = {
      'link': 'https://food.walla.co.il/item/3113079',
      'img': 'https://img.wcdn.co.il/f_auto,w_700/2/5/1/3/2513314-46.jpg',
      'title': '12 בתי קפה שמתאימים לעבודה עם לפטופ',
      'content': 'בין אם אתם סטודנטים או עצמאיים, זה תמיד סיפור למצוא בית קפה נעים וטעים לרבוץ בו. '
                  'קיבצנו עבורכם 12 מקומות אהובים בדיוק למטרה זו, בארבע הערים הגדולות'
    }

    article7 = {
      'link': 'https://news.walla.co.il/item/3114145',
      'img': 'https://img.wcdn.co.il/f_auto,w_700/2/4/9/5/2495334-46.jpg',
      'title': 'שותק על אזריה, נלחם באהוד ברק: בנט מנסה להיבנות כימין ממלכתי',
      'content': 'כשרגב נלחמת ברעש בתאטרון יפו, בנט משנה בשקט את נהלי סל התרבות כך שהחומרים "השמאלנים" ייפלטו. '
                  'כשהקשת הפוליטית מתרעמת על דיווחי ה"דיל" של טראמפ עם הפלסטינים, בנט שותק עד שהרשות תסרב.'
    }

    article8 = {
      'link': 'https://news.walla.co.il/item/3114283',
      'img': 'https://img.wcdn.co.il/f_auto,w_700/2/5/1/4/2514588-46.jpg',
      'title': 'רצח בכל שלושה ימים: צרפת יוצאת למאבק באלימות נגד נשים',
      'content': 'אחרי ש-126 נשים נרצחו בידי בני זוגן בשנה שעברה, הציג מקרון צעדים חדשים למלחמה בתופעה. "זאת בושה לצרפת", '
                 'אמר הנשיא שאחת מהבטחות הבחירות שלו הייתה להשיג שוויון מגדרי.'
    }
    articles = [article1, article2, article3, article4, article5, article6, article7, article8]
    return articles
# Put article on html format
def putArticleHtml(article):
    html = ""
    html += "<div class=\"row\">"
    html += "<div class=\"features\">"
    html +="<div class=\"col-md-4 col-sm-6 wow fadeInDown\" data-wow-duration=\"1000ms\" data-wow-delay=\"600ms\">"
    html += "<div class=\"feature-wrap\">"
    html += "<img src=\"" + article.get('img') + "\" />"
    html += "<h2><a href=\"" + article.get('link') + "\">" + article.get('title') + "</a></h2>"
    html += "<h3>" + article.get('content') + "</h3>"
    html += "</div>"
    html += "</div><!--/.col-md-4-->"
    html += "</div><!--/.services-->"
    html += "</div><!--/.row--> "
    return html

def putArticles(data, numArticles):
    # All of the articles
    articles = createArticles()
    dataToSend = ""
    # Finding where to put to articles
    # Ignore empty lines
    splitted = filter(None, data.split('\n'))
    startIgnore = -1
    endIgnore = -1
    for i in range (0, len(splitted)):
        if str(splitted[i]).__contains__("<div class=\"row\">") and str(splitted[i + 1]).__contains__("<div class=\"features\">"):
            startIgnore = i
            endIgnore = i + 10
            break
    # Did not found where the articles should be
    if startIgnore == -1:
        return data

    for i in range(0, len(splitted)):
        if i == startIgnore:
            for j in range (0, numArticles):
                dataToSend += putArticleHtml(articles[j])
        if i not in range(startIgnore, endIgnore + 1):
            dataToSend += str(splitted[i])

    return dataToSend



