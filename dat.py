#!/usr/bin/env python3
import os
from aiogram import Bot, Dispatcher, types, executor
import random

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot)

programming_facts = [
    "prostovalentinsyka, SCARLET ✨ https://transfiles.ru/c7m7j",
    "Michael South, САЛЮТ, 104😎 Был с тобой на Burn Tour в Студии 21. Ты был хостом с Сеней. Приятного🤟🏼 https://disk.yandex.ru/d/_RNKmUONi3csTQ",
    "Mag, Огромный салам алейкум с Караганды🤝 У кентишки сегодня выходит два трека на площадки Ник - Xolod Интересно узнать вашу оценку Приятного прослушивания Новых творческих успехов вам ✊ Первый трек https://disk.yandex.kz/d/0SNnr33sO9-eVg Второй трек дарк версия https://disk.yandex.kz/d/-QV31GDTyt_Yqw",
    "risky_e, https://disk.yandex.ru/d/1_FnYb9XU5lLCA",
    "blaxtone, https://www.dropbox.com/scl/fo/av1bm55xt13u9hhqiozfp/h?rlkey=cjhduch4vx04wnnt4z1l9sdtd&dl=0",
    "elena, привет с Камчатки ☺️ мой первыыый ❣️ lena kurman - uber https://drive.google.com/drive/folders/1l8LaHF62y96Ook8YL1T9ynpMp5YAqHGQ",
    "$KY🫀, SKY https://disk.yandex.ru/d/y7nvHjXbwEbQZQ",
    "Cosmo Vasili, Салют! 🔥 https://disk.yandex.ru/d/FY0j0RCCIIH49w",
    "Zet, https://disk.yandex.ru/d/yb7Yd1ac-ZTfNA",
    "L V, https://drive.google.com/file/d/1A-GSpJWNT0Uawoh2xz1stGhOWhAMJKRl/view?usp=drivesdk https://drive.google.com/file/d/1-qotVR04j3nT-28Tfa3wFcK1-fajNcNh/view?usp=drivesdk Трек «Teni» лучше слушать с 50 сек.",
    "Danila, салют 👀 https://disk.yandex.ru/d/r6oXxF3N13xu4g",
    "biloff, https://disk.yandex.kz/d/To8x6OlNeSqvOA",
    "Soltan «SOULTYLER» Shakur, йо, здесь база))) https://drive.google.com/drive/folders/1Fd953UKUPMnj61BdFp7tJ1OXTuJvXyn3",
    "David Margiev, Всем саламы из Осетии , Матвей красава Хотелось сделать что то живое в стиле Горрилаз Использовал звучки из китов от пацанов https://disk.yandex.ru/d/iOvuK0sPix5NTw",
    "деньги, Привет из Сочи благодарность от нашего объединения COMPLEX012 ❤️❤️❤️💋 оставил ссылку на весь альбом, самые сильные треки это \"LOOTXDD\", \"Не могу слезть\", \"Ублюдок\" Приятного прослушивания❤️❤️❤️ https://vk.com/music?z=audio_playlist538895328_203/09c05eb7cd485f6208",
    "Danila, салют х2 👀 https://disk.yandex.ru/d/KaqQi3nJlxaxUg",
    "(@), Йоооо, очень люблю музыку, горю ей! https://disk.yandex.ru/d/s8OdfAjEjxWQTg Надеюсь получиться послушать мои работы Спасибо тебе босс!!",
    "Sonicx, Салам джигиряу🤝 https://drive.google.com/file/d/1bN3o21ylhw6lEai1xnffTOJohfomUWaG/view?usp=drivesdk",
    "taratu.black, салам из крг, TU https://disk.yandex.kz/d/uKtwEZuoaLavJA",
    "COMPACTBLUEFAN, https://vk.com/wall-159058959_1719",
    "максим дрип, https://soundcloud.com/phonkmannn/evil-d-uzi",
    "Juzza, Ассаламуалейкум джигиттер. Давно вы меня тут не слышали, а я тем временем замутил плотную колбаску. Советую начать с трека «Звоночки» более сильная демка. Рахмет 🥖 https://disk.yandex.com/d/I8tunlS7hm_oMw",
    "Ibrahim Akhmetzhan, https://drive.google.com/file/d/1ZK3mcxmDhtUsQvt0MzfgaQS04VScvd3M/view?usp=drivesdk",
    "­­, Салам из Екб. Субтитров нет, в описании ссылка на genius https://youtu.be/GQQElLpeVnY?si=dKExykk6UG_AqbYe",
    "... артём🖤, https://www.dropbox.com/scl/fi/7c50ydxdq5shtgs85vs5u/problem.mp3?rlkey=etv4zziseh9otw7yebh8k61in&dl=0",
    "ToiboY, Salam Юрику от KanKan https://disk.yandex.kz/d/_iwwnv4AvFJoOQ",
    "Андрей, Юра, салам. Буду благодарен за комментарий https://drive.google.com/drive/folders/1mnCkKWagHPCv1v4x5cqgyUmCncK4ANi4?usp=sharing",
    "Stepan Kulnev, Всех приветствую, всем Ассаламу алейкум, Юрик, так чисто на заценочку, отдуши. https://disk.yandex.ru/d/RN7-F4EZgprkpA",
    "Адиль Бисенов, https://youtu.be/4WvEftgk44k?si=MlItL1-NlfA_BYe1",
    "💎, https://drive.google.com/file/d/1JSrew5K5vsqzBI_aez0-iYH7Hed2-e8C/view?usp=sharing",
    "Fox_kid_izlesa🦊 VOSSEN❤️‍🔥🎸🎬, https://cloud.mail.ru/public/ViKs/f3E7ArYbt ИЗ ВЛАДИКАВКАЗА С ЛЮБОВЬЮ",
    "balanS, https://disk.yandex.kz/d/rcmPWpcKVuNpIw",
    "Askhat Turmenov, https://drive.google.com/file/d/1CIwNsjn684q6WPAftGi6KSHXbd2ApbYh/view?usp=sharing",
    "ᅠ ᅠ🌬️, http://band.link/0ylCx",
    "dendi, https://disk.yandex.ru/d/SSxAlGKd1bdU9Q",
    "🔥By Vlad 🔥, Салам, Одесса на связи 🔥 Хочу передать привет 104му, спасибо за такой формат, даешь шанс молодым порадоваться оценкам, всего самого, и ебейшего стрима 💪 от души 🙏 https://fex.net/s/xfraaxv",
    "5 $hots, Yo Юра, салам с ЕКБ Фанат твоего творчества, уважаю твое мнение Прослушка топ, спасибо всем https://drive.google.com/drive/folders/1ngx8GQSFkGmvu392hQs9GytKlbTi4iK7",
    "милиан факсуприм, https://drive.google.com/file/d/13ZA2mcvmhZ0eRSVgUdKUZyGMbxFdtz69/view?usp=drivesdk",
    "., https://t.me/musthave_ftp/13 Участников и так много,поэтому приоритет на 3 и 4 трек(Сон под орешиной и Маски) Спасибо!",
    "L, 🙏🙏🙏 Спасибо за внимание https://disk.yandex.ru/d/6BAsT6PMJGRXFQ https://disk.yandex.ru/d/ZvrlUEN7mijQvA (t.me/liura24)",
    "justpve, Салют всем из Кыргызстана , Boss, очень жду твой альбом . Ловите на оценку , если зайдет послушайте второй . Спасибо https://drive.google.com/file/d/125lcmzCbreUNfCHuCo48umKL-C582hqc/view?usp=sharing https://drive.google.com/file/d/1TACWQ66HSWPSLvPBHLwviiVVS1HmTMZl/view?usp=sharing",
    "hohibro, https://drive.google.com/file/d/1Nc2wyYD2xJ8VI5qZtimtJM3pUGfopTQR/view?usp=drivesdk Всем здарова братва, хорошой прослушки ✌️ бит кому понравится , отдам за респект ))",
    "🧡, https://drive.google.com/drive/folders/1U79jYmAZpTvzb6wGRJBF7G9sULv8_9HK",
    "Jesse Crystal's, Всем ку, хорошего дня и приятного прослушивания https://drive.google.com/drive/folders/1evJPhYGjCH992-1Kljoh7E_enIJzI_LY",
    "Kamil, https://disk.yandex.ru/d/gxfF3Ygb7Bqvzg",
    "Ваня, восап из Нижнего Новгорода https://disk.yandex.ru/d/qr4YoxZEK2yC_A",
    "♱, https://on.soundcloud.com/WY5tWrsWBF1FvxuS9",
    "G010, https://bnd.lc/sprut",
    "Ask, https://www.youtube.com/watch?v=J9bd1hPmEvI",
    "Vincenzo, Салют из Омска. Немного джаза и в целом жанрового разнообразия 🫡 Плюсом гружу пост-панк, который скоро выйдет. Хорошей прослушки. https://music.yandex.ru/album/27085924 https://disk.yandex.ru/d/oLhIXwLsoav3uA",
    "YAGA, https://disk.yandex.ru/d/3BB9yT0Tjdp0Eg",
    "aaizawa, https://youtu.be/2TSGq7nAVoM?si=yRu5BxT79laZMmwV",
    "A B, Mikikaiva - VNR https://drive.google.com/file/d/1VQXB1lTD9ghHNu8jMYnvhTM9NCh4cibb/view?usp=drivesdk",
    "Ярослав Леонидов, https://youtu.be/w6GIQJJC5oE?si=NVoYuVnwHoMi5TfE",
    "Yehor, Салам! https://drive.google.com/drive/u/4/folders/1sjcWcTz4tMZUZvE9qScXk5_xlm7lIoRQ",
    "Owen, https://drive.google.com/drive/folders/19IyELOzp6tCtUgeir6dEmgaorEJHUR3Q",
    "БАРАБАСЕР, https://t.me/ohman_ph/168",
    "игорь 👁👁, https://drive.google.com/file/d/11tSFHvOYQIW4yplhl4_v2Omr0mK2JJY-/view?usp=sharing",
    "Saùdion, https://drive.google.com/file/d/1LT3OXmhns1lhdnUgzw0Ue8S1TArq0KhK/view?usp=drive_link",
    "Dmitry Peero, https://disk.yandex.ru/d/gN9rTTAWE-KITQ",
    "Aleksei OUTSIDE G, Челяба, Махачкала, Донецк на связи 🙌 https://disk.yandex.ru/d/Kj4ZyzzcZj0HEQ",
    "yungvest🔇, весь мск грустил под это https://vk.com/music?z=audio_playlist352250663_352&access_key=5e550b6252efa93b20",
    "Lux Potishe, https://disk.yandex.ru/d/KCxVJ3VyMYaOZQ",
    "Angiz, https://open.spotify.com/album/4ny1g2kI7GmN1dtJTnVYiF?si=Kk9RP9xsQtiCsVhDuXcj8w",
    "Madiyar Sovetbay, https://drive.google.com/file/d/1teb7tWeqYXZhSu5AesBRVIlKQzDOkgfs/view?usp=drivesdk",
    "∴, https://vk.com/music?z=audio_playlist-2000731880_17731880&access_key=73bf1cde1baec0fd9a",
    "High Fly, Салют 104 и ребята из SHOUTS 🙏🏼 Этот трек является 4-й по списку из 7 треков с еще не вышедшего EP под названием «Катафалия». Буду рад услышать ваше мнение. Я в ТГ: @high_fly1 (ЛС), @bumerontheblock (Канал) С респектом, BUMERONTHEBLOCK https://drive.google.com/file/d/1ywr_TEQkw7qbNmgZG1kH7DaHCi56M_Zh/view?usp=sharing",
    "Jojo, https://disk.yandex.ru/d/JZ67QvieJzTGNA Бит самопал, так же как запись и сведение",
    "Maks, Привет 👋. 163-ий регион на связи🫡 https://disk.yandex.ru/d/dnbF5BMpdjr1LQ",
    "Бернара, Привет) очень приятно что узнал в прошлый раз! вот еще https://youtu.be/2-PydYW5emE",
    "Egor Skryabov, Пламенный салам с г.Владимир https://disk.yandex.ru/d/EO6_KpAvishjMQ https://disk.yandex.ru/d/ZFs_VgYTeUQsKw",
    "Je Sai, https://disk.yandex.ru/d/sTzFyzLbHbgfxg",
    "Luka Andolini, https://disk.yandex.ru/d/ceRuIqhTYDkwJA Просто кайфаните",
    "acoustc 💘, https://www.dropbox.com/scl/fo/6jr4p20pftyofy6vgcd4w/h?rlkey=2od8t2q057mvun27w1x7v752k&dl=0",
    "rusbekov, в темноте.mp3: https://disk.yandex.ru/d/daKW5zk_rIXjgw",
    "kalepl, https://disk.yandex.ru/d/k4P6qDmkDBRHHg",
    "KUZM111N, https://disk.yandex.ru/d/hdcXziiRuWeUuA",
    "rxno, https://vk.com/music?z=audio_playlist-2000192205_19192205&access_key=bfa0fa851ac3ebd6ea",
    "Limb8, https://music.yandex.ru/album/28129454/track/119071736",
    "Thompson, https://t.me/songs996/848 Недавно дропнул жду не дождусь прослушку🙌🏻",
    "wholazybone, https://disk.yandex.ru/d/D9FSEcN17pl7UQ всем салют, я с Иркутска, пишу рэп читаю биты )",
    "Phettr Shade, https://drive.google.com/file/d/17n7PcKz4jz4hEWudWFS29WaZyltJTyXm/view?usp=sharing",
    "🥷🏽, Салют с Москвы УЛИЦЫ.mp3 https://drive.google.com/file/d/1UNeqABsVQEnpIjl0RohSlAQtAnMBDiO3/view?usp=drivesdk",
    "dim.mai, https://disk.yandex.ru/d/Zc2nQFQna2DM0w",
    "Федор🇷🇺, Парни, салам, ловите демку https://disk.yandex.ru/d/_ZiBE-RZgZ9EzQ",
    "камиллк, Посмотреть или скачать файл «vada-баттл.mp3» https://disk.yandex.ru/d/4j-pLSVwvy0pQA",
    "Gary Choi, https://drive.google.com/file/d/13HMhtHMi-It8jABwhe5SYdQnpwPVn9jm/view?usp=drivesdk",
    "Nil, https://music.yandex.ru/album/27622159/track/117926428",
    "Andrey Moskalenko, https://drive.google.com/file/d/137MyAODKz44Q6On4hd8rdif5_8IxjzC4/view?usp=sharing",
    "Влад Беликов, https://t.me/+N0ZD7C4FSBE5YTUy",
    "maikl, https://drive.google.com/file/d/1fq0-q4uQhZrQ5Xp5mTq63-B6tTIvF8gB/view?usp=sharing",
    "Данила Земцов, https://disk.yandex.ru/client/disk/для%20стрима%20104",
    "Макс, https://music.yandex.ru/album/27563374/track/117796769",
    "whymoonwalker, https://t.me/moon_walker2 ТГК",
    "милиан факсуприм, https://drive.google.com/file/d/13ZA2mcvmhZ0eRSVgUdKUZyGMbxFdtz69/view?usp=drivesdk",
    "Егорио, Алейкум из Костаная. Мне 19. Отправил бит и свой ремикс на трек Скриптонита - Огни. Ремикс просто настроение оценить. Благодарю за прослушивание🙏(в обоих работах гитара живяк, своя) https://disk.yandex.kz/d/xdtfXo4A1rT2fQ - бит (дослушай до припева пж) https://disk.yandex.kz/d/R6yVR7b8GL-xPg - ремикс",
    "Энвилав🕸️, Пред последняя работа, брат, скажи бывало ли у тебя выгорание и как ты с ним справлялся? Всем хорошей прослушки Тюмень https://vk.com/music/album/-2000958623_17958623_66f5105051b48f56eb",
    "Вова, https://www.youtube.com/watch?v=C8l-C5a3NpQ",
    "Haso, https://t.me/hasobusy/163",
    "Timophey, https://music.yandex.com/album/27823223?utm_medium=copy_link",
    "серапунтик, https://disk.yandex.ru/d/wEQ70UTyAucrWg",
    "Mastadont, https://disk.yandex.ru/d/v4hIdFXjFzotww Салам из Челябинска. Сводил сам. Трек Rari - Клиент",
    "KiFFSO - https://drive.google.com/file/d/1OBCkS8G0MrIoCkE9-6LW3VMtJeQtvqMJ/view?usp=sharing Салам парни, вот вам качественного звука от KiFFSO.К слову весь проект делал сам, поэтому можете отдельно оценить сведение и бит.Трек еще не выпустил, хотел бы посмотреть на первую реакцию людей и послушать ваше мнение. Рахмет",
    "via Radle - https://disk.yandex.kz/d/8nN3xk2r3B6vAA via Radle — Общепит Хорошего стрима",
    "abl abdyqasym - https://www.dropbox.com/scl/fi/4ygznfeoi6epbus8ecj99/abdyqasym-SAUDI.mp3?rlkey=obbvp491ov76ui7ukt16uwngo&dl=0",
    "мадияр - https://drive.google.com/file/d/1Wryvsau1m_zSbr8Ii6edK4PuijrGFuQA/view?usp=drive_link",
    "staryrayxxx staryrayxxx - https://youtu.be/X38CZvuKTcQ?si=6ElugOzJv-rrDm73",
    "D) - https://disk.yandex.ru/d/dMawbonACqSwmw",
    "алик янгчен - https://vk.com/music?z=audio_playlist-197915572_8&access_key=4d6f25f4c5cbe93905 приветствую всех, сразу скажу спасибо за прослушивание и оценку трека отдельный привет cruise lirro, лучшие джерси биты)",
    "Merkhat Malik - https://drive.google.com/drive/folders/14Gc2yBXkmfX2t4fd1wlc8GcJJJ-xSOqP?usp=drive_link",
    "Alizhan Kadyrzhan - https://drive.google.com/file/d/1eWoJkvBqrJv6Pwx6GSVkgSazzG9rnV6d/view?usp=drivesdk",
    "Dinane - https://disk.yandex.ru/d/ITvih8w0QwEQ8w",
    "Qazbek Esenjolov - Салам с Костаная) https://disk.yandex.kz/d/63qmSEWT4omi_A",
    "Владислав - https://links.freshtunes.com/A3a0E",
    "jjershsk - Юра, здравствуй Трек о новых этапах в жизни каждого Продакшн полностью мой) Интересно твое мнение Алга Казахстан https://drive.google.com/drive/u/1/folders/1416XRAphp-f8XPrxKcBInxePAnfOroDY",
    "boss🇳🇬 - всем салам, всем удачи в творчестве, это мой вышедший трек в лирическом стиле https://drive.google.com/file/d/1CK1pxpuluXxgITfx2XacoYw0oVF9dWAU/view?usp=drivesdk а это уже дэмо версия но уже хип хоп или как этот стиль называется https://drive.google.com/file/d/1UNgTTVXhXefpkl42BLPpY9tqzMtP4ApU/view?usp=drivesdk",
    "Hunnah - Восап, я Kampit с Кокш, прошлый раз скидывал вам демку смотрю вас качнуло, в этот раз на Казахском, весёлый, вайбовый трэк, надеюсь оцените 🥩 https://disk.yandex.ru/d/uoWf3WZULEhZZQ",
    "GLORY BACK SEASON - Салам всем можно подольше послушать там просто каждую минуту флоу меняется https://drive.google.com/file/d/13ZA2mcvmhZ0eRSVgUdKUZyGMbxFdtz69/view?usp=drivesdk",
    "xandr - https://drive.google.com/drive/folders/1-A7kkLTDMPPJm0fKk8dWtr0McUtIZUlm?usp=drive_link",
    "Triple Slash - салам, хорошей прослушки :) с 0:41 тож послушайте есчоо https://disk.yandex.ru/d/EOxcnqcBl_e5NA",
    "Саид Рабаданов - https://vk.com/audio576260691_456239841_5a97ba1499d4b491e8",
    "Levon - Всем пламенный барев Kaeoki - Alone Demo Нужно добить и перезаписать, но общая картина есть в любом случае Prod me https://disk.yandex.ru/d/HaydljrHW58ZZQ",
    "lomafafafo - https://drive.google.com/file/d/13ZA2mcvmhZ0eRSVgUdKUZyGMbxFdtz69/view?usp=drivesdk",
    "Alizhan Kadyrzhan - https://music.apple.com/kz/album/%D0%BC%D0%B5%D0%BD%D1%82%D0%B0%D0%BB%D0%B8%D1%82%D0%B5%D1%82/1694935953?i=1694935956",
    "jokeovic - https://drive.google.com/drive/folders/1-4ZgIlZsSEjUegq34RVBK1aLvMTY18O7",
    "DEWENSOON DEWENSOON - Давно не кидал ничего . Было чуть тяжко чето . Короч для поднятия настроения 😊 https://youtu.be/rojBqmbE158?si=7MAoGeoDlZxcrNQ_",
    "KiFFSO - https://drive.google.com/file/d/1OBCkS8G0MrIoCkE9-6LW3VMtJeQtvqMJ/view?usp=sharing Салам парни, вот вам качественного звука от KiFFSO.К слову весь проект делал сам, поэтому можете отдельно оценить сведение и бит.Трек еще не выпустил, хотел бы посмотреть на первую реакцию людей и послушать ваше мнение. Рахмет",
    "nothing more 💤 - https://disk.yandex.ru/d/daKzdwsL3CR1NA",
    "👤 - Саламалейкум хорошего стрима🙌🏽 https://youtu.be/vO_yJD8jXS0?si=ua5oyUR8sABxZlc5",
    "https://youtu.be/ToFAgZ8rZNo?si=yzcy4vmiXrKwpRR2",
    "милиан факсуприм - https://drive.google.com/file/d/13ZA2mcvmhZ0eRSVgUdKUZyGMbxFdtz69/view?usp=drivesdk",
    "blubaby bluebaby - https://youtu.be/rQ9pMmlLu0w?si=LTpmQgn9TP-OEk9Z",
    "Alizhan Kadyrzhan - https://music.apple.com/kz/album/bang-bang/1677107166?i=1677107337",
    "PVNIKA - Всем привет, давно меня не было в уличных гонках, Трек крайний класс, бро @soundrugsbeats🍎 https://disk.yandex.ru/d/kxyhQHZC8sm4TQ",
    "Hunnah - https://disk.yandex.ru/d/XV21KTrKpdr9bQ",
    "Qazbek Esenjolov - https://disk.yandex.ru/d/8dV_M4QpBdDjZw",
    "серапунтик - https://disk.yandex.ru/d/wEQ70UTyAucrWg",
    "roman - 🫂🎶 https://www.dropbox.com/scl/fi/w57tchtbwgrlstwcr7nbr/17.10.23.mp3?rlkey=4i1ogel2of3nf0tgjcfszdltu&dl=0",
    "Майлз - Салам! Трек уже вышел и есть на всех витринах! спасибо за внимание https://drive.google.com/drive/folders/12ZNUNAqvwHTbLo3V3rScMBIozmJySFfU",
    "Макс - https://zvonko.link/155794E",
    "Robinzon - https://music.yandex.ru/album/27146283/track/116821928?utm_medium=copy_link",
    "Qara Qush - Всем Ассаламу алейкум братья. Записал демку, жду сведение. ************************* https://disk.yandex.ru/d/an4lwtUr42vJmw",
    "Alizhan Kadyrzhan - https://music.apple.com/kz/album/%D0%BF%D0%BE%D0%B6%D0%B5%D0%BB%D0%B0%D0%B9-%D1%83%D0%B4%D0%B0%D1%87%D0%B8/1710371743?i=1710371744",
    "Максим Викторов - https://drive.google.com/drive/folders/1x3EBl5xJeRhe4JOGhQQW8-Y65MLJP4E-?usp=sharing Freezy-VICMA",
    "N.N. - пара но и я https://drive.google.com/drive/folders/1zG40VMxClCT1l31gqd5zJlyOc7QWlUdJ?usp=sharing",
    "Нурлан Шайырбек - https://youtu.be/LKy0gAjHADI?si=3jMVUbX4LsxYMjV8",
    "Shakar - https://disk.yandex.ru/d/dA-mwu9yMZdtrw",
    "Як - https://disk.yandex.kz/d/WmUCiWSxnkKZtQ",
    "xandr - https://youtu.be/yyCjCyD_6_g",
    "Danik - https://disk.yandex.kz/d/M3Qy8sTa3djuBg",
    "hleborobny - https://disk.yandex.ru/d/C7c71IOlhVaDyQ Надеюсь дойдет!Мир вашему дому 🙌🏻",
    "bluesbmcp - https://disk.yandex.kz/d/K6Mtm7eP3FKFCw",
    "i’m IXENOV - https://youtu.be/s-_IOgkGshI?si=f4oXItdtpUlxIJrQ",
    "HAC - https://vk.com/audio?z=audio_playlist-2000306859_19306859/23300f37df8c130779",
    "bluesbmcp - https://disk.yandex.kz/d/IrpYUGeeaeHUcQ",
    "M - https://drive.google.com/file/d/1zdmc_me8S27E93kT46lsJnPjx11B0DS5/view?usp=drivesdk",
    "Murat Zhashkeyev - https://drive.google.com/file/d/1Bxn5TB2rEpwJLCvHpjbcz7Msy__oOLdT/view?usp=drive_link",
    "ali - https://youtu.be/czqlfz59Qps?si=kI4m2E87mGKBMM-a",
    "M - https://drive.google.com/file/d/1zdmc_me8S27E93kT46lsJnPjx11B0DS5/view?usp=drivesdk",
    "Кто? - 1859 https://drive.google.com/file/d/1s3amW9DtI6Qm8zvkbzRUi-WrdgLkzmKt/view?usp=drivesdk",
    ". . - Салам всем. Юрик я долгое время слушал твой трэк деньги и власть. Лично для меня охуенный трэк. В инсте не читаешь зато здесь могу писать 😁 Новый трэк, который в скором времени появится на всех площадках. https://drive.google.com/file/d/1G3LSmAjONNHLdff5Tj5IT_sjXUgpgV4I/view?usp=drivesdk",
    "Ильяс - https://drive.google.com/file/d/1r47BfArLGB1wTIyf5kcs9LQWo6ZEL8xB",
    "Maybe Friday - https://disk.yandex.ru/d/xMWLlvskjgR3-Q",
    "Tonie - Бит, запись, сводка - сами😎 Первый читает товарищ из Петропавловска, с 1:30 - я Хочу узнать твое мнение о бите, припеве и общем настроении) https://drive.google.com/file/d/1BPM1rVYzHBNYE4ixIOFD8GDhNFL9rKpQ/view?usp=drivesdk",
    ". . - Салам всем. https://drive.google.com/file/d/1rY0UGpTvvkklHqzcLJ9T1k6YKisLbZ3I/view?usp=drivesdk",
    "Blown Baby - https://vk.com/wall-213831567_272",
    "D [NEVER DM FIRST] - https://drive.google.com/file/d/1f0qKmWD-0NMZ90YpN2JG2oz6cUznS3nY/view?usp=drivesdk",
    "Богдан Прайс - https://disk.yandex.com/d/S5ON71lbn4kaCQ",
    "D [NEVER DM FIRST] - https://drive.google.com/file/d/1U8PR5TykZ60MVMePCvJLEN3U_LWVD3s9/view?usp=drivesdk",
    "Әне Міне - https://disk.yandex.ru/d/PO2XZZgSCiDYng",
    "HOBO X - Саламчик всем) Супер черновая демка из печи, прям черная (фейс ту фейс) Не обожгитесь 🔥 А если залетит прослушайте «Мама прости»🫂 Хобо на связах ✊🏽 https://disk.yandex.ru/d/4IILScExIqgh5Q",
    "dosy - https://disk.yandex.ru/d/fQ_xh0rAtIbqDg",
    "OG - https://drive.google.com/drive/folders/1-asUHG_wbWzvZ6E6DrKwJ36B68KVqr3A",
    "KUPRIY текста и исполнение subad imir - Салам, Юра. Здоровья тебе и твоим близким. Я некст ап, базарю, не важно залетит, не залетит https://drive.google.com/drive/folders/1-8AsLJiErDqWYcbBzOJxlX06Omh01RVY",
    "izokon1312 - Салют из Питера https://disk.yandex.ru/client/recent?idApp=client&dialog=slider&idDialog=%2Fdisk%2FIzokon%20-%20ruki%20na%20rule%2FIzokon-rukinarule.mp3",
    "Лев Терентьев - https://drive.google.com/drive/folders/1-6JpSprRA3w0a_bTE0zuN4bNV95Yv_i1",
    "Oan - https://open.spotify.com/album/4Dx8qJeISCqeB1VTL8CgoP?si=tn743B_ZSnWNeRRJWm5N3g",
    "Бро Кляйн - https://vk.com/music?z=audio_playlist-2000903384_18903384&access_key=d08c1c2023f0359d9c",
    "тёма, https://disk.yandex.ru/d/ECx_702vlODgUQ",
    "Андрей Фирсаков, https://disk.yandex.ru/d/_LeRMxCOeNnp0w",
    "tawsogar, салам алейкум, чекайте джерси ремикс на той жыры)) https://www.youtube.com/watch?v=AmIvEux4nTE&ab_channel=melonemes",
    "Джонни Пончик, https://disk.yandex.ru/d/7QGOxvyTneRDUg"
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
