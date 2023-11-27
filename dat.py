#!/usr/bin/env python3
import os
from aiogram import Bot, Dispatcher, types, executor
import random

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot)

programming_facts = [
    "Kamil, [26.11.2023 15:37] Салам ЮЧ, сам поставил каждый синт, сам писал текст, сам собрал всех) https://disk.yandex.ru/d/gxfF3Ygb7Bqvzg",
"Саша Пайро, [26.11.2023 15:41] https://drive.google.com/file/d/1ZhyrGMrk1gnnNAmsufWvGBmAozv-PHd7/view?usp=drivesdk",
"лёня, [26.11.2023 15:46] https://drive.google.com/drive/folders/1F2afgMalARJIq1uKVAcRw8rBtg7wGhMR",
"Дима Берг, [26.11.2023 15:47] REALBERG - 1000 (prod by uluwa) https://drive.google.com/file/d/1u3oGsQlxCfb7Ueu5EBPmNWHVs8oiWm5J/view?usp=drivesdk",
"@SUFANO, [26.11.2023 15:49] Салам из Города Актау летит 104, команде, и вне очередной прослушке. Рады представить на заценон 2 демки от Dresskod, Sufano. Надеюсь вас качнет. Приятной прослушки! https://drive.google.com/file/d/1iPM47iK9ZpAa3WH9-UsuHqGWbZKDJZK-/view?usp=drivesdk https://drive.google.com/file/d/1ViM4BLSz-54awCTAzyYUAbWCMW9re3I2/view?usp=drivesdk",
"dim.mai, [26.11.2023 15:50] https://disk.yandex.ru/d/Zc2nQFQna2DM0w",
"Luka Andolini, [26.11.2023 15:51] https://disk.yandex.ru/d/ceRuIqhTYDkwJA",
"🥷🏻🥷🏻🥷🏻, [26.11.2023 15:52] салам пацанам из тулы - мс балаклава музон из подвала https://disk.yandex.ru/d/lPYXLvscbG3wPg https://disk.yandex.ru/d/Gh7l7e2Bp9lUYA",
"✖, [26.11.2023 15:53] Файл можно получить по ссылке: say_do - веселье .mp3 https://disk.yandex.ru/d/R1vFi6z8d0sOmw",
"WhereIGo, [26.11.2023 15:58] Салют! Хочу поделиться тречком душевным Чисто сторитейлинг одного года https://disk.yandex.ru/d/I-4biH0rwiwplw",
"ⱽᶦᶰᶜʰᵉˢᵗᵉʳ ᵀᵒᶰʸ🥂, [26.11.2023 16:03] https://disk.yandex.ru/d/65o2SoUkeq_XPQ",
"NI, [26.11.2023 16:04] https://disk.yandex.ru/d/2S5AUUcivuVVhg",
"QAZQYR, [26.11.2023 16:04] https://drive.google.com/file/d/1ijGyjnF7JejkPC-IlYD4rq5spYDXt5gQ/view?usp=drivesdk",
"IVENTON, [26.11.2023 16:04] https://disk.yandex.ru/d/jiaxy853qeuQ7w",
"Armless Beats, [26.11.2023 16:08] https://disk.yandex.ru/d/NlTi7zN5DDw5_Q",
"Макс, [26.11.2023 16:08] https://t.me/c/1927820636/44 Спортикам✊",
"koper, [26.11.2023 16:17] https://on.soundcloud.com/Y7LJcQUWVDHKST9S9",
"Han Darksaid, [26.11.2023 16:19] https://www.youtube.com/watch?v=woEoUxOxGNs",
"Smoke Cry, [26.11.2023 16:24] https://drive.google.com/drive/folders/1PjQgUQj3vK2G9HVBZMsFHQEfc4QGUi9N?usp=sharing",
"Owen, [26.11.2023 16:28] https://drive.google.com/drive/folders/19IyELOzp6tCtUgeir6dEmgaorEJHUR3Q",
"Fox_kid_izlesa🦊 VOSSEN❤️‍🔥🎸🎬, [26.11.2023 16:29] https://cloud.mail.ru/public/ViKs/f3E7ArYbt ИЗ ВЛАДИКАВКАЗА С ЛЮБОВЬЮ",
"Adil’, [26.11.2023 16:39] https://youtu.be/-q4B_qRmhUY?si=LSzdTnUE85NHpRl4",
"Rustam Khisamutdinov, [26.11.2023 16:41] XMVPX Татарстан ✌️ PULYA https://drive.google.com/file/d/1XjW4Gjv61fYE_uUQ-1CEzEIo7rRvZX8k/view?usp=drivesdk Eclipse https://drive.google.com/file/d/1Xg9crxOVuuFC-GpGhxkhOOVKXa9WGaoO/view?usp=drivesdk",
"sáirus, [26.11.2023 16:41] https://drive.google.com/drive/folders/1WxGHmgukxzud20dWWxluJXkPS_MdCz-d салам)",
"сплю, [26.11.2023 16:48] https://disk.yandex.com.am/d/r331ECBBgcCLZg Хорошая демочка пред релиз на биточек карусели Парижа",
"east side champ, [26.11.2023 17:07] с Уралмаша салам! спасибо вам за движуху! это демки https://drive.google.com/drive/folders/1ngx8GQSFkGmvu392hQs9GytKlbTi4iK7",
"Karma, [26.11.2023 17:07] Приветствую всех присутствующих. Вот такие композиции приготовлены спасибо. 0482 https://drive.google.com/drive/folders/191ktR5Ufha95ThGsPnqx43dA36XLavFM?usp=sharing",
"Aleksei OUTSIDE G, [26.11.2023 17:22] Челябинск, Махачкала и Донецк передают салам и желают приятного прослушивания 🙌 https://disk.yandex.ru/d/Kj4ZyzzcZj0HEQ",
    "., [26.11.2023 17:35] Восап, я Kampit с Кокш, прошлый раз скидывал вам демку смотрю вас качнуло, в этот раз на Казахском, весёлый, вайбовый трэк, надеюсь оцените 🥩 https://disk.yandex.ru/d/uoWf3WZULEhZZQ",
    "Valhalla, [26.11.2023 17:49] https://disk.yandex.ru/d/bOwsND8Arw12jQ",
    "Mergenov Shyngys, [26.11.2023 17:50] Салам из ускамана",
    "hleborobny, [26.11.2023 17:54] https://disk.yandex.ru/d/C7c71IOlhVaDyQ Зацените,музло и тексты пишу сам 🙌🏻",
    "rusbekov, [26.11.2023 17:56] в темноте.mp3: https://disk.yandex.ru/d/daKW5zk_rIXjgw",
    "тхаурмале, [26.11.2023 17:58] Саламчесы с Казани! треки на выбор: Эй здарова - ты в чате слышал мельком, тебе зашло Ода - вчера делал, лирика Батыр - классика рэпа от урмале https://drive.google.com/drive/folders/1-1uZKJlguvKILtU3VqbuYAXFoHMQKIFQ",
    "Алим Кусатай, [26.11.2023 18:21] https://t.me/twenty_fifthframe/89",
    "taratu.black, [26.11.2023 18:32] https://disk.yandex.kz/d/uKtwEZuoaLavJA salam) 7212 TU",
    "Mag, [26.11.2023 18:42] Огромный салам алейкум 🤝 У кентишки скоро выходит два трека на площадки Интересно узнать вашу оценку Ник - xolod Приятного прослушивания Новых творческих успехов вам ✊ Первый трек https://disk.yandex.kz/d/0SNnr33sO9-eVg Второй трек дарк версия https://disk.yandex.kz/d/-QV31GDTyt_Yqw",
    "Ask, [26.11.2023 18:42] Салам Юрчик отправляю мудвидео для прослушки🙏🏽 Трек уже вышел на площадках, тебе добра и рахмат что делаешь такой формат 👍 https://youtu.be/J9bd1hPmEvI?si=fCMQ1fm5ifkHA3nM",
    "Mergenov Shyngys, [26.11.2023 18:45] https://youtu.be/7U6tc4gpF0I?si=PMMK5Miv26z6qCIv",
    "R S, [26.11.2023 18:53] Всем хай. Я старый, но начинающий музлодел. 104 и Ко прошу на зацен. Критика и провоз мордой по ошибкам приветствуется тепло. Всем добра и успехов! https://drive.google.com/file/d/10ldX6pYprBzElbJ3ZX6LY2IErM9Djqss/view?usp=drivesdk",
    "Sadline, [26.11.2023 19:25] https://t.me/c/1372529032/33",
    "Mergenov Shyngys, [26.11.2023 19:34] https://t.me/samsomode/200 https://youtu.be/7U6tc4gpF0I?si=PMMK5Miv26z6qCIv салам из ускамана",
    "tawsogar, [26.11.2023 20:17] https://www.youtube.com/watch?v=AmIvEux4nTE&ab_channel=melonemes всем салам, зацените джерси ремикс",
    "jonquil, [26.11.2023 21:01] Всем привет! Меня зовут Генри, я битмейкер из Алматы, на данный момент живу в Вене. Пытаюсь искать свой уникальный звук. Приятного прослушивания 🫶 https://disk.yandex.ru/d/3TDlT7e553BcZg",
    "Никодим, [26.11.2023 22:23] https://youtu.be/jYs50iPEdrI?si=incna4xUu-IB8cw3",
    "Богдан Прайс, [26.11.2023 22:29] Всем салам! Приятного прослушивания. Cлушать с 1:16. https://disk.yandex.com/d/JlRH-nEQlUxbzA",
    "Triple Slash, [26.11.2023 22:46] https://disk.yandex.ru/d/QZgSmsvvSy1pPA",
    "(@), [26.11.2023 22:52] БРАТ, ПРОШУ ПОСЛУШАЙ татарская мафия! Я артист из Московской области, но родился в Уфе! На данный момент экспериментирую со звуком и флоу, очень интересно что скажешь! https://disk.yandex.ru/d/s8OdfAjEjxWQTg",
    "B., [26.11.2023 23:20] https://disk.yandex.ru/d/LaKQBAe0_pdzTg",
    "creamybenzz, [26.11.2023 23:30] https://disk.yandex.ru/d/EUtv5jjAfAsivw продюсер с костаная, работал с жак энтони, may waves, 4n way, project x",
    "Бейбарыс, [26.11.2023 23:38] 7292 https://disk.yandex.ru/d/SsKRUGf7tpHfOA",
    "Evan, [27.11.2023 1:23] Привет https://drive.google.com/drive/folders/14V9d6-3clkp9pgtFlolkF-EE3F2n8WOy?usp=sharing",
    "VRMYVN012, [27.11.2023 2:59] Вассап Юрчик, мира и позитива твоей команде. Меня зовут Ренат, я родом из Сочи, пишу музыку около 5-ти лет. Надеюсь попаду к вам на прослушку, очень хочется услышать профессиональное мнение! \
        буду признателен если прослушаете от начала жо конца так как лучше уловите мысль песни. Благодарю за то, что вы снимаете такой формат❤️❤️ https://drive.google.com/file/d/1Ka1ypJwW0qduY6EGKdgxEWV5TSao58cA/view?usp=drivesdk",
    "dxctxr, [27.11.2023 3:41] https://drive.google.com/drive/folders/19iqmc8MXLAAVfOfiiC_eIi9fN2oqs7ty",
    "Ник Ждан, [27.11.2023 3:56] Даров Юрец холодец куловой прослушки парни https://disk.yandex.ru/d/pbs_M8L5PtRM0Q",
    "милиан факсуприм, [27.11.2023 4:46] По названию можно понять под каким состоянием был записан трек (девочки пишите поможем друг другу!😉😉😉) https://drive.google.com/file/d/18yb3JFak_rKh6k7I8TYAldv3nEHU3Q9c/view?usp=drivesdk",
    "Gary Choi, [27.11.2023 6:02] Салам алейкум 104 из ста четырех, это трек с Ер 'Дом с маяком' который выйдет в декабре. Пс Душа бр https://drive.google.com/file/d/13HMhtHMi-It8jABwhe5SYdQnpwPVn9jm/view?usp=drivesdk",
    "Anton Alekseev, [27.11.2023 9:37] Салам с Алтая https://music.yandex.ru/album/28182535/track/119192171",
    "Luca Changretta, [27.11.2023 13:34] здравствуй Юра! зацени старого! Listen to OSA - ДАЛЬШЕ by RealOSA on #SoundCloud https://on.soundcloud.com/dcFrW",
    "Askhat Turmenov, [27.11.2023 13:54] Саламалейкум всем. На оценку, стоит ли выпускать на площадки? Бит мой. https://drive.google.com/file/d/1CIwNsjn684q6WPAftGi6KSHXbd2ApbYh/view?usp=drive_link",
    "KUZM111N, [27.11.2023 16:21] https://disk.yandex.ru/d/NrT4rMax4Tt3Mw",
    "Pappa Juicy, [27.11.2023 17:43] Салам Юра, надеюсь на этот раз бот увидит, содержание чуток жестковатое вообщем грязный уличный бум бэп. https://disk.yandex.ru/d/b2qMlMuKTdT9tg",
    "Валёк Валёк, [27.11.2023 19:40] Всем салам послушайте.wav - Google Диск https://drive.google.com/file/d/1C8e0XQtt7j3EVYnYnODDkWdNKPffr32R/view",
    "Артем, [27.11.2023 20:46] Всем доброго дня, от души за творчество ❤️ Скидывал трек, Юра, ты говорил его свести, что я почти сразу и сделал ахах, вам тогда с Dequine прям зашел трек, ей прям очень! https://disk.yandex.ru/d/tYsoKzbzQ4M80Q",
    "subad imir, [27.11.2023 21:02] https://drive.google.com/drive/folders/1-8AsLJiErDqWYcbBzOJxlX06Omh01RVY",
    "Богдан Прайс, [27.11.2023 21:13] Салам, стрим, 104ый, 208ой. Всем приятного прослушивания. https://disk.yandex.com/d/seiuM00M1exwRw",
    "Даня, [27.11.2023 23:15] https://instagram.com/i.w.w07?igshid=OGQ5ZDc2ODk2ZA==",
    "Кто?, [28.11.2023 0:29] Юра здорова 1859 https://drive.google.com/file/d/1Ww06Px4ZlDoAzkdw0KQnIHL66ABFH6ch/view?usp=drivesdk",
    "Данил Дудко, [28.11.2023 0:55] https://youtu.be/cMmX4qz-rbU?si=kTgyZ0jMWz_9Wxfx",
    "Александр Адамский, [26.11.2023 14:35] https://drive.google.com/file/d/17IWfB7DKSQ7zdi_SSWf6mb5pkSc_65IJ/view?usp=sharing",
    "Yamal, [26.11.2023 14:35] https://drive.google.com/drive/folders/1waKxkAUs44WEKwdhyH6RIiwbrTzJ3JxO",
    "llll, [26.11.2023 14:35] https://disk.yandex.ru/d/shNG6BLsMYMObg Салам 👋🏻 Демочка хочет оценочку",
    "4Outdoor, [26.11.2023 14:36] Салам всем! Респект всем! 4Outdoor на связи 🤲Братишка Кодексиплагг залетел на фит , вот демка , тречок будет называться HASTLA mode . 40 Калуга салам. От души за оценочку ребят https://disk.yandex.ru/d/gd2WIKsNy5mxJA",
"IVENTON, [26.11.2023 14:36] https://disk.yandex.ru/d/8KY58EYjl-baJg",
   "Egor, [26.11.2023 14:37] https://drive.google.com/drive/folders/1yCy3jnJ0n610mYI_-3uJnn7U2Z64jgg3?usp=sharing",
   "Самат, [26.11.2023 14:38] Салям из Астаны Юрик и Даник и отдельно салам Данику NP3.player)) https://drive.google.com/file/d/11XAHJpKDQea9pKjGiWQcEvKbDohVaOxz/view?usp=drivesdk",
   "Magzhan Goi, [26.11.2023 14:38] https://drive.google.com/drive/folders/12a0DCZLrqd-xbncJcvOya_uUGKh_FoU6",
   "NiGHT, [26.11.2023 14:39] https://vk.com/wall-96382224_302",
   "Vadik, [26.11.2023 14:40] https://disk.yandex.ru/d/sL3sNB0ALey9cg",
   "T N, [26.11.2023 14:40] https://drive.google.com/drive/folders/1-BMzAY7N2q8KpwYUlqMoiyrQN0-Z1tJ_",
   "Daniyar Kamin, [26.11.2023 14:41] https://disk.yandex.ru/d/NIhnyAeGwzm_uw",
   "Sonicx, [26.11.2023 14:41] https://drive.google.com/file/d/1bN3o21ylhw6lEai1xnffTOJohfomUWaG/view?usp=drivesdk",
  "DD, [26.11.2023 14:41] https://disk.yandex.ru/client/disk",
  "4Outdoor, [26.11.2023 14:41] https://disk.yandex.ru/d/gd2WIKsNy5mxJA",
    "ᅠ ᅠ, [26.11.2023 14:42] Передаю всем пламенный салам из Сибири, а конкретнее Иркутск. Давно слушаю Юр тебя, нравится твоё творчество,первый раз решил в таком поучаствовать , не на что особо не расчитываю. https://disk.yandex.ru/d/yn2P6hjO5aCfYQ",
    "aaizawa, [26.11.2023 14:42] https://youtu.be/2TSGq7nAVoM?si=yRu5BxT79laZMmwV",
    "Viktor Slay, [26.11.2023 14:42] https://disk.yandex.ru/d/RLJzCVgeSM91PQ",
    "aaizawa, [26.11.2023 14:42] https://youtu.be/yeuzNGvaH3M?si=2yxU84BrqWJm0Xhl",
    "DEWENSOON DEWENSOON, [26.11.2023 14:44] Сто лет уже не попадал https://youtu.be/--jVS28sxU",
    "сплю, [26.11.2023 14:44] Первый офф дроп , жду мнения и оценки !) https://music.yandex.ru/album/27494857",
    "алик янгчен, [26.11.2023 14:44] https://vk.com/music?z=audio_playlist-197915572_8&access_key=4d6f25f4c5cbe93905",
    "Ваня, [26.11.2023 14:45] https://disk.yandex.ru/d/qr4YoxZEK2yC_A",
    "(@), [26.11.2023 14:47] БРАТ, ПРОШУ ПОСЛУШАЙ татарская мафия! Я артист из Московской области, но родился в Уфе! На данный момент экспериментирую со звуком и флоу, очень интересно что скажешь! https://disk.yandex.ru/d/s8OdfAjEjxWQTg",
    "Bislan, [26.11.2023 14:47] https://disk.yandex.ru/d/VGfAkbMIjPJsGA",
    "Богдан Прайс, [26.11.2023 14:48] https://disk.yandex.com/d/seiuM00M1exwRw",
    "Jesse Crystal's, [26.11.2023 14:48] Всем ку, приятного прослушивания господа https://drive.google.com/drive/folders/1evJPhYGjCH992-1Kljoh7E_enIJzI_LY",
    "Ильяс, [26.11.2023 14:48] https://drive.google.com/file/d/1r47BfArLGB1wTIyf5kcs9LQWo6ZEL8xB",
    "Салам, Юрчику и всем пацанам, вот он трапчик Кз Madiyar Sovetbay, [26.11.2023 14:49] https://drive.google.com/file/d/1teb7tWeqYXZhSu5AesBRVIlKQzDOkgfs/view?usp=drivesdk",
    "izokon1312, [26.11.2023 14:49] Салют из холодного Питера https://disk.yandex.ru/client/disk/Izokon?idApp=client&dialog=slider&idDialog=%2Fdisk%2FIzokon%2F1.izokon-s%20pritona%20.mp3 https://disk.yandex.ru/client/disk/Izokon?idApp=client&dialog=slider&idDialog=%2Fdisk%2FIzokon%2F2.izokon-ruki%20na%20rule.mp3",
    "Yoshi, [26.11.2023 14:49] Общий салам из северной Карелии! Юра, большой респект тебе за Сафари, за Беквудс, да и вообще ты хороший парень! Заряженного стрима без базы! Кидаю бит и сразу же ремикс Платины на этот бит. Какую версию захотите, ту и включайте. Ну и если уж сильно зайдет, на всякий случай еще биток закинул допом (саксофончик залетает). Ремикс: https://drive.google.com/file/d/1PLp5hTXPXx8oMs0doNzmrKh02DE9owr1/view?usp=drive_link Бит: https://drive.google.com/file/d/1gdIYvf-XkQxVLgemT5-cs4D1i75555xE/view?usp=drive_link 2й бит: https://drive.google.com/file/d/1q9ma7RGJQCTWaE-tYJwL13_3hl3Dyc7q/view?usp=sharing",
    "maikl, [26.11.2023 14:50] https://drive.google.com/file/d/1h4aMwYozXZpnh4tFw3fus8DJfqGd8qam/view?usp=sharing",
    "тхаурмале, [26.11.2023 14:50] Саламчесы с Казани! треки на выбор: Эй здарова - ты в чате слышал мельком, тебе зашло Ода - вчера делал, лирика Батыр - классика рэпа от урмале https://drive.google.com/drive/folders/1-1uZKJlguvKILtU3VqbuYAXFoHMQKIFQ",
    "Кто?, [26.11.2023 14:51] Здарова Юра 1859 https://drive.google.com/file/d/1s3amW9DtI6Qm8zvkbzRUi-WrdgLkzmKt/view?usp=drivesdk",
    "Qoqs arasynda Koks, [26.11.2023 14:55] https://disk.yandex.ru/d/TfCP9pxevR5zug",
    "caraaaas, [26.11.2023 14:56] https://disk.yandex.ru/d/2SwKto8beIPAsg",
    "black, [26.11.2023 14:58] https://cloud.mail.ru/public/ynAv/BN6Z8AVKj",
    "Rubirocks, [26.11.2023 14:59] https://drive.google.com/file/d/1tbaexWxyaNDnhEM1UnYqMUK2_mbSQSqL/view?usp=drivesdk",
    "Jordan, [26.11.2023 15:01] https://www.dropbox.com/scl/fo/nfxwee3lyrcwuk5y3s012/h?rlkey=pkms7jmyusjywobm7fdg9jzqh&dl=0",
    "Бейбарыс, [26.11.2023 15:01] дальный родственник соседа Боба Марли https://disk.yandex.ru/d/qiWGzv1M3mj1Ww",
    "XVIIVVEEl, [26.11.2023 15:02] https://drive.google.com/drive/folders/1tu270IFAk7PhdCyG2T978Wfs6A4yfG0i",
    "... артём🖤, [26.11.2023 15:06] https://www.dropbox.com/scl/fi/az8cwzy4fhzs9ettj9zuv/taknenado.mp3?rlkey=d7darcv3h6enbox4oxfzcc4mh&dl=0",
    "Planetassaturn, [26.11.2023 15:08] https://disk.yandex.ru/d/oDtW3ldh7a7Kyg",
    "J, [26.11.2023 15:09] https://disk.yandex.ru/d/26QXIBlb5D4eqg",
    "Egor Skryabov, [26.11.2023 15:13] Пламенный салам с г.Владимир https://disk.yandex.ru/d/EO6_KpAvishjMQ https://disk.yandex.ru/d/ZFs_VgYTeUQsKw",
    "Саша Пайро, [26.11.2023 15:13] https://drive.google.com/file/d/1ZhyrGMrk1gnnNAmsufWvGBmAozv-PHd7/view?usp=drivesdk",
    "sol, [26.11.2023 15:14] https://disk.yandex.kz/d/NUcsYCwfm_ZOTw",
    "A B, [26.11.2023 15:19] https://drive.google.com/file/d/1VQXB1lTD9ghHNu8jMYnvhTM9NCh4cibb/view?usp=drivesdk",
    "Саша Пайро, [26.11.2023 15:19] https://drive.google.com/file/d/1ZhyrGMrk1gnnNAmsufWvGBmAozv-PHd7/view?usp=drivesdk",
    "wholazybone, [26.11.2023 15:23] салют, на прошлом стриме вроде неплохо оценили, вот еще, всё сам писал) https://disk.yandex.ru/d/a8EQEdWuRAxh5A",
    "Андрей Герасёв, [26.11.2023 15:25] Салам, оуджей индастриз как всегда здесь )) такой репчик послушаем ? https://disk.yandex.ru/d/jNq0kyQYDS1Bsg",
    "GARTMI, [26.11.2023 15:28] Салют, я Gartmi🎙️ https://disk.yandex.ru/d/0F4hAX1-8BW8yQ",
    "L, [26.11.2023 15:32] Привет, Юра! https://disk.yandex.ru/d/Q8KgFeUjaSON_g (https://t.me/liura24)",
    "Vincenzo, [26.11.2023 14:31] Салют из Омска. Немного джаза и в целом жанрового разнообразия 🫡 https://music.yandex.ru/album/27085924 https://disk.yandex.ru/d/oLhIXwLsoav3uA",
    "D), [26.11.2023 14:31] https://disk.yandex.ru/d/dMawbonACqSwmw САЛАМАЛЕЙКУУММММММ 104444",
    "jjershsk, [26.11.2023 14:31] Юра, здравствуй Трек о новых этапах в жизни каждого Продакшн полностью мой) Интересно твое мнение Алга Казахстан https://drive.google.com/drive/u/1/folders/1416XRAphp-f8XPrxKcBInxePAnfOroDY",
    "Вова, [26.11.2023 14.31] https://www.youtube.com/watch?v=1wRmOEYXZ0Q",
    "Alikhan Bekbayev, [26.11.2023 14.31] https://disk.yandex.ru/d/EpYzUl0UCtuCdg",
    "meis, [26.11.2023 14.31] Ассаламуалейкум с Астаны https://on.soundcloud.com/TvfHPXse3SysAQRj6",
    "goat goatovich 🐐, [26.11.2023 14.31] https://music.yandex.ru/album/26236705?utm_medium=copy_link",
    "Әне Міне, [26.11.2023 14.31] https://disk.yandex.ru/d/PO2XZZgSCiDYng",
    "Kyoma, [26.11.2023 14.31] Привет от Vugiy, готовлю сейчас альбом, второй тречок как аутро к нему https://disk.yandex.ru/d/zdv9fpZCN82zZg https://disk.yandex.ru/d/_SD9W1gOTDckEw",
    "Андрей Курс, [26.11.2023 14.31] https://drive.google.com/drive/folders/1-0d26oEWhhQn_NYDXmi8sDSzwAzajUVW?usp=drive_link",
    "Адиль Бисенов, [26.11.2023 14.31] https://youtu.be/4WvEftgk44k?si=MFxOnWERREx3EtQ_",
    "OG, [26.11.2023 14.31] https://drive.google.com/drive/folders/1-asUHG_wbWzvZ6E6DrKwJ36B68KVqr3A Салам из Алматы! KUPRIY текста и исполнение",
    "мадияр, [26.11.2023 14.31] Салют https://drive.google.com/file/d/1Wryvsau1m_zSbr8Ii6edK4PuijrGFuQA/view?usp=drive_link",
    "игорь 👁👁, [26.11.2023 14.31] https://drive.google.com/file/d/11tSFHvOYQIW4yplhl4_v2Omr0mK2JJY-/view?usp=sharing",
    ".. 🍃, [26.11.2023 14.31] Салам от Вити Бульбаша Алмата на связи Решил разбавить прослушку другим стилем. Отрывок из демочки https://disk.yandex.com/d/x_BNWSrt1E9cKA",
    "Адиль Бисенов, [26.11.2023 14.31] https://youtu.be/o3FHgKrb5KA?si=1JFYdUxtx0ccr1tw",
    "PVNIKA, [26.11.2023 14.31] Всем привет, давно меня не было в уличных гонках, Трек крайний класс, бро @soundrugsbeats🍎 https://disk.yandex.ru/d/kxyhQHZC8sm4TQ",
    "Qazbek Esenjolov, [26.11.2023 14.32] Салам с костаная) https://disk.yandex.kz/d/63qmSEWT4omi_A",
    "Адиль Бисенов, [26.11.2023 14.32] https://youtu.be/aM_QhDW8kaQ?si=7r6sC-rbVlCKjdNp",
    "Merkhat Malik, [26.11.2023 14.32] https://drive.google.com/drive/folders/14Gc2yBXkmfX2t4fd1wlc8GcJJJ-xSOqP?usp=drive_link",
    "Шольц Женя, [26.11.2023 14.32] https://drive.google.com/file/d/1w38iPiEzifFOh84fWkDMX5oHUDw_aXRC/view?usp=drivesdk",
    "ᅠданя ᅠ, [26.11.2023 14.32] всем салам из Алматы парни 👋🏻 https://disk.yandex.ru/d/DuLcDvCwJVGFCQ демка сырая 0:40 дроп",
    "GURMAN, [26.11.2023 14.32] Салют Благодарю за высокие оценки прошлого трека(хроники)(стрим вместе с недры) Сырая демка Всем любви и счастья Inst:@shelovesgurman Tg:@iamgurman P.S. Никнейм гУрман https://disk.yandex.ru/d/-An9BSMeQwwn7Q",
    "bboy flame!, [26.11.2023 14.32] https://disk.yandex.ru/d/EpYzUl0UCtuCdg",
    "dare phobia, [26.11.2023 14.32] https://drive.google.com/file/d/1qrp7H-ZN0gZRMiySwyQb4OaSRddBtjuN/view",
    "Timophey🧟‍♂, [26.11.2023 14.32] https://soundcloud.com/archive-152489760/manhattandemo?si=d5d152a3d8e64f3d8b0b0dd92eabcc31&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing",
    "Турбо Крутыш, [26.11.2023 14.33] СУТЕР - артист из Беларуси, провокация, эпатаж и бессовестное смешивание жанров: рэп, электро, интелледжент, панк, брейк бит. https://drive.google.com/drive/u/1/folders/1fg-X5zwZjF4crKPYAjeMz0zTaIVCq4Dy https://soundcloud.com/a0fuvxg2z8c1/sets/104-demo-suter",
    "(@), [26.11.2023 14.33] БРАТ, ПРОШУ ПОСЛУШАЙ татарская мафия! Я артист из Московской области, но родился в Уфе! На данный момент экспериментирую со звуком и флоу, очень интересно что скажешь! https://disk.yandex.ru/d/s8OdfAjEjxWQTg",
    "SaintHaven, [26.11.2023 14.33] https://vk.com/wall-191657933_394 йо, далеко не законченная работа (опыта не хватало на тот момент) но все же очень интересный звучок 🙏🏽",
    ". ., [26.11.2023 14.33] Салам.трэк в Яндекс музыке «Казахстан: открытия». https://clck.ru/36nmmc и если будет желание то ещё и этот послушайте https://clck.ru/36nmpS дроп 8 декабря. Ссылку укоротил через Яндекс сервис",
    "Danik, [26.11.2023 14.33] https://disk.yandex.kz/d/M3Qy8sTa3djuBg Салам мужики! Записали по угару, там знакомые мотивы, просьба слушать полностью",
    "prostovalentinsyka, [26.11.2023 14:34] https://transfiles.ru/c97e0",
    "Бейбарыс, [26.11.2023 14:34] 7292 https://disk.yandex.ru/d/SsKRUGf7tpHfOA",
    "Phettr Shade, [26.11.2023 14:34] https://drive.google.com/file/d/17n7PcKz4jz4hEWudWFS29WaZyltJTyXm/view?usp=sharing",
    "серапунтик, [26.11.2023 14:34] https://disk.yandex.ru/d/5dVnGwONMCzWpA",
    "Rrrr, [26.11.2023 14:34] https://drive.google.com/file/d/1Ej1BEMzXlpYXaBLhsQSO7Fv4LqV0YP7h/view?usp=drivesdk",
    "MEYAC, [26.11.2023 14:35] САЛАМ БУДЬТЕ ЗДОРОВЫ! https://disk.yandex.ru/d/Q_24giejodd4YA"
]



user_facts = {}  # Словарь для хранения фактов пользователя

@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    user_id = message.from_user.id
    if user_id not in user_facts:
        user_facts[user_id] = []

    await bot.send_message(user_id, "Привет! Я бот для получения демок. Нажми кнопку, чтобы получить демку или введи /GetFact <номер демки>.", reply_markup=get_keyboard(user_id))

def get_keyboard(user_id):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    get_fact_button = types.KeyboardButton("/GetDemos")
    keyboard.add(get_fact_button)
    user_facts_count = len(user_facts[user_id])
    if user_facts_count > 0:
        keyboard.add(types.KeyboardButton(f"/GetDemos {user_facts_count}"))
    return keyboard

@dp.message_handler(commands=['GetDemos'])
async def send_programming_fact(message: types.Message):
    user_id = message.from_user.id
    if user_id not in user_facts:
        user_facts[user_id] = []

    parts = message.get_args().split()
    if len(parts) == 1 and parts[0].isdigit():
        fact_number = int(parts[0]) - 1
        if 0 <= fact_number < len(programming_facts):
            if fact_number not in user_facts[user_id]:
                user_facts[user_id].append(fact_number)
                await bot.send_message(user_id, f"Демка {fact_number + 1}:\n{programming_facts[fact_number]}", reply_markup=get_keyboard(user_id))
            else:
                await bot.send_message(user_id, "Вы уже получили эту демку. Выберите другую.", reply_markup=get_keyboard(user_id))
        else:
            await bot.send_message(user_id, "Укажите допустимый номер демки.", reply_markup=get_keyboard(user_id))
    else:
        available_facts = list(set(range(len(programming_facts))) - set(user_facts[user_id]))
        if available_facts:
            fact_number = random.choice(available_facts)
            user_facts[user_id].append(fact_number)
            await bot.send_message(user_id, f"Демка {fact_number + 1}:\n{programming_facts[fact_number]}", reply_markup=get_keyboard(user_id))
        else:
            await bot.send_message(user_id, "Вы получили все доступные демки. Выберите другую.", reply_markup=get_keyboard(user_id))

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
