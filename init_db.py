import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

# 1 covid

cur.execute("INSERT INTO posts (descriptor, pos_tag, content, notes) VALUES (?, ?, ?, ?)",
            ('COVID-19', 'сущ.', 'острая респираторная инфекция, вызываемая коронавирусом SARS-CoV-2.', '')
            )

cur.execute("INSERT INTO synonyms (post_id, ascriptor, marks, notes) VALUES (?, ?, ?, ?)",
            (1, 'коронавирус', '', '')
            )

cur.execute("INSERT INTO synonyms (post_id, ascriptor, marks, notes) VALUES (?, ?, ?, ?)",
            (1, 'коронавирусная инфекция', '', '')
            )

cur.execute("INSERT INTO synonyms (post_id, ascriptor, marks, notes) VALUES (?, ?, ?, ?)",
            (1, 'ковид', '', '')
            )

cur.execute("INSERT INTO synonyms (post_id, ascriptor, marks, notes) VALUES (?, ?, ?, ?)",
            (1, 'корона', '', '')
            )

cur.execute("INSERT INTO examples (post_id, content, keyword, source) VALUES (?, ?, ?, ?)",
            (1, '<…> списки будут регулярно пересматриваться с учетом таких факторов, как степень распространения COVID-19 и реализация программ вакцинации.', 'COVID-19', 1249)
            )

cur.execute("INSERT INTO examples (post_id, content, keyword, source) VALUES (?, ?, ?, ?)",
            (1, 'Я совсем не обладаю информацией, есть ли в Сочи ковид <...>.', 'ковид', 660)
            )

cur.execute("INSERT INTO examples (post_id, content, keyword, source) VALUES (?, ?, ?, ?)",
            (1, 'В октябре стало известно о смерти 13 пациентов с коронавирусом в ковидном госпитале на базе городской больницы № 20 в Ростове-на-Дону.', 'коронавирус', 1000)
            )

cur.execute("INSERT INTO examples (post_id, content, keyword, source) VALUES (?, ?, ?, ?)",
            (1, 'В больницы районов области с подозрением на коронавирусную инфекцию и лабораторно подтвержденным диагнозом госпитализированы 1590 пациентов.', 'коронавирусная инфекция', 1000)
            )

cur.execute("INSERT INTO examples (post_id, content, keyword, source) VALUES (?, ?, ?, ?)",
            (1, 'Пачка одного из модных сейчас противовирусных, которое даже некоторые врачи пьют при подозрении на корону, пока оно было в Екатеринбурге в аптеках, стоила больше 5 тысяч.', 'корона', 650)
            )

# 2 антимасочник

cur.execute("INSERT INTO posts (descriptor, pos_tag, content, notes) VALUES (?, ?, ?, ?)",
            ('Антимасочник', 'сущ.', 'человек, по разным причинам принципиально отказывающийся носить маску или респиратор в период пандемии коронавируса и/или общепринятого масочного режима.', '')
            )

cur.execute("INSERT INTO antonyms (post_id, ascriptor, marks, notes) VALUES (?, ?, ?, ?)",
            (2, 'масочник', '', 'конт. ант.')
            )

cur.execute("INSERT INTO examples (post_id, content, keyword, source) VALUES (?, ?, ?, ?)",
            (2, 'Что, трудно маску носить? — удивляется читатель под ником KENT. — Нормальные, адекватные люди и так всё соблюдали. Эта информация скорее для антимасочников и бестолковых, — считает читатель под ником Кость.', 'антимасочник', 259)
            )

# 3 антимасочный

cur.execute("INSERT INTO posts (descriptor, pos_tag, content, notes) VALUES (?, ?, ?, ?)",
            ('Антимасочный', 'прил.', 'негативный по отношению к ограничительным мерам, связанным с обязательным ношением медицинской маски/респиратора в общественных местах.', '')
            )

cur.execute("INSERT INTO examples (post_id, content, keyword, source) VALUES (?, ?, ?, ?)",
            (3, 'Тем временем врачи уверены, что рост ковид-пациентов не в последнюю очередь связан именно с антимасочными настроениями.', 'антимасочный', 420)
            )

# 4 бессиммптомник

cur.execute("INSERT INTO posts (descriptor, pos_tag, content, notes) VALUES (?, ?, ?, ?)",
            ('Бессимптомник', 'сущ.', 'пациент с положительным результатом теста на коронавирус, не обнаруживающий у себя внешних симптомов, вызываемых COVID-19.', '')
            )

cur.execute("INSERT INTO examples (post_id, content, keyword, source) VALUES (?, ?, ?, ?)",
            (4, '<…> один просто-напросто бессимптомник, как мы называем, он не знает даже, что он болен, он не носит маску и вокруг может заразить 7, 8, 10 человек <…>.', 'бессимптомник', 499)
            )

# 5 дистант

cur.execute("INSERT INTO posts (descriptor, pos_tag, content, notes) VALUES (?, ?, ?, ?)",
            ('Дистант', 'сущ.', 'режим обучения на дому при помощи специализированного ПО и онлайн-ресурсов в период пандемии COVID-19.', '')
            )

cur.execute("INSERT INTO synonyms (post_id, ascriptor, marks, notes) VALUES (?, ?, ?, ?)",
            (5, 'дистанционка', '', '')
            )

cur.execute("INSERT INTO examples (post_id, content, keyword, source) VALUES (?, ?, ?, ?)",
            (5, 'По каким правилам работают школы? — В школах Петербурга пока не вводят обязательный дистант.', 'дистант', 1004)
            )

cur.execute("INSERT INTO examples (post_id, content, keyword, source) VALUES (?, ?, ?, ?)",
            (5, 'Часть школьников перейдут на дистанционку, а первоклассники отправятся на каникулы.', 'дистанционка', 1002)
            )

# 6 доковидный

cur.execute("INSERT INTO posts (descriptor, pos_tag, content, notes) VALUES (?, ?, ?, ?)",
            ('Доковидный', 'прил.', 'относящийся к периоду времени до пандемии COVID-19.', ' (антонимы являются контекстуальными)')
            )

cur.execute("INSERT INTO synonyms (post_id, ascriptor, marks, notes) VALUES (?, ?, ?, ?)",
            (6, 'докоронавирусный', '', '')
            )

cur.execute("INSERT INTO antonyms (post_id, ascriptor, marks, notes) VALUES (?, ?, ?, ?)",
            (6, 'постковидный', '', 'контекст. ант.')
            )

cur.execute("INSERT INTO examples (post_id, content, keyword, source) VALUES (?, ?, ?, ?)",
            (6, 'В Китае нормальная жизнь с конца марта. Вечеринки, путешествия, кафе, рестораны — все это давным-давно как в доковидные времена, разве что кое-где с масками.', 'доковидный', 939)
            )

cur.execute("INSERT INTO examples (post_id, content, keyword, source) VALUES (?, ?, ?, ?)",
            (6, 'Многие компании после отмены локдауна отметили высокий спрос на квартиры, хотя количество сделок пока не сравнялось ни с докоронавирусным, ни с прошлогодним.', 'докоронавирусный', 534)
            )

# 7 зум

cur.execute("INSERT INTO posts (descriptor, pos_tag, content, notes) VALUES (?, ?, ?, ?)",
            ('Зум', 'сущ. нариц.', 'программа, предоставляющая возможность удалённой конференц-связи с использованием облачных вычислений.', '')
            )

cur.execute("INSERT INTO examples (post_id, content, keyword, source) VALUES (?, ?, ?, ?)",
            (7, 'Например, где-то дети разделились по дням: три дня в неделю группа приходит на занятия, другие три дня учится в зуме.', 'зум', 717)
            )

# 8 инфодемия

cur.execute("INSERT INTO posts (descriptor, pos_tag, content, notes) VALUES (?, ?, ?, ?)",
            ('Инфодемия', 'сущ.', 'информационный шум вокруг коронавируса, включающий в основном негативные и фейковые новости о происходящем в период пандемии.', '(аббр. от «информация» и «пандемия»)')
            )

cur.execute("INSERT INTO examples (post_id, content, keyword, source) VALUES (?, ?, ?, ?)",
            (8, 'Создаются условия инфодемии: мы видим очереди из скорых, кадры из моргов в СМИ. Происходит разрыв восприятия, отсюда недоверие к мерам, которые рекомендуются, и недооценка ситуации.', 'инфодемия', 796)
            )

# 9 ковид-госпиталь

cur.execute("INSERT INTO posts (descriptor, pos_tag, content, notes) VALUES (?, ?, ?, ?)",
            ('Ковид-госпиталь', 'сущ.', 'медицинское (лечебное) учреждение, специально оборудованное и предназначенное для оказания медицинской (стационарно-лечебной) помощи пациентам с COVID-19.', '')
            )

cur.execute("INSERT INTO synonyms (post_id, ascriptor, marks, notes) VALUES (?, ?, ?, ?)",
            (9, 'ковид-центр', '', '')
            )

cur.execute("INSERT INTO synonyms (post_id, ascriptor, marks, notes) VALUES (?, ?, ?, ?)",
            (9, 'ковид-стационар', '', '')
            )

cur.execute("INSERT INTO synonyms (post_id, ascriptor, marks, notes) VALUES (?, ?, ?, ?)",
            (9, 'ковид-больница', '', '')
            )

cur.execute("INSERT INTO synonyms (post_id, ascriptor, marks, notes) VALUES (?, ?, ?, ?)",
            (9, 'ковид-площадка', '', '')
            )

cur.execute("INSERT INTO synonyms (post_id, ascriptor, marks, notes) VALUES (?, ?, ?, ?)",
            (9, 'ковидарий', '', '')
            )

cur.execute("INSERT INTO synonyms (post_id, ascriptor, marks, notes) VALUES (?, ?, ?, ?)",
            (9, 'ковид-центр', '', '')
            )

cur.execute("INSERT INTO synonyms (post_id, ascriptor, marks, notes) VALUES (?, ?, ?, ?)",
            (9, 'ковидарня', '', '')
            )

cur.execute("INSERT INTO synonyms (post_id, ascriptor, marks, notes) VALUES (?, ?, ?, ?)",
            (9, 'ковидник', '', ' (в одном из значений)')
            )

cur.execute("INSERT INTO examples (post_id, content, keyword, source) VALUES (?, ?, ?, ?)",
            (9, 'Из всех районов, где есть ковид-госпитали, приезжают к нам волонтеры, сейчас это порядка 32 человек.', 'ковид-госпиталь', 1039)
            )

cur.execute("INSERT INTO examples (post_id, content, keyword, source) VALUES (?, ?, ?, ?)",
            (9, 'По его словам, около 1,5 тыс. коек в ковид-центрах занимают пациенты с внебольничной пневмонией и коронавирусом.', 'ковид-центр', 302)
            )

cur.execute("INSERT INTO examples (post_id, content, keyword, source) VALUES (?, ?, ?, ?)",
            (9, 'Для сотрудника главного ковид-стационара Петербурга это довольно необычный ответ.', 'ковид-стационар', 849)
            )

cur.execute("INSERT INTO examples (post_id, content, keyword, source) VALUES (?, ?, ?, ?)",
            (9, 'С нами она поделилась историей о том, как выстроен процесс лечения в новосибирских ковид-больницах и видео с огромными очередями в МФЦ на площади Труда.', 'ковид-больница', 536)
            )

cur.execute("INSERT INTO examples (post_id, content, keyword, source) VALUES (?, ?, ?, ?)",
            (9, 'Как мне сегодня говорит одна медсестра: «Учителя боятся приходить к моему ребенку, потому что я работаю в ковидарии».', 'ковидарий', 865)
            )

cur.execute("INSERT INTO examples (post_id, content, keyword, source) VALUES (?, ?, ?, ?)",
            (9, 'Я думаю, у нас можно создать дополнительные койко-места путем переноса ковидария в другой корпус — например, в детское отделение.', 'ковидарий', 1250)
            )

cur.execute("INSERT INTO examples (post_id, content, keyword, source) VALUES (?, ?, ?, ?)",
            (9, '<…> был хороший спад. А сейчас опять очереди, открываются «ковидарни» <…>', 'ковидарня', 945)
            )

cur.execute("INSERT INTO examples (post_id, content, keyword, source) VALUES (?, ?, ?, ?)",
            (9, 'Власти Рязанской области запустят в регионе систему подготовки волонтеров для работы на ковид-площадках, в том числе в "красной зоне", где оказывают помощь пациентам с коронавирусом.', 'ковид-площадка', 1039)
            )

cur.execute("INSERT INTO examples (post_id, content, keyword, source) VALUES (?, ?, ?, ?)",
            (9, 'Оба [волонтёры] пошли в ковидник, потому что не могли сидеть на месте.', 'ковидник', 853)
            )

# 10 ковид-диссидент

cur.execute("INSERT INTO posts (descriptor, pos_tag, content, notes) VALUES (?, ?, ?, ?)",
            ('Ковид-диссидент', 'сущ.', 'человек, не верящий в существование вируса COVID-19 либо отрицающий реальную угрозу с его стороны, часто объясняющий пандемию теориями заговора.', '')
            )

cur.execute("INSERT INTO synonyms (post_id, ascriptor, marks, notes) VALUES (?, ?, ?, ?)",
            (10, 'коронаскептик', '', ' (нем. Corona-Skeptiker)')
            )

cur.execute("INSERT INTO examples (post_id, content, keyword, source) VALUES (?, ?, ?, ?)",
            (10, 'Как насчет чипирования и цифровых ошейников, о которых любят рассуждать ковид-диссиденты?', 'ковид-диссидент', 1011)
            )

cur.execute("INSERT INTO examples (post_id, content, keyword, source) VALUES (?, ?, ?, ?)",
            (10, 'По словам Балашова, основная часть "коронаскептиков" приходится на Дальневосточный и Сибирский федеральные округа, это обусловлено прежде всего плотностью населения.', 'коронаскептик', 1090)
            )

# 11 ковидение

cur.execute("INSERT INTO posts (descriptor, pos_tag, content, notes) VALUES (?, ?, ?, ?)",
            ('Ковидение', 'сущ.', 'поведение, не создающее условий для распространения вируса COVID-19 в период пандемии.', '(аббр. «ковид» и «поведение»)')
            )

cur.execute("INSERT INTO examples (post_id, content, keyword, source) VALUES (?, ?, ?, ?)",
            (11, 'В интернете появился новый флешмоб-марафон для семей с детьми на самоизоляции — «Примерное ковидение».', 'ковидение', 1129)
            )

# 12 ковидиот

cur.execute("INSERT INTO posts (descriptor, pos_tag, content, notes) VALUES (?, ?, ?, ?)",
            ('Ковидиот', 'сущ.', 'человек, безрассудно пренебрегающий средствами коллективной и индивидуальной защиты в период распространения коронавирусной инфекции COVID-19.', '(уничиж., ирон.)')
            )

cur.execute("INSERT INTO examples (post_id, content, keyword, source) VALUES (?, ?, ?, ?)",
            (12, 'В самолете было полно эгоистичных ковидиотов и неумелых бортпроводников, которым все равно», — заявила Уитфилд.', 'ковидиот', 1246)
            )

# 13 ковидник

cur.execute("INSERT INTO posts (descriptor, pos_tag, content, notes) VALUES (?, ?, ?, ?)",
            ('Ковидник', 'сущ.', 'человек, страдающий от симптомов COVID-19; пациент ковид-стационара (см. ковид-пациент) или же медицинское (лечебное) учреждение, специально оборудованное и предназначенное для оказания медицинской помощи пациентам с COVID-19 (см. ковид-госпиталь).', '')
            )

cur.execute("INSERT INTO examples (post_id, content, keyword, source) VALUES (?, ?, ?, ?)",
            (13, 'Оба [волонтёры] пошли в ковидник, потому что не могли сидеть на месте.', 'ковидник', 853)
            )

cur.execute("INSERT INTO examples (post_id, content, keyword, source) VALUES (?, ?, ?, ?)",
            (13, 'Разница в цифрах связана с тем, что в одном случае мы считаем чистых ковидников, в другом — все три категории, — сказал Павел Креков.', 'ковидник', 661)
            )

# 14 ковидный

cur.execute("INSERT INTO posts (descriptor, pos_tag, content, notes) VALUES (?, ?, ?, ?)",
            ('Ковидный', 'прил.', 'относящийся к болезни COVID-19, связанный с ней.', '')
            )

cur.execute("INSERT INTO synonyms (post_id, ascriptor, marks, notes) VALUES (?, ?, ?, ?)",
            (14, 'ковидовский', '', '')
            )

cur.execute("INSERT INTO synonyms (post_id, ascriptor, marks, notes) VALUES (?, ?, ?, ?)",
            (14, 'коронавирусный', '', '')
            )

cur.execute("INSERT INTO synonyms (post_id, ascriptor, marks, notes) VALUES (?, ?, ?, ?)",
            (14, 'пандемийный', '', '')
            )

cur.execute("INSERT INTO antonyms (post_id, ascriptor, marks, notes) VALUES (?, ?, ?, ?)",
            (14, 'нековидный', '', '')
            )

cur.execute("INSERT INTO examples (post_id, content, keyword, source) VALUES (?, ?, ?, ?)",
            (14, 'Это учреждение не работает как ковидный госпиталь, однако оказывает амбулаторную помощь больным COVID-19.', 'ковидный', 748)
            )

cur.execute("INSERT INTO examples (post_id, content, keyword, source) VALUES (?, ?, ?, ?)",
            (14, 'В Новосибирске бушует настоящий ковидный ураган', 'ковидный', 88)
            )

cur.execute("INSERT INTO examples (post_id, content, keyword, source) VALUES (?, ?, ?, ?)",
            (14, 'Он также согласился с тем, что ущерб от климатических изменений существенно выше, чем ущерб от ковидовского кризиса.', 'ковидовский', 1002)
            )

cur.execute("INSERT INTO examples (post_id, content, keyword, source) VALUES (?, ?, ?, ?)",
            (14, 'Родителей и педагогов просят выбрать наиболее оптимальные коронавирусные ограничения для школьников.', 'коронавирусный', 1017)
            )

cur.execute("INSERT INTO examples (post_id, content, keyword, source) VALUES (?, ?, ?, ?)",
            (14, 'По словам Макаровой, люди, которые резко реагируют на просьбы соблюдать "пандемийные" правила, в целом склонны воспринимать все "очень личностно".', 'пандемийный', 1124)
            )

# 15 ковидобесие

cur.execute("INSERT INTO posts (descriptor, pos_tag, content, notes) VALUES (?, ?, ?, ?)",
            ('Ковидобесие', 'сущ.', 'кажущиеся гражданам абсурдными или непоследовательными противокоронавирусные меры.', '(негативн., ирон.)')
            )

cur.execute("INSERT INTO examples (post_id, content, keyword, source) VALUES (?, ?, ?, ?)",
            (15, 'В эфире ютуб-канала «День ТВ» доктор экономических наук Михаил Делягин рассказал о причинах «ковидобесия», охватившего мир, а также поделился размышлениями о том, какие глубинные процессы обнаружили себя в сложившейся ситуации и какое будущее уготовано человечеству.', 'ковидобесие', 1247)
            )

# 16 ковид-паспорт

cur.execute("INSERT INTO posts (descriptor, pos_tag, content, notes) VALUES (?, ?, ?, ?)",
            ('Ковид-паспорт', 'сущ.', 'новый официальный документ, выдающийся гражданину, прошедшему вакцинацию любым из зарегистрированных препаратов (в РФ – электронный бланк, формирующийся через портал Госуслуг).', '')
            )

cur.execute("INSERT INTO examples (post_id, content, keyword, source) VALUES (?, ?, ?, ?)",
            (16, 'Такой ковид-паспорт позволит привитым любым препаратом, который одобрило Европейское агентство лекарственных средств, въезжать в страны — члены Евросоюза.', 'ковид-паспорт', 1244)
            )

# 17 ковид-пациент

cur.execute("INSERT INTO posts (descriptor, pos_tag, content, notes) VALUES (?, ?, ?, ?)",
            ('Ковид-пациент', 'сущ.', 'человек, страдающий от симптомов COVID-19; пациент ковид-стационара.', '')
            )

cur.execute("INSERT INTO synonyms (post_id, ascriptor, marks, notes) VALUES (?, ?, ?, ?)",
            (17, 'ковид-больной', '', '')
            )

cur.execute("INSERT INTO synonyms (post_id, ascriptor, marks, notes) VALUES (?, ?, ?, ?)",
            (17, 'ковидник', '', ' (в одном из значений)')
            )

cur.execute("INSERT INTO examples (post_id, content, keyword, source) VALUES (?, ?, ?, ?)",
            (17, 'Тем временем врачи уверены, что рост ковид-пациентов не в последнюю очередь связан именно с антимасочными настроениями.', 'ковид-пациент', 420)
            )

cur.execute("INSERT INTO examples (post_id, content, keyword, source) VALUES (?, ?, ?, ?)",
            (17, 'К примеру, недавно новый стационар для ковид-больных открыли на базе больницы № 40 Автозаводского района.', 'ковид-больной', 1227)
            )

cur.execute("INSERT INTO examples (post_id, content, keyword, source) VALUES (?, ?, ?, ?)",
            (17, 'Разница в цифрах связана с тем, что в одном случае мы считаем чистых ковидников, в другом — все три категории, — сказал Павел Креков.', 'ковидник', 661)
            )

# 18 ковид-положительный

cur.execute("INSERT INTO posts (descriptor, pos_tag, content, notes) VALUES (?, ?, ?, ?)",
            ('Ковид-положительный', 'прил.; сущ. субст.', '(о человеке) получивший положительный результат теста на наличие в организме генома вируса SARS-CoV-2, независимо от наличия характерных симптомов; положительный человек. ', '(негативн., ирон.)')
            )

cur.execute("INSERT INTO synonyms (post_id, ascriptor, marks, notes) VALUES (?, ?, ?, ?)",
            (18, 'положительный', '', '')
            )

cur.execute("INSERT INTO synonyms (post_id, ascriptor, marks, notes) VALUES (?, ?, ?, ?)",
            (18, 'позитивный', '', '')
            )

cur.execute("INSERT INTO antonyms (post_id, ascriptor, marks, notes) VALUES (?, ?, ?, ?)",
            (18, 'отрицательный', '', '')
            )

cur.execute("INSERT INTO antonyms (post_id, ascriptor, marks, notes) VALUES (?, ?, ?, ?)",
            (18, 'негативный', '', '')
            )

cur.execute("INSERT INTO examples (post_id, content, keyword, source) VALUES (?, ?, ?, ?)",
            (18, 'Мне как ковид-положительной 23-я больница (Эльмаш) выдала направление на КТ в амбулаторный центр компьютерной томографии — на 6-й день после результатов теста.', 'ковид-положительный', 646)
            )

cur.execute("INSERT INTO examples (post_id, content, keyword, source) VALUES (?, ?, ?, ?)",
            (18, 'Мне в КТ отказали — окончательного подтверждения еще нет, положительным я не считаюсь.', 'положительный', 645)
            )

cur.execute("INSERT INTO examples (post_id, content, keyword, source) VALUES (?, ?, ?, ?)",
            (18, '<…> пока в России явной эпидемии нет, не нужно ничего заранее поднимать, это контрпродуктивно. Может, имеет смысл это начать делать, когда почувствуете первые признаки заболевания <…> или если точно знаете, что контактировали с позитивным больным.', 'позитивный', 246)
            )

# 19 ковид-сводка

cur.execute("INSERT INTO posts (descriptor, pos_tag, content, notes) VALUES (?, ?, ?, ?)",
            ('Ковид-сводка', 'сущ.', 'объединение показателей заболеваемости и смертности населения от коронавируса в период пандемии COVID-19.', '')
            )

cur.execute("INSERT INTO examples (post_id, content, keyword, source) VALUES (?, ?, ?, ?)",
            (19, 'Бердниковская школа в Тонкинском районе попала во вчерашнюю ковид-сводку ошибочно, на деле образовательное учреждение находится на карантине именно по ОРВИ.', 'ковид-сводка', 1231)
            )

# 20 ковид-тест

cur.execute("INSERT INTO posts (descriptor, pos_tag, content, notes) VALUES (?, ?, ?, ?)",
            ('Ковид-тест', 'сущ.', 'процедура по обнаружению коронавируса SARS-CoV-2 в организме человека или же результат такого исследования, содержащий информацию о наличии/отсутствии генома вируса.', '')
            )

cur.execute("INSERT INTO synonyms (post_id, ascriptor, marks, notes) VALUES (?, ?, ?, ?)",
            (20, 'тест на ковид', '', '')
            )

cur.execute("INSERT INTO synonyms (post_id, ascriptor, marks, notes) VALUES (?, ?, ?, ?)",
            (20, 'ПЦР-тест', '', '')
            )

cur.execute("INSERT INTO examples (post_id, content, keyword, source) VALUES (?, ?, ?, ?)",
            (20, 'А вот вернуться — проблемно: с 12 августа действует правило, по которому все возвращающиеся из-за границы должны сдавать ковид-тест.', 'ковид-тест', 155)
            )

cur.execute("INSERT INTO examples (post_id, content, keyword, source) VALUES (?, ?, ?, ?)",
            (20, 'При наличии направления врача пациенты с подозрением на COVID-19 сдают ПЦР-тест в поликлинике.', 'ПЦР-тест', 935)
            )

# 21 Коронавир

cur.execute("INSERT INTO posts (descriptor, pos_tag, content, notes) VALUES (?, ?, ?, ?)",
            ('Коронавир', 'сущ. собств.', 'зарегистрированный по ускоренной процедуре противовирусный препарат для лечения COVID-19, предназначенный для применения в условиях стационаров.', '')
            )

cur.execute("INSERT INTO examples (post_id, content, keyword, source) VALUES (?, ?, ?, ?)",
            (21, 'Компания получила контракты на 6,2 млн рублей — почти 26% от всех закупок. В петербургские поликлиники она повезет, например, коронавир за 5,5 тыс. рублей.', 'коронавир', 962)
            )

# 22 коронакризис

cur.execute("INSERT INTO posts (descriptor, pos_tag, content, notes) VALUES (?, ?, ?, ?)",
            ('Коронакризис', 'сущ.', 'кризисное состояние мировой экономики, вызванное пандемией COVID-19.', '')
            )

cur.execute("INSERT INTO examples (post_id, content, keyword, source) VALUES (?, ?, ?, ?)",
            (22, 'Коронакризис ударил по всем регионам мира и отраслям глобальной экономики.', 'коронакризис', '29')
            )

# 23 коронафобия

cur.execute("INSERT INTO posts (descriptor, pos_tag, content, notes) VALUES (?, ?, ?, ?)",
            ('Коронафобия', 'сущ.', 'боязнь быть инфицированным коронавирусом SARS-CoV-2.', '')
            )

cur.execute("INSERT INTO examples (post_id, content, keyword, source) VALUES (?, ?, ?, ?)",
            (23, 'Пандемия коронавируса в мире (на настоящий момент более 1 миллиона заболевших) привела к появлению "коронафобии" – страха быть инфицированным.', 'коронафобия', 1252)
            )

# 24 локдаун

cur.execute("INSERT INTO posts (descriptor, pos_tag, content, notes) VALUES (?, ?, ?, ?)",
            ('Локдаун', 'сущ.', 'режим ограничения в свободе передвижения граждан, работе различных учреждений, который вводится государством с целью предотвращения распространения COVID-19.', ' (от англ. lock down – посадить под замок)')
            )

cur.execute("INSERT INTO examples (post_id, content, keyword, source) VALUES (?, ?, ?, ?)",
            (24, 'Общемировой локдаун и вызванный им экономический кризис — результат ошибки в математической модели, который мог быть отнюдь не случайным, считает философ и футуролог Сергей Переслегин.', 'локдаун', 1011)
            )

# 25 масочник

cur.execute("INSERT INTO posts (descriptor, pos_tag, content, notes) VALUES (?, ?, ?, ?)",
            ('Масочник', 'сущ.', 'человек, агрессивно пропагандирующий ношение масок и требующий этого от окружающих.', '')
            )

cur.execute("INSERT INTO antonyms (post_id, ascriptor, marks, notes) VALUES (?, ?, ?, ?)",
            (25, 'антимасочник', '', 'конт. ант.')
            )

cur.execute("INSERT INTO examples (post_id, content, keyword, source) VALUES (?, ?, ?, ?)",
            (25, '– Как будто это не противоборство "масочников" и "антимасочников", а нападение лично на меня, — объясняет психотерапевт. — Тетенька, которая требует надеть маску, просто пользуется обстоятельствами, чтобы ущемить мою свободу.', 'масочник', 1124)
            )

# 26 масочный режим

cur.execute("INSERT INTO posts (descriptor, pos_tag, content, notes) VALUES (?, ?, ?, ?)",
            ('Масочный режим', 'сущ.', 'ограничительная мера, принятая государством для предотвращения распространения COVID-19, включающая в себя обязательство носить медицинскую маску/респиратор и запрет на появление без них в общественных местах.', '')
            )

cur.execute("INSERT INTO examples (post_id, content, keyword, source) VALUES (?, ?, ?, ?)",
            (26, 'Горожане по-прежнему должны соблюдать масочный режим на транспорте и в помещениях организаций.', 'масочный режим', 1014)
            )

# 27 нековидный

cur.execute("INSERT INTO posts (descriptor, pos_tag, content, notes) VALUES (?, ?, ?, ?)",
            ('Нековидный', 'прил.', 'не имеющий отношения к болезни COVID-19, не связанный с ней.', '')
            )

cur.execute("INSERT INTO antonyms (post_id, ascriptor, marks, notes) VALUES (?, ?, ?, ?)",
            (27, 'ковидный', '', '')
            )

cur.execute("INSERT INTO antonyms (post_id, ascriptor, marks, notes) VALUES (?, ?, ?, ?)",
            (27, 'ковидовский', '', '')
            )

cur.execute("INSERT INTO antonyms (post_id, ascriptor, marks, notes) VALUES (?, ?, ?, ?)",
            (27, 'пандемийный', '', '')
            )

cur.execute("INSERT INTO examples (post_id, content, keyword, source) VALUES (?, ?, ?, ?)",
            (27, 'Будут гибнуть от сепсиса, от внебольничных нековидных и невирусных в принципе пневмоний. Нечем будет лечить ангины, остеомиелиты.', 'нековидный', 650)
            )

cur.execute("INSERT INTO examples (post_id, content, keyword, source) VALUES (?, ?, ?, ?)",
            (27, 'По словам начальника госпиталя, бытует мнение, что больницы это рассадники ковида, хотя на самом деле, уверен Кабанов, поступить в нековидный стационар можно с коронавирусом, подцепленным, например, в общественном транспорте.', 'нековидный', 865)
            )

# 28 отрицательный

cur.execute("INSERT INTO posts (descriptor, pos_tag, content, notes) VALUES (?, ?, ?, ?)",
            ('Отрицательный', 'прил.; сущ. субст.', '(о человеке) получивший отрицательный результат теста на наличие в организме генома вируса SARS-CoV-2, независимо от наличия характерных симптомов; отрицательный человек.', '')
            )

cur.execute("INSERT INTO synonyms (post_id, ascriptor, marks, notes) VALUES (?, ?, ?, ?)",
            (28, 'негативный', '', '')
            )

cur.execute("INSERT INTO antonyms (post_id, ascriptor, marks, notes) VALUES (?, ?, ?, ?)",
            (28, 'ковид-положительный', '', '')
            )

cur.execute("INSERT INTO antonyms (post_id, ascriptor, marks, notes) VALUES (?, ?, ?, ?)",
            (28, 'положительный', '', '')
            )

cur.execute("INSERT INTO antonyms (post_id, ascriptor, marks, notes) VALUES (?, ?, ?, ?)",
            (28, 'позитивный', '', '')
            )

cur.execute("INSERT INTO examples (post_id, content, keyword, source) VALUES (?, ?, ?, ?)",
            (28, 'Регистратор время от времени выпускает наружу отрицательных, абсолютно не реагируя на просьбы — сначала сдержанные, потом все более и более возмущённые — запустить людей внутрь.', 'отрицательный', 646)
            )

cur.execute("INSERT INTO examples (post_id, content, keyword, source) VALUES (?, ?, ?, ?)",
            (28, 'Мы были негативны, рожали спокойно.', 'отрицательный', 37)
            )

# 29 постковидный

cur.execute("INSERT INTO posts (descriptor, pos_tag, content, notes) VALUES (?, ?, ?, ?)",
            ('Постковидный', 'прил.', 'связанный с последствиями пандемии в целом или единичного случая болезни COVID-19.', ' (антонимы являются контекстуальными)')
            )

cur.execute("INSERT INTO antonyms (post_id, ascriptor, marks, notes) VALUES (?, ?, ?, ?)",
            (29, 'доковидный', '', 'контекст. ант.')
            )

cur.execute("INSERT INTO antonyms (post_id, ascriptor, marks, notes) VALUES (?, ?, ?, ?)",
            (29, 'докоронавирусный', '', 'контекст. ант.')
            )

cur.execute("INSERT INTO examples (post_id, content, keyword, source) VALUES (?, ?, ?, ?)",
            (29, 'Как показали наблюдения за пациентами, проблемы со здоровьем у переболевших COVID-19 могут возникать и сохраняться еще длительное время. Почитайте, как проявляется постковидный синдром.', 'постковидный', 796)
            )

# 30 Противоковидный

cur.execute("INSERT INTO posts (descriptor, pos_tag, content, notes) VALUES (?, ?, ?, ?)",
            ('Противоковидный', 'прил.', '(о препарате) предназначенный для лечения коронавирусных больных или (о мерах) противостояния распространению вируса SARS-CoV-2.', '')
            )

cur.execute("INSERT INTO synonyms (post_id, ascriptor, marks, notes) VALUES (?, ?, ?, ?)",
            (30, 'антиковидный', '', '')
            )

cur.execute("INSERT INTO synonyms (post_id, ascriptor, marks, notes) VALUES (?, ?, ?, ?)",
            (30, 'антикоронавирусный', '', '')
            )

cur.execute("INSERT INTO examples (post_id, content, keyword, source) VALUES (?, ?, ?, ?)",
            (30, 'Его представители начали фигурировать в многочисленных противоковидных конструкциях, которые в изобилии создавал Смольный.', 'противоковидный', 1013)
            )

cur.execute("INSERT INTO examples (post_id, content, keyword, source) VALUES (?, ?, ?, ?)",
            (30, 'Современное высокотехнологичное производство будет выпускать 100 видов фармацевтических субстанций, включая противоковидные, без закупки импортных компонентов.', 'противоковидный', 636)
            )

cur.execute("INSERT INTO examples (post_id, content, keyword, source) VALUES (?, ?, ?, ?)",
            (30, 'Применение антиковидной плазмы сейчас — это практически терапия отчаяния, которая показана тяжелым пациентам.', 'антиковидный', 1082)
            )

cur.execute("INSERT INTO examples (post_id, content, keyword, source) VALUES (?, ?, ?, ?)",
            (30, 'Журналист Ая Шафран на израильском опыте рассказывает, как антиковидные меры помогают победить эпидемию и как резкий выход из карантина преподносит неприятные сюрпризы.', 'антиковидный', 724)
            )

cur.execute("INSERT INTO examples (post_id, content, keyword, source) VALUES (?, ?, ?, ?)",
            (30, 'Тем временем Владимир Путин подписал пачку «антикоронавирусных» законов.', 'антикоронавирусный', 557)
            )

# 31 самоизолироваться

cur.execute("INSERT INTO posts (descriptor, pos_tag, content, notes) VALUES (?, ?, ?, ?)",
            ('Самоизолироваться', 'гл.', 'изолировать себя в целях предотвращения распространения COVID-19.', '')
            )

cur.execute("INSERT INTO examples (post_id, content, keyword, source) VALUES (?, ?, ?, ?)",
            (31, 'В связи со вспышкой всем путешественникам рекомендовали самоизолироваться на две недели.', 'самоизолироваться', 1246)
            )

# 32 самоизоляция

cur.execute("INSERT INTO posts (descriptor, pos_tag, content, notes) VALUES (?, ?, ?, ?)",
            ('Самоизоляция', 'сущ.', 'комплекс ограничительных мер, направленных на реализацию самостоятельной изоляции населения или отдельных лиц в целях предотвращения распространения COVID-19.', '')
            )

cur.execute("INSERT INTO examples (post_id, content, keyword, source) VALUES (?, ?, ?, ?)",
            (32, 'Какие ограничения введены для граждан? — Действует обязательная самоизоляция для людей старше 65 лет и людей, страдающих хроническими заболеваниями (перечень установлен комитетом по здравоохранению). ', 'самоизоляция', 1015)
            )

# 33 санитайзер

cur.execute("INSERT INTO posts (descriptor, pos_tag, content, notes) VALUES (?, ?, ?, ?)",
            ('Санитайзер', 'сущ.', 'антисептическое средство для гигиены рук, созданное на основе спирта, используемое для дезинфекции в тех случаях, когда нет доступа к мылу или воде или некоторая ёмкость, содержащая такое средство.', '')
            )

cur.execute("INSERT INTO examples (post_id, content, keyword, source) VALUES (?, ?, ?, ?)",
            (33, 'Диалог происходит быстро. — Имя, фамилия, время записи на компьютерную томографию, указание на бахилы, перчатки и санитайзер.', 'санитайзер', 643)
            )

cur.execute("INSERT INTO examples (post_id, content, keyword, source) VALUES (?, ?, ?, ?)",
            (33, 'На входе также стоит санитайзер, которым можно и нужно обработать руки.', 'санитайзер', 1251)
            )

# 34 социальная дистанция

cur.execute("INSERT INTO posts (descriptor, pos_tag, content, notes) VALUES (?, ?, ?, ?)",
            ('Социальная дистанцция', 'сущ.', 'мера, предпринимаемая для предотвращения распространения COVID-19, включающая в себя обязательство держать расстояние между собой и другими людьми в общественных местах, минимальное рекомендованное значение которого 1,5 м.', '')
            )

cur.execute("INSERT INTO synonyms (post_id, ascriptor, marks, notes) VALUES (?, ?, ?, ?)",
            (34, '(социальное) дистанцирование', '', '')
            )

cur.execute("INSERT INTO examples (post_id, content, keyword, source) VALUES (?, ?, ?, ?)",
            (34, 'В краевом минобре пояснили, что во время занятий педагоги могут не надевать маски, так как в классе соблюдается социальная дистанция.', 'социальная дистанция', 442)
            )

cur.execute("INSERT INTO examples (post_id, content, keyword, source) VALUES (?, ?, ?, ?)",
            (34, 'Но на этот прогноз могут оказать негативное влияние несоблюдение рекомендованных профилактических мер (масочный режим, социальное дистанцирование, гигиена рук) <…> .', 'социальное дистанцирование', 1101)
            )

cur.execute("INSERT INTO examples (post_id, content, keyword, source) VALUES (?, ?, ?, ?)",
            (34, 'Напомним, что в Роспотребнадзоре призывают нижегородцев не паниковать, а ответственно соблюдать дистанцирование и не пренебрегать СИЗами.', 'дистанцирование', 1241)
            )

# 35 Спутник

cur.execute("INSERT INTO posts (descriptor, pos_tag, content, notes) VALUES (?, ?, ?, ?)",
            ('Спутник V', 'сущ. собств.', 'зарегистрированная российская вакцина, разработанная для профилактики новой коронавирусной инфекции COVID-19.', '')
            )

cur.execute("INSERT INTO synonyms (post_id, ascriptor, marks, notes) VALUES (?, ?, ?, ?)",
            (35, 'Гам-КОВИД-Вак', '', '')
            )

cur.execute("INSERT INTO examples (post_id, content, keyword, source) VALUES (?, ?, ?, ?)",
            (35, 'Напомним, первой зарегистрированной вакциной от коронавируса стал российский препарат «Спутник V» Центра имени Гамалеи.', 'Спутник V', 328)
            )

cur.execute("INSERT INTO examples (post_id, content, keyword, source) VALUES (?, ?, ?, ?)",
            (35, 'Вакцина от коронавируса — «Гам-КОВИД-Вак», разработанная в институте Гамалеи, уже используется в нашем регионе, но пока её ставят только сотрудникам инфекционных госпиталей и врачам.', 'социальное дистанцирование', 18)
            )

# 36 Стопкоронавирус.рф

cur.execute("INSERT INTO posts (descriptor, pos_tag, content, notes) VALUES (?, ?, ?, ?)",
            ('Стопкоронавирус.рф', 'сущ. собств.', 'основной правительственный информационный ресурс в Российской Федерации, на котором можно узнать подробную информацию про Коронавирус COVID–19, его симптомы, меры профилактики, возможность сдачи анализов, вакцинацию и многое другое.', '')
            )

cur.execute("INSERT INTO examples (post_id, content, keyword, source) VALUES (?, ?, ?, ?)",
            (36, 'Правительство РФ запустило ресурс стопкоронавирус.рф для информирования о ситуации в стране.', 'стопкоронавирус.рф', 1159)
            )

# 37 ЭпиВакКорона

cur.execute("INSERT INTO posts (descriptor, pos_tag, content, notes) VALUES (?, ?, ?, ?)",
            ('ЭпиВакКорона', 'сущ. собств.', 'синтетическая пептидная вакцина против COVID-19, разработанная ФБУН «Государственный научный центр вирусологии и биотехнологии „Вектор“ Роспотребнадзора» в г. Новосибирск.', '')
            )

cur.execute("INSERT INTO examples (post_id, content, keyword, source) VALUES (?, ?, ?, ?)",
            (37, 'Все те изменения, которые мы констатируем в настоящее время, <...> тем более не способны ускользать от иммунитета, который формируется с помощью нами разработанной вакцины «Эпиваккорона», — цитирует ТАСС Максютова.', 'эпиваккорона', 1082)
            )

# ТАБЛИЦА С ТЕКСТАМИ

csvfile = open("C:/Users/sofia/PycharmProjects/txt_csv/metadata.csv", encoding="utf-8")
metadata = []
for line in csvfile:
    meta = line.split(',')
    metadata.append(meta)
for d in range(1, 1251):
    file_name = 'C:/Users/sofia/PycharmProjects/txt_csv/{}.txt'.format(d)
    with open(file_name, 'r', encoding='utf-8') as f:
        text = f.read()
        f.close()
        cur.execute("INSERT INTO texts (title, link, date, content) VALUES (?, ?, ?, ?)",
                    (metadata[d][4], metadata[d][1], metadata[d][2], text)
                    )

connection.commit()
connection.close()